print("Practical 6 Performed by JayKalambate")
def overlapping(list1,list2):
    for i in range(0,len(list1)):
        for j in range(0,len(list2)):
            if(list1[i]==list2[j]):
                return 1
            return 0
list1 = [1,2,3,4,5]
List2=[6,7,8,9,0]
if(overlapping(list1,List2)):
    print("overlapping !")
else:
    print("Not Overlapping !")
