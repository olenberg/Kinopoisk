class Config:
    DEBUG = True
    SECRET = 'test'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./../data/movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
    RESTX_JSON = {'ensure_ascii': False}
    RESTFUL_JSON = {'ensure_ascii': False}
    PWD_HASH_SALT = b'secret here'
    PWD_HASH_ITERATIONS = 100_000
    ALGO = 'HS256'
    TOKEN_EXPIRE_MINUTES = 30
    TOKEN_EXPIRE_DAYS = 130
    RECORDS_PER_PAGE = 12
    MAX_PAGE = 100
