import sys
sys.setrecursionlimit(2000)
def determine_last_pos(child, parent):
    if parent == None:
        return None
    position = None
    for ind in range(0,3):
        if parent.value[ind] != child.value[ind]:
            position = ind
    return position       

def h(a,b):
    return (abs(int(a[0]) - int(b[0])) + abs(int(a[1]) - int(b[1])) + abs(int(a[2]) - int(b[2])))
    
class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.children =[]
        self.last_pos = None        
        self.last_pos = determine_last_pos(self, self.parent)
        self.heu = None
            
    def expand(self):       
        for i in range(0,3):
            if self.last_pos == i:
                continue
                
            if int(self.value[i]) == 0: 
                child = str(int(self.value)+10**(2-i)).zfill(3)                
                if child in forbidden:
                    continue                 
                self.children.append(Node(child, self))  
                for pos,elem in enumerate(non_cycle_list):                    
                    if self.children[-1].value == elem.value and elem.last_pos == self.children[-1].last_pos:                       
                        del self.children[-1]
                        break  

            elif int(self.value[i]) == 9:
                child = str(int(self.value)-10**(2-i)).zfill(3)
                if child in forbidden:
                    continue
                self.children.append(Node(child, self))
                for pos,elem in enumerate(non_cycle_list):                    
                    if self.children[-1].value == elem.value and elem.last_pos == self.children[-1].last_pos:                       
                        del self.children[-1]
                        break  

            else:
                child = str(int(self.value)-10**(2-i)).zfill(3)                                
                if child not in forbidden:                     
                    self.children.append(Node(child, self))
                    for pos,elem in enumerate(non_cycle_list):                    
                        if self.children[-1].value == elem.value and elem.last_pos == self.children[-1].last_pos:                       
                            del self.children[-1]
                            break 

                child = str(int(self.value)+10**(2-i)).zfill(3)
                if child in forbidden:
                    continue
                    
                self.children.append(Node(child, self))
                for pos,elem in enumerate(non_cycle_list):                    
                    if self.children[-1].value == elem.value and elem.last_pos == self.children[-1].last_pos and elem is not self.children[-1]:                       
                        del self.children[-1]
                        break
        if mode == 'B':
            for each in self.children:
                non_cycle_list.append(each)
                
    def expand_IDS(self, ugh_list):       
        for i in range(0,3):
            if self.last_pos == i:
                continue
                
            if int(self.value[i]) == 0: 
                child = str(int(self.value)+10**(2-i)).zfill(3)                
                if child in forbidden:
                    continue                 
                self.children.append(Node(child, self))  
                for pos,elem in enumerate(ugh_list):                    
                    if self.children[-1].value == elem.value and elem.last_pos == self.children[-1].last_pos:                       
                        del self.children[-1]
                        break  

            elif int(self.value[i]) == 9:
                child = str(int(self.value)-10**(2-i)).zfill(3)
                if child in forbidden:
                    continue
                self.children.append(Node(child, self))
                for pos,elem in enumerate(ugh_list):                    
                    if self.children[-1].value == elem.value and elem.last_pos == self.children[-1].last_pos:                       
                        del self.children[-1]
                        break  

            else:
                child = str(int(self.value)-10**(2-i)).zfill(3)                                
                if child not in forbidden:                     
                    self.children.append(Node(child, self))
                    for pos,elem in enumerate(ugh_list):                    
                        if self.children[-1].value == elem.value and elem.last_pos == self.children[-1].last_pos:                       
                            del self.children[-1]
                            break 

                child = str(int(self.value)+10**(2-i)).zfill(3)
                if child in forbidden:
                    continue
                    
                self.children.append(Node(child, self))
                for pos,elem in enumerate(ugh_list):                    
                    if self.children[-1].value == elem.value and elem.last_pos == self.children[-1].last_pos and elem is not self.children[-1]:                       
                        del self.children[-1]
                        break

        
def disp(arr):
    for ind,num in enumerate(arr):
        if ind < len(arr)-1:
            print(arr[ind].value,end=',')
        else:
            print(arr[ind].value)
        
