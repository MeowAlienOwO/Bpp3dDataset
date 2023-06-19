from typing import List
from instance import Instance
from problem import ProblemInitiator

class Problem(object):

    """Problem Basic Class
    A problem contains a series of immutable problem
    instances.
    """

    def __init__(self, initiator: ProblemInitiator):
        self.instances = initiator.initialize_problem()

    @property
    def instances(self) -> List[Instance]:
        return self._problem_instances

    @instances.setter
    def instances(self, value: List[Instance]):
        self._instances = value

        

    




