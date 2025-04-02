# ProtocolV4
- libcanard的h：
551af7f
- public_regulated_data_types：
f9f6790
## 所需python包:
`pip install pycyphal -i https://pypi.tuna.tsinghua.edu.cn/simple`
## .c/.h文件的生成
```
nnvg --target-language c --outdir .cFolder --lookup-dir ./public_regulated_data_types/reg ./public_regulated_data_types/uavcan

nnvg --target-language c --outdir .cFolder --lookup-dir  ./public_regulated_data_types/uavcan ./custom_data_types
```

## pyqt6安装
- `pip install PyQt6 PyQt6-tools -i https://pypi.tuna.tsinghua.edu.cn/simple`
- `qt designer`安装位置“.myvenv/lib/python3.x/site-packages/qt6_applications/Qt/bin/designer”
- 首次运行报错，执行`export QT_QPA_PLATFORM=xcb`
- 将designer添加到当前虚拟环境下的环境变量
    - 打开.myvenv/bin/active文件，在末尾添加`alias designer="$VIRTUAL_ENV/lib/python3.10/site-packages/qt6_applications/Qt/bin/designer"  `
    - 关闭虚拟环境重新打开后生效
### python调用ui文件
使用生成的 .py 文件（推荐）‌
将 .ui 文件转换为 Python 代码，再通过继承调用。
‌步骤：‌
    ‌生成 .py 文件‌
    使用 `pyuic6` 工具将 .ui 文件转换为 Python 代码：
    `pyuic6 your_ui_file.ui -o ui_mainwindow.py`
