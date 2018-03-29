#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pprint
import serpscrap
import datetime

with open('keywords_AdwordsDelicorner.txt') as f:
    keywords = (f.read().splitlines())

config = serpscrap.Config()
# config.set('use_own_ip', False)
# config.set('proxy_file', 'proxies.txt')
config.set('use_own_ip', True)
config.set('sleeping_min', 90)
config.set('sleeping_max', 120)
config.set('sel_browser', 'chrome')
config.set('chrome_headless', True)
config.set('google_search_url', 'https://www.google.fr/search?')
config.set('num_pages_for_keyword', 1)
config.set('num_workers', 10)
# config.set('screenshot', True)
config.set('clean_cache_after', 24)
config.set('executable_path', '/usr/local/bin/chromedriver')

scrap = serpscrap.SerpScrap()
scrap.init(config=config.get(), keywords=keywords)
results = scrap.as_csv('seo-research-' + datetime.datetime.now().isoformat())

# results = scrap.run()

# for result in results:
#     pprint.pprint(result)
#     print()