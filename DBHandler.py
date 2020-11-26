import mysql.connector
import constants
class DBHandler:
    def __init__(self):
        DBHandler.HOST = constants.HOST
        DBHandler.USER = constants.USER
        DBHandler.DBNAME = constants.DATABASE
        DBHandler.PASSWORD = constants.PASS
    HOST = constants.HOST
    USER = constants.USER
    DBNAME = constants.DATABASE
    PASSWORD = constants.PASS
    @staticmethod
    def get_mydb():
        if DBHandler.DBNAME == '':
            constants.init()
        db = DBHandler()
        mydb = db.connect()
        return mydb

    def connect(self):
        mydb = mysql.connector.connect(
            host=DBHandler.HOST,
            user=DBHandler.USER,
            passwd=DBHandler.PASSWORD,
            database = DBHandler.DBNAME
        )
        return mydb