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
    "postgresql://username:password@localhost:portnumber/dbname"
    SQLALCHEMY_DATABASE_URI = "postgresql://flask:iti@localhost:5432/flask_menia"



app_config={
    'dev':DevelopmentConfig,
    'prd': ProductionConfig
}
