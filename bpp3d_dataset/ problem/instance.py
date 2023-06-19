from typing import List, Dict



class Instance(object):
    """An instance is an immutable representation of a certain problem.
    The problem instance specifies:
    1. immutable sequence of item
    2. instance-specific configuration(e.g. bin size)

    """

    def __init__(self, sequence: List, instance_configuration: Dict):
        """Initialize problem instance with given data

        @param sequence the sequence of 
        @param instance_configuration
        """
        self.sequence = sequence
        self.configuration = instance_configuration

    @property
    def sequence(self):
        return self._sequence

    @sequence.setter
    def sequence(self, value: List):
        self._sequence = value

    def __len__(self):
        return len(self._sequence) if self._sequence is not None else 0

    def __next__(self):
        return self.sequence.__next__()

    def __iter__(self):
        return self.sequence.__iter__()

    def __getitem__(self, key):
        return self.sequence[key]
