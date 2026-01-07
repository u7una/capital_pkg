# capital_pkg
![Capital Package CI](https://github.com/u7una/capital_pkg/actions/workflows/capital.yml/badge.svg)

ROS 2 Humble を使用した、東南アジアの国名から首都名を検索するサービス通信用のパッケージです。 

---

## 概要
このパッケージはカスタムサービス(.srv)を使用して以下の機能を提供します。
* **Server**: 国名のリクエストを受け取り、対応する首都名を返します。
* **Client**: コマンドライン引数から国名を受け取り、サーバーへ問い合わせて結果を表示します。

## サービス仕様

### ノード一覧
| ノード名 | 役割 | サービス名 | サービス型 |
|----------|------|------------|------------|
| `capital_server` | 国名を受け取り対応する首都名を返す | `get_capital` | `capital_pkg/srv/Capital` | 
| `capital_client` | 入力をサーバーに送信し、結果を表示 | `get_capital` | `capital_pkg/srv/Capital` |

### サービス型の表
| 変数名 | 型 | 内容 |
|:------:|:--:|:----:|
| `country_name` | `string` | 検索したい国名 |
| `capital_name` | `string` | 首都名 |
| `success` | `bool` | データが見つかれば`true`、なければ`false` |

---

## 動作環境
* OS: Ubuntu 22.04 LTS
* ROS 2 Distribution: Humble
* Python: 3.10

## テスト済み環境
* OS: Ubuntu 22.04
* ROS 2 Version: Humble

---

## インストール方法
あらかじめROS 2 のインストールをしてください。
```bash
# このリポジトリをクローン
# ros_2wsは各自のワークスペース名に変更してください
$ cd ~/ros2_ws/src
$ git clone https://github.com/u7una/capital_pkg.git

# ビルドを実行
$ cd ~/ros2_ws
$ colcon build
$ source install/setup.bash

```
---

## 使い方


### 1. サーバーの起動
```bash
# 新しいターミナルで実行してください
$ ros2 run capital_pkg server_node.py
```

### 2. クライアントの実行
```bash
# 別のターミナルを開き、国名を指定して実行してください
$ ros2 run capital_pkg client_node.py [国名]

```
---

## 実行結果

### サーバー側
サーバーが起動すると、以下のように表示されます。
```text
[INFO] [1767016277.263041563] [capital_server]: Server is Ready
[INFO] [1767016296.380670087] [capital_server]: received request for: フィリピン
```

### クライアント側
リクエストを受信すると指定した国名に対応する首都名が表示されます。
```text
Capital: マニラ
```

## ライセンス
* このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
---
© 2025 Yuna Furuhata
