# def bla(*a):# variable positional arguments
#     print(a)

# bla(3, 3, 4, 576, 67, 8, 89, 8, 45)


# def key_word_func(a,b,c):
#     print("a =", a,"b =", b, "c =", c)

# key_word_func("b", "c", "a")
# key_word_func(b = "b", c = "c",  a ="a")

# def students(**data): # variable keyword arguments
#     print(data.values())

# students(ade=23, bolu=12, shade=54, sean=50)


# def products(**data): # variable keyword arguments
#     for key in data:
#         print(key, ":", data[key])

#     prices = sum(data.values())
#     print("Total :", prices )

# products(oil=23, rice=12, greens=54, garri=50)

# def sort_values(*scattered_list, should_be_ascending = True):

#     scattered_list = list(scattered_list)

#     for i in range(len(scattered_list)):

#         for i in range(len(scattered_list)-1):

#             if scattered_list[i][1] > scattered_list[i+1][1]:

#                     scattered_list[i], scattered_list[i+1] = scattered_list[i+1], scattered_list[i]
    
#     if should_be_ascending:
#         print(scattered_list)
#     else:
#         print(scattered_list[::-1])


# # sort_values(2,1,4,7,1,2,4,2,5,67,12, should_be_ascending=False)

# def string_processor(string):
#     string = string.lower()
#     unique_values = list(set(string))
#     quantities = []
    
#     for value in unique_values:
#         quantities.append(string.count(value))
    
#     zipped_vals = list(zip(unique_values,quantities))
    
#     sort_values(*zipped_vals, should_be_ascending=False)

    

# string_processor("I have a dream, a song to sing. To help me cope")

# def xyz():
#     print(1)

# # print(xyz())
# answer = xyz()
# print(answer)

# def tri_recursion(k):
#     if(k > 0):
#         x = tri_recursion(k - 1)
#         result = k + x
#         print(k, x, result)
#     else:
#         result = 0
#         print(result)
#     return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)


## FUNCTION DEFINATION

# def say_hello(name):

#     """THIS IS JUST TO DESCRIBE A FUNCTION AND ITS A DOCSTRING"""

#     print(f"hello{name}.")

#    # say_hello("tahir")


## USING DEF TO DEFINE SQUARE ROOT OF A NUMBER

# def sqrt(number,power):

#     answer = number**(1/power)

#     print(answer)
#     return answer

# x = sqrt(9,2)
# print(x)

# def sqrt(number):

#     answer = number**2

#     # print(answer)
#     return answer

# def sq(number):

#     answer = number**2

#     # print(answer)
#     return answer

# a = 9
# b = 6

# x = sqrt(sq(a) + sq(b)) 

# print(x)  


## USING DEF FUNCTION TO KNOW THE TIME A TXT IS WRITTEN USING DATETME FORMAT  
# 
# import datetime
# time_now = datetime.datetime.now()
# print(time_now.weekday()) ## GIVES WEEKDAY IN NUMERALS

# print(time_now.strftime("%a %H %M.")) ## gives a formatted srting representation of time

# time_stamp = time_now.strftime("%a %H %M")

# def get_timestamp():

#     time_now = datetime.datetime.now()

#     time_stamp = time_now.strftime("%a %b %d %H %M.")

#     return time_stamp

# def store_memory(memory,time_stamp,txt_len):

#     file = open(f"{time_stamp}-{txt_len}.txt","w")

#     file.write(memory)

#     file.close()
#     return True

# text = input("please enter a text:")
# time_stamp = get_timestamp()
# store_memory(text,time_stamp,len(text))

### POSITIONAL ARGUEMENT AND KEYWORD ARGUEMENT
# def sum_nums(*args):
#     print(args)

#     sum_nums(3,2,4,5,6,77,88,) 

# # VARIABLE POSITIONAL AND KEYWORD ARGUEMENT

# def sum_nums(**kwargs):
#     print(kwargs)


# word = list("alphabet")
# numbers = list("12345678")
# zipped_vals = zip(word,numbers)
# print(next(zipped_vals)


# print(list(zipped_vals))

# def mini(x):
#     return"A"+str(x)
# mini2 = lambda x: "A" + str(x)

# mapped_result = map(mini,numbers)
# print(list(mapped_result))

# mapped_result2 = map(mini2,numbers)
#print(list(mapped_result2))


# def factorial(n):
#  val

#     if n <= 1:
#         return n
#     else:
#         val = n + factorial(n-1)
#         print(val)
#         return
# factorial(3)           


## RECURSION

# def count_down(num):
#     if num == -1:
#         return(num)
#     print(num)
#     return count_down(num-1)

# count_down(10)        


previous_num = 0

nums = 20,60,90,103,109,120

for i in nums:
    print(i - previous_num)
    previous_num = i










