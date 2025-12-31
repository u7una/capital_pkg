#!/usr/bin/python3
# SPDX-FileCopyrightText: 2025 Yuna Furuhata
# SPDX-License-Identifier: BSD-3-Clause
import sys
import rclpy
from rclpy.node import Node
from capital_pkg.srv import GetCapital

def main():
    if len(sys.argv) < 2:
        print("Usage: ros2 run capital_pkg client_node <Country>")
        return

    rclpy.init()
    node = rclpy.create_node('capital_client')
    client = node.create_client(GetCapital, 'get_capital')
    
    while not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('waiting...')

    req = GetCapital.Request()
    req.country_name = sys.argv[1]
    
    future = client.call_async(req)
    rclpy.spin_until_future_complete(node, future)
    
    res = future.result()
    if res.success:
        print(f"Capital: {res.capital_name}")
    else:
        print("Not found")

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
