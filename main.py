# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# # if __name__ == '__main__':
# #     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/


# first_name  = "Bro"
# last_name = "Myint"
# full_name = first_name + " " + last_name;
# print("Hello" + full_name)
# print(type(first_name))

#
# age = 21
# age += 1
# print("Your age is: " + str(age))
# print(type(age))
#
#
# human = False
# print(human)

# name= "Arfan"
# age = 21
# attractive = True
# name,age,attractive = "Bro",21,True
# print(name,age,attractive)


# name = "Bro Code"
# # print(name.upper())
# # print(name.lower())
# print(name*3)
#
# x=1
# y=2.0
# z="3"
#
# print(x)
# print(y)
# print(z)

# name = input("What is your name?")
# age = int(input("AGE?"))
# height = float(input("How tall are you"))
#
# print("Hello " + name + " Are you " + str(age))
# print("Your height is " + str(height))

import math
from random import randrange, random, choice

# x,y,z=1,2,3
# print(min(x,y,z))

# name = "Bro Code"
#
# first_name = name[:]
# last_name = name[4:8]
# funky_name = name[::-1]
# reversed_name = name[::-1]
#
# print(name)
# print(funky_name)
# # print(reversed_name)
#
# website = "http://google.com"
#
# slice = slice(7,-4)
#
# print(website[slice])

# temp = int(input("Whats the temp?"))
#
# if not(temp>=0 and temp<30):
#     print("cold")
# elif temp>=30 and temp<60:
#     print("hot")


# name = None
#
# while not name:
#     name = input("Enter your name: ")
#
# print("hello "+name)

# for i in "Bro Code":
#     print(i)

# row = int(input("How many rows?: "))
# column = int(input("How many col?: "))
#
# symbol = input("Enter a symbol: ")
#
# for i in range(row):
#     for j in range(column):
#         print(symbol,end="")
#     print()

# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break

# phone_number = "123-456-8901"
#
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i,end="")

# food = ["pizza","mohinga","pasta","burger"]
# food.append("ice cream")
# for x in food:
#     print(x)

# drinks = ["coffee","soda","tea"]
# dinner = ["pizza","burger","hotdog"]
# dessert = ["cake","ice-cream"]
#
# food = [drinks,dinner,dessert]
# print(food)s

# student = ("bro",21,"male")
# student.index("male")

# utensils = {"fork","spoon","knife","spoon"}
# dishes = {"bowl","plate","cup"}
#
# # dishes.update(utensils)
# dinner_table = utensils.union(dishes)
# for x in dinner_table:
#     print(x)
#
# capitals = {'Myanmar':'Nay Pyi Taw',
#     'USA':'Washington DC',
#     'China':'Beijing',
#     'Saudi':'Mecca'
# }
# capitals.update({'Germany':'Berlin'})
#
# capitals.update({'USA':'Los Angeles'})
# # print(capitals['China'])
# # print(capitals.get('Saudi'))
# # print(capitals.items())
# print(capitals.items())
# for key,value in capitals.items():
#     print(key,value)

# name = "juju Maung!"
#
# if(name[0].islower()):
#     name = name.capitalize()
#
# first_name = name[:4].upper()
# last_name = name[5:].capitalize()
# last_character = name[-1]
# print(last_character)

# def hello(name):
#     print ("Hello " + name)
#
# hello("Arfan")

# def multiply(n1,n2):
#     return n1*n2
#
# tmsp = multiply(2,3)
#
# print(tmsp)

# def hello(fname,lname,mname):
#     print("hello " + fname +" " +mname +" "+lname +" ")
#
# hello(mname="myo",fname="myint",lname="kyauk")

# s = "anagram"
# t = "nagaram"
# # if len is not the same, FALSE
# # s = {a:2,n:1}
# # t = {
# def isAnagram(s,t):
#
#
#     if len(s) != len(t):
#         return False
#
#     countS, countT = {}, {}
#
#     for i in range(len(s)):
#         countS[s[i]] = 1+ countS.get(s[i],0)
#         countT[s[i]] = 1+ countT.get(t[i],0)
#     for c in countS:
#         if countS[c] != countT.get(c,0):
#             return False
#     return True


# Input: nums = [1,2,3,1]
# Output: true

# nums = [1,2,3,3]
# def contain(nums):
#     hashSet = set()
#
#     for i in nums:
#         if i in hashSet:
#             return True
#         hashSet.add(i)
#     return False
# print(contain(nums))
# create a hashset:
# add stuffs into hashset: 1,2,3
# def containsDup(n):
#
#     for i in len(nums):
# Example 1:
#
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
#
# Input: s = "rat", t = "car"
# Output: false

