## Palindrome Tester

### Write a function that takes some input (a string, number, or combination of the two) and print out true
## if the input is a palindrome and false otherwise. Your function should IGNORE ALL PUNCTUATION.
    ## eg. "A man, a plan, a canal: Panama" IS a palindrome.
    ## eg. "No 'x' in 'Nixon'" IS a palindrome.

# string='A man, a plan, a canal: Panama'
#
# def normalize(someString):
#     upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     x = 0
#     normalized_string = ''
#     for x in range(0,len(string)):
#         if string[x] in upper_alphabet:
#             normalized_string = normalized_string + string[x].lower()
#         elif string[x] in lower_alphabet:
#             normalized_string = normalized_string + string[x]
#         else:
#             normalized_string = normalized_string
#     return normalized_string
#
# # print 'normalized string: %s' % normalize(string)
#
#
# def palindrome_test(somestring):
#     # reverse string
#     revString = ''
#     for n in string:
#         revString = n + revString
#
#     if normalize(somestring) == normalize(revString):
#         print 'Is it a palindrome? TRUE!'
#     else:
#         print 'Is it a palindrome? FALSE!'
#
# palindrome_test(string)

# This works but no need to split the string in half then reverse the second half.
# def palindrome_test(somestring):
#     string_length = len(string)
#     #print 'string length: %s' % string_length
#     half_string_length = string_length / 2
#
#     first_half_of_string = ''
#     second_half_of_string = ''
#
#     for n in range (0,half_string_length):
#         first_half_of_string = string[:half_string_length]
#         if string_length%2 == 0:
#             second_half_of_string = string[half_string_length:]
#         else:
#             second_half_of_string = string[half_string_length+1:]
#
#
#     #print 'first half of string: %s' % first_half_of_string
#     #print 'second half of string: %s' % second_half_of_string
#
#     reverse_second_half_of_string = ''
#     for n in second_half_of_string:
#         reverse_second_half_of_string = n + reverse_second_half_of_string
#
#     #print 'reverse second half of string: %s' % reverse_second_half_of_string
#
#     if first_half_of_string == reverse_second_half_of_string:
#         print 'Is it a palindrome? TRUE!'
#     else:
#         print 'Is it a palindrome? FALSE!'

## Geometric or Arithmetic?

### Write a function that takes a list of numbers, eg. [1, 2, 3, 4], and returns the word "Geometric" if the list
## is geometric in nature (meaning each term after the first is multiplied by some constant, as in 2, 4, 8, 16...),
## returns the word "Arithmetic" if the list is arithmetic (meaning each term after the first has some constant
## added or subtracted from it, as in (3, 8, 13, 18...), or returns the word "None" if neither case holds.


# numlist=[2,4,8,18]
#
# #not sure if this is right..
# def geometric(some_numlist):
#     result = ''
#     for x in range(1,len(some_numlist)):
#         if float(some_numlist[x]) / float(some_numlist[x-1]) == float(some_numlist[1]) / float(some_numlist[0]):
#             result = result + 'y'
#         else:
#             result = result + 'n'
#     # print result
#
#     if 'n' in result:
#         # print '%s is NOT geometric' % some_numlist
#         return 0
#     else:
#         # print '%s is geometric' % some_numlist
#         return 1
#
# # geometric(numlist)
#
# def arithmetic(some_numlist):
#     for x in range(1,len(some_numlist)-1):
#         result = ''
#         if some_numlist[x] - some_numlist[x-1] == some_numlist[x+1] - some_numlist[x]:
#             result = result + 'y'
#         else:
#             result = result + 'n'
#
#     if 'n' in result:
#         # print '%s is NOT arithmetic' % some_numlist
#         return 0
#     else:
#         # print '%s is arithmetic' % some_numlist
#         return 1
#
# arithmetic(numlist)
#
# print 'Number List: %s' % numlist
#
# if (geometric(numlist) == 0) and (arithmetic(numlist) == 0):
#     print 'None'
# elif geometric(numlist) == 1 and arithmetic(numlist) == 0:
#     print 'Geometric'
# else:
#     print 'Arithmetic'

## Strings and Substrings

### Write a function that takes two strings, str1 and str2. The function will tell you if a portion of the letters in
## str2 can be arranged to create str1. For example, if str2 is "goodness" and str1 is "good", then the function
## would output true because good (str2) is found in goodness (str1). However, the function would also output true
## if str2 were "reasonable" and str1 were "lean" because we can get the word "lean" from the letters in "reasonable."
    ### Note: If str2 were "reasonable" and str1 were "loon", we would get false. Even though all the letters in
    ## "loon" can be found in "reasonable", we cannot double-use the "o".

# str1 = 'reasonable'
# str2 = 'loon'
#
# # in_string = ''
#
# # print str2.count(str2[0])
#
# def amalgam(somestr1,somestr2):
#     x=0
#     while x < len(somestr2):
#         if somestr2[x] not in somestr1:
#             print 'False. %s not in str1.' % somestr2[x]
#             return
#         else:
#             if somestr2.count(somestr2[x]) > somestr1.count(somestr2[x]):
#                 print 'False. str2 contains too many of the letter %s!' % somestr2[x]
#                 return
#             else:
#                 x +=1
#     print 'True'
#
#
#
# amalgam(str1,str2)




## Caesar Cipher

### This is a fun one! Implement the Caesar Cipher -- that is, given a string, such as "Hello there" and a number,
## such as 2, shift every letter in the string down the alphabet by the number specified. So "a" becomes "c", "b"
## becomes "d", and so on. You should maintain the original capitalization and ignore punctuation marks.
    ## Note: The cipher should loop when it gets to the end of the alphabet. That is, "z" shifted by 1 becomes "a".
    ## Test input: CaeserCipher("Causer Cipher", 2) => "Ecguct Ekrjgt"

str1 = 'Causer Cipher'
num1 = 28

lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def CaeserCipher(str,num):
    # if the given number is greater than 26, divide it by 26 and use the remainder as the new number.
    if num > 26:
        num = num % 26

    x=0
    new_str=''

    for x in range(0,len(str)):
        old_letter = str[x]
        if str[x] in lower_alphabet:
            alpha_index = lower_alphabet.index(old_letter) + num
            # if alpha_index is greater than 25 (the letter 'z'), subtract 26 to loop thru the alphabet
            if alpha_index > 25:
                alpha_index = alpha_index - 26
            new_letter = lower_alphabet[alpha_index]
            new_str = new_str + new_letter
        elif str[x] in upper_alphabet:
            alpha_index = upper_alphabet.index(old_letter) + num
            if alpha_index > 25:
                alpha_index = alpha_index - 26
            new_letter = upper_alphabet[alpha_index]
            new_str = new_str + new_letter
        elif str[x] == ' ':
            new_str = new_str + ' '
        else:
            new_str = new_str + str[x]
        x += 1

    print new_str

CaeserCipher(str1,num1)
