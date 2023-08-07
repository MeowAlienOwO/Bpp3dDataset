


from pathlib import Path
from typing import Dict, List
from bpp3d_dataset.problems.bppinstance import BppInstance
from bpp3d_dataset.problems.initiator import ProblemInitiator
import numpy as np

from typing import NamedTuple

class ExternalInstance(NamedTuple):
    config: Dict
    sequence: List[int]


class Bpp1DSWHInitiator(ProblemInitiator):
    """from schwerin / waescher / hard28 
    """
    def __init__(self, data_path:Path, shuffle=False) -> None:
        super().__init__()
        self.dim = 1
        self.data_path = data_path
        self.shuffle = shuffle

        self.instances: List[ExternalInstance] = []
        with open(self.data_path) as f:
            lines = f.readlines()
            problem_slices = [i for i in range(len(lines)) if lines[i].startswith("'")]
            sliced_lines = [lines[i:j] for i,j in zip(problem_slices[:-1], problem_slices[1:] + [len(lines)])]
            for group in sliced_lines:

                sequence = []
                for item_line in group[3:]:
                    item, num = tuple(item_line.split())
                    sequence += [int(item)] * int(num)
                config = {
                    "name": group[0],
                    "item_num": int(group[1]),
                    "items": sorted(list(set(sequence))),
                    "capacity": int(group[2])
                }
                if self.shuffle:
                    np.random.shuffle(sequence)
                
                self.instances.append(ExternalInstance(config, sequence))

    def initialize_problem(self) -> List[BppInstance]:

        return [BppInstance(inst.sequence, inst.config) for inst in self.instances]

    def initialize_configuration(self) -> Dict:
        return {
            "capacity": self.instances[0].config['capacity'], 
            "set_name": self.data_path.stem,
            "shuffled": self.shuffle
        }

class Bpp1DDualNormalInitiator(ProblemInitiator):
    def __init__(self, data_path:Path, shuffle=False) -> None:
        self.dim = 1
        self.data_path = data_path
        self.shuffle = shuffle
        self.capacity = 100

        self.instances: List[ExternalInstance] = []
        for data_file in data_path.glob("*.txt"):
            with open(data_file) as f:
                sequence = [int(i) for i in f.readlines()]
                config  = {
                    "capacity": 100, 
                    "name": data_file.stem,
                    "shuffled": self.shuffle,
                    "items": sorted(list(set(sequence)))
                }
                if self.shuffle:
                    np.random.shuffle(sequence)
                self.instances.append(ExternalInstance(config, sequence))

    def initialize_problem(self) -> List[BppInstance]:
        return [BppInstance(inst.sequence, inst.config) for inst in self.instances]

    def initialize_configuration(self) -> Dict:
        return {
            "capacity": self.capacity,
            "set_name": self.data_path.name,
            "shuffled": self.shuffle
        }



