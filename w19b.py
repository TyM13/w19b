print('welcome to the simple calculator, please select from the following options')
print('1: Addition')
print('2: Subtraction')
print('3: Multiplication')
print('4: Division')

def add_user_num(user_num_one, user_num_two):
    return user_num_one + user_num_two
   
def sub_user_num(user_num_one, user_num_two):
    return user_num_one - user_num_two

def mult_user_num(user_num_one, user_num_two):
    return user_num_one * user_num_two

def div_user_num(user_num_one, user_num_two):
    return user_num_one / user_num_two



users_choice = input('enter your selection:')
users_choice = int(users_choice)

user_num_one = input('enter a number:')
user_num_one = int(user_num_one)
user_num_two = input('enter a number:')
user_num_two = int(user_num_two)


#addition-----------
if(users_choice == 1):
    add_user_num(user_num_one, user_num_two)
    print(user_num_one + user_num_two)
#Subtraction----------
elif(users_choice == 2):
    sub_user_num
elif(users_choice == 3):
    mult_user_num
elif(users_choice == 4):
    div_user_num 