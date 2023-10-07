"""
main.py
"""
from rss import RssReader
from util.rss_info import RssInfo
from typing import List, Dict
import logging

# loggerの設定
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


def main():
    # RSS Urlの取得
    rss_infos: List[Dict] = RssInfo.get_rss_infos()

    feed_dict = {}

    for rss_info in rss_infos:
        name = rss_info.get("name")
        description = rss_info.get("description")
        url = rss_info.get("url")
        logging.info("rss_name : %s description : %s", name, description)
        rss_reader = RssReader(rss_url=url)
        feed_list = rss_reader.get_feed()
        logging.info("rss_info : %s", feed_list)
        feed_dict[name] = feed_list


if __name__ == "__main__":
    main()