# 1. Use HashMap
# Put the counts of each value in HashMap
# {a:2,n:1}
# str1 = "tmsp"
# # print(str1)


# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

# str = input("Whats the string? ")
# size = len(str)
# print(size)
# # input("give me a string")
# x=list(str)
# for i in x[::]:
#     print(i)

# for i in range(0,len(str)-1,2):
#     print("Index", i , ":",str[i])


list = [10, 20, 33, 46, 55]

# for i in range(len(list)):
#     print(list[i])
#
# for i in list:
#     print(i)

# for i in list:
#     if i%5==0:
#         print(i)
# print("Another ")
# for i in range(len(list)):
#     if list[i] % 5 == 0:
#         print(list[i])

# str_x = "Emma is good developer. Emma is a writer"
#
# # print("Emma appears " , str_x.count("Emma"))
#
# A=[1,2,3,4]
# B=[4,5,6,7]
#
# ans = set(B).difference(A)
#
# print(ans)

# size = input("Size? S,M, or L")
# add_pepp = input("Y or N")
# extra_cheese= input("Cheese or No")
# cost = 0
# s,m,l = 15,20,25
# extra_cheese = cost+1
#
# pepForM = 3
# pepForL= 3
# pepForS = 2
#
# if size == "S":
#     cost +=s
# elif size == "M":
#     cost+=m
# elif size == "L":
#     cost+=l
#
# if add_pepp =="Y":
#     if size == "S":
#         cost+=pepForS
#     else:
#         cost+=pepForM
#
# if extra_cheese =="Y":
#     cost+=1
# print(f"Your final: ${cost}")

# print("Welcome to love calc")
# name1 = input("whats your name?\n")
# name2 = input("whats your partner name?\n")
#
# name1,name2 = name1.lower(),name2.lower()

# arfanjuju
# names = name1+name2
#
# count = 0
# t = names.count("t")
# r = names.count("r")
# u = names.count("u")
# e = names.count("e")
# l = names.count("l")
# o = names.count("o")
# v = names.count("v")
# e = names.count("e")
# true = t+r+u+e
# love = l+o+v+e
# lovescore = str(true)+str(love)
# lovescore = int(lovescore)
# if lovescore < 10 or lovescore >90:
#     print(f"Your score is {lovescore}, you two matched!! ")
# elif lovescore>40 and lovescore<50:
#     print(f"Your score is {lovescore}, you two alright ")
# else:
#     print(f"Your score is {lovescore}. ")

#
# names = "Arfan Juju Myo PhuPhu"
# # input("Give me the names:with a space")
# names = names.split()
# num = len(names)
# rand = randrange(num)
# payer = names[rand]
# print(payer)
# # print(f"{choose} is going to pay")
#
# Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
# password = ''
# #Eazy Level - Order not randomised:
# #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# for i in range(1,nr_letters+1):
#     rand_i = choice(letters)
#     password +=rand_i
# for i in range(1,nr_symbols+1):
#     rand_i =choice(symbols)
#     password+=rand_i
# for i in range(1,nr_numbers+1):
#     rand_i =choice(numbers)
#     password+=rand_i
#
# print(password)
# password_list = []
# for i in password:
#     password_list.append(i)
#
# ''.join.random.shuffle(password_list)
# print(password_list)
# print(password)
# #Hard Level - Order of characters randomised:
# #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# import random
# #Step 1
#
# word_list = ["aardvark", "baboon", "camel"]
#
# #TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# chosen = random.choice(word_list)
# print(chosen)
# #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# guess = input("guess a letter: ")
# guess = guess.lower()
# #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# for i in chosen:
#     if guess == i:
#         print("correct")
#     else:
#         print("wrong")

# #Step 2
#
# import random
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
#
# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')
#
# #TODO-1: - Create an empty List called display.
# #For each letter in the chosen_word, add a "_" to 'display'.
# #So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
#
# display = []
# for i in chosen_word:
#     display.append("_")
#
# print(display)
# guess = input("Guess a letter: ").lower()
#
#
#
#
#
#
# #TODO-2: - Loop through each position in the chosen_word;
# #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
# for index in range(len(chosen_word)):
#     if chosen_word[index] == guess:
#         display[index] = chosen_word[index]
#
# print(display)
# #TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# #Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

