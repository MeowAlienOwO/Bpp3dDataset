from typing import List
from bpp3d_dataset.problems.bppinstance import BppInstance
from .initiator import ProblemInitiator

class Problem(object):

    """Problem Basic Class
    A problem contains a series of immutable problem
    instances.
    """

    def __init__(self, initiator: ProblemInitiator):
        self.instances = initiator.initialize_problem()

    @property
    def instances(self) -> List[BppInstance]:
        return self._instances

    @instances.setter
    def instances(self, value: List[BppInstance]):
        self._instances = value
    
    def __len__(self):
        return len(self.instances)

    def __next__(self):
        return self.instances.__next__()

    def __iter__(self):
        return self.instances.__iter__()

    def __getitem__(self, key):
        return self.instances[key]

    




