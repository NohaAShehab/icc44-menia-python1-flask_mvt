# define possible congfiguration you might need

class Config:
    @staticmethod
    def init_app():
        pass


class DevelopmentConfig(Config):
    DEBUG=True
    #DB_Config
    SQLALCHEMY_DATABASE_URI= "sqlite:///project.sqlite"



class ProductionConfig(Config):
    DEBUG=False
    SQLALCHEMY_DATABASE_URI = "sqlite:///project.sqlite"



app_config={
    'dev':DevelopmentConfig,
    'prd': ProductionConfig
}
