
#math  function  
def mat(a,op,b):
    if op=='+': return str(float(a)+float(b))
    if op=='-': return str(float(a)-float(b))
    if op=='/': return str(float(a)/float(b))
    if op=='*': return str(float(a)*float(b))
#then we calculate function
def calc(pr2):
    res=pr2
    while '/' in res or '*' in res:
        for x in res:
            if x=='*'or x=='/': 
                r=res.index(x)
                c=mat(res[r-1],res[r],res[r+1])
                res=res[:r-1]+res[r+2:]
                res.insert(r-1,c)
    pr2=res
    while len(res)>=3:
        x=mat(res[0],res[1],res[2])
        res=res[3:]  
        res.insert(0,x) 
    return res[0]
# we looking for objects in string
def  fin(pr):
    pr='( '+pr+' )'
    pr2=pr.split()
    while len(pr2)>=3:
        f=-1
        l=0
        for x in range(len(pr2)):
            if pr2[x]=='(':
                f=x
            elif pr2[x]==')':
                l=x
                break
        c=str(calc(pr2[f+1:l]))
        pr2=pr2[:f]+[c]+pr2[l+1:]
    return (float(pr2[0]))
       
prik='22 / 33 / 44 - 55 * 66'
print('22 / 33 / 44 - 55 * 66=-3629.98484848=={}'.format(fin(prik)))
prik='( 2 / 3 ) * 4'
print('( 2 / 3 ) * 4=={}'.format(fin(prik)))
prik='2 + 2'
print('2+2=4=={}'.format(fin(prik)))