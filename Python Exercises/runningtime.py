#Ask the runtime thrice and record to a list.
#Any character other than float/integer will end the program.
import sys

num_tries = 3
runtime_list = []

count = 0
while count < num_tries:   
        for _ in range(num_tries): 
                try:
                        usr_input = float(input('How long did you run today?'))
                        runtime_list.insert(0,usr_input)
                        count += 1                
                except ValueError:
                       print('Bye!')
                       sys.exit()

print(runtime_list)

