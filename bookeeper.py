
'''
This program is for keeping the list of boook '''


import sys
bookList = []

def main():
    print("Welcome to BOOKKEEPER. Type:")
    print("\t\"ADD\" to add a book to your temp list.")
    print("\t\"LIST\" to read out your temp list.")
    print("\t\"READ\" to read an existing file.")
    print("\t\"SAVE NEW\" to save to a new file.")
    print("\t\"SAVE EXISTING\" to save to an existing file.")
    print("\t\"CLEAR\" to clear your temporary list.")
    print("\t\"EXIT\" to exit.")
    action()
    
def action():
    userInput = input()
    if userInput.lower() == "add":
        addBok()
    elif userInput.lower() == "list":
        listBook()
    elif userInput.lower() == "read":
        readBook()
    elif userInput.lower() == "save new":
        writeToNew()
    elif userInput.lower() == "save existing":
        writeToExisting(5)
    elif userInput.lower() == "clear":
        clearBook()
        
    elif userInput.lower() == "exit":
        sys.exit()
    else:
        print("The command was invalid!\n\n")
    
def addBok():
    title = input("what is the name of the book? ")
    author = input("what is the author's name ?")
    bookList.append({
        'TITLE': title.upper(),
        'AUTHOR': author.title()})
    print(bookList)
    main()
    
def listBook():
    for i in bookList:
        print(f"{i['TITLE']} by {i['AUTHOR']}")
    main()
    

        
def readBook():
    bList = []

    f = open(input("enter the filename"))
    for line in f:
        comma = line.find(",")
        title = line[0:comma].rstrip(',')
        author = line[comma + 1:].strip()
        bList.append({title.upper(), author.title()})
        print(f"{title.upper()}, {author.title()}")
        userInput = input("would you like to record this to your temporary list?")
        if userInput == 'yes':
            for i in bList:
                bookList.append(i)
            print("saved")
        else:
            print("Not saved")
        f.close()
        
def writeToNew(bookList):
    userInput = input("Enter the filename you'd like to export to.")
    f = open(userInput, 'w')
    for i in bookList:
        f.write(f"{i.title.upper()}, {i.author.title()}")
        f.close()

def writeToExisting(bookList):
    userInput = input("Enter the filename you'd like to add to.")
    f = open(userInput, 'a')
    for i in bookList:
        f.write(f"{i.tilte.upper()}, {i.author.title()}")
        f.close()    

def clearBook():
    bookList.clear
        


main()
action()
        







# class book(object):
#     def __int__(self, title, author):
#         self.title = title
#         self.author = author
        
#     def addBok(bookList):
#         title = input("what is the name of the book? ")
#         author = input("what is the author's name ?")
#         bookList.append({title.upper(),author.title()})
        
#     def listBook(BookList):
#         for i in BookList:
#             print(f"{i.title} by \n {i.author}")
        
#     def readBook(bookList):
#         bList = []
        
#         f = open(input("enter the filename"))
#         for line in f:
#             comma = line.find(",")
#             title = line[0:comma].rstrip(',')
#             author = line[comma + 1:].strip()
#             bList.append(book(title.upper(), author.title()))
#             print(f"{title.upper()}, {author.title()}")
#             userInput = input("would you like to record this to your temporary list?")
#             if userInput == 'yes':
#                 for i in bList:
#                     bookList.append(i)
#                 print("saved")
#             else:
#                 print("Not saved")
#             f.close()
            
#     def writeToNew(bookList):
#         userInput = input("Enter the filename you'd like to export to.")
#         f = open(userInput, 'w')
#         for i in bookList:
#             f.write(f"{i.title.upper()}, {i.author.title()}")
#             f.close()
    
#     def writeToExisting(bookList):
#         userInput = input("Enter the filename you'd like to add to.")
#         f = open(userInput, 'a')
#         for i in bookList:
#             f.write(f"{i.tilte.upper()}, {i.author.title()}")
#             f.close()        
        
            

#     running = True

#     while running == True:
#         print("Welcome to BOOKKEEPER. Type:")
#         print("\t\"ADD\" to add a book to your temp list.")
#         print("\t\"LIST\" to read out your temp list.")
#         print("\t\"READ\" to read an existing file.")
#         print("\t\"SAVE NEW\" to save to a new file.")
#         print("\t\"SAVE EXISTING\" to save to an existing file.")
#         print("\t\"CLEAR\" to clear your temporary list.")
#         print("\t\"EXIT\" to exit.")
        
#         running = False 

#     userInput = input()
#     if userInput.lower() == "add":
#         addBok(bookList)
#     elif userInput.lower() == "list":
#         listBook(bookList)
#     elif userInput.lower() == "read":
#         readBook(bookList)
#     elif userInput.lower() == "save new":
#         writeToNew(bookList)
#     elif userInput.lower() == "save existing":
#         writeToExisting(bookList)
#     elif userInput.lower() == "clear":
#         bookList = []
        
#     elif userInput.lower() == "exit":
#         running = False
#     else:
#         print("The command was invalid!\n\n")