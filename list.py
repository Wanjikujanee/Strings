
#Reverse the string
x="Epuu is loving"
y=x.split()[::-1]
l=[]
for i in y:
    l.append(i)
    print("".join(l))


#Remove ith char fron string
# x = "janewanjiku"
y = ""
for i in range(len(x)):
    if i != 2:
        y = y + x[i]
print (x + y)


# find length
def findLen(str):
    count = 0   
    for i in str:
        count += 1
    return count
str = "Janemarywanjiku"
print(findLen(str))


#print even length words in string
x="This is 2022 class"
y=x.split(" ")
for i in y:
  if len(i)%2==0:
    print(i)
 
#Python program to capitalize
# first and last character of
# each word of a String
def letters(str):
     str = i = str.title()
     i =  ""
     for word in str.split():
        i += word[:-1] + word[-1].upper() + " "
     return i[:-1]  
     
print(letters("jane mary wanjiku"))
print(letters("hopperlab class"))


# Uppercase Half String
# Using upper() + loop + len()
  

x = 'childrenplayinginplayground'
y= len(x) // 2
string = ''
for i in range(len(x)):    
    if i <= y:
      string += x[i].upper()
    else :
      string +=x[i].lower()         
print(string) 

#remove all duplicates from list
def Duplicate(str):
    x=set(str)
    x="".join(x)
    print(x)
    t=""
    for i in str:
        if(i in t):
            pass
        else:
            t=t+i
        print(t)
     
str="sheleadssheserves"
Duplicate(str)