from .problem import Problem
from .bppinstance import BppInstance
from .storage import Storage, store_problem
from .initiator import (ProblemInitiator, 
                        Bpp1DJsonInitiator, Bpp1DRandomInitiator)
from .registration import register_bpp, make_bpp, check_bpp_registered
from pathlib import Path

_data_path  = Path(__file__).parent.parent.absolute() / "data"

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
    "check_bpp_registered",
    "store_problem",
    "ProblemInitiator",
    "Bpp1DJsonInitiator",
    "Bpp1DRandomInitiator",
]
