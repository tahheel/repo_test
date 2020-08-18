# quantity = 5

# x = 0
# y = 1
# print(x)
# print(y)

## FIBONNACI SERIES:

# for i in range(quantity):
#     print(x + y)
#     x, y = y, x+y

## SLICING AND INDEXING:

# students_scores= [
#     ["atha", [
#         ["m",30],
#         ["e",30]],
#         [["reading","20%"], ["playing","80%"]]
#         ], 
#     ["Flipzig", [
#         ["m",60],
#         ["e",47]],
#         [["Sleep","40%"], ["Eat","60%"]]
#         ], 
#     ["bolu", [
#         ["m",30],
#         ["e",30]],
#         [["singing","40%"], ["jumping","60%"]]
#         ], 
#     ["seun", [
#         ["m",30],
#         ["e",30]],
#         [["dancing","45%"], ["traveling","45%"]]
#     ]
#     ]

# target_student = students_scores[2]

# name = target_student[0]
# # print("Name : ", name)

# # math_score = target_student[1][0][1]
# # print("Math Score : ", math_score)

# # english_score = target_student[1][1][1]
# # print("English Score : ", english_score)

# # hobbies = target_student[2]

# # hobby1_is_greater = int(hobbies[0][1][:-1]) > int(hobbies[1][1][:-1]) 
# # favourite_hobby = hobbies[0][0] if hobby1_is_greater == True else hobbies[1][0]
# # print("Favourite Hobby is : ", favourite_hobby)

# for target_student in students_scores:

#     name = target_student[0]
#     print("Name : ", name)

#     math_score = target_student[1][0][1]
#     print("Math Score : ", math_score)

#     english_score = target_student[1][1][1]
#     print("English Score : ", english_score)

#     hobbies = target_student[2]

#     hobby1_is_greater = int(hobbies[0][1][:-1]) > int(hobbies[1][1][:-1]) 
#     favourite_hobby = hobbies[0][0] if hobby1_is_greater == True else hobbies[1][0]
#     print("Favourite Hobby is : ", favourite_hobby)

#     print()
#     print("-------------------------")
#     print("-------------------------")
#     print()


## FIBONACCI SERIES:

# x,y = 0,1

# while y<100:
#     print(x+y)
#     x,y = y,x+y

## REVERSE A WORD

# word = input("enter a word to reverse:")

# for char in range(len(word) -1,-1,-1,):

#     print(word[char],end="")

#     print("\n")

    

# i = 7
# while i < 7:
#     print(i)
#     if i==3:
#         continue
#     i=+1

## ASSIGNMENT (CHANGE FROM ONE UNIT TO ANOTHER IN TEMP);


# unit = input("Enter the unit you want to convert to? ('F' for Fahrenheit and 'C' for Celsius): ")

# t = float(input("Enter the temperature you want to convert: "))

# con = 0

# if unit == "f":

#     con = 5*((t-32)/9)

#     print(str(t) + "ºF equals to " + str(con) + "ºC")

# elif unit == "c":

#     con = (9*(t/5))+32

#     print(str(t) + "ºC equals to " + str(con) + "ºF")



# unit=input("Insert the temperature to convert:")
# temp=float
# result=input("Type C for convert to Celsius and F for Fahrenheit:")
# if result == 'F':
#      convert= (9*temp+32*5)/5
#      print("Fahrenheit is :",convert)
# elif result == 'C':
#         convert = (5 * temp - 32 * 5) / 9
#         print("Celsius is :", convert)
# else:
#             print("Please insert correct syntax")

## ASSIGNMENT (USING LOOP)
# n = 10
# for i in range(10):
#     if i <=5:
#         print('* ' *i)
#     elif i > 5:
#         print('* ' * (n - i))

# n=5
# for i in range(1,n+1):
#     print("* " *i)
# for i in range(n-1,-1,-1):
#     print("* " *i)


# word = input("Enter a word that you would want to reverse: ")
# print(word[::-1])

## ASSIGNMENT (USING LOOP TO GET ODD OR EVEN IN A RANGE OF NUMS)

# even=0
# odd=0
# for i in range(1,20):
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1
#         print("The number of even numbers is "+str(even))
#         print("The number of odd numbers is "+str(odd))


# odd = 0
# even = 0

# for i in range(1,100):
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1
#         print("the nums of even is "+str(even))
#         print("the nums of odd is "+str(odd))

## ADDING MR TO NAMES IN A LIST

# names = ["john","paul","sean"]

# index = 0

# while True:
#     print(index,names[index])

#     names[index] = "Mr" + names[index]

#     index +1

#     if index== len(names):
#         break
#     print(names)


# names = ["john","paul","sean"]

# for index in range(len(names)):

#     names[index] = "Mr" + names[index]
#     print(names)

## APPENDING TO A LIST


#list_of_values_entered = []

# while True:
#     value = input("please enter a value\n:")
#     list_of_values_entered.append(value)

#     for value in list_of_values_entered:
#         print(value.center(10),str(len(value)).center(10))



# list_of_values_entered = []

# while True:
#     value = input("please enter a value\n:")

#     list_of_values_entered.append(value)

#     print("you now have",len(list_of_values_entered), "values in your list")

#     stop_or_continue = input("press y to continue entering values or n to stop:")

#     if stop_or_continue=="n":
#         break
# total_character = 0

# print("value".center(10),"lenght".center(10),"Qty_A".center(10),"Qty_B".center(10),"Qty_C".center(10))

# for value in list_of_values_entered:
#     lenght_of_value = len(value)"Qty_A".center(10)

#     total_characters+=lenght_of_value

#     print(value.center(10),str(lenght_of_value).center(10),str(value.count("a")).center(10),str(value.count("b")).centre(10),str(value.count("c")).center(10))

# print(f"\nValues in list : {len(list_of_values_entered)} Total characters : {total_characters}:")


# word_list = []
# index = 0

# for char in "alphabet":
#     index += 1
#     word_list.append((index,char,char.upper()))
#     print(word_list)


## EXTEND

# nums = [1,2,3,5,6,7]

# nums.insert(3,4)
# print(nums)


# nums = [1,2,34,7,7,7,7,7,7]

# number_of_sevens =nums.count(7)

# for q in range(number_of_sevens):
#     nums.remove(7)


### Write a script that takes in txt with dashes as missing values.Then take in a list of values and numbers
## and then insert these values iiinto the dashes based on the corresponding number.

sentence = input("please enter your sentence \n with dashes denoting blankpoints :\n")
replacements =input("please enter your replacements in order\n seperated by commas:\n")

##SPLIT SENTENCE INTO WORDS
sentence_words = sentence.split(" ")

print(sentence_words)

## GET CORRESPONDING REPLACEMENTS
replacement_word = replacements.split(',')
replacement_index = 0

## search and replace dashes with replacement words
for i in range(len(sentence_words)):

    if sentence_words[i].find("_") != -1:

        sentence_words[i] = sentence_words[i].replace("_",replacement_word[replacement_index])
        replacement_index+=1

print(sentence_words)