# Step 3
#
# import random
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)
#
# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')
#
# #Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"
# end_of_game = False
# #TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
# while not end_of_game:
#     guess = input("Guess a letter: ").lower()
#
#     #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter
#
#     print(display)
#
#     if "_" not in display:
#         end_of_game = True

# Step 4
#
# import random
#
# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']

# end_of_game = False
# word_list = ["ardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)
#
# #TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
# #Set 'lives' to equal 6.
# lives = 6
# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')
#
# #Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"
#
# while not end_of_game:
#     guess = input("Guess a letter: ").lower()
#
#     #Check guessed letter
#     for position in range(word_length):
#         letter = chosen_word[position]
#         # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter
#             print(f"still {lives}")
#     #TODO-2: - If guess is not a letter in the chosen_word,
#     #Then reduce 'lives' by 1.
#     #If lives goes down to 0 then the game should stop and it should print "You lose."
#     if guess not in chosen_word:
#             lives -= 1
#             print(f"down to {lives}")
#             if lives == 0:
#                 end_of_game = True
#                 print("You lose!")
#     #Join all the elements in the list and turn it into a String.
#     print(f"{' '.join(display)}")
#
#     #Check if user has got all letters.
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")
#
#     #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
#     print(stages[lives])

# Write your code below this line 👇


# Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.
# import math
# def paint_calc(height,width,cover):
#     print(f"You need {math.ceil((height*width)/cover)}")
# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)


# Write your code below this line 👇
# def prime_checker(number):
#     if number % 2== 0:
#         print(f"{number} is a prime number")
#
# # Write your code above this line 👆
#
# # Do NOT change any of the code below👇
# n = int(input("Check this number: "))
# prime_checker(number=n)


# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
# #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(text,shift):
#     cipher_text = ""
#     for letter in text:
#         position = alphabet.index(letter)
#         new_position = position + shift
#         new_letter = alphabet[new_position]
#         cipher_text +=new_letter
#     print(cipher_text)
#     #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
#     #e.g.
#     #plain_text = "hello"
#     #shift = 5
#     #cipher_text = "mjqqt"
#     #print output: "The encoded text is mjqqt"
#
#     ##HINT: How do you get the index of an item in a list:
#     #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
#
#     ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
#
# #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
# encrypt(text,shift)

# def lengthOfLongestSubstring(s):
#     """
#     :type s: str
#     :rtype: int
#     """
#     charSet = set()
#     l = 0
#     res = 0
#     # a b c a b c b b
#     #       l
#     #             r
# #set = [a,b,c
#
#     for r in range(len(s)):
#         while(s[r] in charSet):
#             charSet.remove(s[l])
#             l+=1
#         charSet.add(s[r])
#         res = max(res,r-l+1)
#     return res
#
#     # hs = set()
#     # i, j, maxi = 0, 0, 0
#     # while j < len(s):
#     #     if s[j] not in hs:
#     #         hs.add(s[j])
#     #         maxi = len(hs)
#     #     else:
#     #         hs.remove(s[i])
#     #         i += 1
#     # j += 1
#     # return maxi
#
#
#
# print(lengthOfLongestSubstring("abcabcbb"))
#
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
# def encrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     cipher_text += alphabet[new_position]
#   print(f"The encoded text is {cipher_text}")
#
# #TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# def decrypt(cy_text,shiftAmount):
#     new_letter = ""
#     for position in cy_text:
#         print(position)
#         cur = alphabet.index(position)
#         new_pos = cur - shiftAmount
#         new_letter += alphabet[new_pos]
#     print(new_letter)
#   #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
#   #e.g.
#   #cipher_text = "mjqqt"
#   #shift = 5
#   #plain_text = "hello"
#   #print output: "The decoded text is hello"
#
#
# #TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
# if direction is "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# else:
#     decrypt(cy_text=text,shiftAmount=shift)

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))
#
# #TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
# def combine(start,shiftAmount,dir):
#     end = ""
#
#     for letter in start:
#         position = alphabet.index(letter)
#         if dir == "encode":
#             new_position = position + shiftAmount
#             end += alphabet[new_position]
#         else:
#             new_position = position - shiftAmount
#             end += alphabet[new_position]
#     print(f"The {dir}d text is {end}")
#
#
# def encrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     cipher_text += alphabet[new_position]
#   print(f"The encoded text is {cipher_text}")
#
# def decrypt(cipher_text, shift_amount):
#   plain_text = ""
#   for letter in cipher_text:
#     position = alphabet.index(letter)
#     new_position = position - shift_amount
#     plain_text += alphabet[new_position]
#   print(f"The decoded text is {plain_text}")
#
# # if direction == "encode":
# #   encrypt(plain_text=text, shift_amount=shift)
# # # elif direction == "decode":
# # #   decrypt(cipher_text=text, shift_amount=shift)
# # combine(start=text,shiftAmount=shift,dir=direction)
# # #TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
#
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
#             'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
#             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
#
# def caesar(start_text, shift_amount, cipher_direction):
#     end_text = ""
#     if cipher_direction == "decode":
#         shift_amount *= -1
#     for char in start_text:
#         if char in alphabet:
#             position = alphabet.index(char)
#             new_position = position + shift_amount
#             end_text += alphabet[new_position]
#         else:
#             end_text += char
#         # TODO-3: What happens if the user enters a number/symbol/space?
#         # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
#         # e.g. start_text = "meet me at 3"
#         # end_text = "•••• •• •• 3"
#
#
#     print(f"Here's the {cipher_direction}d result: {end_text}")
#
#
# # TODO-1: Import and print the logo from art.py when the program starts.
# from art import logo
# print(logo)
#
# # TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# # e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# # If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# # Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
# should_continue = True
# while should_continue:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#
#     # TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#     # Try running the program and entering a shift number of 45.
#     # Add some code so that the program continues to work even if the user enters a shift number greater than 26.
#     # Hint: Think about how you can use the modulus (%).
#     if shift >= 45:
#         shift = shift % 26
#     caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
#
#     result = input("Yes or No?\n")
#     if result == "no":
#         should_continue = False
#         print("BYEEE!")
#
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
#
# # TODO-1: Create an empty dictionary called student_grades.
# student_grades = {}
#
# # TODO-2: Write your code below to add the grades to student_grades.👇
# for person in student_scores:
#     score = student_scores[person]
#     if score > 91:
#         student_grades[person] = "Outstanding"
#     elif score > 80:
#         student_grades[person] = "Exceeds ecpectations"
#     elif score > 80:
#         student_grades[person] = "Acceptable"
#     else:
#         student_grades[person] = "Fail"
#
#
# # 🚨 Don't change the code below 👇
# print(student_grades)


