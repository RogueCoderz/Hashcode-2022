import linecache

input_filename = input("enter input file : ")
output_filename= input("enter output file : ")

output_filename = f"../output_data/{output_filename}.out.txt"


pl = int(linecache.getline(input_filename, 1))
with open(input_filename,'r') as f:  
  list_indi = [[0 for a in range(2)] for b in range(pl)] 
  def find_ingerdiants(list_indi):
    a=0
    for i in f:      
      a+=1
      if len(i)>2:
        k = i.split()
        if (a%2==0):
          k.pop(0)          
          list_indi[(a//2)-1][0]=k          
        else:
          k.pop(0)  
          list_indi[(a//2)-1][1]=k          
           
  find_ingerdiants(list_indi)

input_file = open(output_filename,"r")
lst = input_file.read().split()
lst.pop(0)

customer=0
for i in range(0,pl):
  a=0
  
  if list_indi[i][1] != 0:

    for j in range(0,len(list_indi[i][1])):
      if list_indi[i][1][j] in lst:
        a+=1
    if a>0:
      continue  
  if (set(list_indi[i][0]).issubset(set(lst))):
    customer+=1
    
print(customer)