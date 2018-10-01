#Nikita Sawant week 5 homework

#Ask for two DNA sequences
DNA_1 = input("Enter DNA Sequence 1: ")
DNA_2 = input("Enter DNA Sequence 2: ")

#Have variables for length of each String
DNA1_length = len(DNA_1)
DNA2_length = len(DNA_2)

#counting varibales

transitions = 0
transversions = 0
count = -1



#report how many different positions there are in the sequence

#checks if the length of the Strings are equal
if DNA1_length != DNA2_length:
   print("SIZES ARE NOT EQUAL!!!!!")
#if they are equal
else:
    badLetter = False # boolean value to track if there is a bad letter
    for letter in DNA_1: # loop through first DNA to check for bad letter
        if not(letter == "A" or letter == "G" or letter == "C" or letter == "T"):
            print("bad character '" + letter + "' found in DNA sequnce")
            badLetter = True # set true if bad letter is found
            break

    for letter in DNA_2: # loop through second DNA to check for bad letter
        if not(letter == "A" or letter == "G" or letter == "C" or letter == "T"):
            print("bad character '" + letter + "' found in DNA sequnce")
            badLetter = True # set true if bad letter is found
            break

    if not(badLetter): # only run if a bad letter is not found
        for letter in DNA_1:
            count += 1 # increment count each loop starting at 0

    #case for letter being A
            if letter == "A":
                if DNA_2[count] == "A":
                    continue
                elif DNA_2[count] == "C" or DNA_2[count] == "T":
                    transversions += 1
                elif DNA_2[count] == "G":
                     transitions += 1

    # case for letter being G
            elif letter == "G":
                if DNA_2[count] == "G":
                    continue
                elif DNA_2[count] == "C" or DNA_2[count] == "T":
                    transversions += 1
                elif DNA_2[count] == "A":
                     transitions += 1

    # case for letter being C
            elif letter == "C":
                if DNA_2[count] == "C":
                    continue
                elif DNA_2[count] == "A" or DNA_2[count] == "G":
                    transversions += 1
                elif DNA_2[count] == "T":
                     transitions += 1

    # case for letter T
            elif letter == "T":
                if DNA_2[count] == "T":
                    continue
                elif DNA_2[count] == "A" or DNA_2[count] == "G":
                    transversions += 1
                elif DNA_2[count] == "C":
                     transitions += 1


# total of different postions (total of transitions and tranvserisons)
        diff_pos = transitions + transversions

        print("There are " + str(diff_pos) + " different positions in the sequence")
        print("There are " + str(transitions) + " transitions")
        print("There are " + str(transversions) + " transversions")
