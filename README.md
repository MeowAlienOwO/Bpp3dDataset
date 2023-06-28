

3D BPP 数据集部分

# Features
数据导出
- [ ] 提供结构化的数据文本文件供后续处理
- [ ] 提供读写数据的module

数据生成
- [ ] 将不同类型的数据集转化为统一格式
    - [ ] (TODO 数据集)
- [ ] 随机生成的数据
    - [ ] 存储数据

接口
- [ ] 命令行
- [ ] 模块导入


# How to use

## Install

```bash
python -m pip install .
```

# Development

- POSIX环境(Unix/Linux)或者Docker环境, Windows下开发请使用WSL/Docker
- 遵循 PEP8 规范, 使用 `ruff` 作为linter 
- 避免使用`sys.path.append`, 使用临时的变量替代: `export PYTHONPATH="YOUR/PATH:$PYTHONPATH"` 或者走包安装流程



