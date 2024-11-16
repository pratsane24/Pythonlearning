
# import argparse
# if __name__=="__main__":
#     parser = argparse.ArgumentParser()
#     args = parser.parse_args()

# There are 2 types of Arguments,
# 1. Positional
# 2. Optional


# Postional
#Here we are writing a program that takes 3 inputs,
# 1.First no
# 2. Second no
# 3.Operation("add,sub,multiply")
# It should return result of operation based on inputs


import argparse
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number1",help="first number")
    parser.add_argument("number2",help="second number")
    parser.add_argument("operation",help="operation")
    args = parser.parse_args()

    print(args.number1)
    print(args.number2)
    print(args.operation)

 
n1 = int(args.number1)
n2 = int(args.number2)
result = None
if args.operation=="add":
    result = n1+n2
elif args.operation =="substract":
    result= n1-n2
elif args.operation == "multiple":
    result= n1*n2

print(result)