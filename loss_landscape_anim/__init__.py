"""Package init."""
from .main import loss_landscape_anim
from .model import GenericModel, MLP, LeNet, CNNNet
from .loss_landscape import LossGrid
from .datamodule import SpiralsDataModule, MNISTDataModule, CIFARDataModule

__version__ = "0.1.9"

__all__ = [
    "loss_landscape_anim",
    "GenericModel",
    "MLP",
    "LeNet",
    "LossGrid",
    "SpiralsDataModule",
    "MNISTDataModule",
    "CNNNet",
    "CIFARDataModule",
]
