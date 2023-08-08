import os
from pathlib import Path
from typing import List, Optional
import typer
from typer import Argument, Option
from typing_extensions import Annotated
import random
import numpy as np

from bpp3d_dataset.utils.distributions.discrete import DEFAULT_1D_ITEMS
from .utils.problem_generation import discrete1d_generate, discrete1d_periodic_generate
from .problems.registration import bpp_registry

# DEFAULT_1D_ITEMS = [i for i in range(10, 60, 5)]
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

# @list_app.command("1d")
# def list_1d_problems():
#     """List registered 1d problems
#     """
#     print(list(k for k in bpp_registry.keys() if "1D" in k))
    
@list_app.command("search")
def list_1d_problems(keyworkd: str):
    """List registered 1d problems
    """
    print(list(k for k in bpp_registry.keys() if keyworkd in k))

@generate_app.command("1d")
def dim1(distribution: Annotated[str, Argument(help="distribution name")] = DEFAULT_DISTRIBUTION, 
            items:Annotated[List[int], Option("-i", "--item", help="item kinds in the problem")] = DEFAULT_1D_ITEMS,
            item_range: Annotated[Optional[List[int]], Option("--ir", "--item-range", help="item range")] = None,
            item_step: Annotated[Optional[int], Option("--is", "--item-step", help="item step")] = 1,
            probs:Annotated[Optional[List[float]], Option("-p", "--prob", 
                                                        help="probability list")] = None,
            capacity:Annotated[int, Option("-C", "--capacity", 
                                            help="bin capacity")] = DEFAULT_1D_CAPACITY,
            item_num:Annotated[int, Option("-N","--num-item", 
                                            help="item num per instance")] = DEFAULT_INSTANCE_ITEM_NUM,
            instance_num:Annotated[int, Option("-I", "--num-inst", 
                                                help="instance num")] = DEFAULT_INSTANCE_NUM,
            dir:Annotated[Path, Option("-d", "--dir", help="target data directory")] = DEFAULT_PATH,
            file:Annotated[Optional[str], Option("-f", "--file", help="target data file name")] = None,
            seed:Annotated[Optional[int], Option("-s", "--seed", help="seed")] = 42):

    random.seed(seed)
    np.random.seed(seed)
    # try:
    if not os.path.exists(dir):
        os.mkdir(dir)

    target_file = f"{distribution.capitalize()}1D.json" if not file else file
    target = dir / target_file
    if item_range:
        items = list(range(item_range[0], item_range[1], item_step))
    discrete1d_generate(capacity, items, item_num, instance_num, distribution, target, probs=probs)

    
@generate_app.command("periodic1d")
def dim1_periodic(distributions: Annotated[Optional[List[str]], 
                                            Argument(help="add distribution to list")],
                    capacity:Annotated[int, Option("-C", "--capacity", 
                                            help="bin capacity")] = DEFAULT_1D_CAPACITY,
                    items:Annotated[List[int], Option("-i", "--item", 
                                            help="item kinds in the problem")] = DEFAULT_1D_ITEMS,
                    item_num:Annotated[int, Option("-N","--num-item", 
                                                    help="item num per instance")] = DEFAULT_INSTANCE_ITEM_NUM,
                    sample_step:Annotated[int, Option("-S","--sample-step", 
                                                    help="item num per instance")] = DEFAULT_INSTANCE_ITEM_NUM,
                    instance_num:Annotated[int, Option("-I", "--num-inst", 
                                                        help="instance num")] = DEFAULT_INSTANCE_NUM,
                    dir:Annotated[Path, Option("-d", "--dir", help="target data directory")] = DEFAULT_PATH,
                    file:Annotated[Optional[str], Option("-f", "--file", help="target data file name")] = None,
                    seed:Annotated[Optional[int], Option("-s", "--seed", help="seed")] = 42
                    ): 
    random.seed(seed)
    np.random.seed(seed)
    
    if not os.path.exists(dir):
        os.mkdir(dir)

    target_file = "Periodic1D.json" if not file else file
    target = dir / target_file
    if not distributions:
        print("no distribution specified")
        return
    
    discrete1d_periodic_generate(capacity, items, item_num, sample_step, instance_num, distributions, target)






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
