"""Import specific class that will use."""
from .drone_deploy import DroneDeploy
from .aerialcactus import AerialCactus
from .eurosat import EuroSat
from .resisc45 import RESISC45
from .ucmercedland import UCMercedLand
from .l8sparcs import L8SPARCS
from .deepsat import DeepSat
from .landcover import LandCover
from .cowc import COWC
from .l7irish import L7Irish

__all__ = ['DroneDeploy', 'AerialCactus', 'RESISC45',
           'UCMercedLand', 'EuroSat', 'L8SPARCS', 'DeepSat', 'LandCover', 'COWC','L7Irish','SpaceNet7']
