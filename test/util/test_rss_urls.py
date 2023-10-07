from src.util.rss_urls import RssUrls


def test_get_rss_url():
    """正常系のテスト"""
    ans = [
        {
            "url": "http://feeds.feedburner.com/GoogleAdsDeveloperBlog",
            "description": "Google Ads API RSS URL",
        }
    ]
    rss_urls = RssUrls()
    assert rss_urls.rss_url == ans
