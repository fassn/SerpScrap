# -*- coding: utf-8 -*-
import logging
import re

from scrapcore.database import SearchEngineResultsPage
from scrapcore.parser.google_parser import GoogleParser
from scrapcore.parser.yandex_parser import YandexParser
from scrapcore.parser.bing_parser import BingParser
from scrapcore.parser.yahoo_parser import YahooParser
from scrapcore.parser.baidu_parser import BaiduParser
from scrapcore.parser.duckduckgo_parser import DuckduckgoParser
from scrapcore.parser.qwant_parser import QwantParser
from scrapcore.parser.ask_parser import AskParser


logger = logging.getLogger(__name__)


class Parsing():

    def get_parser_by_url(self, url):
        """Get the appropriate parser by an search engine url."""
        parser = None

        if re.search(r'^http[s]?://www\.google', url):
            parser = GoogleParser
        elif re.search(r'^http[s]?://yandex\.ru', url):
            parser = YandexParser
        elif re.search(r'^http://www\.bing\.', url):
            parser = BingParser
        elif re.search(r'^http[s]?://search\.yahoo.', url):
            parser = YahooParser
        elif re.search(r'^http://www\.baidu\.com', url):
            parser = BaiduParser
        elif re.search(r'^https://duckduckgo\.com', url):
            parser = DuckduckgoParser
        elif re.search(r'^https://qwant\.com', url):
            parser = QwantParser
        if re.search(r'^http[s]?://[a-z]{2}?\.ask', url):
            parser = AskParser
        if not parser:
            raise Exception('No parser for {}.'.format(url))

        return parser

    def get_parser_by_search_engine(self, search_engine):
        """Get the appropriate parser for the search_engine"""
        if search_engine == 'google' or search_engine == 'googleimg':
            return GoogleParser
        elif search_engine == 'yandex':
            return YandexParser
        elif search_engine == 'bing':
            return BingParser
        elif search_engine == 'yahoo':
            return YahooParser
        elif search_engine == 'baidu' or search_engine == 'baiduimg':
            return BaiduParser
        elif search_engine == 'duckduckgo':
            return DuckduckgoParser
        elif search_engine == 'ask':
            return AskParser
        elif search_engine == 'qwant':
            return QwantParser
        else:
            raise Exception('No such parser for "{}"'.format(search_engine))

    def parse_serp(self,
                   config,
                   html=None,
                   parser=None,
                   scraper=None,
                   search_engine=None,
                   query=''):
        """parse and store data in the sqlalchemy session.
        Returns:
            The parsed SERP object.
        """

        if not parser and html:
            parser = self.get_parser_by_search_engine(search_engine)
            parser = parser(config, query=query)
            parser.parse(html)

        serp = SearchEngineResultsPage()

        if query:
            serp.query = query

        if parser:
            serp.set_values_from_parser(parser)
        if scraper:
            serp.set_values_from_scraper(scraper)

        return serp
