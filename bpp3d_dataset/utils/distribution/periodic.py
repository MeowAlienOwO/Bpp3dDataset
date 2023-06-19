from distribution import Distribution
import numpy as np

class Periodic(Distribution):
    def __init__(self, distrs, sample_step) -> None:
        super().__init__()
        self.distrs = distrs
        self.sample_step = sample_step
        # self.types = sorted(list(set().union([distr.types for distr in distrs])))
        self.types = sorted(list(set([t for d in distrs for t in d.types])))

    def sample(self, num):
        steps = (num // self.sample_step) + 1
        items = [self.distrs[i % len(self.distrs)].sample(self.sample_step) for i in range(steps)]
        items = np.concatenate(items)
        # for i in range(steps):
            
            # items += self.distrs[i % len(self.distrs)].sample(self.sample_step)
        return items[:num]

    def p(self, x, method='first'):
        """return distribution for first one or total distribution

        Args:
            x (_type_): item type
            method (str, optional): first distribution as priori or total. Defaults to 'first'.

        Returns:
            _type_: _description_
        """
        if method == 'first':
            return self.distrs[0].p(x)
        elif method == 'all':
            return sum([self.distrs[i].p(x) for i in range(len(self.distrs))]) / len(self.distrs)