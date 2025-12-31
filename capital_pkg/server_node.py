#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Yuna Furuhata
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from capital_pkg.srv import GetCapital # 自作型をインポート

class CapitalServer(Node):
    def __init__(self):
        super().__init__('capital_server')
        self.data = {"Japan": "Tokyo", "France": "Paris", "USA": "Washington D.C."}
        self.srv = self.create_service(GetCapital, 'get_capital', self.callback)
        self.get_logger().info('Server is Ready')

    def callback(self, request, response):
        data = {
                "インドネシア": "ジャカルタ",
                "フィリピン": "マニラ",
                "シンガポール": "シンガポール",
                "タイ": "バンコク",
                "マレーシア": "クアラルンプール",
                "ベトナム": "ハノイ",
                "ラオス": "ビエンチャン",
                "カンボジア": "プノンペン",
                "ミャンマー": "ネピドー",
                "ブルネイ": "バンダルスリブガワン",
                "東ティモール": "ディリ"
                }

        country = request.country_name
        self.get_logger().info(f'received request for: {country}')
        if country in data:
            response.capital_name = data[country]
            response.success = True
        else:
            response.capital_name = "Not Found"
            response.success = False

        return response

def main(args=None):
    rclpy.init(args=args)
    node = CapitalServer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

   