def trace_path(node):
    sol_path.insert(0,node)
    if node.parent == None:
        return
    else:        
        trace_path(node.parent)
                
def BFS(visited, node, num_nodes_expanded):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0) 
        nodes_expanded.append(s)
        num_nodes_expanded += 1        
        if s.value == goal:
            trace_path(s)
            disp(sol_path)
            disp(nodes_expanded)
            return
        if num_nodes_expanded == 1000:
            print("No solution found.")
            disp(nodes_expanded[:1000])
            return
        s.expand()
        if s.children:
            for neighbour in s.children:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)                

def DFS(visited, node, num_nodes_expanded):
    if node not in visited:
        nodes_expanded.append(node)
        visited.append(node)
        num_nodes_expanded += 1
        if node.value == goal:
            trace_path(node)           
            disp(sol_path)
            disp(nodes_expanded)            
            exit()
        if num_nodes_expanded == 1000:
            print("No solution found.")            
            disp(nodes_expanded[:1000])
            exit()
        non_cycle_list.append(node)
        node.expand()
        for neighbour in node.children:
            DFS(visited, neighbour, num_nodes_expanded)

def IDS2(non_cycle_list,node,maxDepth, num_nodes_expanded): 
    num_nodes_expanded = num_nodes_expanded+1
    non_cycle_list.append(node)
    nodes_expanded.append(node)
    if node.value == goal:
        trace_path(node)           
        disp(sol_path)
        disp(nodes_expanded)   
        exit()
    if len(nodes_expanded) >= 1000:
        print("No solution found.")            
        disp(nodes_expanded[:1000])
        exit()
    node.expand_IDS(non_cycle_list)

    if maxDepth <= 0: 
        return 
    
    for neighbour in node.children: 
        flag = False
        for thisone in non_cycle_list:
            if thisone.value == neighbour.value and thisone.last_pos == neighbour.last_pos and thisone is not neighbour:
                flag = True
        if flag:
            continue
        IDS2(non_cycle_list,neighbour,maxDepth-1, num_nodes_expanded)     
    return 

def IDS1(): 
    num_nodes_expanded = 0
    for depth in range(10):
        new_node = Node(lines[0], None)
        visited = []
        non_cycle_list = []
        IDS2(non_cycle_list, new_node, depth, num_nodes_expanded) 

def take_heu(elem):
    return elem.heu

def greedy():        
    fringe = []
    expanded = []
    fringe.append(start)
    while fringe:
        s = fringe.pop(0)
        expanded.append(s)
        nodes_expanded.append(s)
        non_cycle_list.append(s)
        if s.value == goal:
            trace_path(s)           
            disp(sol_path)
            disp(nodes_expanded)   
            exit()
        if len(nodes_expanded) >= 1000:
            print("No solution found.")            
            disp(nodes_expanded[:1000])
            exit()
        s.expand()
        for each in s.children:
            each.heu = h(each.value,goal)
            fringe.insert(0,each)
        fringe.sort(key=take_heu)
            
filename = sys.argv[2]
file = open(filename,"r")
lines = file.read().split('\n')
file.close()
mode = sys.argv[1]
start = Node(lines[0], None) 
goal = lines[1]
if len(lines)>=3:
    forbidden = lines[2].split(',')
else:
    forbidden = []
non_cycle_list =[]
sol_path = []
nodes_expanded = []
num_nodes_expanded = 0
visited = []

if mode == 'B':     
    queue = []         
    BFS(visited, start, num_nodes_expanded)
    
elif mode == 'D':
    DFS(visited, start, num_nodes_expanded)
    
elif mode == 'I':
    IDS1()

elif mode == 'G':
    greedy()
###    
# x = Node('090', True)
# x.expand()
# k = 2  # parent's child
# for i in range(0,len(x.children)):
#     print(x.children[i].value)
# print("children's children:")
# x.children[k].expand() 

# for i in range(0,len(x.children[k].children)):
#     print(x.children[k].children[i].value)  
###    




