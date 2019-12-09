import sys
sys.path.append('../../')

from datetime import datetime
from time import mktime

from Headline import Headline
from scraping.parsers import parse_errors


PUBLISHER = 'The New York Times'

def parse(item):

    if 'title' in item:
        text = item['title']
    else:
        raise parse_errors.MissingAttributeError('Missing attribute: `title`')
    if 'published_parsed' in item:
        datetime_published = datetime.fromtimestamp(mktime(item['published_parsed']))
    else:
        raise parse_errors.MissingAttributeError('Missing attribute: `published_parsed`')
    if 'id' in item:
        link = item['id']
    else:
        raise parse_errors.MissingAttributeError('Missing attribute: `id`')
    if 'author' in item:
        author = item['author']
    else:
        author = None
    if 'summary' in item:
        summary = item['summary']
    else:
        summary = None
    if 'media_content' in item and len(item['media_content']) > 0 and 'url' in item['media_content'][0]:
        image_link = item['media_content'][0]['url']
        if 'media_credit' in item and len(item['media_credit']) > 0 and 'content' in item['media_credit'][0]:
            image_credit = item['media_credit'][0]['content']
    else:
        image_link = None
        image_credit = None

    return Headline(
            text=text,
            datetime_published=datetime_published,
            publisher=PUBLISHER,
            link=link,
            author=author,
            summary=summary,
            image_link=image_link,
            image_credit=image_credit)
