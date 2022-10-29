import math as m
#def jacob(a,b):
    #a=list(a)
b=[3,2,4]
mat=[[1,1,-1],[2,3,-1],[1,1,3]]
var=[]
var0=[]
var1=[]
td=10**-3
#l=int(m.sqrt(len(a)))
#r=0
for i in range(len(mat)):
    #mat.append(list())
    #var.append(0)                        #jacob([1,1,-1,2,3,-1,1,1,3],[3,2,4])
    var0.append(0)
    var1.append(0)
    #for j in range(r,l+r):
     #   mat[i].append(a[j])
    #r+=l
    
while(len(var)<len(mat)):

    for i in range(len(mat)):      
        for j in range(len(mat[i])):
            if j==i:
                continue
            else:
                var1[i]=var1[i]+(mat[i][j]*var0[j])
        var1[i]=(b[i]-var1[i])/mat[i][i]
        if(abs(var1[i]-var0[i])<td):
            var.append((var1[i]," " ,i))
    var0=var1.copy()
    for i in range(len(b)):
        var1[i]=0
    

print(var,mat,b)


#jacob([1,1,-1,2,3,-1,1,1,3],[3,2,4])
