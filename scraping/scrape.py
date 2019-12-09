#!/usr/bin/python3
import argparse
import logging
import feedparser
import sys

from pprint import pprint

sys.path.append('../')

from scraping.parsers.nyt_parser import parse as nyt_parse
from scraping.parsers import parse_errors 
from scraping import write_to_cloud

NYT_RSS_ADDRESS = 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'


def scrape(
        source_type,
        source_rss_uri=None, 
        source_file_path=None,
        write_function=print):
    logging.basicConfig(level=logging.NOTSET)
    l = logging.getLogger('parselog')
    l.setLevel(logging.DEBUG)
    if source_type == 'rss':
        feed = feedparser.parse(source_rss_uri)
    elif source_type == 'file':
        feed = feedparser.parse(open(source_file_path, 'rb'))

    for item in feed['items']:
        try:
            parsed_headline = nyt_parse(item)
            l.info('Successful parse.')
        except Exception as e:
            l.info('Failed parse: {}\n\n{}'.format(e, str(item)))
        try:
            write_function(parsed_headline)
            l.info('Successful write.')
        except Exception as e:
            l.info('Failed write: {}\n\n{}'.format(e, str(item)))


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument('--source_type', default='rss', choices=['rss', 'file'])
    argparser.add_argument('--source_rss_uri', default=NYT_RSS_ADDRESS)
    argparser.add_argument('--source_file_path', default=None)
    argparser.add_argument('--write_to', default='stdout', choices=['stdout', 'cloud'], help='Desired destination to write output to. From {stdout, cloud}')
    args = argparser.parse_args()
    
    if args.write_to == 'cloud':
        write_function = write_to_cloud.write_to_cloud
    else:
        write_function = print
    
    print(write_function)

    scrape(
        source_type=args.source_type,
        source_rss_uri=args.source_rss_uri,
        source_file_path=args.source_file_path,
        write_function=write_function
        )
