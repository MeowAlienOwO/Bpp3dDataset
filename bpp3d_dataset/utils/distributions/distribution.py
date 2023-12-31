from abc import abstractclassmethod
from typing import Dict

class Distribution(object):
    """Distributions for sampling items
    """

    @abstractclassmethod
    def sample(self, num):
        """Sample items by shape

        Args:
            num (int): shape to be sampled
        """

        raise NotImplementedError

    @abstractclassmethod
    def p(self, x):
        """probability mass function at x

        Args:
            x (int): x value of pmf

        """
        raise NotImplementedError


    @property
    def prob_dict(self) -> Dict:
        raise NotImplementedError
