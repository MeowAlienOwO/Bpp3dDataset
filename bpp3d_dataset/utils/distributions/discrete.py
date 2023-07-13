from bpp3d_dataset.utils.distributions.distribution import Distribution
from typing import List
import numpy as np
from scipy.stats import poisson, binom 

class Discrete(Distribution):
    def __init__(self, probs:List[float], items:List) -> None:
        super(Discrete, self).__init__()
        assert np.isclose(np.sum(probs), 1), \
            f"The sum of probabilities does not sum to 1: {probs}"
        assert len(probs) == len(items)

        self.probs = probs

        self.items = items

    @property
    def prob_dict(self):
        return {c:p for c, p in zip(self.items, self.probs)}

    def sample(self, num):
        return np.random.choice(self.items, size=num,p=self.probs)

    def p(self, x):
        return self.prob_dict.get(x, 0)

    def __repr__(self) -> str:
        return "{" + ",".join([f"{k}:{p} " 
                               for k, p in self.prob_dict.items()]) + "}"

class Uniform(Discrete):
    def __init__(self, items: List) -> None:
        super(Uniform, self).__init__([1 / len(items) for _ in items], items)

class Binomial(Discrete):
    def __init__(self, items:List, p:float=0.5) -> None:


        probs = [binom.pmf(i, len(items), p) for i in range(len(items))]
        probs = [ p / sum(probs) for p in probs]
        super(Binomial, self).__init__(probs, items)

class Poisson(Binomial):
    def __init__(self, items, mu):

        probs = [poisson.pmf(i, mu) for i in range(len(items))]
        probs = [ p / sum(probs) for p in probs]
        print("Poission Probs", probs)
        super(Binomial, self).__init__(probs, items)
