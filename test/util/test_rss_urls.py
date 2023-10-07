from src.util.rss_info import RssUrls


def test_get_rss_url():
    """正常系のテスト"""
    ans = [
        {
            "url": "http://feeds.feedburner.com/GoogleAdsDeveloperBlog",
            "description": "Google Ads API RSS URL",
        }
    ]
    rss_urls = RssUrls.get_rss_urls()
    assert rss_urls == ans
