from datapipeline.get_feed.lambda_function import lambda_handler
import pytest


def test_lambda_handler(monkeypatch: pytest.MonkeyPatch):

  monkeypatch.setattr("sys.stdin.readline", )
  assert True

