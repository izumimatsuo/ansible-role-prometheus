# ansible-role-prometheus [![Build Status](https://travis-ci.org/izumimatsuo/ansible-role-prometheus.svg?branch=master)](https://travis-ci.org/izumimatsuo/ansible-role-prometheus)

CentOS7 へ監視機能を導入するansible-roleです

対象のコンポーネントは以下

| コンポーネント    | 概要                               |
| ----------------- | ---------------------------------- |
| node_exporter     | 各ノードのメトリクス情報を収集する |
| blackbox_exporter | 外形監視メトリクス情報を収集する   |
| prometheus_server | メトリクスを収集・蓄積する         |
| alertmanager      | アラート通知する                   |

## 設定項目

以下の設定項目は上書き可能。

| 項目名                         | デフォルト値        | 説明               |
| ------------------------------ | ------------------- | ------------------ |
| prometheus_server              | no                  | サーバへ導入       |
| prometheus_storage_path        | /var/lib/prometheus | データディレクトリ |
| prometheus_tsdb_retention_time | 15d                 | データ保存期間     |

## アラート通知のルール

### prometheus

| アラート名                           | severity | 閾値     | 説明                  |
| ------------------------------------ | -------- | -------- | --------------------- |
| PrometheusTargetMissing              | warning  | 0        | exporter 障害         |

### blackbox_exporter

| アラート名                           | severity | 閾値     | 説明                  |
| ------------------------------------ | -------- | -------- | --------------------- |
| BlackboxProbeFailed                  | warning  | 0        | ネットワーク到達不能  |
| BlackboxProbeHttpFailure             | critical | 200-399  | HTTP ステークスコード |
| BlackboxProbeSlowHttp                | warning  | > 1s     | HTTP レスポンス時間   |
| BlackboxSslCertificateWillExpireSoon | warning  | < 30days | SSL証明書更新期日     |

### node_exporter

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
