
import RoleManagementSystem

from datetime import datetime


bookListBorrowLog = {}


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

    print(currentBookListDataFrame.loc[currentBookListDataFrame['Title'] == inputTitle , 'Status'].iloc[0])

    if currentBookListDataFrame.loc[currentBookListDataFrame['Title'] == inputTitle , 'Status'].iloc[0] != 'available' :

        print("Book is already issued")
        return

    currentBookListDataFrame.loc[currentBookListDataFrame['Title'] == inputTitle , 'Status'] = 'issued'

    print(currentBookListDataFrame[currentBookListDataFrame['Title'] == inputTitle])

    LogTheBookIntoBorrowReturnLog(currentBookListDataFrame, inputTitle, 'borrowed')



def ReturnABookToLibrary(currentBookListDataFrame) :

    print("current Logged in User is : " + RoleManagementSystem.globalCurrentUserId)

    if RoleManagementSystem.globalCurrentUserId == "" or RoleManagementSystem.globalCurrentUserId == "admin@gmail.com" :

        print("Please login as Member to borrow the book based on Title")
        return
    
    inputTitle = input("Please Enter the Book Title that you are returning :  ")

    if DoesBorrowerAndReturnedMatch(currentBookListDataFrame, inputTitle) == False :

        print("Current User hasn't borrwed the book. User = " + RoleManagementSystem.globalCurrentUserId) 
        return
    
    currentBookListDataFrame.loc[currentBookListDataFrame['Title'] == inputTitle , 'Status'] = 'available'

    print(currentBookListDataFrame[currentBookListDataFrame['Title'] == inputTitle])
    
    LogTheBookIntoBorrowReturnLog(currentBookListDataFrame, inputTitle, 'returned')



def LogTheBookIntoBorrowReturnLog(currentBookListDataFrame, inputTitle, inputStatus) :

    currentBookId = currentBookListDataFrame.loc[currentBookListDataFrame['Title'] == inputTitle, 'BookId'].iloc[0]

    currentBorrowLog = {}

    currentBorrowLog['Time'] = datetime.now()
    currentBorrowLog['Status'] = inputStatus
    currentBorrowLog['User'] = RoleManagementSystem.globalCurrentUserId

    global bookListBorrowLog
    
    if currentBookId in bookListBorrowLog :

        bookListBorrowLog[currentBookId].append(currentBorrowLog)

    else :

        bookListBorrowLog[currentBookId] = []
        bookListBorrowLog[currentBookId].append(currentBorrowLog)

    print(bookListBorrowLog)


def DoesBorrowerAndReturnedMatch(currentBookListDataFrame, inputTitle) :

    currentBookId = currentBookListDataFrame.loc[currentBookListDataFrame['Title'] == inputTitle, 'BookId'].iloc[0]

    global bookListBorrowLog

    currentBookLogCount = len(bookListBorrowLog[currentBookId])

    if bookListBorrowLog[currentBookId][currentBookLogCount - 1]['User'] == RoleManagementSystem.globalCurrentUserId and bookListBorrowLog[currentBookId][currentBookLogCount - 1]['Status'] == 'borrowed' :

        return True

    else :
    
        return False





