array=[]
evenarray=[]
oddarray=[]
n=int(input("enter the number of array elements to be inserted"))
for i in range(0,n):
  arr= int(input("enter array elements"))
  array.append(arr)
  if i%2==0:
    evenarray.append(array[i])
  else:
     oddarray.append(array[i])
evenarray=sorted(evenarray)
print("the sorted evenarray are:",evenarray)
oddarray=sorted(oddarray)
print("the sorted oddarray are:",oddarray)
print("the sum of second highest number is:",evenarray[-2]+oddarray[-2]