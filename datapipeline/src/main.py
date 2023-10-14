"""
main.py
"""
from rss.rss import RssReader
from util.rss_info import RssInfo
from typing import List, Dict
from util.log import logger
from llm.base_prompt import BasePrompt, OutputSchema
import copy
import json
from datetime import datetime
import uuid


def main() -> str:
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
        feed_list = rss_reader.get_feed(date_duration=30)
        logger.debug("rss_info : %s", feed_list)
        feed_dict[name] = feed_list
    # file exportは実装する...？
    # 例えば、bigqueryのテーブルにインサートする的なノリのもの。

    # 要約レポート作成部分
    # 要約レポート作成部分は、別のlambdaでもいいかもしれない。
    # 根拠：全てのレポート作成に時間がかかる可能性がある。その場合、1レポート生成に1lambdaの方がコスト面でいいかもしれない。
    reports = copy.deepcopy(feed_dict)
    for feed_key, feeds in feed_dict.items():
        logger.debug("feed key is %s", feed_key)
        idx: int
        feed: Dict[str, List[Dict[str, str]]]
        for idx, feed in enumerate(feeds):
            logger.info("feed_title : %s", feed["title"])
            base_prompt = BasePrompt(output_schema=OutputSchema)
            query = f"下記のメッセージについて\n-どのような広告で\n-いつから\n-どのような変更があるのか\nを答えてください。\n---------\n{feed['summary']}"
            base_prompt.gen_prompt(query)
            logger.debug("query : %s", query)
            logger.debug("API Requst Prompt : %s", base_prompt.get_prompt())
            # response = base_prompt.run_prompt()
            response = "hogehoge"
            logger.info("report生成完了")
            logger.debug("report : %s", response)
            reports[feed_key][idx]["report"] = response

    # 本来だったら、ここでslack通知に繋げたいけど、jsonファイルにexportする。
    OUTPUT_PATH = "src/outputs/"
    # 一意のID（UUID）を生成
    unique_id = uuid.uuid4()
    # 現在の日付と時刻を取得
    current_datetime = datetime.now().strftime("%Y%m%d-%H%M%S")
    # 一意のファイル名を生成
    unique_filename = f"{current_datetime}_{unique_id}.json"

    with open(OUTPUT_PATH + unique_filename, "w", encoding="utf-8") as json_file:
        json.dump(reports, json_file)

    return OUTPUT_PATH + unique_filename


if __name__ == "__main__":
    main()
