mas=[[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
[0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
[0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
[0, 1, 0, 0, 1, 0, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0]]

def found(ls):
    n=[]
    one=[]
    army=[]
    a=0
    for x in range(10):
        for y in range(10):
            
            if ls[x][y]==1:
                d=(diag(x,y))
                if d==1:
                    army.append([[],[],[],[]])
                else:
                    n.append([x,y])
                    a+=1
                    
            elif ls[x][y]==0:
                if a>=2:
                    army.append(n)
                    n=[]
                    a=0
                elif a==1:
                    one.append(n)
                    n=[]
                    a=0
            if y==9:
                if a>=2:
                    army.append(n)
                    n=[]
                    a=0
                elif a==1:
                    one.append(n)
                    n=[]
                    a=0
    for x in range(10):
        for y in range(10):
            
            if ls[y][x]==1:
                n.append([y,x])
                a+=1
                
            elif ls[y][x]==0:
                if a>=2:
                    army.append(n)
                    n=[]
                    a=0
                elif a==1:
                    one.append(n)
                    n=[]
                    a=0
            if y==9:
                if a>=2:
                    army.append(n)
                    n=[]
                    a=0
                elif a==1:
                    one.append(n)
                    n=[]
                    a=0
    res=one
    one=[]
    for x in res:
        if res.count(x)>1 and one.count(x)==0 :
            one.append(x)
    army+=one
    print(len (army))
    return army

def diag(x,y):
    global mas
    if x-1>=0 and y-1>=0:
        a=mas[x-1][y-1]
    else:
        a=0
    if x-1>=0 and y+1<=9:
        b=mas[x-1][y+1]
    else:
        b=0
    if x+1<=9 and y-1>=0:
        c=mas[x+1][y-1]
    else:
        c=0
    if x+1<=9 and y+1<=9:
        d=mas[x+1][y+1]
    else:
        d=0
    
    print(f'{a},{b},{c},{d}', end=' -->  ')
    r=a+b+c+d
    print(r)
    return r

def cont(arm):
    a,b,c,d=0,0,0,0
    for x in arm:
        
        m=len(x)
        if m==4: a+=1
        if m==3: b+=1
        if m==2: c+=1
        if m==1: d+=1
    
    return a==1 and b==2 and c==3 and d==4
print(cont(found(mas)))
