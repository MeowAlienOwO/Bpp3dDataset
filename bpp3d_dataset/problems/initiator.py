import json
from pathlib import Path

from typing import Dict, List
from bpp3d_dataset.problems.bppinstance import BppInstance
from bpp3d_dataset.utils.distributions import Discrete


class ProblemInitiator(object):

    def initialize_problem(self) -> List['BppInstance']:
        raise NotImplementedError

    def initialize_configuration(self) -> Dict:
        raise NotImplementedError

    @property
    def dim(self) -> int:
        return self._dim

    @dim.setter
    def dim(self, value: int) -> None:
        self._dim = value



class Bpp1DJsonInitiator(ProblemInitiator):
    """Initialize problem with a json file or string.
    The problem json defines as following:
    [
        {
            "configuration": {...},
            "sequence": 
            [
                {...instance 1}, //number,array-like vector, specific item definition, etc
                {...instance 2},
            ]
        }
    ]

    """

    def __init__(self, problem_data: Path | str):
        """

        Args:
            problem_data (Path | str): problem data file or string, must in correct json format
            dim (int, optional): dimension number. Defaults to 1.
        """
        if isinstance(problem_data, Path):
            with open(problem_data, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = json.loads(problem_data)
        self.dim = 1

    def initialize_problem(self) -> List[BppInstance]:
        return [BppInstance(inst["sequence"], inst["configuration"]) 
                    for inst in self.data['instances']]

    def initialize_configuration(self) -> Dict:
        return self.data['configuration']


class Bpp1DRandomInitiator(ProblemInitiator):
    def __init__(self, capacity: int, item_num: int, 
                    instance_num: int, distribution: Discrete):
        """

        Args:
            capacity (int): bin capacity
            item_num (int): number of items should be generated for each instance
            instance_num (int): number of instances in the problem set
            distribution (Discrete): sample instance by distribution
        """
        self.item_num = item_num
        self.instance_num = instance_num
        self.distribution = distribution
        self.capacity = capacity
        self.dim = 1
    
    @property
    def configuration(self) -> Dict:
        return {
            "distribution": self.distribution.prob_dict,
            "capacity": self.capacity,
            "item_num": self.item_num
        }


    def initialize_problem(self) -> List[BppInstance]:

        return [BppInstance(self.distribution.sample(self.item_num)
            , self.configuration) for _ in range(self.instance_num)]

    def initialize_configuration(self) -> Dict:
        return self.configuration