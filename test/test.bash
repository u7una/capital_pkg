#!/bin/bash
# SPDX-FileCopyrightText: 2025 Yuna Furuhata
# SPDX-License-Identifier: BSD-3-Clause

ng () {
    echo "${1}行目が違うよ"
    res=1
}

res=0

source ./install/setup.bash || ng "$LINENO"

ros2 run capital_pkg server_node.py &
SERVER_PID=$!
sleep 5


out=$(ros2 run capital_pkg client_node.py フィリピン)
status=$?

[ "$status" -eq 0 ] || ng "$LINENO"
echo "$out" | grep -q "マニラ" || ng "$LINENO"

out=$(ros2 run capital_pkg client_node.py 日本)
echo "$out" | grep -q "Not found" || ng "$LINENO"

kill $SERVER_PID

[ "$res" = 0 ] && echo "OK"
exit $res
