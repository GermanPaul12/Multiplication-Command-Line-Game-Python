import random
multiplication = input('Input the mean number you want to calculate with. Type "no" to quit: ')
while multiplication != 'no':
  try:
    mult_table = [i for i in range(int(multiplication) * 10)]
    random_num_1 = random.choice(mult_table)
    random_num_2 = random.choice(mult_table)
    random_result = random_num_1 * random_num_2
    your_result = int(input(f'Enter the result to \033[34m{random_num_1} * {random_num_2} \033[0m:'))
    if random_result == your_result:
      print(f"\033[32m Congratulations \033[34m{your_result}\033[0m \033[32m is correct!  \033[0m")
    elif your_result == 'no':
      exit()
    else:
      print(f'Sorry but \033[34m {your_result} \033[0m is \033[31m wrong \033[0m. \033[32m {random_result} \033[0m was correct')
  except:
    print("Thank's for playing.")
    exit()