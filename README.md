# capital_pkg

ROS 2 Humble を使用した、東南アジアの国名から首都名を検索するサービス通信用のパッケージです。 

---

## 概要
このパッケージはカスタムサービス(.srv)を使用して以下の機能を提供します。
* **Server**: 国名のリクエストを受け取り、対応する首都名を返します。
* **Client**: コマンドライン引数から国名を受け取り、サーバーへ問い合わせて結果を表示します。

---

## 動作環境
* OS: Ubuntu 22.04 LTS
* ROS 2 : Humble
* 言語: Python

---

## インストール方法
あらかじめROS 2 のインストールをしてください。
```bash
# このリポジトリをクローン
# ros_2wsは各自のワークスペース名に変更してください
$ cd ~/ros2_ws/src
$ git clone https://git.com/u7una/capital_pkg.git

# ビルドを実行
$ cd ~/ros2_ws
$ colcon build
$ source install/setup.bash

```
---

## 使い方

```bash

# 1. サーバーの起動

# 新しいターミナルで実行してください
$ ros2 run capital_pkg server_node.py

# 2. クライアントの実行

# 別のターミナルで、国名を指定して実行しれください
$ ros2 run capital_pkg client_node.py [国名]

```
## ライセンス
