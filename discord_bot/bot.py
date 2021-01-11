import os
import logging

from discord.ext import commands

from discord_bot import current_config
from discord_bot.database import get_history, insert_squery
from discord_bot.google_search import google_search

# set discord command prefix
bot = commands.Bot(command_prefix='!')

logger = logging.getLogger(__name__)


@bot.command(name='google', help='Gets the top search results for your query from google')
async def query_google(ctx):
    """
    Triggers discord bot on !google command

    Args: 
        ctx (instance): context instance of discord

    Actions:
        Responds to same channel with a message containing top 5 search queries
    """
    query = ' '.join(ctx.message.content.split()[1:])
    logging.info("Someone searched for %s", query)
    await insert_squery(user_id=str(ctx.message.author), query=str(query))
    results = google_search(
        query, current_config.GOOGLE_SEARCH_API_KEY, current_config.CSE_KEY)
    if(results):
        top_links = '\n'.join([str(res['link']) for res in results])
        response = f'Hi {ctx.message.author}, Here are the top 5 search results for your query \"{query}\": \n{top_links}'
    else:
        response = f'Hi {ctx.message.author}, I was unable to find any relevant results for your query \"{query}\"'
    await ctx.send(response)


@bot.command(name='recent', help='Helps to search recent queries from your search history')
async def search_history(ctx):
    """
    Triggers discord bot on !recent command

    Args:
        ctx (instance): context instance of discord

    Actions:
        Responds to same channel with a message containing matching results from search history
    """
    query = ' '.join(ctx.message.content.split()[1:])
    results = await get_history(user_id=str(ctx.message.author), query=query)
    if(results):
        recent_queries = '\n'.join([res['query'] for res in results])
        response = f'Hi {ctx.message.author}, Your recent searches regarding \"{query}\" were : \n{recent_queries}'
    else:
        response = f'Hi {ctx.message.author}, You have no past queries regarding \"{query}\"'
    await ctx.send(response)

bot.run(current_config.DISCORD_TOKEN)
