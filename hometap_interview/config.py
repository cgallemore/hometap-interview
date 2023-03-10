class Config:
    HOUSE_CANARY_URL = "https://api.housecanary.com/v3"


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False

    # NOTE: These wouldn't be hard coded here normally, instead secerts like this
    # would be pulled in dynamically via something like AWS SecretsManager or via environment variables
    HOUSE_CANARY_API_KEY = ''
    HOUSE_CANARY_API_SECRET = ''


class DevConfig(Config):
    # Overrides the HOUSE_CANARY_URL with the mock I setup at beeceptor
    HOUSE_CANARY_URL = 'https://cgallemore.free.beeceptor.com'
    DEBUG = True
    TESTING = False


class TestConfig(Config):
    # Mock URL for testing
    HOUSE_CANARY_URL = "http://mock_canary.com/v3"
    HOUSE_CANARY_API_KEY = 'DUMMY_KEY'
    HOUSE_CANARY_API_SECRET = 'DUMMY_SECRET'
    TESTING = True
    DEBUG = True
