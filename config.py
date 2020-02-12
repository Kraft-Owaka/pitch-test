import os

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://kraft:admin123@localhost/pitches"
    SECRET_KEY=os.environ.get('SECRET_KEY')

    @staticmethod
    def init_app(app):
        pass  
  


class ProdConfig(Config):

    pass

class DevConfig(Config):
    
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}