import math
import data as dataReader
import datetime
from anytree import Node, RenderTree

path = './data/ta20_5_1.txt'
matrix = dataReader.read(path, 3)
job_count =3
nb_machines = len(matrix[0])
SUP =9999
Solution = ""
f = open ( './data/ta20_5_1.txt' , 'r')
l = [] 
matrix=[]
l = [ line.split() for line in f]
instance =0
for i in range(instance,instance+5):
    matrix.append(l[i]) 

def generate_tree(nmbr_of_jobs):
    U=""
    for i in range(nmbr_of_jobs):
        U=U+'-'+str(i)
    root= Node("",inf=-1)
    U = U.split("-")
    U.remove(U[0])
    for i in range(len(U)):
        child = Node(root.name+U[i],parent=root,inf=-1)
        J=[]
        for j in range(len(U)):
            J.append(U[j])
        J.remove(J[i])
        generate_Node(J,child)
    return root
def generate_Node(U,parent):
    for i in range(len(U)):
        child = Node(parent.name+U[i],parent=parent,inf=-1)
        J=[]
        for j in range(len(U)):
            J.append(U[j])
        J.remove(J[i])
        generate_Node(J,child)
def generate_alpha(node,nombre_machine): 
    αβγ=[0]*nombre_machine
    if(node.name==""):
        return αβγ
    else:
        for char in node.name:
            αβγ[0]=αβγ[0]+int(matrix[0][int(char)])
            for i in range(1,len(αβγ)):
                αβγ[i]=max(αβγ[i-1],αβγ[i])+int(matrix[i][int(char)])
        return αβγ
def evaluate_node(node,param,matrix,nombre_machine,nmbr_of_jobs):
    global SUP 
    global Solution
    min_i= [9999] * nombre_machine
    sum_i= [0] * nombre_machine
    for j in range(nombre_machine):
        min_it =[]
        for i in range(nmbr_of_jobs):
            if  (node.name.find(str(i)) == -1):
                sum_i[j] = sum_i[j] + int(matrix[j][int(i)])
                min_sum= 0
                for k in range(j+1,nombre_machine):
                    min_sum = min_sum + int(matrix[k][int(i)])
                min_it.append(min_sum)
        if(node.is_leaf):
            min_i[j] = 0
        else:
            min_i[j]=min(min_it)
        
    if(node.is_root):
        node.inf=-1
        if(node.is_leaf):
            if (node.inf<SUP):
                SUP = node.inf
                Solution = node.name
        #elif(node.inf<SUP):
        αβγ= generate_alpha(node,nombre_machine)
        for child in node.children:
            evaluate_node(child,αβγ,matrix,nombre_machine,nmbr_of_jobs)
    else:
        αβγ= generate_alpha(node,nombre_machine)
        list_to_maximize =[]
        for l in range(nombre_machine):
            list_to_maximize.append(αβγ[l]+sum_i[l]+min_i[l])
        node.inf = max(list_to_maximize)
        if(node.is_leaf):
            if (node.inf<SUP):
                SUP = node.inf
                Solution = node.name
        if(node.inf<SUP):
            for child in node.children:
                evaluate_node(child,param,matrix,nombre_machine,nmbr_of_jobs)
    return Solution

def Branch_and_bound():
    new_sol  = []
    root = generate_tree(8) #number of jobs as param 
    solution = evaluate_node(root,[0]*5,matrix,5,8) # 5 number of machines  // 3 number of jobs 
    for i in range(len(solution)):
        new_sol.append(int(solution[i]))
    return new_sol
    
if __name__ == "__main__":
    print(Branch_and_bound())
    