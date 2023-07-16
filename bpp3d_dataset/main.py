import os
from pathlib import Path
from typing import List, Optional
import typer
from typer import Argument, Option
from typing_extensions import Annotated

from bpp3d_dataset.utils.distributions.discrete import Discrete
from .utils.problem_generation import discrete1d_generate, uniform1d_generate, normal1d_generate
from .problems.registration import bpp_registry

DEFAULT_1D_ITEMS = [i for i in range(10, 60, 5)]
DEFAULT_1D_CAPACITY = 100
DEFAULT_INSTANCE_NUM = 10

DEFAULT_INSTANCE_ITEM_NUM = 1000
DEFAULT_DISTRIBUTION = 'uniform'
DEFAULT_PATH = Path("data/")

app = typer.Typer()

generate_app = typer.Typer()
app.add_typer(generate_app, name="generate")
list_app = typer.Typer()
app.add_typer(list_app, name="list")


@list_app.command("all")
def list_all_problems():
    """List registered problems
    """
    print(list(bpp_registry.keys()))

@list_app.command("1d")
def list_1d_problems():
    """List registered 1d problems
    """
    print(list(k for k in bpp_registry.keys() if "1D" in k))

@generate_app.command("1d")
def dim1(distribution: Annotated[str, Argument(help="distribution name")] = DEFAULT_DISTRIBUTION, 
            items:Annotated[List[int], Option("-i", "--item", help="item kinds in the problem")] = DEFAULT_1D_ITEMS,
            probs:Annotated[Optional[List[float]], Option("-p", "--prob", 
                                                        help="probability list")] = None,
            capacity:Annotated[int, Option("-C", "--capacity", 
                                            help="bin capacity")] = DEFAULT_1D_CAPACITY,
            item_num:Annotated[int, Option("-N","--num-item", 
                                            help="item num per instance")] = DEFAULT_INSTANCE_ITEM_NUM,
            instance_num:Annotated[int, Option("-I", "--num-inst", 
                                                help="instance num")] = DEFAULT_INSTANCE_NUM,
            dir:Annotated[Path, Option("-d", "--dir", help="target data directory")] = DEFAULT_PATH,
            file:Annotated[Optional[str], Option("-f", "--file", help="target data file name")] = None):
    try:
        if not os.path.exists(dir):
            os.mkdir(dir)

        target_file = f"{distribution.capitalize()}1D.json" if not file else file
        target = dir / target_file

        if distribution.lower() == "uniform":
            uniform1d_generate(capacity, items, item_num, instance_num, target)
        elif distribution.lower() == "normal": 
            normal1d_generate(capacity, items, item_num, instance_num, target)
        elif distribution.lower() == "discrete": 
            assert probs is not None and len(probs) == len(items)
            discrete1d_generate(capacity, item_num, instance_num, Discrete(probs, items), target)
        else:
            raise NotImplementedError("Other distributions are not implemented yet.")
    except Exception:
        print("Generation Failed")
    

@generate_app.command("2d")
def dim2():
    print("Not Implemented")

@generate_app.command("3d")
def dim3():
    print("Not Implemented")

def main():
    app()
if __name__ == "__main__":
    # app()
    main()
