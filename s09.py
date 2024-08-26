#problem1
def min_removals_to_equal_frequency(s:str)->int:
  
   a=(s.count("a"))
   b= (s.count("b"))
   c= (s.count("c"))
   d= (s.count("d"))

   if a<b and a<c and a<d:
     rb=(b-a)
     rc=(c-a)
     rd=(d-a)
     return (rb+rc+rd)
          

   if b<a and b<c and b<d:
     ra=(a-b)
     rc=(c-b)
     rd=(d-b)
     return (rb+rc+rd)
 
   if c<a and c<b and c<d:
     rb=(b-c)
     ra=(a-c)
     rd=(d-c)
     return (rb+ra+rd)

   if d<a and d<c and d<b:
     rb=(b-d)
     rc=(c-d)
     ra=(a-d)
     return (rb+rc+ra)

s=str(input("enter the word : "))
print(min_removals_to_equal_frequency(s))
    

#problem 2

def manage_scoreboard(rounds:list[tuple[int,int]])->dict:
    scoreboard={}
    for i in range():
      dict[rounds[i][0]]=dict.get(rounds[i][0]+rounds[i][1])



# #problem3
lst_name=[]
lst_num=[]
def add():
    lst_name.append(input("enter the new contant name:"))
    lst_num.append(input("Enter the new content number:"))
def remove():
    lst_name.remove(input("entre the name you want remove :"))
    lst_num.remove(input("entre the num you want to remove :"))
def search():
    tool = str(input("Enter your search here:"))
    for i in range(len(lst_name)):
        if lst_name[i]==tool:
            print(f"contact[{i}]:{lst_name[i]},{lst_num[i]}")
        else:
            continue
def veiw():
    for i in range(len(lst_name)):
            print(f"contact[{i}]:{lst_name[i]},{lst_num[i]}")
def update():
    name = str(input("Enter the name that you want to change:"))
    new = int(input("Enter the new number:"))
    for i in range(len(lst_name)):
        if lst_name[i]==name:
            lst_num[i]=new

y=0
while y==0:
    what = str(input("Enter what you want:"))
    if what=='add':
     add()
    elif what=='remove':
        remove()
    elif what=='search':
       search()
    elif what=='veiw':
       veiw()
    elif what=='update':
       update()
    else:
      print ("erorrr")











