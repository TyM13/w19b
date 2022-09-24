print('welcome to the simple calculator, please select from the following options')
print('1: Addition')
print('2: Subtraction')
print('3: Multiplication')
print('4: Division')
users_choice = input('enter your selection:')
if(users_choice == 1):
    print()
  
    #addition
def add_user_num():
    user_choice = input('enter a number')
    user_choice = float(user_choice)

    add_user_num_one = add_user_num()
    add_user_num_two = add_user_num()
    results = add_user_num_one + add_user_num_two
    print(results)




    #Subtraction
def sub_user_num():
    user_choice = input('enter a number')
    user_choice = float(user_choice)

    sub_user_num_one = sub_user_num()
    sub_user_num_two = sub_user_num()
    results = sub_user_num_one - sub_user_num_two
    print(results)



  
    #Multiplication
def mult_user_num():
    user_choice = input('enter a number')
    user_choice = float(user_choice)

    mult_user_num_one = mult_user_num()
    mult_user_num_two = mult_user_num()
    results = mult_user_num_one * mult_user_num_two
    print(results)




    #Division
def div_user_num():
    user_choice = input('enter a number')
    user_choice = float(user_choice)

    div_user_num_one = div_user_num()
    div_user_num_two = div_user_num()
    results = div_user_num_one / div_user_num_two
    print(results)


    
  
    # def user_num():
    #     user_choice = input('enter a number:')
    #     try:
    #         user_choice = float(user_choice)
    #     except ValueError:
    #         print('you entered a invalid value')
    #         user_choice = user_num()
    #     except:
    #         print('something went wrong')     
    #         user_choice = user_num() #recursion gets rid of the first call and lest you overwrite it if it was invalid
    #     return user_choice

    