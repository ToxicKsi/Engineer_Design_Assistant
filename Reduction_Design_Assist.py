#file:this software is an assistant for helping make eng.

import math
import numpy

#这是一个用来创建电机字典的类：
#Motors.para(n,'str()')
#n--->电机标号
#‘p’-->功率;‘n’-->转数;‘i’-->总传动比;‘s’-->电机型号;
class Motors():
    def __init__(self):
        pass
    def para(self,x,request):
        if(request=='s'):
                return(namedict[x])
        if(request=='p'):
                return(powerdict[x])
        if(request=='n'):
                return(npmdict[x])
        if(request=='i'):
                return(transmissiondict[x])
    def new(self,n,name,power,npm,transmission):
        namedict[n]=name
        powerdict[n]=power
        npmdict[n]=npm
        transmissiondict[n]=transmission
        name=""
        power=0
        npm=0
        transmission=0

class Sumtransmis():
    def __init__(self):
        pass
    def distribtwn():#减速齿轮两级减速之间的传动比分配
        pass
    def distribute(self,transmission,axis,change):
        #传动比的分配
        if(change==1):
                for cir in range(0,int(axis),1):
                        if(maxtransmisdict[drivetype[cir]]!=1):
                                powr[cir]=1
                print(powr)
                outsys=input("请输入非减速箱内配合的主动件轴号:")
                powr[int(outsys)]=0
                print(powr)
        #只进行一次即可
        for pr in range(0,int(axis),1):
                if(powr[pr]!=1):
                        transmission=transmission/(maxtransmisdict[drivetype[pr]]+mintransmisdict[drivetype[pr]])
        return transmission
        
def efctcl(x,maxormin):
        #delete max
        if(maxormin=='max'):
                return(maxdict[x])
        if(maxormin=='max'):
                return(mindict[x])   

def motorgroom():
        pw=0
        f=0
        v=0
        yelta=1
        i=0
        j=0
        drivetype=[0,0,0,0,0,0,0]
        f=input("输送带有效拉力:(N)")
        v=input("输送带工作速度:(m/s)")
        d=input("滚筒的工作直径:(mm)")
        
        pw=float(f)*float(v)*0.001
        bearingtype=input("轴承类型:( 1>球轴承 2>滚子轴承)")
        
        if(int(bearingtype)==1):
                bearing=0.99
        if(int(bearingtype)==2):
                bearing=0.98
        for i in range(0,int(axis)+1,1):
                if(i==int(axis)):
                        drivetype[i]=input("%s%s轴之间的传动形式为:"% (i, 'w'))
                else:
                        drivetype[i]=input("%s%s轴之间的传动形式为:"% (i, i+1))
                p=drivetype[i]
                effect[i]=efctcl(int(p),'max')
                if(i==0):
                        print("%s%s轴之间的传动效率为:%s" % (i, i+1,effect[i]))
                else:
                        print("%s%s轴之间的传动效率为:%s" % (i, i+1,effect[i]*bearing))
        for j in range(0,int(axis)+1,1):
                if(j==0):
                        yelta*=effect[j]
                else:
                        yelta*=effect[j]*bearing
        pr=float(pw)/float(yelta)
        print("该机构所需电动机的功率:%s kW"%(pr))
        npmneed=60000*float(v)/(pi*int(d))
        print("输送机滚筒的工作转速:%s rpm"%(npmneed))
        return(npmneed,drivetype,pr)

