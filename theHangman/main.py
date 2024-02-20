import random
import sys

word_list = []
chosen_word_list = []
slot_list = []
slots = ""
choice = ""
position = ""
tries = 3

# Υποστήριξη ελληνικών χαρακτήρων
sys.stdin.reconfigure(encoding='utf-8')

print("#################################################")
print("Καλως ήρθατε στην Κρεμάλα!\n"
    "Η python επιλέγει μια τυχαία λέξη\n"
    "κι εσείς έχετε 3 προσπάθειες για να την βρείτε!")
print("#################################################\n")

# Άνοιγμα text αρχείου
with open('words.txt', 'r', encoding='utf-8') as file:
    # Προσθήκη όλων των λέξεων σε λίστα
    for line in file:
        if line.strip():
            word_list.append(line.strip())

# Επιλογή μιας τυχαίας λέξης απο την λίστα
word_chosen = random.choice(word_list).upper()

# Δημιουργία κρυφής λέξης
for letter in word_chosen:
    chosen_word_list.append(letter)
    slot_list.append("_")
    slots += letter


# Μέθοδος επαλήθευσης επιλογής του χρήστη
def checkLetter(user_input):
    global slot_list
    global tries
    if choice == word_chosen.upper():
        print("\nΒρήκες την λέξη! Κέρδισες!")
        print("Η λέξη ήταν", word_chosen)
        slot_list = word_chosen
    elif len(choice) > 1 or choice == " " or choice.isdigit():
        print("Επιλέξτε μόνο ένα γράμμα: ")
    else:
        if user_input in word_chosen:
            print("\nΤο γράμμα " + choice + " υπάρχει στην λέξη! Μπράβο!")
            for index, element in enumerate(word_chosen):
                if element == user_input:
                    slot_list[index] = element
        else:
            print("\nΤο γράμμα " + choice + " δεν υπάρχει στην λέξη!")
            tries -= 1
            print("Προσπάθειες που έχουν απομείνει:", tries)
            if tries == 0:
                print("\nΛυπάμαι αλλά έχασες! Δοκίμασε ξανά!")
                print("Η λέξη ήταν", word_chosen)
    if tries > 0 and "_" not in slot_list and choice != word_chosen.upper():
        print("\nΒρήκες την λέξη! Κέρδισες!")
        print("Η λέξη ήταν", word_chosen)

while "_" in slot_list:
    if tries > 0 and "_" in slot_list:
        print("Λέξη: ", ' '.join(slot_list))
        choice = input("Επιλέξτε γράμμα: ").upper()
        checkLetter(choice)
    else:
        break






























































































