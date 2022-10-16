import sys

start = [8, 0, 6, 5, 2, 4, 7, 3, 1]  # 주어진 값
goal =  [1, 2, 3, 4, 5, 6, 7, 8, 0] # 찾는 값


def up(x):
    
    index = 0
    
    for i in range(len(x)):
        
        if x[i] == 0:
            
            index = i
    
    if index == 0 or index == 1 or index == 2:
        
        return x
    
    else:
        
        x[index] = x[index - 3]
        x[index - 3] = 0
        
        return x
    
def down(x):
    
    index = 0
    
    for i in range(len(x)):
        
        if x[i] == 0:
            
            index = i
            
    if index == 6 or index == 7 or index == 8:
    
        return x
    
    else:
        
        x[index] = x[index + 3]
        
        x[index + 3] = 0
        
        return x

def right(x):
    
    index = 0
    
    for i in range(len(x)):
        
        if x[i] == 0:
            
            index = i
            
    if index == 2 or index == 5 or index == 8:
        
        return x
    
    else:
        
        x[index] = x[index + 1]
        x[index + 1] = 0
        
        return x
    
def left(x):
    
    index = 0
    
    for i in range(len(x)):
        
        if x[i] == 0:
            
            index = i
            
    if index == 0 or index == 3 or index == 6:
        
        return x
    
    else:
        
        x[index] = x[index - 1]
        x[index - 1] = 0
        
        return x
    
def depth_first_search():
    
    print(" 깊이 우선 분석 ")
    
    open = [start]      # 시작 노드
    
    closed = []
    
    print("시작 노드 : ", open)
    
    count = 1
    
    while open != []:
        
        x = open[0]
        
        print("현재노드 : ", count, " : ")
        print("현재 open LIST ", open)
        
        print("-------------")
        
        print("|", X[0], "|", X[1], "|", X[2], "|")
        
        print("-------------")
        
        print("|", X[3], "|", X[4], "|", X[5], "|")
        
        print("-------------")
        
        print("|", X[6], "|", X[7], "|", X[8], "|")
        
        print("-------------\n")
        
        count = count + 1
        
        if x == goal:
            
            print("Success")
            
            return True
        
        else:
            
            # x의 자식 노드를 생성한다.
            
            child = []
            
            tmp = (tuple(x))
            
            child.append(down(list(tmp)))
            
            child.append(right(list(tmp)))  # 여백이 오른쪽으로 이동한 것
            
            child.append(up(list(tmp)))     # 여백이 중앙으로 이동한 것
            
            child.append(left(list(tmp)))   # 여백이 왼쪽으로 이동한 것
            
        closed.append(x)
        
        open.remove(x)
        
        for i in range(len(child)):
            
            if child[i] not in open and child[i] not in closed:
                
                open.insert(0, child[i])
                
    print("Fail")
    
    return False

depth_first_search()

        