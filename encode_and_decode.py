# ####################### FUNDAMENTALS OF PYTHON ###########################################

encode_dictionary = {
    "a" : "b",
    "b" : "y",
    "c" : "z",
    "d" : "r",
    "e" : "m",
    "f" : "q",
    "g" : "x",
    "h" : "l",
    "i" : "e",
    "j" : "s",
    "k" : "w",
    "l" : "f",
    "m" : "o",
    "n" : "p",
    "o" : "h",
    "p" : "t",
    "q" : "v",
    "r" : "d",
    "s" : "k",
    "t" : "u",
    "u" : "g",
    "v" : "n",
    "w" : "i",
    "x" : "J",
    "y" : "c",
    "z" : "a",
    " " : " "
}

decode_dictionary = {}

for (key, value) in encode_dictionary.items():
    decode_dictionary[value] = key

raw_text = input("Enter the secret message here: \n> ")


def encode():
    global secret_message

    secret_message = ""
    for each_letter in raw_text:
        secret_message += encode_dictionary[each_letter]
    print(secret_message)

encode()


def decode():
    decode_secret_message = ""
    for each_letter in secret_message:
        decode_secret_message += decode_dictionary[each_letter]
    print(decode_secret_message)


want_to_decode = input("Do you want to decode it?: ")
if want_to_decode == "Y".lower():
    decode()
else:
    pass