# travel_log = [
# {
#   "country": "France",
#   "visits": 12,
#   "cities": ["Paris", "Lille", "Dijon"]
# },
# {
#   "country": "Germany",
#   "visits": 5,
#   "cities": ["Berlin", "Hamburg", "Stuttgart"]
# },
# ]
# #🚨 Do NOT change the code above
#
# #TODO: Write the function that will allow new countries
# #to be added to the travel_log. 👇
# def add_new_country(country,times,cities):
#     new_country = {}
#     new_country["country"] = country
#     new_country["visits"] = times
#     new_country["cities"] = cities
#     travel_log.append(new_country)
#
#
#
#
# #🚨 Do not change the code below
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)
#
#
#
#
# print("Welcome to the SECRET AUCTION PROGRAM")
#
#
#
#
# def find_higest(bidder):
#     # for i in bidder.values():
#     #     if
#     highest = 0
#     winner = ""
#     for i in bidder:
#         bid_amount = bidder[i]
#         if bid_amount > highest:
#             highest = bid_amount
#             winner = i
#     print(f"Winner is {winner} with amount {highest}")
#
# bidders = {}
# going = True
# while going:
#     name = input("Name?")
#     bid = int(input("Bid?"))
#     bidders[name] = bid
#     print(bidders)
#     going = input("any other bidders?")
#     if going == "no":
#         find_higest(bidders)
#         going = False

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#
#         else:
#             return True
#
#     else:
#         return False
#
#
# def days_in_month(year,month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year) and month == 2:
#         return 29
#     return month_days[month-1]
#
#
# # 🚨 Do NOT change any of the code below
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# def add(n1,n2):
#     return n1+n2
#
# def substract(n1,n2):
#     return n1-n2
#
# def multiply(n1,n2):
#     return n1*n2
#
# def divide(n1,n2):
#     return n1%n2
#
# operations= {
#     "+": add,
#     "-": substract,
#     "*": multiply,
#     "/": divide
# }
# def calculator():
#     num1 = int(input("first num?"))
#     for i in operations:
#         print(i)
#     should_go = True
#
#     while should_go:
#         operation_sym = input("pick a symbol: ")
#         num2 = int(input("second num?"))
#         calculation_function = operations[operation_sym]
#         first_answer = calculation_function(num1,num2)
#
#         print(f"{num1} {operation_sym} {num2} = {first_answer}")
#         if input(f"your answer: {first_answer}, wanna contiue? Y or N") == "y":
#             num1 = first_answer
#         else:
#             should_go =False
#             calculator()
#
# calculator()

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################
import random
#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# print(random.choice(cards))
# def deal_card():
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     return random.choice(cards)
#
# def calculate_score(cards):
#     if sum(cards) == 21 and len(cards) ==2:
#         return 0
#     if 11 in cards and sum(cards) >21:
#         cards.remove(11)
#         cards.append(1)
#
#     return sum(cards)
#
# def compare(user,comp):
#     if user > 21 and comp > 21:
#         return "You went over. You lose 😤"
#
#     if user == comp:
#         return "Draw!"
#     elif comp == 0:
#         return "Lose, opponent has BLACKJACK"
#     elif user == 0:
#         return "Win with BLACKJACK"
#     elif user>21:
#         return "You lose! :("
#     elif comp>21:
#         return "You WIN!!!"
#     elif user > comp:
#         return "You WIN!!"
#     else:
#         return "You LOSE!!! :("
#
#
# #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
# #user_cards = []
# #computer_cards = []
# def play_game():
#     user_cards = []
#     computer_cards = []
#     is_game_over = False
#
#     while len(user_cards) < 2 and len(computer_cards) < 2:
#         user_cards.append(deal_card())
#         computer_cards.append(deal_card())
#
#
#     while not is_game_over:
#         user_score = calculate_score(user_cards)
#         comp_score = calculate_score(computer_cards)
#         print(f"Your card: {user_cards}, current score: {user_score}")
#         print(f"Computer's first card: {computer_cards[0]}")
#         #Hint 6: Create a function called calculate_score() that takes a List of cards as input
#         #and returns the score.
#         #Look up the sum() function to help you do this.
#
#         if user_score == 0 or comp_score == 0 or user_score >21:
#             is_game_over = True
#         else:
#             user_go = input("Do you want another card? 'y' or 'n'? ")
#             if user_go == "y":
#                 user_cards.append(deal_card())
#             else:
#                 is_game_over = True
#
#     while comp_score!=0 and comp_score  < 17:
#         computer_cards.append(deal_card())
#         comp_score = calculate_score(computer_cards)
#
#     #Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
#
#     print(f"Your score: {user_score}, Comp score: {comp_score}")
#     print(compare(user_score,comp_score))
# #Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
#
# while input("restart? y or n") == "y":
#     play_game()

