def binary_search(l,item):
   size=len(l)
   count=0
   left=0
   right=size-1
   mid=left+(right-left)//2
   while(left<=right):
      if(l[mid]==item):
         count=count+1
         print("Element is found ",l[mid])
         break
      
      elif(l[mid]>item):
         right=mid-1
      
      else:
         left=mid+1
      
      mid=left+(right-left)//2
   if(count==0):
     print("Element is not found ")

l=[2,5,6,34,2,14,63,134,340]
l.sort()
item=int(input("Enter the element that you want search = "))
binary_search(l,item)
