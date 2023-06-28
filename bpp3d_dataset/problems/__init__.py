from .problem import Problem, ProblemSpec
from .bppinstance import BppInstance
from .storage import Storage, store_problem
from .initiator import (ProblemInitiator, 
                        Bpp1DJsonInitiator, Bpp1DRandomInitiator)
import os

from .registration import register_bpp, make_bpp
from pathlib import Path

_data_path  = Path(__file__).parent.parent.absolute()

register_bpp(make_bpp(
    "Normal1D", 
    initiator=Bpp1DJsonInitiator( _data_path / "data/Normal1D.json")
    ))
register_bpp(make_bpp(
    "Uniform1D", 
    initiator=Bpp1DJsonInitiator(_data_path / "data/Uniform1D.json")
    ))
register_bpp(make_bpp(
    "Discrete1D", 
    initiator=Bpp1DJsonInitiator(_data_path / "data/Discrete1D.json")
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
