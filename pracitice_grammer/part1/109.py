N = int(input())
firstNumber= int(input())
Answer = firstNumber
for i in range(1,N+1):
    line = input().split()
    sign = line[0]
    SecondNumber = int(line[1])
    if sign == "+":
        Answer = Answer + SecondNumber
        print(i,Answer)
    elif sign == "-":
        Answer = Answer - SecondNumber
        print(i,Answer)
    elif sign == "*":
        Answer = Answer * SecondNumber
        print(i,Answer)
    elif sign == "/":
        if SecondNumber == 0:
            print("error")
            break
        else:
            Answer = Answer // SecondNumber
            print(i,Answer)
        