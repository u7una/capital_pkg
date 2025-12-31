# capital_pkg
![CI Status](https://github.com/u7una/capital_pkg/blob/main/.github/workflows/capital.yml)

ROS 2 Humble を使用した、東南アジアの国名から首都名を検索するサービス通信用のパッケージです。 

---

## 概要
このパッケージはカスタムサービス(.srv)を使用して以下の機能を提供します。
* **Server**: 国名のリクエストを受け取り、対応する首都名を返します。
* **Client**: コマンドライン引数から国名を受け取り、サーバーへ問い合わせて結果を表示します。

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
$ git clone https://git.com/u7una/capital_pkg.git

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
サーバーが起動すると、リクエスト待機状態になります。
```text
yuna@DESKTOP-300LQJ8:~/ros2_ws$ ros2 run capital_pkg server_node.py
[INFO] [1767016277.263041563] [capital_server]: Server is Ready
[INFO] [1767016296.380670087] [capital_server]: received request for: フィリピン
```

### クライアント側
国名を引数として渡すと、サーバーから取得した首都名を表示します。
```text
yuna@DESKTOP-300LQJ8:~/ros2_ws$ ros2 run capital_pkg client_node.py フィリピン
Capital: マニラ
```

## ライセンス
* このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
---
© 2025 Yuna Furuhata
