from typing import List, NamedTuple, Dict

from bpp3d_dataset.problems.bppinstance import BppInstance
from .initiator import ProblemInitiator

class ProblemSpec(NamedTuple):
    name: str
    dim: int = 1
    type: str | None = None




class Problem:
    """Problem Basic Class
    A problem contains a series of immutable problem
    instances.
    """

    def __init__(self, initiator: ProblemInitiator, spec: ProblemSpec | None = None):
        if spec is not None:
            assert initiator.dim == spec.dim
        self.initiator = initiator
        self._instances: List[BppInstance] = []
        self._configuration: Dict = {}
        self.spec = spec
        # self.instances = initiator.initialize_problem()
        # self.configuration = initiator.initialize_configuration()

    @property 
    def configuration(self) -> Dict:
        if not self._configuration :
            self._configuration = self.initiator.initialize_configuration()
        return self._configuration

    @configuration.setter
    def configuration(self, value: Dict):
        self._configuration = value
        

    @property
    def instances(self) -> List[BppInstance]:
        if not self._instances:
            self._instances = self.initiator.initialize_problem()
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