#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
# import random
# EASY = 10
# HARD = 5
# def check_answer(ans,guess,turn):
#     if guess < ans:
#         print("Too low")
#         return turn-1
#     elif guess > ans:
#         print("Too high")
#         return turn-1
#     else:
#         print(f"You got it!, the answer was {ans}")
# def set_level():
#     level = input("Choose difficulty: Easy or Hard?")
#     if level == "easy":
#         return EASY
#     else:
#         return HARD
#
# def game():
#     #Choose a random number
#     answer = random.randint(1, 100)
#     turns = set_level()
#     # print(f"You have {turns} attempts remaining to guess")
#     guess =0
#     while guess!=answer:
#         print(f"You have {turns} attempts remaining to guess")
#
#         # turns -=1
#         # print(f"You have {turns} attempts remaining to guess")
#
#         #Let the user guess
#         guess = int(input("Guess the number?"))
#
#         turns = check_answer(answer,guess,turns)
#         if turns == 0:
#             print("You have ran out of guess, you lose :(")
#             return
# game()


# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#
#   print(b_list)
#
# mutate([1,2,3,5,8,13])

# number = int(input("Which number do you want to check?"))
#
# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

# year = int(input("Which year do you want to check?"))
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not leap year.")

# for number in range(1, 101):
#   print(f"Our number: {number}")
#   if number % 3 == 0 and number % 5 == 0:
#     print("FizzBuzz")
#   elif number % 3 == 0:
#     print("Fizz")
#   elif number % 5 == 0:
#     print("Buzz")
#   else:
#     print(number)
#
# from data_file import data
# import random
#
# print(data[0].values())
#
# # for item in data:
# #     name = item['name']
# #     follower = item['follower_count']
# #     print(f"Name: {name} has {follower}")
# score = 0
# def choose_random():
#     first = random.choice(data)
#     second = random.choice(data)
#     while(first == second):
#         second=random.choice(data)
#     print(f"Compare A: {first['name']}, a {first['description']}, from {first['country']}")
#     print(f"Compare B: {second['name']}, a {second['description']}, from {second['country']}")
#     print(f"{first['name']}'s Follower: {first['follower_count']}")
#     print(f"{second['name']}'s Follower: {second['follower_count']}")
#     first_fol = first['follower_count']
#     sec_fol = second['follower_count']
#     return first_fol,sec_fol
# def compare(first,sec,guess):
#     if (guess == 'A' and first > sec) or (guess == 'B' and first < sec):
#         return True
#     else:
#         return False
#
# keep_going = True
# # check who has more follower and user input
# while keep_going:
#     first_fol, sec_fol = choose_random()
#     guess = input("Who has more follower?")
#     if compare(first_fol,sec_fol,guess):
#     # if (guess == 'A' and first_fol > sec_fol) or (guess == 'B' and first_fol < sec_fol):
#         print("You're right")
#         score +=1
#         print(f"Your score is {score}")
#     else:
#         print("WRONG!")
#         keep_going= False

