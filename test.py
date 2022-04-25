


# def safeIntergerInput(prompt):
#     inputString = input(prompt)
#     try:
#         number = int(inputString)
#         return number
#     except ValueError:
#         print("Error in number format:", inputString)
#         return safeIntergerInput(prompt)

# if __name__ == "__main__":
#     age = safeIntergerInput("Enter your age:")
#     print("Your age is ",age )



# f = open("myfile.txt",'w')
# f.write("""All data output to or input from a text file must be strings. Thus, numbers must be converted to strings before output, and these strings must be converted back to numbers after
# input.
# You can output data to a text file using a file object. Python’s open function, which expects
# a file pathname and a mode string as arguments, opens a connection to the file on disk and
# returns a file object. The mode string is 'r' for input files and 'w' for output files. Thus, the
# following code opens a file object on a file named myfile.txt for output:""")
# f.close()

# import random
# f = open("integers.txt",'w')
# for count in range(500):
#     number = random.randint(1,500)
#     f.write(str(number) + "\n")
# f.close()

# f= open('myfile.txt','r')
# while True:
#     line = f.readline()
#     if line == "":
#         break
#     print(line)



# f = open("integers.txt",'r')
# theSum = 0
# for line in f:
#     line = line.strip()
#     number = int(line)
#     theSum + number
# print("the sum is ", theSum)



# f = open("integers.txt",'r')
# theSum = 0
# for line in f:
#     wordlist = line.split()
#     for word in wordlist:
#         number = int(word)
#         theSum += number
# print("The sume is", theSum)

from date import Date 

def main():
    bornBefore = Date(6,1,1998)

    date = promptAndExtractDate()
    while data is not None:
        if date <= bornBefore:
            print('Is a least 21 years of age: ', date)
        date = promptAndExtractDate()

def promptAndExtractDate():
    print('Enter a birth date.')
    month = int(input('month (0 to quit: '))
    if month == 0:
        return None
    else:
        day = int(input('day: '))
        year = int(input('year: '))
        return Date(month,day, year)

main()






















