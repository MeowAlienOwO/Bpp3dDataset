from bpp3d_dataset.utils.distributions.distribution import Distribution
from typing import List
import numpy as np
from scipy.stats import poisson, binom 
from enum import Enum

class ValidDiscrete(str, Enum):
    discrete = 'discrete'
    uniform = 'uniform'
    normal = 'normal'
    binomial = 'binomial'
    poission = 'poission'
    set1 = 'set1'
    set2 = 'set2'
    set3 = 'set3'

    

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

# Predefined
DEFAULT_1D_ITEMS = [i for i in range(10, 60, 5)]

class Set3Discrete(Discrete):
    def __init__(self, items: List=DEFAULT_1D_ITEMS) -> None:
        probs = [0.2, 0.05, 0.1, 0.12, 0.08, 0.05, 0.03, 0.01, 0.18, 0.18]
        super().__init__(probs, items)
# see https://github.com/hubbs5/or-gym/blob/master/or_gym/envs/classic_or/binpacking.py
# and paper https://arxiv.org/abs/1911.10641
OR_GYM_ITEMS0 = [2, 3]
OR_GYM_ITEMS1 = [i for i in range(1, 10)]
OR_GYM_PROBS = {
    'or-gym-lw0': [0.8, 0.2],
    'or-gym-lw1': [0.14, 0.1, 0.06, 0.13, 0.11, 0.13, 0.03, 0.11, 0.19],
    'or-gym-pp0': [0.75, 0.25],
    'or-gym-pp1': [0.06, 0.11, 0.11, 0.22, 0, 0.11, 0.06, 0, 0.33],
    'or-gym-bw0': [0.5, 0.5],
    'or-gym-bw1': [0, 0, 0, 1/3, 0, 0, 0, 0, 2/3]
}



def generate_discrete_dist(items: List = DEFAULT_1D_ITEMS, 
                        dist: ValidDiscrete | str = ValidDiscrete.uniform, 
                        *args, **kwargs):

    if dist == ValidDiscrete.uniform or dist == ValidDiscrete.set1:
        return Uniform(items)
    elif dist == ValidDiscrete.normal or dist ==ValidDiscrete.set2:
        return Binomial(items)
    elif dist == ValidDiscrete.binomial:
        return Binomial(items, *args, **kwargs)
    elif dist == ValidDiscrete.poission:
        return Poisson(items, *args, **kwargs)
    elif dist == ValidDiscrete.set3:
        return Set3Discrete(items)
    elif dist == ValidDiscrete.discrete:
        # assert 'probs' in kwargs
        if 'probs' not in kwargs or not kwargs['probs'] :
            raise NotImplementedError
        
        return Discrete(probs=kwargs['probs'], items=items)
    else:
        raise NotImplementedError

def generate_or_gym_dist(key: str = 'or-gym-lw0'):
    if key in OR_GYM_PROBS:
        return Discrete(probs=OR_GYM_PROBS[key], 
                        items=OR_GYM_ITEMS0 if '0' in key else OR_GYM_ITEMS1)
    else:
        raise NotImplementedError