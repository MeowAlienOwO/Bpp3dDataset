from typing import Dict, Tuple
from .problem import Problem, ProblemSpec
from .initiator import ProblemInitiator

import re

PROB_ID_RE = re.compile(r"^(?P<name>[\w]+?)(?P<dim>\d+)D(?:-v(?P<version>\d+))?$")

# global problem registry, similar to gym global registry
bpp_registry: Dict[str, Problem] = {} 


def parse_prob_name(id: str) -> Tuple[str, int, int | None]:
    
    """Parse the problem name to be a tuple containing: problem name, dimension, version

    Args:
        name (str): problem name string
    
    Returns:

    Raises:
        ValueError: if problem id not match
    """
    match = PROB_ID_RE.fullmatch(id)
    if not match:
        raise ValueError(f"Malformed problem id: {id}")
    name, dim, ver = match.group("name", "dim", "version")

    name = str(name)
    dim = int(dim) if dim is not None else 1
    ver = int(ver) if ver is not None else None
    

    
    return name, dim, ver
    

def _check_registry_exists(name: str) -> bool:
    return name in bpp_registry

def _check_spec_register(testing_spec: ProblemSpec) -> bool:
    is_registered = _check_registry_exists(testing_spec.name)

    return not is_registered

def register_bpp(problem: Problem):
    assert problem.spec is not None and problem.spec.name != ""
    bpp_registry[problem.spec.name] = problem

def make_bpp(id: str, spec: ProblemSpec | None = None, initiator: ProblemInitiator | None = None):
    if _check_registry_exists(id):
        return bpp_registry[id]
    else:
        assert initiator is not None, \
                "make a non-registered bpp should include initiator!"
        if spec is None:
            name, dim, version = parse_prob_name(id)

            spec = ProblemSpec(id, dim=dim, type=f"{name}_{dim}d_v{version}")
        return Problem(initiator, spec)
