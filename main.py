import random
import array as arr

HANGMAN_ASCII_ART = "Welcome to the game Hangman!\n" \
                    "     _    _\n    | |  | |\n" \
                    "    | |_| | _ _ _ _   _ _ _ _ __   _ _ _ _\n" \
                    "    |  _  |/ _' | ' \ / ' | ' ' _ \ / ' | ' \ \n" \
                    "    | |  | | (| | | | | (| | | | | | | (_| | | | |\n" \
                    "    ||  ||\_,|| ||\_, || || ||\_,|| ||\n" \
                    "                         _/ |\n                        |__/"
# print("   | |  | |")
# print("   | |_| | _ _ _ _   _ _ _ _ __   _ _ _ _")
# print("   |  _  |/ _' | ' \ / ' | ' ' _ \ / ' | ' \ ")
# print("   | |  | | (| | | | | (| | | | | | | (_| | | | |")
# print("   ||  ||\_,|| ||\_, || || ||\_,|| ||")
# print("                        __/ |")
# print("                       |_/")

photo1 = " x-------x\n"
# print("x-------x")

photo2 = " x-------x\n |\n |\n |\n |\n |\n"
# #print("|")
# print("|")
# print("|")
# print("|")
# print("|")

photo3 = "x-------x\n|       |\n|       0\n|\n|\n|\n"
# #print("|       |")
# print("|       0")
# print("|")
# print("|")
# print("|")

photo4 = " x-------x\n |       |\n |       0\n |       |\n |\n |\n"
# print("x-------x")
# print("|       |")
# print("|       0")
# print("|       |")
# print("|")
# print("|")

photo5 = " x-------x\n |       | \n |       0 \n |      /|\ \n |\n |\n"
# print("x-------x")
# print("|       |")
# print("|       0")
# print("|      /|\ ")
# print("|")
# print("|")

photo6 = " x-------x\n |       | \n |       0 \n |      /|\ \n |      /\n |\n"
# print("x-------x")
# print("|       |")
# print("|       0")
# print("|      /|\ ")
# print("|      /   ")
# print("|")

photo7 = " x-------x\n |       |\n |       0\n |      /|\ \n |      / \ \n |\n"
# print("x-------x")
# print("|       |")
# print("|       0")
# print("|      /|\ ")
# print("|      / \ ")
# print("|")

Levels = [photo1, photo2, photo3, photo4, photo5, photo6, photo7]
words = ["ModiiMn"]  # , "bet_horon", "hashmonaim", "maccabim"]


def Check_if_latter_is_ok(list, str):
    if (str < chr(65)) or (chr(90) < str < chr(97)) or (str > chr(122)):
        print("Invalid character\n")
        return False
    for item in list:
        if item == str:
            print("your alrady used at that latter")
            return False
    return True


def Print_the_Current_word_status(list):
    str = ""
    for item in index_letters:
        str += item + ' '
    print(str)


def Print_a_hangman_level(str):
    print(str)


def Print_latters_that_used(list, str):
    list += str
    print(list)


def Check_if_already_used_the_latter(list, str):
    for item in list:
        if item == str:
            return True
    return False


def Add_spaces_to_count(list):
    num = 0
    for item in list:
        if item == " ":
            num += 1
        if item == "_":
            num += 1
    return num


def Print_wrong_or_good(bool):
    if bool == True:
        print("Good :)")
    else:
        print("Wrong :(")


def Enter_word():
    word = (random.choice(words))
    return word


MAX_TRIES = 6
status = 0
latter_that_used = list()

print(HANGMAN_ASCII_ART)
print("MAX TRIES:", MAX_TRIES)

WORD = (random.choice(words))
List_of_letters = list(WORD)  # רשימה שאליה נשווה את האות המוכנסת
print("\n \n \n \n \n")

index_letters = list(WORD)  # רשימה שאליה ייכנסו האותיות החדשות

for i in range(len(index_letters)):  # איפוס הרשימה הסופית
    if (index_letters[i] != " "):
        index_letters[i] = "_"

Print_the_Current_word_status(index_letters)
Print_a_hangman_level(Levels[0])

count_latters = Add_spaces_to_count(List_of_letters)

while status != 6 and count_latters < len(WORD):
    found = False
    Latter = input("Enter a letter:")

    if Check_if_latter_is_ok(latter_that_used, Latter):
        for i in range(len(List_of_letters)):
            if List_of_letters[i] == Latter:
                index_letters[i] = Latter
                count_latters += 1
                found = True

        Print_the_Current_word_status(index_letters)
        if found == False:
            status += 1
            Print_a_hangman_level(Levels[status])
            Print_wrong_or_good(found)
            Print_latters_that_used(latter_that_used, Latter)

        else:
            Print_a_hangman_level(Levels[status])
            Print_wrong_or_good(found)
            Print_latters_that_used(latter_that_used, Latter)

if (status == 6):
    print("Loser!!!!!!!!")
else:
    print("Winner!!!!!!")
    print("The word is: ", WORD)

    # words = [Modiin, bet_horon, hashmonaim, maccabim ]

if (WORD == "Modiin"):
    print: ""
