import os
import datetime

from motor.motor_asyncio import AsyncIOMotorClient
import asyncio
import logging

from discord_bot import current_config

# DB connection and config
uri = f"mongodb+srv://{current_config.DB_USERNAME}:{current_config.DB_PASSWORD}@cluster0.8bei2.mongodb.net/retryWrites=true&w=majority"
client = AsyncIOMotorClient(uri)
db = client.get_database(f'{current_config.DB_NAME}')
collection = db.get_collection(f'{current_config.COLLECTION_NAME}')


async def get_history(user_id, query):
    """
    Utility func - Gets all the related queries from user's search history

    Args:
        user_id (string): user's discord userID
        query (string): search query 

    Returns (iterable object) : results retrieved from DB
    """
    results = await collection.find({'user_id': user_id, 'query': {'$regex': query}}).sort(
        'modified_time', -1).to_list(length=None)
    logging.info("Successfully Fetched query results from DB")
    if(len(list(results)) == 0):
        return 0
    else:
        return results


async def insert_squery(user_id, query):
    """
    Utility func - Inserts the user's search query into DB, 
    Updates modified_time if query already exists

    Args:
        user_id (string): user's discord userID
        query (string): search query (eg. nodejs in !google nodejs)

    Returns : None
    """
    curr_time = datetime.datetime.utcnow()
    old_doc = await collection.find_one({'user_id': user_id, 'query': query})
    try:
        if old_doc:
            _id = old_doc['_id']
            result = await collection.update_one({'_id': _id}, {'$set': {'modified_time': curr_time}})
            if (result.modified_count):
                logging.info("Successfully updated user query into db")
        else:
            document = {'user_id': user_id,
                        'query': query,
                        'created_time': curr_time,
                        'modified_time': curr_time}
            result = await collection.insert_one(document)
            if(result.inserted_id):
                logging.info("Successfully inserted user query into db")
    except Exception:
        logging.error("DB insertion failed", exc_info=True)
