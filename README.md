# ansible-role-prometheus [![Build Status](https://travis-ci.org/izumimatsuo/ansible-role-prometheus.svg?branch=master)](https://travis-ci.org/izumimatsuo/ansible-role-prometheus)

CentOS7 へ監視機能を導入するansible-roleです

対象のコンポーネントは以下

| コンポーネント    | 概要                               |
| ----------------- | ---------------------------------- |
| node_exporter     | 各ノードのメトリクス情報を収集する |
| blackbox_exporter | 外形監視メトリクス情報を収集する   |
| prometheus_server | メトリクスを収集・蓄積する         |
| alertmanager      | アラート通知する                   |

監視対象は、以下のファイルを設定する

| ファイル名                          | 監視項目                       | 設定内容                   |
| ----------------------------------- | ------------------------------ | -------------------------- |
| /etc/prometheus/targets/service.yml | service の死活、レイテンシ監視 | URL を設定                 |
| /etc/prometheus/targets/node.yml    | node の死活、リソース監視      | ホスト名かIPアドレスを設定 |

node_exporter の --collector.textfile.directory オプションを利用して独自のメトリクスを収集可能

- prometheus_storage_path で指定したデータディレクトリにメトリクスデータを記述したファイルを配置する
- デフォルト値だと ```/var/lib/prometheus/collector``` に ```*.prom``` ファイルを配置する

## 設定項目

以下の設定項目は上書き可能。

| 項目名                         | デフォルト値        | 説明               |
| ------------------------------ | ------------------- | ------------------ |
| prometheus_is_server           | no                  | サーバへ導入       |
| prometheus_storage_path        | /var/lib/prometheus | データディレクトリ |
| prometheus_tsdb_retention_time | 30d                 | データ保存期間     |
| blackbox_probe_http_target     | []                  | http service リスト |
| blackbox_probe_http_skip_verify | no                 | SSL証明書検証をスキップ |
| alert_email_host               | none                | メールホスト       |
| alert_email_from               | none                | メール送信元       |
| alert_email_to                 | none                | メール送信先       |

## アラート通知のルール

### job名: prometheus

| アラート名                           | severity | 閾値     | 説明                  |
| ------------------------------------ | -------- | -------- | --------------------- |
| PrometheusTargetMissing              | warning  | 0        | exporter 障害         |

### job名: blackbox_exporter_icmp/http

| アラート名                           | severity | 閾値     | 説明                  |
| ------------------------------------ | -------- | -------- | --------------------- |
| BlackboxProbeFailed                  | warning  | 0        | ネットワーク到達不能  |
| BlackboxProbeHttpFailure             | critical | 200-399  | HTTP ステークスコード |
| BlackboxProbeSlowHttp                | warning  | > 1s     | HTTP レスポンス時間   |
| BlackboxSslCertificateWillExpireSoon | warning  | < 30days | SSL証明書更新期日     |

### job名: node_exporter

| アラート名                      | severity | 閾値      | 説明                            |
| ------------------------------- | -------- | --------- | ------------------------------- |
| HostHighCpuLoad                 | warning  | > 90%     | CPU 使用率                      |
| HostHighCpuLoadAverage          | warning  | > 1       | CPU ロードアベレージ（1分）     |
| HostOutOfMemory                 | warning  | > 90%     | メモリ使用率                    |
| HostSwapIsFillingUp             | warning  | > 90%     | Swap メモリ使用率               |
| HostOutOfDiskSpace              | warning  | > 90%     | ディスク使用率                  |
| HostDiskWillFillIn6Hours        | warning  | < 0       | 6時間以内にディスクフルになるか |
| HostUnusualDiskReadLatency      | warning  | > 100ms   | ディスクへの書き込み時間        |
| HostUnusualDiskWriteLatency     | warning  | > 100ms   | ディスクからの読み込み時間      |
| HostUnusualNetworkThroughputIn  | warning  | > 100MB/s | ネットワーク受信データ量        |
| HostUnusualNetworkThroughputOut | warning  | > 100MB/s | ネットワーク送信データ量        |
| HostNetworkDrops                | warning  | > 0       | ネットワークDrop数              |
| HostNetworkErrors               | warning  | > 0       | ネットワークエラー数            |
