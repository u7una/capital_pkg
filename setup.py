from setuptools import find_packages, setup

package_name = 'capital_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yuna',
    maintainer_email='s24c1107ca@s.chibakoudai.jp',
    description='東南アジアの国名から首都名を出す',
    license='BSD-3-Clause',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'server_node = capital_pkg.server_node:main',
            'client_node = capital_pkg.client_node:main',
        ],
    },
)
