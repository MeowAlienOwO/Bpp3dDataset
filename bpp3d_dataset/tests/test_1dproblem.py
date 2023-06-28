from pathlib import Path
from bpp3d_dataset.problems import ProblemSpec
from bpp3d_dataset.utils.distributions import Discrete
from bpp3d_dataset.problems import Problem, Bpp1DRandomInitiator, Bpp1DJsonInitiator, Storage
from bpp3d_dataset.problems import make_bpp
import json


PROBLEM_1D = [
    {
        "configuration":{
            "capacity": 10
        },
        "sequence": list(range(1, 11)),
    },
    {
        "configuration":{
            "capacity": 15
        },
        "sequence": list(range(1, 11))[::-1],
    },
]


def test_readproblem(tmp_path: Path) -> None:

    with open(tmp_path / "problem.json", "w+") as f:
        json.dump(PROBLEM_1D, f)

    problem = Problem(Bpp1DJsonInitiator(tmp_path / "problem.json"), ProblemSpec('test1d'))
    assert len(problem.instances) == 2

    for prob_instance, real_instance in zip(problem.instances, PROBLEM_1D):
        assert len(prob_instance) == len(real_instance["sequence"])
        for i in range(len(real_instance)):
            assert prob_instance[i] == real_instance["sequence"][i]


def test_random_problem(tmp_path: Path) -> None:
    capacity= 10
    item_num = 10
    instance_num = 3
    distribution = Discrete([0.2, 0.3, 0.1, 0.2, 0.2], [1,2,3,4,5])
    

    problem = Problem(Bpp1DRandomInitiator(capacity, item_num, 
                                            instance_num, distribution), 
                                            ProblemSpec('test1d'))

    storage = Storage(problem)
    storage.save(tmp_path / "problem2.json")
    problem2 = Problem(Bpp1DJsonInitiator(tmp_path / "problem2.json"), ProblemSpec('test1d'))

    for i in range(instance_num):
        for j in range(item_num):
            assert problem[i][j] == problem2[i][j]

def test_make_problem() -> None:
    make_bpp("Discrete1D")
    make_bpp("Normal1D")
    make_bpp("Uniform1D")