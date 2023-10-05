"""
rss feed readerによるrssのリクエストモジュール
"""
import feedparser
from datetime import datetime, timezone, timedelta
import logging

# loggerの設定
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


class RssReader:
    def __init__(self, rss_url: str):
        self.rss_url = rss_url

    def get_feed(self, date_duration: int = 7, n: int = None):
        feeds = feedparser.parse(self.rss_url)

        today = datetime.now(timezone.utc)
        limit_date = today - timedelta(days=date_duration)

        logger.debug("feedsの取得開始")
        feed_list = []

        for feed in feeds.entries:
            dt = datetime.fromisoformat(feed.published)
            dt_utc = dt.astimezone(timezone.utc)
            if limit_date <= dt_utc:
                logger.info("feed title : %s\nfeed link : %s", feed.title, feed.link)
                logger.debug("feed summary : %s", feed.summary)
                feed_list.append(
                    {"title": feed.title, "link": feed.link, "summary": feed.summary}
                )
            else:
                logger.info(
                    "FEED distribution dates are no longer in the search range."
                )
                break

        logger.debug("feedsの取得完了")

        return feed_list