def plot(mot):
    lpower=[pw,pw*effect[0],pw*effect[0]*effect[1]*bearing,pw*effect[0]*effect[1]*bearing*effect[2]*bearing,pw*effect[0]*effect[1]*bearing*effect[2]*bearing*effect[3]*bearing,pw*effect[0]*effect[1]*bearing*effect[2]*bearing*effect[1]*bearing*effect[4]*bearing]
    lnpm=[npmdict[int(mot)],npmdict[int(mot)]/((maxtransmisdict[drivetype[0]]+mintransmisdict[drivetype[0]])/2),(npmdict[int(mot)]/((maxtransmisdict[drivetype[0]]+mintransmisdict[drivetype[0]])/2))/(math.sqrt(1.3*transmit[int(mot)])),((npmdict[int(mot)]/((maxtransmisdict[drivetype[0]]+mintransmisdict[drivetype[0]])/2))/(math.sqrt(1.3*transmit[int(mot)])))/(transmit[int(mot)]/(math.sqrt(1.3*transmit[int(mot)]))),(((npmdict[int(mot)]/((maxtransmisdict[drivetype[0]]+mintransmisdict[drivetype[0]])/2))/(math.sqrt(1.3*transmit[int(mot)])))/(transmit[int(mot)]/(math.sqrt(1.3*transmit[int(mot)]))))/((maxtransmisdict[drivetype[3]]+mintransmisdict[drivetype[3]])/2),((((npmdict[int(mot)]/((maxtransmisdict[drivetype[0]]+mintransmisdict[drivetype[0]])/2))/(math.sqrt(1.3*transmit[int(mot)])))/(transmit[int(mot)]/(math.sqrt(1.3*transmit[int(mot)]))))/((maxtransmisdict[drivetype[3]]+mintransmisdict[drivetype[3]])/2))/((maxtransmisdict[drivetype[4]]+mintransmisdict[drivetype[4]])/2)]
    print("=============================================================")
    print("          Report for the motor named: %s"%(namedict[int(mot)]))
    print("       |  电动机  |      两级圆柱齿轮减速器    |   V带传动 | 工作机")
    print(" axis  |   0轴   |   1轴  |   2轴  |   3轴  |   4轴  |     5轴")
    print(" speed |   %.0f  |  %.0f  | %.0f   | %.2f| %.2f |   %.2f"% (lnpm[0],lnpm[1],lnpm[2],lnpm[3],lnpm[4],lnpm[5]))
    print(" power |   %.2f  |  %.2f  |  %.2f |  %.2f |  %.2f  |   %.2f "% (pw, pw*effect[0],pw*effect[0]*effect[1]*bearing,pw*effect[0]*effect[1]*bearing*effect[2]*bearing,pw*effect[0]*effect[1]*bearing*effect[2]*bearing*effect[3]*bearing,pw*effect[0]*effect[1]*bearing*effect[2]*bearing*effect[1]*bearing*effect[4]*bearing                                                ))#    print("moment |  %.2f  | %.2f  | %.2f | %.2f| %.2f |  %.2f  "% (9550*lpower[0]/lnpm[0],9550*lpower[1]/lnpm[1],9550*lpower[2]/lnpm[2],9550*lpower[3]/lnpm[3],9550*lpower[4]/lnpm[4],9550*lpower[5]/lnpm[5]))#    print("-------------------------------------------------------------")
    print("moment |   %.2f |  %.2f | %.2f | %.2f|  %.2f  | %.2f"%(9550*lpower[0]/lnpm[0],9550*lpower[1]/lnpm[1],9550*lpower[2]/lnpm[2],9550*lpower[3]/lnpm[3],9550*lpower[4]/lnpm[4],9550*lpower[5]/lnpm[5]))
    print("connect|  联轴器 |  齿轮   |  齿轮  |  联轴器  |  齿轮")
    print("trasmis|  %.2f  |  %.2f  |  %.2f  |  %.2f  |  %.2f  "% ((maxtransmisdict[drivetype[0]]+mintransmisdict[drivetype[0]])/2,math.sqrt(1.3*transmit[int(mot)]),transmit[int(mot)]/(math.sqrt(1.3*transmit[int(mot)])),(maxtransmisdict[drivetype[3]]+mintransmisdict[drivetype[3]])/2,(maxtransmisdict[drivetype[4]]+mintransmisdict[drivetype[4]])/2))
    print("yelta  |  %.2f  |  %.2f  |  %.2f  |  %.2f  |  %.2f  "% (effect[0],effect[1]*bearing,effect[2]*bearing,effect[3]*bearing,effect[4]*bearing))
    print("=============================================================")
    lnpm=[0,0,0,0,0,0,0,0]

pi=3.14159265
pw=0
d=0
name=""
power=0
npm=0
npmneed=0
transmission=0
num=0
bearing=0.99
drivetype=[0,0,0,0,0,0,0]
powr=[0,0,0,0,0,0,0,0,0]
transmit=[0,0,0,0,0,0]
effect=[0,0,0,0,0,0,0]
namedict={}
powerdict={}
npmdict={}
transmissiondict={}
maxtransmisdict={'17':5,'18':5,'19':5,'10':6,'27':3,'28':3,'20':4,'30':4,'31':4,'81':1,'82':1,'83':1,'90':1}
mintransmisdict={'17':3,'18':3,'19':3,'10':4,'27':2,'28':2,'20':1.2,'30':2,'31':2,'81':1,'82':1,'83':1,'90':1}
maxdict={17:0.98,18:0.97,19:0.96,10:0.96,27:0.97,28:0.97,20:0.95,30:0.95,31:0.94,81:0.99,82:0.99,83:0.995,90:0.96}
mindict={17:0.98,18:0.97,19:0.96,10:0.94,27:0.97,28:0.94,20:0.92,30:0.95,31:0.94,81:0.97,82:0.99,83:0.99,90:0.96}
matransmisdict={17:5,18:5,19:5,10:6,27:3,28:3,20:4,30:4,31:4,81:1,82:1,83:1,90:1}
mitransmisdict={17:3,18:3,19:3,10:4,27:2,28:2,20:1.2,30:2,31:2,81:1,82:1,83:1,90:1}

motors=Motors()
trans=Sumtransmis()#定义‘trans’为一个总传动比

axis=input("减速机构中轴数目:")


(npmneed,drivetype,pw)=motorgroom()#电机需求功率计算&推荐功率&工作速度
num=input("根据该功率，您的备选电机的数目:")

for t in range(1,int(num)+1,1):
        name=input("该电机的名称:")
        power=int(input("该电机的功率:"))
        npm=int(input("该电机的转数:"))

        transmission=int(npm)/npmneed
        motors.new(t,name,power,npm,transmission)
        print("写入成功！")


for i in range(1,int(num)+1,1):

        s=motors.para(i,'s')
        p=motors.para(i,'p')
        n=motors.para(i,'n')
        ii=motors.para(i,'i')
        print(i,s,p,n,ii)

i=0
for i in range(1,int(num)+1,1):
        transmission=motors.para(i,'i')#每个电机的总传动比
        transmit[i]=trans.distribute(transmission,axis,i)#这个操作的目的式进行每个电机的总传动比分配

for hah in range(1,int(num)+1,1):
    plot(hah)
