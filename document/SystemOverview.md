# システム概要

## 目的

媒体 API のアップデート情報を取得し、GPT を活用して日本語レポートとしてまとめたい。

## ユースケース

1. 媒体アップデート情報を早めに検知し、プロダクト影響があるのかを検知したい。
1. 媒体 API の変更による修正対応を迅速にするため。

## 運用イメージ

### ワークフロー

```mermaid
flowchart TD;
  subgraph a[workflow]
    b-->c-->d
    データ基盤以外の人-->e
  end

  subgraph b[媒体アップデート検知]
  end

  subgraph c[朝会（出社日拡大版）]
    c1[最近のアップデート情報の共有会]-->
    c2[優先度の確認]
  end

  subgraph d[スプリントプランニング会]
    d1[優先度とスケジュールに\n合わせてプランニング]
  end

  subgraph e[アップデート確認]
    e1[slackの要約確認]
    e2[notionのDB参照]
  end
```

### システムフロー

```mermaid
flowchart TD;
  subgraph a[Lambda_rss_reader]
    a1[start]-->|cron起動|b[データ取得]
    b-->c
  end

  subgraph b[データ取得]
    b1[request rss url]-->b2[get_rss_message]
  end

  subgraph c[GPT レポート生成]
  end

  subgraph d[outputs]
    c-->d1[slack通知]
    c-->d2[!notion DB]
    c-->d3[!変更スケジュールカレンダー追記]
    c-->d4[!チケット起票]
  end
```

!は発展系

## .env について

| key            | description                              | 備考                                      |
| -------------- | ---------------------------------------- | ----------------------------------------- |
| OPENAI_API_KEY | OpenAI へのリクエストに必要になる APIkey | 現状開発者（林田）の自前の API key を利用 |
