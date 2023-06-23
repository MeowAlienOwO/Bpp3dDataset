from .problem import Problem
import numpy as np
from pathlib import Path
import json


class Storage:
    """Store the problem with json representation"""

    def __init__(self, problem: Problem):
        self.problem = problem

    def save(self, filepath: Path):
        """Save problem instance to target file"""
        store_problem(self.problem, filepath)


def store_problem(problem: Problem, filepath: Path):
    datadict = []
    for inst in problem:
        datadict.append(
            {"configuration": inst.configuration, "sequence": inst.sequence}
        )

    with open(filepath, "w") as f:
        json.dump(datadict, f, cls=NpEncoder)


class NpEncoder(json.JSONEncoder):
    """deal with numpy output
    see https://stackoverflow.com/questions/50916422/python-typeerror-object-of-type-int64-is-not-json-serializable
    """

    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)
