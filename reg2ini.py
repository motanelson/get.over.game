print( "\033c\033[40;37m\give the file .txt reg key to show ? ")
a=input()
backs=""
#a="reg.txt"
f1=open(a,"r")
b=f1.read()
f1.close()
c=b.split("\n")
for counter in range(len(c)):
    cc=c[counter].strip().replace("="," =").replace("\\","/")
    c[counter]=cc
c.sort()
for counter in range(len(c)):
    c[counter]=c[counter].strip()
    if c[counter]!="":
        
        i=c[counter]
        if i[0]=="/" and len(c[counter])>1:
           c[counter]=i[1:]
        
        t=c[counter].split(" =")
        
        
        if len(t)==1:
            y=t[0].split("/")
            y[0]=y[0].strip()
            
            if backs!=y[0]:
                backs=y[0]
                print("["+backs+"]")
        else:
            y=t[0].split("/")
            y[0]=y[0].strip()
            
            if backs!=y[0]:
                backs=y[0]
                print("["+backs+"]")
                if len(y)>1 and len(t)>1:
                    print(y[0]+" = "+t[1])
            else:
                if len(y)>1 and len(t)>1:
                    print(y[0]+" = "+t[1])