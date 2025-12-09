print("Practicl 1 performed by Jay Kalambate")
x=int(input("Enter the value of x"))
b=int(input("Enter the value of bias"))
w=int(input("Enter the value of weight"))
ynet=x*w+b
print("Net input=",ynet)
print("Apply activation Function over net input, Ramp function")
if ynet<0:
    output=0
elif ynet>0 and ynet<=1:
    output=ynet
else:
    output=1

print("Output =", output)