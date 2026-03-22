
'''
    
    Author : Vamshi Krishna Kancharla
    Have You used AI Tools to generate code : No 
    Have You used documentation for Syntax & to learn Concepts : Yes, Searched through google.
    Have You used ChatGpt to generate bookList of 20 items : Yes.
    
'''

import pandas as pd

from RoleManagementSystem import UserLogin, LogoutUser, AddMemberToTheLibrarySystem
from BookManagementSystem import AddBookToTheLibrarySystem, ShowAvailableBooksInGivenGenre, SearchBooksBasedOnTitle, ReturnMostPopularGenre
from BookManagementSystem import BorrowABookFromLibrary, ReturnABookToLibrary, SearchBooksBasedOnAuthor, ReturnListOfMembersThatBorrowedBooks


'''
    Task Input values to process the city library system
'''

def PrintTaskInputParameterDetails() :

    print("1 :=> Add a book to the system")
    print("2 :=> Add a member to the system")
    print("3 :=> Login with user credentials")
    print("4 :=> Show all the available books in a Given Genre")
    print("5 :=> Borrow a book")
    print("6 :=> Return a book")
    print("7 :=> List of members who have borrowed books")
    print("8 :=> Search For a book by Title")
    print("9 :=> Search For a book by Author")
    print("10 :=> Display the most Popular Genre")
    print("11 :=> Logout from current User Session")
    print("12 :=> Exit the Retail Transactions Insights code")

    print('\n')


'''
    Process the Library System from given input
'''

def ProcessCityLibrarySystemInput(currentBookListDataFrame) :

    '''
       Execute the code forever until the exit input is received from user

    '''

    while True :

        try :

            print('\n')
            print('\n')
            print('=' * 40)

            PrintTaskInputParameterDetails()
            task = int(input('enter the given task input : '))

            print('\n')

            match task :

                case 1 :

                    AddBookToTheLibrarySystem(currentBookListDataFrame)

                case 2 :

                    AddMemberToTheLibrarySystem()

                case 3 :

                    UserLogin()

                case 4 :

                    ShowAvailableBooksInGivenGenre(currentBookListDataFrame)

                case 5 :

                    BorrowABookFromLibrary(currentBookListDataFrame)

                case 6 :

                    ReturnABookToLibrary(currentBookListDataFrame)

                case 7 :

                    ReturnListOfMembersThatBorrowedBooks()

                case 8 :

                    SearchBooksBasedOnTitle(currentBookListDataFrame)

                case 9 :

                    SearchBooksBasedOnAuthor(currentBookListDataFrame)

                case 10 :

                    ReturnMostPopularGenre(currentBookListDataFrame)

                case 11 :

                    LogoutUser()

                case 12 :

                    break

                case _ :

                    print("Invalid input entered...Please try again")

        
        except Exception as e :

            print("Exception occured while executing the code => ", e)



'''
    Read the CSV File
    Print the DataFrame

'''

print("Reading CSV File of book list ")

currentBookListDataFrame = pd.read_csv("InputBookList.csv")

currentBookListDataFrame['Title'] = currentBookListDataFrame['Title'].str.lower()
currentBookListDataFrame['Genre'] = currentBookListDataFrame['Genre'].str.lower()
currentBookListDataFrame['Author'] = currentBookListDataFrame['Author'].str.lower()

print(currentBookListDataFrame)

ProcessCityLibrarySystemInput(currentBookListDataFrame)


