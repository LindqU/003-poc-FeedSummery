from rss.rss import RssReader

RSS_URL = "http://feeds.feedburner.com/GoogleAdsDeveloperBlog"

rss_reader = RssReader(RSS_URL)

feed_list = rss_reader.get_feed()


