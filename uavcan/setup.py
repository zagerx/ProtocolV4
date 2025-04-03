from setuptools import setup, find_packages

setup(
    name="myproject",
    version="0.1.0",
    # 显式声明所有包（避免自动发现失败）
    packages=[
        "dinosaurs",
        "reg",
        "uavcan",
        "uavcan.time"  # 嵌套子包需单独声明
    ],
    package_dir={
        "": ".pyFolder",        # 根包映射到 .pyFolder
        "dinosaurs": ".pyFolder/dinosaurs",
        "reg": ".pyFolder/reg",
        "uavcan": ".pyFolder/uavcan"
    },
    install_requires=[
        "pycyphal>=1.20",
        "uavcan[dsdl]==1.0.0.dev35",
        "numpy>=1.20.0",
        "requests"
    ],
    python_requires=">=3.10",
)
