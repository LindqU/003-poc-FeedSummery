"""
RSSフィードで取得するURL群の管理
"""

from dataclasses import dataclass
from typing import List, Dict
import json


# @dataclass
# class RssUrl:
#     url: str
#     description: str


RSS_JSON_PATH = "src/util/target_rss.json"


class RssInfo:
    @staticmethod
    def get_rss_infos() -> List[Dict]:
        with open(RSS_JSON_PATH, "r", encoding="utf-8") as file:
            rss_urls = json.loads(file.read())
        return rss_urls
