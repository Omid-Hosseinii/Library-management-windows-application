class Book:
    def __init__(self,guideid,title,creator,publicationdetails):
        self.guideid = guideid
        self.title = title
        self.creator = creator
        self.publicationdetails = publicationdetails

    def __str__(self):
        return f"{self.guideid}\t{self.title}\t{self.creator}\t{self.publicationdetails}"    