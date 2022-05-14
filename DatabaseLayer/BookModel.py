
class Book:
    def __init__(self,record,guideid,title,creator,publicationdetails):
        self.record = record
        self.guideid = guideid
        self.title = title
        self.creator = creator
        self.publicationdetails = publicationdetails


    def __str__(self):
        return f"{self.record}\t{self.guideid}\t{self.title}\t{self.creator}\t{self.publicationdetails}"    