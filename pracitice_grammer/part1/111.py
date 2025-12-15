S = input()
i = 0
sum = int(S[0])
sign = "a"
for x in S:
   if x == "+":
       sign = "+"
       i += 1
       continue
   elif x == "-":
       sign = "-"
       i += 1
       continue
   else:
       if sign == "+":
           sum += int(x)
           i += 1
       elif sign == "-":
           sum -= int(x)
       else:
           continue
       
print(sum)
#基本的にはキャストしないといけない