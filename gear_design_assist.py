import math
#liner(version:1)函数适用于 X轴为自变量，并且具有一个比例参量控制的函数，cintemp输入要求0~1输入。
def liner(a,b,c,d,e,f,g,h,cominx,cintemp):
    kmax=(d-b)/(c-a)
    kmin=(h-f)/(g-e)
    maxout=(cominx-a)*kmax+b
    minout=(cominx-e)*kmin+f
    comout=maxout-cintemp*(maxout-minout)
    return comout

def discirbe(a,b,c,d,e,f,g,h,i,j,inputx):
    outputy=0
    if(inputx>=a and inputx<c):
        outputy=(inputx-a)*((d-b)/(c-a))+b
    if(inputx>=c and inputx<e):
        outputy=(inputx-c)*((f-d)/(e-c))+d
    if(inputx>=e and inputx<g):
        outputy=(inputx-e)*((h-f)/(g-e))+f
    if(inputx>=g and inputx<i):
        outputy=(inputx-g)*((j-h)/(i-g))+h
    return outputy

def getint(unint):
    unzero=unint-int(unint)
    if(unzero>=0.5):
        unint=int(unint)+1
    if(unzero<0.5):
        unint=int(unint)
    return unint

def choose(numb):
    numbzero=numb-int(numb)
    if(numb<=3 and numbzero>=0.5):
        numb=int(numb)+1
    if(numb<=3 and numbzero<0.5):
        numb=int(numb)+0.5
    if(numb>3):
        numb=int(numb)+1
    return numb
        
def geteven(numb):
    if(numb%2==1):
        numb=numb+1
    return numb

def zv(z):
    return (getint(z/(math.cos(math.pi*belt/180)**3)))

def Ybelt(belt,fyd,zls):
    ebelt=Eblet(fyd,zls,belt)
    ybelt=liner(10,1,20,1,10,0.92,20,0.835,belt,ebelt)
    #print(ybelt)#调试用
    return ybelt

def Ye(zls,zms):
    ealpha=Ealpha(zls,zms)
    return (0.25+0.75/ealpha)

def YFa(zv):
    return (discirbe(15,3.12,20,2.8,30,2.5,80,2.25,200,2.125,zv))

def YSa(zv):
    return (discirbe(17,1.56,23,1.58,30,1.645,100,1.8,200,1.88,zv))

def Eblet(fyd,zls,belt):
    ebelt=0.318*fyd*zls*math.tan(belt*math.pi/180)
    #print(ebelt)
    return (ebelt)

def Ealpha(zls,zms):
    alphals=math.acos((zls*math.cos(alpha))/(zls+2*haex))
    alphams=math.acos((zms*math.cos(alpha))/(zms+2*haex))
    ealpha=(0.5/math.pi)*(zls*(math.tan(alphals)-math.tan(alpha))+zms*(math.tan(alphams)-math.tan(alpha)))
    return ealpha

def Zms(zls,urt):
	zguess=zls*urt
	zzero=zguess-int(zguess)
	if(zzero>=0.5):
		zms=int(zguess)+1
	if(zzero<0.5):
		zms=int(zguess)
	return zms

def Kv():
    dls=m*zls
    vls=math.pi*nls*dls/60000
    return (discirbe(0,0,2,1.12,5,1.2,10,1.24,20,1.36,vls))

def Kbelt():
    dls=m*zls
    return ((discirbe(0.2,1.02,0.4,1.078,0.5,1.1,0.7,1.156,1.2,1.3,(bls-5)/dls))-0.1)

def Kalpha():
    esum=Eblet(fyd,zls,belt)+Ealpha(zls,zms)
    return (discirbe(1.9,1.4,2.0,1.42,2.2,1.47,2.5,1.5,4,1.56,esum))

def Kcount():
    kv=Kv()
    kbelt=Kbelt()
    kalpha=Kalpha()
    #print(kv,kbelt,kalpha)
    K=ka*kv*kbelt*kalpha
    return K

def Fya():
    urt=zms/zls
    fya=2*fyd/(1+urt)
    fya=getint(10*fya)
    fya=fya*0.1
    return fya

def Zh():
    return(discirbe(0,2.5,5,2.5,15,2.44,28,2.25,45,1.92,belt))

def Zcount():
    zh=Zh()
    ebelt=Eblet(fyd,zls,belt)
    ealpha=Ealpha(zls,zms)
    zeps=math.sqrt((4-ealpha)*(1-ebelt)/3+ebelt/ealpha)
    zbelt=math.sqrt(math.cos(belt/180*math.pi))
    z=zeps*zbelt*ze*zh
    return z

def mo(belt,fyd,zls,im):
    zms=Zms(zls,im)
    zvls=zv(zls)
    zvms=zv(zms)
    ye=Ye(zls,zms)
    ybelt=Ybelt(belt,fyd,zls)
    yFals=YFa(zvls)
    ySals=YSa(zvls)
    yFams=YFa(zvms)
    ySams=YSa(zvms)
    mox=((2000*K*Tmin*ye*ybelt*((math.cos(math.pi*belt/180))**2)*yFals*ySals)/(fyd*(zls**2)*cigadmitls))**(1/3)
    moy=((2000*K*Tmin*ye*ybelt*((math.cos(math.pi*belt/180))**2)*yFams*ySams)/(fyd*(zms**2)*cigadmitls))**(1/3)
    moguess=choose(max(mox,moy))
    return(moguess)

def design(belt,fyd,zls,zms,im):
    m=mo(belt,fyd,zls,im)
    a=geteven(getint(0.5*m*(zls+zms)/math.cos(math.pi*belt/180)))
    belt=math.acos((m*(zls+zms))/(2*a))*180/math.pi
    fya=Fya()
    bms=getint(a*fya)
    bls=bms+5
    return (a,m,belt,bms,bls)

def sig():
    K=Kcount()
    z=Zcount()
    urt=zms/zls
    sighls=z/a*math.sqrt((500*K*Tmin*(urt+1)**3)/(bls*urt))
    #sighms=z/a*math.sqrt((500*K*Tmin*(urt+1)**3)/(bms*urt))
    return (sighls)

def counter():
    K=Kcount()
    z=Zcount()
    if(sig()<1092):
        print("该齿面接触强度足够")
        print("a  :"+str(a)+"mm")
        print("m_n:"+str(m))
        print("z_1:"+str(zls))
        print("z_2:"+str(zms))
        print("b_1:"+str(bls)+"mm")
        print("b_2:"+str(bms)+"mm")
        print("d_1:%0.2fmm"%(m*zls/math.cos(belt*math.pi/180)))
        print("d_2:%0.2fmm"%(m*zms/math.cos(belt*math.pi/180)))
        print("belt:%0.6f(请自行换算为度分秒)"%(belt))
        print("精度等级：8级")
        print("齿轮材料：45钢，表面淬火")
        print("小齿轮：45~50HRC")
        print("大齿轮：40~50HRC")


#初始数据
im=4.04
zls=20
nls=970
ze=189.8
zms=Zms(zls,im)
Tmin=88.6
K=1.7
ka=1.25
fyd=0.7
belt=10
minblet=20
haex=1.0
alpha=20
cigadmitls=504
cigadmitms=456

#执行阶段
(a,m,belt,bms,bls)=design(belt,fyd,zls,zms,im)
print("模数初取值为:"+str(m))
K=Kcount()
(a,m,belt,bms,bls)=design(belt,fyd,zls,zms,im)
print("计算载荷系数：%0.2f"%(K))
print("模数初修正值为:"+str(m))

#校验阶段
counter()

