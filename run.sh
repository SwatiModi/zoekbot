# All environment currently have almost same configuration and can be modified with requirement
# Production : logging level in INFO
# Development/Pre-production : logging level in DEBUG

#export DISCORD_BOT_ENV=development
export DISCORD_BOT_ENV=production
#export DISCORD_BOT_ENV=pre-production

python -m discord_bot.bot
