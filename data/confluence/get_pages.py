from bs4 import BeautifulSoup
from get_token import get_access_token, get_url, get_user_name
from atlassian import Confluence

confluence = Confluence(url=get_url(), username=get_user_name(), password=get_access_token(), cloud=True)

def get_all_confluence_text(confluence):
    
    spaces = confluence.get_all_spaces(start=0, limit=500, expand=None, space_type='global')
    ans = ''
    for result in spaces['results']:
        space_id = result['id']
        space_key = result['key']
        space_name = result['name']

        de_pages = confluence.get_all_pages_from_space(space_key, start=0, limit=100, status=None, expand=None, content_type='page')

        for page in de_pages:
            page_id = page['id']
            page_title = page['title']
            try:
                page_content = confluence.get_page_by_id(page_id, expand='body.storage',
                                                        status='current', version=None)['body']['storage']['value']
                page_str = BeautifulSoup(page_content, "lxml").text
                ans = '\n'.join([ans,page_str])
            except:
                continue
    return ans

text_out  = get_all_confluence_text(confluence=confluence)

with open('./data/confluence/confluence_text.txt', 'w', encoding="utf-8") as f:
    f.write(text_out)
