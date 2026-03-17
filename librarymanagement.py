class Admin :
    def __init__(self, name , Employee_ID):
        self.name = name
        self.ID = Employee_ID
        
        self.registeredMembers = []

    def __str__(self):
        return  f"Admin name : '{self.name}' , ID : '{self.ID }' , Registerd Memebers : '{self.registeredMembers}' "

    def register(self , Students):
        self.registeredMembers.append(Students)

    def viewMembers(self):
        print  (f"\n\n The members registered in our system are :\n")
        for members in self.registeredMembers :
            print(f" Name : {members} \n\n" )

        
    pass

class Students :
    def __init__(self, name , library_ID):
        self.name = name 
        self.identification = library_ID
        self.myBooks = []
        self.returnedBooks = []

    def __str__(self):
        return f"{self.name} ID: {self.identification}"

    def borrow(self, book_name) :
        self.myBooks.append(book_name)
     
    
    def view_books(self ,):
        print(f"\n The Books {self.name} has  borrowed are : '{self.myBooks}'\n ")
    
    def return_book(self, book_name):
        if book_name in  self.myBooks :
            self.myBooks.remove(book_name)
            self.returnedBooks.append(book_name)
        print(f"\n  The books {self.name} has returned to the library are : {self.returnedBooks} ")

    def view_fees (self):
        pass


class Books :
    def __init__(self , name , Author ):
        self.name = name 
        self.author = Author
    pass


s1 = Students("Ian Mutai ", 1)
s2 = Students("Deby Monda ", 2)
s3 = Students(" Ryan Kiptoo ", 3)


s1.borrow('Diary of Leon')
s1.borrow("Atomic Habits")
s2.borrow ("The Principle of power")
s2.borrow("Think Big")
s1.view_books()
s2.view_books()
s2.return_book("Think Big")
s2.view_books()
