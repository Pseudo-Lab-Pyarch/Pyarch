from pydantic import BaseModel
from typing import Optional, Any
from datetime import date


class UpdateHouseData(BaseModel):
    Id: Optional[int]
    MSSubClass: Optional[int]
    MSZoning: Optional[str]
    LotFrontage: Optional[float]
    LotArea: Optional[int]
    Street: Optional[str]
    LotShape: Optional[str]
    LandContour: Optional[str]
    Utilities: Optional[str]
    LotConfig: Optional[str]
    LandSlope: Optional[str]
    Neighborhood: Optional[str]
    Condition1: Optional[str]
    Condition2: Optional[str]
    BldgType: Optional[str]
    HouseStyle: Optional[str]
    OverallQual: Optional[int]
    OverallCond: Optional[int]
    YearBuilt: Optional[int]
    YearRemodAdd: Optional[int]
    RoofStyle: Optional[str]
    RoofMatl: Optional[str]
    Exterior1st: Optional[str]
    Exterior2nd: Optional[str]
    MasVnrType: Optional[str]
    MasVnrArea: Optional[float]
    ExterQual: Optional[str]
    ExterCond: Optional[str]
    Foundation: Optional[str]
    BsmtQual: Optional[str]
    BsmtCond: Optional[str]
    BsmtExposure: Optional[str]
    BsmtFinType1: Optional[str]
    BsmtFinSF1: Optional[int]
    BsmtFinType2: Optional[str]
    BsmtFinSF2: Optional[int]
    BsmtUnfSF: Optional[int]
    TotalBsmtSF: Optional[int]
    Heating: Optional[str]
    HeatingQC: Optional[str]
    CentralAir: Optional[str]
    Electrical: Optional[str]
    firstFlrSF: Optional[int]
    secondFlrSF: Optional[int]
    LowQualFinSF: Optional[int]
    GrLivArea: Optional[int]
    BsmtFullBath: Optional[int]
    BsmtHalfBath: Optional[int]
    FullBath: Optional[int]
    HalfBath: Optional[int]
    BedroomAbvGr: Optional[int]
    KitchenAbvGr: Optional[int]
    KitchenQual: Optional[str]
    TotRmsAbvGrd: Optional[int]
    Functional: Optional[str]
    Fireplaces: Optional[int]
    FireplaceQu: Optional[str]
    GarageType: Optional[str]
    GarageYrBlt: Optional[float]
    GarageFinish: Optional[str]
    GarageCars: Optional[int]
    GarageArea: Optional[int]
    GarageQual: Optional[str]
    GarageCond: Optional[str]
    PavedDrive: Optional[str]
    WoodDeckSF: Optional[int]
    OpenPorchSF: Optional[int]
    EnclosedPorch: Optional[int]
    threeSsnPorch: Optional[int]
    ScreenPorch: Optional[int]
    PoolArea: Optional[int]
    PoolQC: Optional[str]
    Fence: Optional[str]
    MiscFeature: Optional[str]
    MiscVal: Optional[int]
    MoSold: Optional[int]
    YrSold: Optional[int]
    SaleType: Optional[str]
    SaleCondition: Optional[str]
    SalePrice: Optional[int]
    update_date: Optional[date]


class TrainingModelData(BaseModel):
    MSSubClass: Optional[int]
    MSZoning: Optional[str]
    LotFrontage: Optional[float]
    LotArea: Optional[int]
    Street: Optional[str]
    Alley: Optional[str]
    LotShape: Optional[str]
    LandContour: Optional[str]
    Utilities: Optional[str]
    LotConfig: Optional[str]
    LandSlope: Optional[str]
    Neighborhood: Optional[str]
    Condition1: Optional[str]
    Condition2: Optional[str]
    BldgType: Optional[str]
    HouseStyle: Optional[str]
    OverallQual: Optional[int]
    OverallCond: Optional[int]
    YearBuilt: Optional[int]
    YearRemodAdd: Optional[int]
    RoofStyle: Optional[str]
    RoofMatl: Optional[str]
    Exterior1st: Optional[str]
    Exterior2nd: Optional[str]
    MasVnrType: Optional[str]
    MasVnrArea: Optional[float]
    ExterQual: Optional[str]
    ExterCond: Optional[str]
    Foundation: Optional[str]
    BsmtQual: Optional[str]
    BsmtCond: Optional[str]
    BsmtExposure: Optional[str]
    BsmtFinType1: Optional[str]
    BsmtFinSF1: Optional[int]
    BsmtFinType2: Optional[str]
    BsmtFinSF2: Optional[int]
    BsmtUnfSF: Optional[int]
    TotalBsmtSF: Optional[int]
    Heating: Optional[str]
    HeatingQC: Optional[str]
    CentralAir: Optional[str]
    Electrical: Optional[str]
    firstFlrSF: Optional[int]
    secondFlrSF: Optional[int]
    LowQualFinSF: Optional[int]
    GrLivArea: Optional[int]
    BsmtFullBath: Optional[int]
    BsmtHalfBath: Optional[int]
    FullBath: Optional[int]
    HalfBath: Optional[int]
    BedroomAbvGr: Optional[int]
    KitchenAbvGr: Optional[int]
    KitchenQual: Optional[str]
    TotRmsAbvGrd: Optional[int]
    Functional: Optional[str]
    Fireplaces: Optional[int]
    FireplaceQu: Optional[str]
    GarageType: Optional[str]
    GarageYrBlt: Optional[float]
    GarageFinish: Optional[str]
    GarageCars: Optional[int]
    GarageArea: Optional[int]
    GarageQual: Optional[str]
    GarageCond: Optional[str]
    PavedDrive: Optional[str]
    WoodDeckSF: Optional[int]
    OpenPorchSF: Optional[int]
    EnclosedPorch: Optional[int]
    threeSsnPorch: Optional[int]
    ScreenPorch: Optional[int]
    PoolArea: Optional[int]
    MiscVal: Optional[int]
    MoSold: Optional[int]
    YrSold: Optional[int]
    SaleType: Optional[str]
    SaleCondition: Optional[str]
    SalePrice: Optional[int]


class UpdatePredictionModel(BaseModel):
    update_date: Optional[date]
    model_type: str
    model_name: Optional[str]
    url: str


class ModelInfo(BaseModel):
    model_name: str
    model: Any
