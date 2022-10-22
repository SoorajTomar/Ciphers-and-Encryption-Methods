def p10(k):
    l=['0' for i in range(10)]
    a=list(k)
    #print(a)
    l[0]=a[2]
    l[1]=a[4]
    l[2]=a[1]
    l[3]=a[6]
    l[4]=a[3]
    l[5]=a[9]
    l[6]=a[0]
    l[7]=a[8]
    l[8]=a[7]
    l[9]=a[5]
    #print("After P10 we get:",*l)
    return l
def shift1(k):
    lh=k[:5]
    rh=k[5:]
    lh=lh[1:]+lh[:1]
    rh=rh[1:]+rh[:1]
    x=lh+rh
    #print("After Shift 1 we get:",*x)
    return x
def shift2(k):
    lh=k[:5]
    rh=k[5:]
    lh=lh[2:]+lh[:2]
    rh=rh[2:]+rh[:2]
    x=lh+rh
    #print("After Shift 2 we get:",*x)
    return x
def p8(k):
    l = ['0' for i in range(8)]
    a = list(k)
    #print(a)
    l[0] = a[5]
    l[1] = a[2]
    l[2] = a[6]
    l[3] = a[3]
    l[4] = a[7]
    l[5] = a[4]
    l[6] = a[9]
    l[7] = a[8]
    #print("After P8 we get:",*l)
    return l
def p4(a):
    l = ['0' for i in range(4)]
    l[0] = a[1]
    l[1] = a[3]
    l[2] = a[2]
    l[3] = a[0]
    return l
def ep(a):
    l=['0' for i in range(8)]
    l[0] = a[3]
    l[1] = a[0]
    l[2] = a[1]
    l[3] = a[2]
    l[4] = a[1]
    l[5] = a[2]
    l[6] = a[3]
    l[7] = a[0]
    #print("EP gives:",*l)
    return l
def s0(a):
    s=[[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
    r=''
    r=r+a[0]+a[3]
    c=''
    c=c+a[1]+a[2]
    r=int(r,2)
    c=int(c,2)
    x=s[r][c]
    #print("S0 gives:",x)
    return x
def s1(a):
    s=[[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]
    r = ''
    r = r + a[0] + a[3]
    c = ''
    c = c + a[1] + a[2]
    r = int(r, 2)
    c = int(c, 2)
    x = s[r][c]
    #print("S1 gives:", x)
    return x
def Fk(p,k):
    l=p[:4]
    r=p[4:]
    z=p[4:]
    r=ep(r)
    r1=''
    k1=''
    for i in r:
        r1+=i
    for i in k:
        k1+=i
    a=int(r1,2)
    b=int(k1,2)
    a^=b
    a=(bin(a).replace('0b',''))
    while len(a)!=8:
        a='0'+a
    #print(a)
    #print("XOR gives {} which is {}".format(a^b,bin(a^b).replace("0b",'')))
    a=list(a)
    la=a[:4]
    ra=a[4:]
    la=s0(la)
    ra=s1(ra)
    d={0:'00',1:'01',2:'10',3:'11'}
    la=d[la]
    ra=d[ra]
    a=la+ra
    a=list(a)
    a=p4(a)
    r1=''
    l1=''
    for i in a:
        r1+=i
    r1=int(r1,2)
    for i in l:
        l1+=i
    l1=int(l1,2)
    a=r1^l1
    a=bin(a).replace('0b','')
    while len(a)!=4:
        a='0'+a
    a=list(a)
    #print("a here is ",*a)
    ans=z+a
    #print("After Fk we get:",*ans)
    return ans
def ip(p):
    a=list(p)
    l=['0' for i in range(8)]
    l[0] = a[1]
    l[1] = a[5]
    l[2] = a[2]
    l[3] = a[0]
    l[4] = a[3]
    l[5] = a[7]
    l[6] = a[4]
    l[7] = a[6]
    return l
def ipinv(p):
    a=list(p)
    l=['0' for i in range(8)]
    l[0] = a[3]
    l[1] = a[0]
    l[2] = a[2]
    l[3] = a[4]
    l[4] = a[6]
    l[5] = a[1]
    l[6] = a[7]
    l[7] = a[5]
    return l
ct=input("Enter Cipher Text: ")
k=input("Enter Key: ")
k=p10(k)
k=shift1(k)
#print("Here:",*k)
k1=p8(k)
print("Key 1 is:",*k1)
k=shift2(k)
k2=p8(k)
print("Key 2 is:",*k2)
ct=ip(ct)
fk1ans=Fk(ct,k2)
fk2ans=Fk(fk1ans,k1)
ct=fk2ans[4:]+fk2ans[:4]
pt=ipinv(ct)
print("Plain Text is:",*pt)