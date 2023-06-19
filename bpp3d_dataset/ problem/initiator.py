import json
import numpy as np

from typing import List,Tuple
from instance import Instance
from bpp3d_dataset.utils.distribution.distribution import Discrete


class ProblemInitiator(object):
    def initialize_problem(self) -> List['Instance']:
        raise NotImplementedError



class Bpp1DJsonInitiator(ProblemInitiator):
    """Initialize problem with a json file.
    The problem json file defines as following:
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

    def __init__(self, problem_file):
        with open(problem_file, 'r') as f:
            self.data = json.load(f)

    def initialize_problem(self) -> List[Instance]:
        return [Instance(inst["sequence"], inst["configuration"]) 
                    for inst in self.data]

class Bpp1DRandomInitiator(ProblemInitiator):
    def __init__(self, capacity: int, item_num: int, 
                    instance_num: int, distribution: Discrete):
        self.item_num = item_num
        self.instance_num = instance_num
        self.distribution = distribution
        self.capacity = capacity


    def initialize_problem(self) -> List[Instance]:
        configuration = {
            "distribution": self.distribution.prob_dict,
            "capacity": self.capacity,
            "item_num": self.item_num
        }

        return [Instance(self.distribution.sample(self.item_num)
            , configuration) for _ in range(self.instance_num)]
