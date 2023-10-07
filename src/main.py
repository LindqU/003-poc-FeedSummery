"""
main.py
"""
import os
from rss import RssReader
from util.rss_info import RssInfo
from typing import List, Dict
from util.log import logger


def main():
    # RSS Urlの取得
    rss_infos: List[Dict] = RssInfo.get_rss_infos()

    # feed 取得部分
    feed_dict = {}
    for rss_info in rss_infos:
        name = rss_info.get("name")
        description = rss_info.get("description")
        url = rss_info.get("url")
        logger.info("rss_name : %s description : %s", name, description)
        rss_reader = RssReader(rss_url=url)
        feed_list = rss_reader.get_feed()
        logger.debug("rss_info : %s", feed_list)
        feed_dict[name] = feed_list
    # file exportは実装する...？
    # 例えば、bigqueryのテーブルにインサートする的なノリのもの。

    # 要約レポート作成部分


if __name__ == "__main__":
    main()
