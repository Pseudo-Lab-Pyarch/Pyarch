from abc import ABCMeta, abstractmethod
from src.house_price.domain.entity import UpdateHouseData, UpdatePredictionModel, TrainingModelData, ModelInfo
from src.database import mysql_commit_query, execute_query
from typing import Optional, List
import datetime


class Repository(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def add_house_data(self, data: List[UpdateHouseData]):
        pass

    @abstractmethod
    def get_house_data(self, date_range: Optional[str]) -> Optional[List[UpdateHouseData]]:
        pass

    @abstractmethod
    def save_prediction_model(self, model):
        pass


class RepositoryImpl(Repository):
    def __init__(self, conn, ):
        self.conn = conn
        super().__init__()

    @staticmethod
    def _get_date_filter(date_range: Optional[str]):
        if date_range is None or date_range == 'all':
            return ""

        try:
            days = int(date_range)
            today = datetime.date.today()
            week_ago = today - datetime.timedelta(days=days)
            return f"AND update_date BETWEEN '{week_ago}' AND '{today}'"
        except ValueError:
            return ""

    def add_house_data(self, data: List[UpdateHouseData]):
        query = f"""
        INSERT INTO house_pricing (
        Id, MSSubClass, MSZoning, LotFrontage, LotArea, Street, Alley, LotShape, LandContour,
        Utilities, LotConfig, LandSlope, Neighborhood, Condition1, Condition2, BldgType, HouseStyle,
        OverallQual, OverallCond, YearBuilt, YearRemodAdd, RoofStyle, RoofMatl,
        Exterior1st, Exterior2nd, MasVnrType, MasVnrArea, ExterQual, ExterCond, Foundation,
        BsmtQual, BsmtCond, BsmtExposure, BsmtFinType1, BsmtFinSF1, BsmtFinType2, BsmtFinSF2, BsmtUnfSF,
        TotalBsmtSF, Heating, HeatingQC, CentralAir, Electrical, `1stFlrSF`, `2ndFlrSF`, LowQualFinSF,
        GrLivArea, BsmtFullBath, BsmtHalfBath, FullBath, HalfBath, BedroomAbvGr, KitchenAbvGr, KitchenQual,
        TotRmsAbvGrd, Functional, Fireplaces, FireplaceQu, GarageType, GarageYrBlt, GarageFinish, GarageCars,
        GarageArea, GarageQual, GarageCond, PavedDrive, WoodDeckSF, OpenPorchSF, EnclosedPorch, `3SsnPorch`,
        ScreenPorch, PoolArea, PoolQC, Fence, MiscFeature, MiscVal, MoSold, YrSold, SaleType, SaleCondition, SalePrice, update_date
        ) VALUES %s
        """

        mysql_commit_query(query, [tuple(instance.dict().values()) for instance in data], self.conn)

    def get_house_data(self, date_range: Optional[str]) -> Optional[List[TrainingModelData]]:
        query = f"""
                SELECT * FROM house_pricing
                WHERE 1=1
                {self._get_date_filter(date_range)}
                """

        raw_results = execute_query(query, self.conn)

        if not raw_results:
            return None

        return [TrainingModelData(**result) for result in raw_results]

    def save_prediction_model(self, model_info: ModelInfo):
        # 모델 자체 저장히 힘드므로, 가상의 URL로 변환하여 저장
        # s3로 저장된 코드
        url = "www.test.com/2024_04_21_rf_1"

        data = UpdatePredictionModel(
            update_date=datetime.date.today(),
            model_type=type(model_info.model).__name__,
            model_name=model_info.model_name,
            url=url
        )

        query = f"""
                INSERT INTO house_pricing_model (
                    update_date
                ) VALUES %s
                """

        mysql_commit_query(query, [tuple(data.dict().values())], self.conn)
