import pytest

from bpp3d_dataset.utils.distributions.discrete import generate_discrete_dist

from bpp3d_dataset.utils.distributions import Uniform, Binomial, Poisson, Discrete
ITEM = [1, 2, 3, 4, 5]
@pytest.mark.parametrize(
    ('dist', 'items', 'type', 'kwargs'), [
        ('uniform', ITEM, Uniform, {}),
        ('normal', ITEM, Binomial, {}),
        ('binomial', ITEM, Binomial, {'p': 0.6}),
        ('poisson', ITEM, Poisson, {'mu': 0.7}),
        ('discrete', ITEM, Discrete, {'probs': [0.2, 0.2, 0.3, 0.15, 0.15]}),
    ]

    
)
def test_distributions(dist, items, type, kwargs):
    distr = generate_discrete_dist(items, dist_key=dist, **kwargs)
    assert isinstance(distr, type)

    