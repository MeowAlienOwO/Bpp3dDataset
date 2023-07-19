# import argparse
from pathlib import Path
from typing import List
from bpp3d_dataset.problems import Problem, Bpp1DRandomInitiator
from bpp3d_dataset.problems import store_problem
from bpp3d_dataset.utils.distributions.periodic import Periodic
from bpp3d_dataset.utils.distributions.discrete import generate_discrete_dist, generate_or_gym_dist


def discrete1d_generate(capacity: int, items: List, item_num: int, 
                        instance_num:int, name:str, path: Path | None = None, **kwargs) -> Problem:

    distr = generate_or_gym_dist(name) if 'or-gym' in name else generate_discrete_dist(items, name, **kwargs)
    problem = Problem(Bpp1DRandomInitiator(capacity, item_num, instance_num, distr))
    if path is not None:
        store_problem(problem, path)
    return problem

def discrete1d_periodic_generate(capacity: int, items: List, item_num: int, 
                                    sample_step: int,
                                    instance_num:int, names:List[str], 
                                    path: Path | None = None, **kwargs) -> Problem:
    distributions= [generate_or_gym_dist(dist) if 'or-gym' in dist 
                    else generate_discrete_dist(items, dist, **kwargs)
                    for dist in names]
    periodic = Periodic(distributions, sample_step)
    problem = Problem(Bpp1DRandomInitiator(capacity, item_num, instance_num, periodic))

    if path is not None:
        store_problem(problem, path)
    return problem

