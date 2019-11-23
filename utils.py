import os

from googleapiclient.discovery import build
from dotenv import load_dotenv
load_dotenv()


api_key = os.getenv('GOOGLE_SEARCH_API_KEY')
cse_id = os.getenv('GOOGLE_CSE_ID')


def search_google(search_term, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    # import pdb;pdb.set_trace()
    results = service.cse().list(q=search_term, cx=cse_id, sort='date', **kwargs).execute().get('items', [])
    search_result = []
    for result in results[:5]:
        print(result['title'], result['link'])
        search_result.append({
            'title': result.get('title'),
            'link': result.get('link'),
            'description': result.get('snippet')
        })

    # print(search_result)
    return search_result


# search_google('python')