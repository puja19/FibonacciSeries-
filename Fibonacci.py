#Fibonacci numbers

#Starting two initial values
x1=0
x2=1

#Taking term number input from the user

#dummy variable
i=1
while i==1:
    x=int(input("Till which term number you want to display fibonacci series for? "))
    if x<=2:
	# As first two numbers of the series is already known the user is asked again to give other input
        print("Please enter value above 2")
        continue
    else:
	#printing of Fibonacci numbers
        print("Fibonacci numbers till term no. ", x)
        print(x1)
        print(x2)
        j=1
        while j<=(x-2):
            temp=x1+x2
            print(temp)
            x1=x2
            x2=temp
            j+=1
        if j==(x-1):
            break
        

