from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date
from typing import *

@dataclass
class House:
    Id: int
    YearBuilt: int 
    FirstFlrSF: int  # 1stFlrSF
    BedroomAbvGr: int
    SalePrice: int

    def __hash__(self):
        return hash(self.Id)

    def __gt__(self, other):
        if self.SalePrice is None:
            return False
        if other.SalePrice is None:
            return True
        return self.SalePrice > other.SalePrice
    
    @property
    def get_features(self):
        return {
            'id': self.Id, 
            'YearBuilt': self.YearBuilt, 
            '1stFlrSF': self.FirstFlrSF, 
            'BedroomAbvGr': self.BedroomAbvGr, 
            'SalePrice': self.SalePrice
            }

