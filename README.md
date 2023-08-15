
A dataset for 1D-3D Bin Packing Problems.

Currently, the package contains only 1D bin packing problem instances.

# How to use


## Installation

```bash

pip install poetry
poetry install
```

## Command Line Interface

Show the problem included in package
```bash
python -m bpp3d_dataset.main list all

```

Generate a series of problem instances

```bash
python -m bpp3d_dataset.main generate 1d uniform -C 100 -N 1000 -I 100 -d your/directory -f "Problem-Name.json"
```


