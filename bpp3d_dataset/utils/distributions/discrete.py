from bpp3d_dataset.utils.distributions.distribution import Distribution
from typing import List
import numpy as np
from scipy.stats import poisson, binom 

class Discrete(Distribution):
    def __init__(self, probs:List[float], types:List) -> None:
        super(Discrete, self).__init__()
        assert np.isclose(np.sum(probs), 1), \
            f"The sum of probabilities does not sum to 1: {probs}"
        assert len(probs) == len(types)

        self.probs = probs

        self.types = types

    @property
    def prob_dict(self):
        return {c:p for c, p in zip(self.types, self.probs)}

    def sample(self, num):
        return np.random.choice(self.types, size=num,p=self.probs)

    def p(self, x):
        return self.prob_dict.get(x, 0)

    def __repr__(self) -> str:
        return "{" + ",".join([f"{k}:{p} " 
                               for k, p in self.prob_dict.items()]) + "}"

class Uniform(Discrete):
    def __init__(self, types: List) -> None:
        super(Uniform, self).__init__([1 / len(types) for _ in types], types)

class Binomial(Discrete):
    def __init__(self, types:List, p:float=0.5) -> None:


        probs = [binom.pmf(i, len(types), p) for i in range(len(types))]
        probs = [ p / sum(probs) for p in probs]
        super(Binomial, self).__init__(probs, types)

class Poisson(Binomial):
    def __init__(self, types, mu):

        probs = [poisson.pmf(i, mu) for i in range(len(types))]
        probs = [ p / sum(probs) for p in probs]
        print("Poission Probs", probs)
        super(Binomial, self).__init__(probs, types)
