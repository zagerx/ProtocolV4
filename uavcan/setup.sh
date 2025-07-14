#!/bin/bash
set -e

# 激活虚拟环境
source .myvenv/bin/activate

# 安装必要依赖
pip install pyinstaller parsimonious --upgrade

# 清理旧构建
rm -rf build dist

# 打包命令 - 不再需要添加额外数据文件
pyinstaller \
    --onefile \
    --name "MotorAsstor" \
    --hidden-import=parsimonious \
    --hidden-import=pycyphal.dsdl \
    --clean \
    MotorAsst/src/main.py

# 创建运行目录结构
mkdir -p dist/MotorAsst/output
mkdir -p dist/MotorAsst/logs
mkdir -p dist/MotorAsst/config

# 复制默认配置文件（如果需要）
# cp config/default.yaml dist/MotorAsst/config/

# 设置可执行权限
chmod +x dist/MotorAsst

echo -e "\n\033[32m打包成功！\033[0m"
echo "可执行文件: dist/MotorAsst"
echo "输出目录: dist/MotorAsst/output"
echo "日志目录: dist/MotorAsst/logs"