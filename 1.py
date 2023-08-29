"""Run the code in console using command line.
It'll run for 1 minute.
For every time it'll show 2 random numbers and random arithmetic operations such as add, subtract, multiply and divide. 
If the operation is divide then the divisor can not be 0.
It'll judge if your answer is correct or not, then show next question.
When time is up it'll show how many questions you answered and show the correct rate for total questions."""

import random
import time

def addition(first, second):
    return first+second

def subtraction(first,second):
    return first-second

def multiplication(first,second):
    return first*second

def division(first,second):
    return int(first/second)

ur_ans_arr=[]
cor_ans_arr=[]

t_end = time.time() + 60
while time.time() < t_end:

    num1=random.randint(0,10)
    num2=random.randint(0,10)
    op_num=random.randint(1,4)
    arr=['+','-','x','/']
    while(num2==0 and op_num==4):
        num2=random.randint(0,10)

    print('First num: ', num1, "       Operation: ", arr[op_num-1], "        Second num: ", num2)
    ans=input("Your Answer: ")
    ur_ans_arr.append(ans)
    cor_ans=0
    if(op_num==1):
        cor_ans=addition(num1,num2)
    elif(op_num==2):
        cor_ans=subtraction(num1,num2)
    elif(op_num==3):
        cor_ans=multiplication(num1,num2)
    elif(op_num==4):
        cor_ans=division(num1,num2)

    cor_ans_arr.append(cor_ans)

    if(int(ans)==cor_ans):
        print('Correct! Next Question\n')
    else:
        print('Bzz Wrong! Correct answer: ', cor_ans)
print('\nTime finished!')
cor_count=0
ind=0
for m in cor_ans_arr:
    if int(ur_ans_arr[ind])==int(m):
        cor_count+=1
    ind+=1
print('Score:', cor_count, '/',len(cor_ans_arr))
