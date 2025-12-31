#!/bin/bash
# SPDX-FileCopyrightText: 2025 Yuna Furuhata
# SPDX-License-Identifier: BSD-3-Clause

source ~/ros2_ws/src/install/setup.bash

ng () {
    echo "${1}行目が違うよ"
    res=1
}

res=0

ros2 run capital_pkg client_node.py フィリピン
status=$?

[ "$status" -eq 0 ] || ng "$LINENO"
echo "$out" | grep -q "マニラ" || ng "LINENO"

out=$(ros2 run capital_pkg client_node.py アメリカ
echo "$out" | grep -q "not found" || ng "$LINENO"

kill $SERVER_PID

[ "$res" = 0 ] && echo "OK"
exit $res
