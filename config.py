class Config:
    """This is the class that will define basic configurations for the app
    """

class DevConfig(Config):
    """This defines configurations in the development environment

    Args:
        Config ([type]): [description]
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kenmbira:1234@localhost/movie_galore'

config_options = {
    'development' : DevConfig
}