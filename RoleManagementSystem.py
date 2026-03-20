

import getpass


membersData = [

    { 'MemberId' : 1, 'Role' : 'Admin', 'Name' : 'Admin User', 'Age' : 35, 'Email' : 'admin@gmail.com', 'Mobile' : '9849908934', 
     'Password' : '12345' },

] 


globalCurrentUserId = ""



def UserLogin() :

    userEmailAddress = input("Enter User's email Address :  ")
    userPassword = getpass.getpass(prompt="Enter User's password : ")

    for currentUser in membersData :

        if currentUser['Email'] == userEmailAddress and currentUser["Password"] == userPassword :

            global globalCurrentUserId
            globalCurrentUserId = userEmailAddress

            break

    if globalCurrentUserId == "" :

        print("Invalid User Name and Password provided")

    else :

        print("Logged in User is : ", globalCurrentUserId)


def LogoutUser() :

    global globalCurrentUserId
    globalCurrentUserId = ""


def AddMemberToTheLibrarySystem() :

    if globalCurrentUserId != "admin@gmail.com" :

        print("Please login as Admin to register the User")
        return
    
    currentUser = {}

    currentUser['Name'] = input("Please Enter the user name :  ")
    currentUser['Age'] = input("Please Enter the Age :  ")
    currentUser['Email'] = input("Please Enter the Email Address :  ")
    currentUser['Mobile'] = input("Please Enter the Mobile Number :  ")

    currentUserPassword = getpass.getpass(prompt="Enter the User Password : ")
    currentUserRePassword = getpass.getpass(prompt="Re-Enter the User Password : ")

    if currentUserPassword != currentUserRePassword :

        print("Entered Passwords do not match")
        return
    
    currentUser['Password'] = currentUserPassword
    currentUser['Role'] = 'Member'
    currentUser['MemberId'] = len(membersData)

    membersData.append(currentUser)

    print(membersData)






