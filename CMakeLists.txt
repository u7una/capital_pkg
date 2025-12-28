cmake_minimum_required(VERSION 3.8)
project(capital_pkg)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclpy REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# srvのビルド設定
rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/GetCapital.srv"
)

# Pythonノードのインストール設定
#ament_python_install_package(${PROJECT_NAME} PACKAGE_DIR ${PROJECT_NAME})

install(PROGRAMS
  capital_pkg/server_node.py
  capital_pkg/client_node.py
  DESTINATION lib/${PROJECT_NAME}
)

# ローンチファイルのインストール
#install(DIRECTORY launch DESTINATION share/${PROJECT_NAME})

ament_package()
