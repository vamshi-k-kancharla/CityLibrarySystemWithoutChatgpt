
import RoleManagementSystem


def AddBookToTheLibrarySystem(currentBookListDataFrame) :

    print("current Logged in User is : " + RoleManagementSystem.globalCurrentUserId)

    if RoleManagementSystem.globalCurrentUserId != "admin@gmail.com" :

        print("Please login as Admin to Add a book to the library system")
        return
    
    currentBook = {}

    currentBook['Title'] = input("Please Enter the book Title :  ")
    currentBook['Author'] = input("Please Enter the book Author :  ")
    currentBook['Genre'] = input("Please Enter the book Genre :  ")

    currentBook['Status'] = 'available'
    currentBook['BookId'] = len(currentBookListDataFrame) + 1

    currentBookListDataFrame.loc[len(currentBookListDataFrame)] = currentBook

    print(currentBookListDataFrame)


def ShowAvailableBooksInGivenGenre(currentBookListDataFrame) :

    print("current Logged in User is : " + RoleManagementSystem.globalCurrentUserId)

    if RoleManagementSystem.globalCurrentUserId == "" :

        print("Please login as Admin/Member to view available books in current Genre")
        return
    
    inputGenre = input("Please Enter the Genre that you are interested in :  ")
    
    print(currentBookListDataFrame[currentBookListDataFrame['Genre'] == inputGenre])


def SearchBooksBasedOnTitle(currentBookListDataFrame) :

    print("current Logged in User is : " + RoleManagementSystem.globalCurrentUserId)

    if RoleManagementSystem.globalCurrentUserId == "" :

        print("Please login as Admin/Member to view books Based on Title")
        return
    
    inputTitle = input("Please Enter the Book Title that you are interested in :  ")
    
    print(currentBookListDataFrame[currentBookListDataFrame['Title'] == inputTitle])

    
def SearchBooksBasedOnAuthor(currentBookListDataFrame) :

    print("current Logged in User is : " + RoleManagementSystem.globalCurrentUserId)

    if RoleManagementSystem.globalCurrentUserId == "" :

        print("Please login as Admin/Member to view books Based on Author")
        return
    
    inputAuthor = input("Please Enter the Book Author that you are interested in :  ")
    
    print(currentBookListDataFrame[currentBookListDataFrame['Author'] == inputAuthor])

    
def BorrowABookFromLibrary(currentBookListDataFrame) :

    print("current Logged in User is : " + RoleManagementSystem.globalCurrentUserId)

    if RoleManagementSystem.globalCurrentUserId == "" or RoleManagementSystem.globalCurrentUserId == "admin@gmail.com" :

        print("Please login as Member to borrow the book based on Title")
        return
    
    inputTitle = input("Please Enter the Book Title that you are interested in :  ")

    currentBookListDataFrame.loc[currentBookListDataFrame['Title'] == inputTitle , 'Status'] = 'issued'

    print(currentBookListDataFrame[currentBookListDataFrame['Title'] == inputTitle])


def ReturnABookToLibrary(currentBookListDataFrame) :

    print("current Logged in User is : " + RoleManagementSystem.globalCurrentUserId)

    if RoleManagementSystem.globalCurrentUserId == "" or RoleManagementSystem.globalCurrentUserId == "admin@gmail.com" :

        print("Please login as Member to borrow the book based on Title")
        return
    
    inputTitle = input("Please Enter the Book Title that you are interested in :  ")

    currentBookListDataFrame.loc[currentBookListDataFrame['Title'] == inputTitle , 'Status'] = 'available'

    print(currentBookListDataFrame[currentBookListDataFrame['Title'] == inputTitle])
    


