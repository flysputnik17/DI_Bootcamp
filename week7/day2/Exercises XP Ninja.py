
side = int(input("Please Enter any Side of a Square  : "))

print("Hollow Square Star Pattern")
i = 0
while(i < side):
    j = 0
    while(j < side):
        if(i == 0 or i == side - 1 or j == 0 or j == side - 1):
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
        j = j + 1
    i = i + 1
    print()

# its sorts the numbers in the alist
def insertion_sort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
insertion_sort(alist)
print(alist)