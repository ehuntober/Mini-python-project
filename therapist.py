# ################# THERAPIST ##############################################
from random import choice
from time import sleep


hedges = ["Please tell me more.", "Many of my patients tell me the same thing.", "Please continue.", "Wow, go ahead please", "Why did you say that?"]
qualifiers = ["Why do you say ", "You seem to think ", "Can you explain why "]

replacements = {
    "I":"You",
    "Me":"You",
    "My":"Your",
    "We":"You",
    "Us":"You",
    "Mine":"Yours",
    "You":"Me",
    "I've": "You've",
    "I'm" : "You're",
    "Cos" : "",
    }



def reply_user(sentence):
    probability = choice(range(1, 5))
    if probability <= 2:
        return choice(hedges).title()
    else:
        return f"{choice(qualifiers).title() + change_person(sentence)}?"





def flashback_response(sentence, response_tracker):
    sentence_holder = []
    msg = choice(response_tracker)
    msg = msg.split()

    for each_word in msg:
        sentence_holder.append(replacements.get(each_word, each_word))

    ending_part =  " ".join(sentence_holder)
    response_tracker.clear()
    return f"Earlier On, You said {ending_part}"




def change_person(sentence):
    sentence_holder = []
    sentence = sentence.split()

    for each_word in sentence:
            sentence_holder.append(replacements.get(each_word, each_word))
    return " ".join(sentence_holder)
        




def main():
    response_tracker = []
    print("\nHello, Good day...\nWhat can I do for you?\n")
    while True:
        sentence = input("\n>>> ")
        sentence = sentence.title()
        if sentence == "Quit":
            print("\n\t\tHave a nice day! <<<")
            break
        elif "Hello" in sentence:
            sleep(1)
            print("\n\t\tHello, What can I do for you? <<<")
        elif "Hi" in sentence:
            sleep(1)
            print("\n\t\tHi, what can I do for you? <<<")
        else:
            sleep(1)
            if len(response_tracker) == 10:
                print(f"\t\t{flashback_response(sentence, response_tracker)} <<<")
            else:
                print(f"\t\t{reply_user(sentence)} <<<")
                response_tracker.append(sentence)



if __name__ == "__main__":
    main()




