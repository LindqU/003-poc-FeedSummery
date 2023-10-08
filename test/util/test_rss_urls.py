from src.util.rss_info import RssInfo


def test_get_rss_url():
    """正常系のテスト"""
    ans = [
        {
            "url": "http://feeds.feedburner.com/GoogleAdsDeveloperBlog",
            "description": "Google Ads API RSS URL",
        }
    ]
    rss_urls = RssInfo.get_rss_infos()
    assert rss_urls == ans
