from typing import Dict, Tuple
from .problem import Problem, ProblemSpec
from .initiator import Bpp1DJsonInitiator, ProblemInitiator
from .extra_initiator import Bpp1DSWHInitiator, Bpp1DDualNormalInitiator
from pathlib import Path
import re

PROB_ID_RE = re.compile(r"^(?P<name>[\w]+?)-(?P<dim>\d+)D(?:-v(?P<version>\d+))?$")

# global problem registry, similar to gym global registry
bpp_registry: Dict[str, Problem] = {} 
_SWH_PATHS = [
    Path(__file__).parent.parent.absolute() / "data" / "waescher" ,
    Path(__file__).parent.parent.absolute() / "data" / "schwerin",
    Path(__file__).parent.parent.absolute() / "data" / "hard28",
]

_DUAL_TEST = Path(__file__).parent.parent.absolute() / "data" / "dualdistribution" / "test"
_DUAL_TRAIN = Path(__file__).parent.parent.absolute() / "data" / "dualdistribution" / "train"


_data_paths  = [ 
                    Path(__file__).parent.parent.absolute() / "data"
                ]

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
    

def check_bpp_registered(name: str) -> bool:
    return name in bpp_registry

def _check_spec_register(testing_spec: ProblemSpec) -> bool:
    return not check_bpp_registered(testing_spec.name)

def register_bpp(problem: Problem):
    assert problem.spec is not None and problem.spec.name != ""
    bpp_registry[problem.spec.name] = problem

def add_data_path(path: Path):
    _data_paths.append(path)

def make_bpp(id: str, spec: ProblemSpec | None = None, initiator: ProblemInitiator | None = None):
    if check_bpp_registered(id):
        return bpp_registry[id]
    else:
        assert initiator is not None, \
                "make a non-registered bpp should include initiator!"
        if spec is None:
            name, dim, version = parse_prob_name(id)

            spec = ProblemSpec(id, dim=dim, type=f"{name}_{dim}d_v{version}")
        return Problem(initiator, spec)


def _register_swh():
    for data_path in _SWH_PATHS:
        for fpath in data_path.glob("*.bpp"):
            register_bpp(make_bpp(fpath.stem + "-1D", initiator=Bpp1DSWHInitiator(fpath))) 

def _register_dual():
    for dir in _DUAL_TEST.iterdir():
        register_bpp(make_bpp(f"Dual{dir.name.capitalize()}-1D",
                                initiator=Bpp1DDualNormalInitiator(dir)))
    register_bpp(make_bpp("DualTrain-1D", initiator=Bpp1DDualNormalInitiator(_DUAL_TRAIN)))
    


def register_all():

    for data_path in _data_paths:
        for fpath in data_path.glob('*.json'):
            register_bpp(make_bpp(fpath.stem, initiator=Bpp1DJsonInitiator(fpath)))

    _register_swh()
    _register_dual()