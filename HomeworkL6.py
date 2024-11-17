numlar=int(input(" Enter the largest number"))
numsmall=int(input(" Enter the smallest"))
while(numsmall):
    numstore=numsmall
    numsmall=numlar%numlar
    numlar=numstore
print("HCF is ",numlar)


