HOST = "database-1.cqxmuomoj1g2.us-east-1.rds.amazonaws.com"
PORT = "3306"
DB = "info"
USER = "admin"
PASSWORD = "123456789"
CHARSET = "utf8"
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset={}".format(USER, PASSWORD, HOST, PORT, DB, CHARSET)
SQLALCHEMY_DATABASE_URI = DB_URI
