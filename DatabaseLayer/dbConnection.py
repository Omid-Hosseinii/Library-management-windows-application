from mysql.connector import connect,Error

def createDB(databaseName):
    try:
        with connect (host="localhost",user="root",password="your password") as db:
            dbcursor=db.cursor()
            dbcursor.execute(f"CREATE DATABASE {databaseName}")
            db.commit()
    except Error as error:
        print(error)        


def dbConnection():
    try:
        return connect(host="localhost",user="root",password="OmId57311",database='library')        
    except Error as error:
        print(error)  


def createTable():
    try:
        db=dbConnection()    
        dbcursor=db.cursor()
        query='''
        create table book(
                                record int primary key AUTO_INCREMENT,
                                guideid varchar(100),
                                title varchar(200),
                                creator varchar(100),
                                publicationdetail varchar(50)
        )
        '''
        dbcursor.execute(query)
        db.commit()
    except Error as error:
        print(error)       