# def solution(sequence):
#     # can remove one item in the list
#     # check if the list is increasing
#
#     counter = 0
#     for i in sequence:
#         print(sequence[i])
#         if sequence[i + 1] <= sequence[i]:
#             counter += 1
#             print(f"first: {sequence[i]}, second: {sequence[i + 1]}, counter:{counter}")
#             if counter > 1:
#                 return False
#     return True
#
# solution([1, 2, 1, 2])

# s = "durgasoftware"
# vowel = ['a','e','i','o','u']
# d = {}
#
# for ch in s:
#     if ch in vowel:
#         d[ch] = d.get(ch,0) + 1
#
# for k,v in sorted(d.items()):
#     print(f'{k} occurs {v} times')


# #anagram
# s1 = 'level'
# # s2 = 'zaly'
#
# out = ''
#
# if s1[::1] == s1[::-1]:
#     print("true")
# else:
#     print("false")

# import numpy as np
#
# # Create an empty array
#
# a= np.ones(3, dtype = int)
# print("matrix a:",a)
#
# b = np.ones([2,3],dtype=int)
# print("matrix b:",b)

# A = [[1, 4, 5, 12],
#     [-5, 8, 9, 0],
#     [-6, 7, 11, 19]]
#
# print("A =", A)
# print("A[1] =", A[1])      # 2nd row
# print("A[1][2] =", A[1][2])   # 3rd element of 2nd row
# print("A[0][-1] =", A[0][-1])   # Last element of 1st Row
#
# print("Third column")
# column = [];        # empty list
# for row in A:
#   column.append(row[2])
#
# third = []
# for i in A[0]:
#     third.append(i[2])
# print(third)'

# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]
#
# Y = [[5,8,1],
#     [6,7,3],
#     [4,5,9]]
#
# result = [[0,0,0],
#          [0,0,0],
#          [0,0,0]]
#
# row = len(X)
# col = len(X[0])
#
# for i in range(row):
#     for j in range(col):
#         result[i][j] = X[i][j] + Y[i][j]
#
# for i in result:
#     print(i)


# Program to transpose a matrix using a nested loop

# X = [[12,7],
#     [4 ,5],
#     [3 ,8]]
#
# result = [[0,0,0],
#          [0,0,0]]
#
# for i in range(len(X)):
#     for j in range(len(X[0])):
#         result[j][i] = X[i][j]
#
# for i in result:
#     print(i)



import numpy as np

# A = np.array([[1,2,3],[3,4,5]])
# print(A)
#
# zero = np.zeros((2,3),dtype=int)
# print(zero)

# A = np.arange(12).reshape(2,6)
# print(A)

# A= np.array([[2,4],[5,3]])
# B= np.array([[9,-3],[3,6]])
# print(A.transpose())
# print(A)


# A = np.array([[1, 4, 5, 12],
#             [-5, 8, 9, 0],
#             [-6, 7, 11, 19]])
#
# print(A[:,-1])

# A = np.array([[1, 4, 5, 12, 14],
#     [-5, 8, 9, 0, 17],
#     [-6, 7, 11, 19, 21]])
#
# print(A[:,1])
#

