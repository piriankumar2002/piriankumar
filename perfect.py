#perfect number

Input_Number = int(input("Enter the number: "))
Sum = 0
for i in range(1, Input_Number):
    if(Input_Number % i == 0):
        Sum = Sum + i
if (Sum == Input_Number):
    print("Number is a Perfect Number.")
else:
    print("Number is not a Perfect Number.")
