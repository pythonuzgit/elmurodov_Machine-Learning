# Intersection of lines
 

for row in range(9):
    for col in range(9):

      
        if (row - col ==0): 
            print("0", end= " ")
        elif (row + col ==8): 
             print("0", end= " ")
        elif (row ==4 and col%1 ==0): #or (row==1 and col%4==0):
            print("0", end= " ")  
        elif (row%1 == 0 and col ==4): 
            print("0", end= " ")     
        else:
            print(end= "  ")

    print()         
