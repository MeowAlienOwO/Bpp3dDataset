from .problem import Problem
from .bppinstance import BppInstance
from .storage import Storage, store_problem
from .initiator import (ProblemInitiator, 
                        Bpp1DJsonInitiator, Bpp1DRandomInitiator)
from .registration import register_bpp, make_bpp
from pathlib import Path

_data_path  = Path(__file__).parent.parent.absolute() / "data"

# Now not lazy loading, when modify the data file, 
# following registration should be commented

register_bpp(make_bpp(
    "Normal1D", 
    initiator=Bpp1DJsonInitiator( _data_path / "Normal1D.json")
    ))
register_bpp(make_bpp(
    "Uniform1D", 
    initiator=Bpp1DJsonInitiator(_data_path / "Uniform1D.json")
    ))
register_bpp(make_bpp(
    "Discrete1D", 
    initiator=Bpp1DJsonInitiator(_data_path / "Discrete1D.json")
    ))

__all__ = [
    "Problem",
    "BppInstance",
    "Storage",
    "register_bpp",
    "make_bpp",
    "store_problem",
    "ProblemInitiator",
    "Bpp1DJsonInitiator",
    "Bpp1DRandomInitiator"
]
