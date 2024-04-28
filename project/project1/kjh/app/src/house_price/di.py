from src.house_price.application.facade import HousePriceFacade
from src.house_price.domain.service import HousePriceServiceImpl
from src.house_price.infrastructure.model_training import HousePricePredictorImpl
from src.house_price.adapters.repository import RepositoryImpl

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Factory, Configuration, Resource
from src.database import get_mysql_conn


class HousePriceContainer(DeclarativeContainer):
    config = Configuration()

    conn = Resource(
        get_mysql_conn,
        host=config.host,
        user=config.user,
        password=config.password,
        database=config.database
    )

    repository = Factory(RepositoryImpl, conn=conn)

    house_price_di = Factory(
        HousePriceFacade,
        house_price_servie=Factory(
            HousePriceServiceImpl,
            repository=repository,
            house_price_predictor=HousePricePredictorImpl))
