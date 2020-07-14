# ansible-role-prometheus [![Build Status](https://travis-ci.org/izumimatsuo/ansible-role-prometheus.svg?branch=master)](https://travis-ci.org/izumimatsuo/ansible-role-prometheus)

監視機能を導入するansible-roleです

対象のコンポーネントは以下

| コンポーネント | 概要 |
| -------------- | ---- |
| node_exporter  | 各ノードのメトリクス情報を収集する |
| blackbox_exporter | 外形監視メトリクス情報を収集する |
| prometheus     | メトリクスを収集・蓄積する |
| alertmanager   | アラート通知する |

## 設定項目

以下の設定項目は上書き可能。

| 項目名             | デフォルト値| 説明               |
| ------------------ | ----------- | ------------------ |
| prometheus_server | yes          | サーバへ導入       |
| prometheus_storage_path | /var/lib/prometheus | データディレクトリ |
| prometheus_tsdb_retention_time | 15d | データ保存期間 |
