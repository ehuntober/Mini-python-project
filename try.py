
# word_list = ['cat','dog','rabbit']
# letter_list = []

# for a_word in word_list:
#     for a_letter in a_word:
#         letter_list.append(a_letter)

# print(letter_list)


# sq_list = []
# for x in range(1,11):
#     sq_list.append(x *10)

# print(sq_list)


# sq_list = [x * x for x in range(1,11)]
# sq_list = [x * x for x in range(1,11) if x % 2 != 0]
# print(sq_list)

# x = [ch.upper() for ch in 'comprenhension' if ch not in 'aeious']
# print(x)

# import math

# a_number = int(input("please enter a integer"))

# try:
#     print(math.sqrt(a_number))
# except:
#     print("Bad Value for square root")
#     print("Using absolute value instead")
#     print(math.sqrt(abs(a_number)))

# def sum_of_n(n):
#     the_sum = 0
#     for i in range(1, n+1):
#         the_sum = the_sum + i
#     return the_sum

# print(sum_of_n)

# def foo(tom):
#     fred = 0
#     for bill in range(1, tom+1):
#         barney = bill
#         fred = fred + barney
#     return fred
# print(foo(10))

def anagram_solution2(s1,s2):
    a_list1 = list(s1)
    a_list2 = list(s2)

    a_list1.sort()
    a_list1.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if a_list1(pos) == a_list2(pos):
            pos= pos +1 
        
        else:
            matches = False
    return matches

print(anagram_solution2('abcde','edcba'))

