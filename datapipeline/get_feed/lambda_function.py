"""
descripiton : 登録されているfeedの内容を取得するためのlambda
input : None or Feed List
Output: Feedのtitle, link, summaryを含むjson
"""
import os
import json
from typing import Dict
from src.util.log import logger
from src.rss.rss import RssReader
from src.util.SQS import send_message_queue


def lambda_handler(event, context):
    """feedの取得を行うlambda"""
    logger.debug("feedの取得を開始します。")
    logger.debug("event : %s", event)
    logger.debug("context : %s", context)

    next_queue_name = os.getenv("FEED_SUMMARY_SQS_NAME", "")
    dlq_name = os.getenv("GET_FEED_DLQ_NAME", "")

    for record in event["Recorda"]:
        message = json.loads(record["body"])
        try:
            logger.debug("record: %s", record)
            for rss_info in message:
                rss_info: Dict
                name = rss_info.get("name")
                description = rss_info.get("description")
                url = rss_info.get("url")
                logger.info("rss_name : %s description : %s", name, description)
                rss_reader = RssReader(rss_url=url)
                feed_list = rss_reader.get_feed()
                logger.debug("rss_info : %s", feed_list)
                for feed in feed_list:
                    send_message_queue(next_queue_name, json.dumps(feed))
        except KeyError as e:
            logger.error("KeyErrorが発生しました。%s", e)
            send_message_queue(dlq_name, json.dumps(message))
        else:
            logger.info("正常に処理が完了しました。")
