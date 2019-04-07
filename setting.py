

class BaseSetting(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1:3306/test?charset=utf8"
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'yaaooo'



class DevvlopmentSetting(BaseSetting):
    pass


class ProductionSetting(BaseSetting):
    pass


class TestSetting(BaseSetting):
    pass