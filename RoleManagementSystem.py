

import getpass
import bcrypt


membersData = [

    { 'MemberId' : 1, 'Role' : 'Admin', 'Name' : 'Admin User', 'Age' : 35, 'Email' : 'admin@gmail.com', 'Mobile' : '9849908934', 
     'Password' : b'$2b$12$xz.MoT8rOQG0Gk68oYm2O.CRAYPfSjZRE40.y3lJuw4nV25bqIzFa' },

    { 'MemberId' : 2, 'Role' : 'Member', 'Name' : 'Member User', 'Age' : 35, 'Email' : 'member1@gmail.com', 'Mobile' : '9849908944', 
     'Password' : b'$2b$12$xz.MoT8rOQG0Gk68oYm2O.CRAYPfSjZRE40.y3lJuw4nV25bqIzFa' },

    { 'MemberId' : 3, 'Role' : 'Member', 'Name' : 'Member User', 'Age' : 37, 'Email' : 'member2@gmail.com', 'Mobile' : '9849908954', 
     'Password' : b'$2b$12$xz.MoT8rOQG0Gk68oYm2O.CRAYPfSjZRE40.y3lJuw4nV25bqIzFa' },

] 


globalCurrentUserId = ""



def UserLogin() :

    global globalCurrentUserId
    globalCurrentUserId = ""
    
    userEmailAddress = input("Enter User's email Address :  ")
    userPassword = getpass.getpass(prompt="Enter User's password : ")

    for currentUser in membersData :

        if currentUser['Email'] == userEmailAddress :

            usrPasswordEncoded = userPassword.encode('utf-8')

            if bcrypt.checkpw(usrPasswordEncoded, currentUser['Password']) :

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
    
    currentUserPasswordEncoded = currentUserPassword.encode('utf-8')
    salt = bcrypt.gensalt()
    currentUserPasswordHashed = bcrypt.hashpw(currentUserPasswordEncoded, salt)
    
    currentUser['Password'] = currentUserPasswordHashed
    currentUser['Role'] = 'Member'
    currentUser['MemberId'] = len(membersData)

    membersData.append(currentUser)

    print(membersData)






