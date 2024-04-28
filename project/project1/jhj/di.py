from src.service_layer.service import HouseDataServiceImpl, HouseModelServiceImpl
from src.infrastructure.data_repository import DataRepositoryImpl
from src.infrastructure.data_processor import DataProcessorImpl
from src.infrastructure.model_repository import ModelRepositoryImpl

from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Factory, Configuration
import sqlite3


class HouseContainer(DeclarativeContainer):
    config = Configuration()
    connection_factory = Factory(sqlite3.connect, config.database_url)

    house_data_di = Factory(
        HouseDataServiceImpl,
        data_repository=Factory(
            DataRepositoryImpl,
            connection=connection_factory
        )
    )
    house_model_di = Factory(
        HouseModelServiceImpl,
        data_processor=Factory(
            DataProcessorImpl
        ),
        model_repository=Factory(
            ModelRepositoryImpl
        )
    )
