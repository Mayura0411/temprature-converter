temp=float(input("Enter the temprature in celcius:"))
far=(temp*1.8)+32
print("%0.1f degree celcius is equal to %0.1f degree farhrenheit"%(temp,far))
if(far>=104):
    print("it's hot")
elif(far<=50):
    print("it's cold")
else:
    print("the temprature is nice")