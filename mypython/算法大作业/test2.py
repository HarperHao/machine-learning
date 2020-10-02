import re
import math
import matplotlib.pyplot as plt
def get_data():
   x=input("请输入平面点集x1,y1 x2,y2...：")
   data=[]
   try:
       for i in re.split(",| ",x):
           data.append(float(i))
       result=[]
       for i in range(0,len(data)-1,2):
           p=(data[i],data[i+1])
           result.append(p)
       if len(result)<2:
           1/0
       else:
           result=sorted(result,key=lambda x:x[0])#将输入的点按横坐标排序
           return result
   except:
       print("输入不合法：横纵坐标间以英文逗号分隔，两点间以空格分隔，在冒号后直接输入至少两个点")
       return "error"
def distance2(x,y):
   #求解两点间距的平方
   result=pow(x[0]-y[0],2)+pow(x[1]-y[1],2)
   return result
def show(data,result,color):
   data_x=[]
   data_y=[]
   for item in data:
       data_x.append(item[0])
       data_y.append(item[1])
   plt.scatter(data_x,data_y,c='g')#画出所有的点
   plt.plot([result[1][0],result[2][0]],[result[1][1],result[2][1]],c=color)#画出最近对或正在检查的点对的连线
   d=round(math.sqrt(result[0]),3)
   plt.title("Distance:"+str(d))
   plt.grid()
   plt.show()
   plt.pause(1)
def solve(data,all_data):
   if len(data)<=3:#点的个数小于等于三时直接求解
       result=[]
       for i in range(len(data)-1):
           j=i+1
           while j<len(data):
               d=distance2(data[i],data[j])
               show(all_data,(d,data[i],data[j]),'y')#画出正在检查的点对的连线
               plt.clf()
               result.append((d,data[i],data[j]))
               j+=1
       result=min(result,key=lambda x:x[0])
       return result
   else:
       #点的个数大于三时，先等分点集，对两侧分别递归，而后合并结果
       mid=len(data)//2
       left=data[0:mid]
       right=data[mid:len(data)]
       d1=solve(left,all_data)
       d2=solve(right,all_data)
       d=min(d1,d2,key=lambda x:x[0])
       left2=[]
       right2=[]
       i=len(left)-1
       #先选出合并结果时要检查的点集
       tempd=math.sqrt(d[0])
       while i>=0:
           if left[i][0]>data[mid][0]-tempd:
               left2.append(left[i])
               i-=1
           else:
               break
       i=0
       while i<len(right):
           if right[i][0]<data[mid][0]+tempd:
               right2.append(right[i])
               i+=1
           else:
               break
       #而后检查两点集间是否存在距离更近的点对
       for p1 in left2:
           for p2 in right2:
               if p2[0]<p1[0]+tempd and p1[1]-tempd<p2[1]<p1[1]+tempd:
                   temp=distance2(p1,p2)
                   show(all_data,(temp,p1,p2),'y')#画出正在检查的点对的连线
                   plt.clf()
                   if temp<d[0]:
                       d=(temp,p1,p2)
       return d
while True:
   data=get_data()
   if data!="error":
       plt.close()
       result=solve(data,data)
       print(result[1],result[2])
       show(data,result,'g')#画出最近对的连线
       break