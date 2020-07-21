from settings.configs.dev import DevelopmentConfig
from settings.configs.prod import ProductionConfig

config = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig,
)
