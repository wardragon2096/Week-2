total=0
count=0
while True:
    num=input("Enter the number(press enter to exit):")
    
    if num=="":
        break
    else:
        total=total+int(num)
        count=count+1
        
avg=total/count
print("Sum of numbers: ", total)
print("Average:", avg)
