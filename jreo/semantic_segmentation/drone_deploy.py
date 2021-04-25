from .images2chips import run
from ..utils import _urlretrieve
import sys
import os


class DroneSemantic():
    """Drone Deploy Semantic Dataset.
    
    Args:
        root (string): Root directory of dataset where ``MNIST/processed/training.pt``
            and  ``MNIST/processed/test.pt`` exist.
        train (bool, optional): If True, creates dataset from ``training.pt``,
            otherwise from ``test.pt``.
        download (bool, optional): If true, downloads the dataset from the internet and
            puts it in root directory. If dataset is already downloaded, it is not
            downloaded again.
        transform (callable, optional): A function/transform that  takes in an PIL image
            and returns a transformed version. E.g, ``transforms.RandomCrop``
        target_transform (callable, optional): A function/transform that takes in the
            target and transforms it.
    """
    
    resources = {
        'dataset-sample' : 'https://dl.dropboxusercontent.com/s/h8a8kev0rktf4kq/dataset-sample.tar.gz?dl=0',
        'dataset-medium' : 'https://dl.dropboxusercontent.com/s/r0dj9mhyv4bgbme/dataset-medium.tar.gz?dl=0'
    }
    
    def __init__(self, root:str, dataset_type='dataset-sample', download: bool = False):
        self.root = root
        self.dataset = dataset_type
        self.filename = f'{self.dataset}.tar.gz'
        
        if self._check_exists():
            print(f'zipfile "{self.filename}" already exists, remove it if you want to re-download.')
            return
        
        if download:
            self.download()
        
    def download(self):
        """ Download a dataset, extract it and create the tiles """

        print(f'Downloading "{self.dataset}"')
        self.root = os.path.expanduser(self.root)
        fpath = os.path.join(self.root, self.filename)
        _urlretrieve(self.resources[self.dataset], fpath)
        
        if not os.path.exists(self.dataset):
            print(f'Extracting "{self.filename}"')
            os.system(f'tar -xvf {self.filename}')
        else:
            print(f'Folder "{self.dataset}" already exists, remove it if you want to re-create.')

        image_chips = f'{self.dataset}/image-chips'
        label_chips = f'{self.dataset}/label-chips'
        
        if not os.path.exists(image_chips) and not os.path.exists(label_chips):
            print("Creating chips")
            run(self.dataset)
        else:
            print(f'chip folders "{image_chips}" and "{label_chips}" already exist, remove them to recreate chips.')
            
    
    def _check_exists(self) -> bool:
        if self.dataset not in self.resources.keys():
            print(f"Unknown dataset {self.dataset}")
            print(f"Available dataset : {self.resources.keys()}")
            sys.exit(0)
        
        if os.path.exists(self.filename):
            return True
        else:
            return False