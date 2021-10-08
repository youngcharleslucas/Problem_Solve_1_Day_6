'''
To be a good problem solver, it is important to be able to break problems down. One way to go about this is to write out the 
steps it will take to solve the problem. These steps are written down in English in a manner that are easily explainable to 
someone who may not be technical. The idea is that in order to code something out, you first need to have a good understanding 
of what it is you are attempting to solve.

For each of the four problem solving problems below, write out the steps it will take to go about solving the problem. 
For example, once you are done writing out the steps for the “reverse a string” problem, you would then write out the code to 
solve the problem. You would then repeat the process for each ensuing problem. Ideally, this will be a good habit that you 
will develop and carry forward with you for all problems you encounter at devCodeCamp and beyond.

Problems to solve

1. Reverse a string

    a. Write code that takes a string as input and returns the string reversed

    b. i.e. “Hello” will be returned as “olleH”

2. Capitalize letter

    a. Write code that takes a string as input and capitalize the first letter of each word. Words will be separated by only one 
        space. i.e. “hello world” should be outputted as “Hello World”

3. Compress a string of characters

    a. For example, an input of "aaabbbbbccccaacccbbbaaabbbaaa" would compress to "3a5b4c2a3c3b3a3b3a"

4. BONUS CHALLENGE: Palindrome

    a. A word, phrase, or sequence that reads the same backward as forward i.e. madam

    b. Write code that takes a user input and checks to see if it is a Palindrome and reports the result

'''

# 1. Reverse a string-----------------------------------------------

"""
Create a string using user input
Create a function to reverse the string with string as argument
    for loop the string

"""
# string_1 = input("I can say things backwards. Ask me a word to say! ")

# def reverse_string (string_1):
#     reverse_word = ""
#     for letter in range(len(string_1)-1, -1, -1):
#         reverse_word += string_1[letter]
#     print(reverse_word)

# reverse_string(string_1)



# 2. Capitalize every word in a string----------------------------------------

"""
Create a user input for a string

Create a function that capitalizes every word of string:
    String for capitalized words
    for loop that pulls the index of each word:
        add the capitalized word to new string
    print the new string

"""

# capitalize_input = input("Give me a sentence to capitalize! ")

# def capitalize_string (capitalize_input):
#     capital = False
#     sentence = ""
#     for word_lower in range(len(capitalize_input)):
#         if capitalize_input[word_lower] == " ":
#             capital = True
#             sentence += capitalize_input[word_lower]
#         elif capital == True:
#             sentence += capitalize_input[word_lower].capitalize()
#             capital = False
#         elif word_lower == 0:
#             sentence += capitalize_input[word_lower].capitalize()
#         else:
#             sentence += capitalize_input[word_lower]
#     print(sentence)




# capitalize_string (capitalize_input)

# I know the goal is to be efficient with the amount of code we use, but I am proud of how much extra code I had to use to make this work



# 3. Compress a string of characters--------------------------------------------------------------

'''
create a string of code that can be compressed


'''