#
# MENU = {
#     "espresso": {
#         "ingredients": {
#             "water": 50,
#             "coffee": 18,
#         },
#         "cost": 1.5,
#     },
#     "latte": {
#         "ingredients": {
#             "water": 200,
#             "milk": 150,
#             "coffee": 24,
#         },
#         "cost": 2.5,
#     },
#     "cappuccino": {
#         "ingredients": {
#             "water": 250,
#             "milk": 100,
#             "coffee": 24,
#         },
#         "cost": 3.0,
#     }
# }
# profit = 0
# resources = {
#     "water": 300,
#     "milk": 200,
#     "coffee": 100,
# }
#
# def is_resource_sufficient(order):
#     for item in order:
#         if order[item] >= resources[item]:
#             print(f"Sorry, we are out of {item}")
#             return False
#     return True
#
# def process_coins():
#     print("Please insert coins.")
#     total = int(input("How many quarters: ")) *0.25
#     total += int(input("How many dimes: ")) *0.10
#     total += int(input("How many nickels: ")) *0.05
#     total += int(input("How many pennies: ")) *0.01
#     return total
#
# def is_trans(received,cost):
#     if received >= cost:
#         change = round(received - cost,2)
#         print(f"Here is ${change}! thank you")
#         global profit
#         profit+=received
#         return True
#     else:
#         print("Sorry, not enough money")
#         return False
#
# def make_coffee(drink,order):
#
#     for item in order:
#         resources[item] -= order[item]
#
#     print(f"Here is your {drink}")
#
# is_on = True
# while is_on:
#     choice = input("What would u like? (espresso/latte/cap)\n")
#
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         print(f"Water: {resources['water']}ml")
#         print(f"Milk: {resources['milk']}ml")
#         print(f"Coffee: {resources['coffee']}g")
#         print(f"Money: ${profit}")
#     else:
#         drink = MENU[choice]
#         if is_resource_sufficient(drink["ingredients"]):
#             payment = process_coins()
#             if is_trans(payment,drink['cost']):
#                 make_coffee(choice,drink['ingredients'])

#
# def solution(inputString):
#     stack = []
#     result = []
#
#     # Iterate through each character in the string
#     for c in inputString:
#         # If the character is an opening parenthesis,
#         # add the current result list to the stack and start a new result list
#         if c == '(':
#             stack.append(result)
#             result = []
#         # If the character is a closing parenthesis,
#         # reverse the current result list, append it to the top of the stack,
#         # and store the result in the result variable
#         elif c == ')':
#             result = stack.pop() + result[::-1]
#         # If the character is any other character, add it to the result list
#         else:
#             result.append(c)
#
#     # Join the characters in the result list into a single string and return it
#     return ''.join(result)
# print(solution("(abc)d(efg)"))


# "(())"

# def is_balanced(s):
#     stack = []
#     for c in s:
#         if s == "(":
#             stack.append(s)
#         elif s ==")":
#             if not stack:
#                 return False
#             stack.pop()
#     if not stack:
#         return True
#     else:
#         return False


# def solution(matrix):
#     price = 0
#     row = len(matrix)
#     col = len(matrix[0])
#     # for i in range(row):
#     #     for j in range(col):
#     #         print(matrix[i][j])
#     for row in matrix:
#         # Iterate through each element in the row
#         for element in row:
#             print(element)


    # price = 0
    # scary_rooms = []
    # for level in matrix:
    #     for (index, room) in enumerate(level):
    #         if index not in scary_rooms:
    #             price += room
    #             # print (price)
    #             if room == 0:
    #                 scary_rooms.append(index)
    # return price



# print(solution([[0, 1, 1, 2],
#           [0, 5, 0, 0],
#           [2, 0, 3, 3]]))

# matrix = [[1, 1, 1, 0],
#           [0, 5, 0, 1],
#           [2, 1, 3, 10]]

# haunted_room = []
# total = 0
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         if matrix[i][j] == 0:
#             haunted_room.append(j)
#     for k in range(len(matrix[0])):
#         if k not in haunted_room:
#             total += matrix[i][k]





# sum = 0
# for i in range(0, len(matrix)):
#     for j in range(len(matrix[0])):
#         if matrix[i][j] == 0:
#             haunted_room.append(j)
#
#     for k in range(len(matrix[0])):
#         if k not in haunted_room:
#             sum+=matrix[i][k]
# print(haunted_room)
#
# def solution(s):
#     stack= []
#     closeToOpen = {")" : "(",
#                    "]":"[",
#                    "}":"{"}
#
#     for c in s:
#         if c in closeToOpen:
#             if stack and stack[-1] == closeToOpen[c]:
#                 stack.pop()
#             else:
#                 return False
#         else:
#             stack.append(c)
#     return True if not stack else False
#
# solution("([)]")
#
#
# def solution(s):
#     # stack = ( [
#     # c -> )
#     # see close, check top of the stack
#     # if its the same as top of the stack, return true
#     stack = []
#     closeToOpen = {
#         ")" : "(",
#         "}" : "{",
#         "]":"["
#     }
#     for c in s:
#         if c == "(":
#             stack.append(c)
#         elif c ==")":
#             if closeToOpen[c] == stack[-1]:
#                 stack.pop()
#             else:
#                 return False
#     return True is not stack else False

