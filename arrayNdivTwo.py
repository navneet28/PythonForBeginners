ar=list(map(int,(input("Enter the elements of array: ").split(' '))))
print(ar)
l=int(len(ar)/2)
for i in range(0,l+1):
    if ar[l+1]==ar[i]:
        print(ar[i])
        break
