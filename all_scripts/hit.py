a=int (input("enter a num :"))

k=a+1
k=k/2
print (k)
r,c=0,0


for l in range (k) :##l means iterations ,int of (a+1)/2 times.... a = side of the square 
 if  r < a and c < a :            ##to keep constarints for r,c...
   
  for i in range (1) : 
   
   print(((2*c)+1)/(2.0),((2*r)+1)/(2.0))
   r=r+4
   print()

 if  r < a and c < a :

  print(((2*c)+1)/(2.0),((2*r)+1)/(2.0))
  c=c+1
  print()

 if  r < a and c < a : 

  for i in range (1):
    
    print(((2*c)+1)/(2.0),((2*r)+1)/(2.0))
    r=r-4
    print()
    
 if  r < a and c < a :
  print(((2*c)+1)/(2.0),((2*r)+1)/(2.0))
  c=c+1
  print()
 