# # Initialize a list to hold the rows of the picture
# picture = ["abc",
#             "ded"]
# border_picture = []
# rows = len(picture)
# cols = len(picture[0])
# # Iterate over the number of rows
# for i in range(rows + 2):
#     # Initialize a list to hold the characters in this row
#     row = []
#
#     # Iterate over the number of columns
#     for j in range(cols + 2):
#         # Append a '*' character to the row
#         row.append('*')
#
#     # Add the row to the picture
#     border_picture.append(row)
#
# print(border_picture)
#
# for i in range(rows):
#     for j in range(cols):
#         border_picture[i + 1][j + 1] = picture[i][j]
#
# print(border_picture)


# Initialize a 2D array with 3 rows and 4 columns
# array = [[1, 2, 3, 4],
#          [5, 6, 7, 8],
#          [9, 10, 11, 12]]
#
# row = len(array)
# col = len(array[0])
#
# for i in range(row):
#     for j in range(col):
#         print(array[i][j])

# A
# BB
# CCC
# DDDD

# n = int(input("enter n value:"))
#
# for i in range(n):
#     print(f"*"* int(i+1))


# rows = 3
# cols = 3
#
# mtx = [[0 for c in range(cols)] for r in range(rows)]
#
# # for r in range(rows):
# #     row = []
# #     for c in range(cols):
# #         row.append(0)
# #     mtx.append(row)
#
# print(mtx)


# nums = [1,2,3,4]
# fruits = ["apple","orange","Pears","peaches"]
#
# print([(i,f) for i in nums for f in fruits])
#
#
#
# import numpy as np
# # M1 = [[8, 14, -6],
# #         [12,7,4],
# #         [-11,3,21]]
# M2 = [[3, 16, -6],
#            [9,7,-4],
#            [-1,3,13]]
# # M1 = np.array(M1)
# M1 = np.array([[2, 4, 6, 8, 10],
#     [3, 6, 9, -12, -15],
#     [4, 8, 12, 16, -20],
#     [5, -10, 15, -20, 25]])
# print("All rows, third column", M1[:,2:])
# print("First rows, all column", M1[:1,])
# print("the first three rows and first 2 columns", M1[:3,:2])
#
# print("Before trans: ",M1)
#
# M1= M1.transpose()
# print("After trans: ",M1)
# res = []
# res = np.zeros([3,3],dtype=int)
# print(res)
# # for i in range(len(M1)):
# #     for j in range(len(M2)):
# #         res[i][j] = M1[i][j] + M2[i][j]
#
#
#
#
# print(res)
#


#
# print([i for i in nums])
# result = []
# for i in nums:
#     result.append(i*2)
#
# print(result)
#
# print([i*2 for i in nums])
#
# strings = ["intro", "to", "List","compre"]
#
# print([i.upper() for i in strings])
#
# def timesFive(num):
#     return num * 5
#
# results = []
# for i in nums:
#     i = timesFive(i)
#     print("i",i)
#     results.append(i)
#
# print(results)
#
# new_nums = [timesFive(i) for i in nums]
# print(new_nums)


# from turtle import Turtle, Screen
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.forward(100)
# timmy.color("AliceBlue")
# print(timmy)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# str_x = "Emma is good developer. Emma is a writer"
#
# emma = str_x.count("Emma")
# print("Emma appears ", emma, " times")

# for num in range(10):
#     for i in range(num):
#         print(num,end="")
#     print("\n")

# def palin(num):
#     if num == reversed(num):
#         return True
#     else:
#         return False

# num = str(121)
#
# i = 0
# j = len(num)-1
#
# while j > i:
#     if num[i]!=num[j]:
#         print("not palin")
#     i+=1
#     j-=1
# print("Palin")
# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
#
# list3 = []
#
# for i in list1:
#     if i % 2==1:
#         list3.append(i)
# for i in list2:
#     if i % 2==0:
#         list3.append(i)
# print(list3)

# num = 7536
#
# num = str(num)
#
# print(" ".join(num[::-1]))

for i in range(1,11):
    for j in range(1,11):
        print(i*j,end="")
    print("\t\t"
          "")
