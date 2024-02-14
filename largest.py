list=[45,56,98,3,67,9,90]
print(list)
def  largest(list):
     large=list[0]
     for i in list:
         if i>large:  
            large=i  
     return  large

print ("biggest  number is",largest(list))
    