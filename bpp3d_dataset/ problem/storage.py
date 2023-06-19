from problem import Problem
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
            obj = dict()
            obj["configuration"] = inst.configuration
            obj["sequence"] = inst.sequence
            datadict += obj

        with open(filepath, 'w') as f:
            json.dump(datadict, f)

