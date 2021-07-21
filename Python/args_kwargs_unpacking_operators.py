#Objective:
#1 what does args*, kwargs* mean?
#2How to use them and why?
#3 How to unpack iterables with * and **?

def sum_nums(x, y):
	return x + y
print(sum_nums(2,3))


def sum_list(my_list):
	result = 0
	for x in my_list:
		result += x
	return result

list_of_num = [1,2,3,4,5,6]
print(sum_list(list_of_num))


#	*args vs **kwargs
# The first enables you to have multiple arguments.
# The second enables you to habe multiple keyword arguments.

#This function can deal with any number of inputs as long as they are float or int types
#All the inputs are considered as tuples

def sum_nums(*args):
	result = 0
	for x in args:
		result += x
	return result

print(sum_nums(1,2,3))


#Kwargs
def my_sum(a, b, *args, option=True):
	result = 0
	if option:
		for x in args:
			result += x
		return a + b + result
	else:
		return result

print(my_sum(1,2,3,4,5, option = False))

#kwargs is treated as dictionary
def make_sentence(**kwargs):
	result = ""
	for arg in kwargs.values():
		result += arg
	return result

print(make_sentence(a= "Bassel", b = " is ", c = "an Engineer."))

def human_details(**kwargs):
	for key, value in kwargs.items():
		print(f"{key}: {value}")

human_details(name="Bassel", job="Engineer", age= "22")
print('---------')
human_details(name="Ahmed", job="Student")


#Revision for everything has been explained:
def print_args(x, y, *args, option=True, **kwargs):
	print(x,y)
	print(args)
	print(option)
	print(kwargs)

print_args(1,2, "3 is args", "4 is args", channel = "Codebery", action = "subscribe")

#Important Note:
# Arrangements in the arguments of the function will result in errors...
#	*args and **kwargs again:
#	*args packing the elements in tuple.
#	**kwargs packing the keyward arguments in dict.

#Examples
my_list = [1,2,3]
print(my_list) #packing
print('----------')
print(*my_list) #unpacking

def my_sum(x, y, z):
	print(x + y + z)

my_sum(*my_list)

# Use the function for summing the lists you get...
def sum_lists(*args):
	result = 0
	for x in args:
		result += x
	return result

list_1 = [2,5,8]
list_2 = [6,5,4]
list_3 = [7,5,3]
print(sum_lists(*list_1, *list_2, *list_3))

a, *b, c = [1,2,3,6,5,8,5]
#	b will take the values in between first and last elemnts of the list.

#combine two lists or many whatever you want.
ax = [1,2,3,5]
bx = [8,5,2,3]
total = [*ax, *bx] #Result will be [1,2,3,5, 8,5,2,3]





