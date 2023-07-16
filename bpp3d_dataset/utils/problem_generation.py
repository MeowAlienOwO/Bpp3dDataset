import argparse
from pathlib import Path
from typing import List
from bpp3d_dataset.problems import Problem, Bpp1DRandomInitiator
from bpp3d_dataset.problems import store_problem
from bpp3d_dataset.utils.distributions import Uniform, Binomial, Discrete


def uniform1d_generate(capacity: int, types: List[int], 
                            item_num: int, instance_num: int, path: Path | None = None) -> Problem:
    """Generate a single 1D uniform distribution problem

    Args:
        capacity (int): bin capacity
        type (List[int]): list of types, indicate each size of type
        item_num (int): number of items
        instance_num (int): number of instances
        path (Path): **Json** data file to be saved, 
    """

    return discrete1d_generate(capacity, item_num, instance_num, Uniform(types), path)

def normal1d_generate(capacity: int, types: List[int], 
                            item_num: int, instance_num: int, path: Path | None = None) -> Problem:
    """Generate a single 1D normal distribution problem

    Args:
        capacity (int): bin capacity
        type (List[int]): list of types, indicate each size of type
        item_num (int): number of items
        instance_num (int): number of instances
        path (Path): **Json** data file to be saved, 
    """
    return discrete1d_generate(capacity, item_num, instance_num, Binomial(types), path)


def discrete1d_generate(capacity: int,
                            item_num: int, instance_num: int, distribution: Discrete, 
                            path: Path | None = None) -> Problem:
    """Generate a single 1d problem with given discrete distribution

    Args:
        capacity (int): bin capacity
        item_num (int): item num in each instance
        instance_num (int): number of instances
        distribution (Discrete): distribution specification
        path (Path | None, optional): **Json** datafile to be stored. Defaults to None.

    Returns:
        Problem: _description_
    """


    problem = Problem(Bpp1DRandomInitiator(capacity, item_num, instance_num, distribution))
    if path is not None:
        store_problem(problem, path)
    return problem

def generate_all_1d(data_path: Path):
    items = [i for i in range(10, 60, 5)]
    uniform1d_generate(100, items, 1000, 100, data_path / "Uniform1D.json")
    normal1d_generate(100, items, 1000, 100, data_path / "Normal1D.json")
    discrete1d_generate(100,  1000, 100, 
                        Discrete([0.2, 0.05, 0.1, 0.12,0.08, 0.05, 0.03, 0.01, 0.18, 0.18], items), 
                        data_path / "Discrete1D.json")
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = 'bpp3d_dataset.utils.problem_generation', 
                                        description='A tool of generating problem files')

    parser.add_argument('-d', '--data-dir', dest='data_dir', default="", type=Path)
    args = parser.parse_args()
    
    generate_all_1d(args.data_dir)
