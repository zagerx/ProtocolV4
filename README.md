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