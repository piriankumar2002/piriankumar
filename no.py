no=798965
sum_of_digits=0
while no>0:
    rem = no%10
    sum_of_digits = sum_of_digits + rem
    no=no//10
else:
    print(sum_of_digits)
