"""
RSSフィードで取得するURL群の管理
"""

from dataclasses import dataclass
from typing import List
import json


@dataclass
class RssUrl:
    url: str
    description: str


RSS_JSON_PATH = "src/util/target_rss.json"


class RssUrls:
    def __init__(self):
        self._rss_url: List[RssUrl] = self.__get_rss_urls()

    def __get_rss_urls(self) -> List[RssUrl]:
        with open(RSS_JSON_PATH, "r", encoding="utf-8") as file:
            rss_urls = json.loads(file.read())
        return rss_urls

    @property
    def rss_url(self) -> List[RssUrl]:
        return self._rss_url
