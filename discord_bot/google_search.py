from googleapiclient.discovery import build
import logging

# suppress file_cache warning of googleapi client
logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)


def google_search(search_term, api_key, cse_id, num=5, **kwargs):
    """
    Utility func - Creates a custom search engine and retreives results for given query

    Args:
        search_term (string) : search term for getting results
        api_key (string) : GOOGLE_SEARCH_API_KEY
        cse_key (string) : SEARCH_ENGINE_ID
        num (int, optional) : number of search results to return

    Returns :
        res (list) : search results from google_search_api for given i/p query
    """
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    try:
        logging.info("Successfully retrived results for the query")
        return res['items'][:num]
    except:
        logging.warning("No results for the query")
        return []
