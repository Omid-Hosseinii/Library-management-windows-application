import sys
sys.path.insert(0, 'C:/Users/Omid/Desktop/library app')
from DatabaseLayer.dbConnection import *
from DatabaseLayer.BookModel import *

class Database:
    def __init__(self):
        self.db=dbConnection()
        self.cursor=self.db.cursor()
    #------------------------------------------------------------------------------
    def insertBook(self,book):
        try:
            val=book.guideid,book.title,book.creator,book.publicationdetails
            query="Insert INTO book(guideid,title,creator,publicationdetail) Values(%s,%s,%s,%s)"
            self.cursor.execute(query,val)
            self.db.commit()
            return True
        except:
            print("unexeption error..!")
            return False          
    #------------------------------------------------------------------------------
    def deleteBook(self,record):
        try:
            
            query=f"DELETE FROM book WHERE record IN ({record})"
            self.cursor.execute(query)
            self.db.commit()
        except:
            print("unexeption error..!") 
    #------------------------------------------------------------------------------
    def deleteBooks(self,firstId,endId):
        try:
            query=f"DELETE FROM book WHERE record BETWEEN {firstId} and {endId}"
            self.cursor.execute(query)
            self.db.commit()
        except:
            print("unexeption error..!")         
    #------------------------------------------------------------------------------
    def updateBook(self):
        pass
    #------------------------------------------------------------------------------    
    def getBooks(self):
        try:
            self.crusor.execute("Select guideid,title,creator,publicationdetail from book")
            list1=self.crusor.fetchall()
            return list1
        except:
            print('Error') 


# book1=Book('asdas','asdas','asda','asdas')
# db=Database()
# db.insertBook(book1)


