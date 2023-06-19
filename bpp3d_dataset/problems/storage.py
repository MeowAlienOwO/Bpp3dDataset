from .problem import Problem
import numpy as np
import json

class Storage:
    """Store the problem with json representation
    """
    def __init__(self, problem: Problem):
        self.problem = problem


    def save(self, filepath: str):
        """Save problem instance to target file
        """

        datadict = []
        for inst in self.problem:
            datadict.append({
                "configuration": inst.configuration,
                "sequence": inst.sequence
            })

        with open(filepath, 'w') as f:
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