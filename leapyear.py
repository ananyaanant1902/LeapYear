a=int(input("Enter Year: "))
if(a%4==0): 
  if(a%100==0 and a%400==0):
      print("LEAP YEAR")
  else:
      print("NOT LEAP YEAR")
else:
    print("NOT LEAP YEAR")
