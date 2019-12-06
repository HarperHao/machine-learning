# # 进程池创建进程
# # 进程池是用来创建成百上千的多个进程
#
# from multiprocessing import Pool
# import random, time
#
#
# def work(num):
#     print(random.random() * num)
#     time.sleep(3)
#
#
# if __name__ == "__main__":
#     po = Pool(4)  # 定义一个进程池，最大进程数为3，默认大小为CPU核数
#     for i in range(10):
#         po.apply_async(work,(i,))  # apply_async选择要调用，每次循环会用空出来的子进程去调用目标
#     po.close()  # 进程池关闭之后不再接收新的请求，但是之前已经接收的请求会执行完
#     po.join()  # 等待po中所有子进程结束，必须放在close后面

# # 进程间通信
# from multiprocessing import Queue, Process
# import time
#
#
# def write(q):
#     for value in ['a', 'b', 'c']:
#         print("开始写入：", value)
#         q.put(value)
#         time.sleep(1)
#
#
# def read1(q):
#     while True:
#         if not q.empty():
#             print("read1读取到的是:", q.get())
#             time.sleep(1)
#         else:
#             break
#
#
# def read2(q):
#     for x in range(3):
#         a = q.get()
#         print("read2读取到的是：", a)
#         q.put(a)
#         time.sleep(1)
#
#
# if __name__ == "__main__":
#     q = Queue(4)
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read1, args=(q,))
#     pr2=Process(target=read2,args=(q,))
#     pw.start()
#     pr2.start()
#     pr.start()
#     pw.join()
#     pr.join()
#     pr2.join()
#     print("接受完毕")


#进程池间的信息的通信
# from  multiprocessing import Pool,Manager
# import time
# def write(q):
#     for i in "welcome":
#         print("开始写入：",i)
#         q.put(i)
# def read(q):
#     time.sleep(3)
#     for i in range(q.qsize()):
#         print("得到消息：",q.get())
# if __name__=="__main__":
#     print("主进程启动")
#     q=Manager().Queue()
#     po=Pool()
#     po.apply_async(write,(q,))
#     po.apply_async(read,(q,))
#     po.close()
#     po.join()

#多线程(互斥锁)
# import threading
# num=0
# def test1():
#     global num
#     if mutex.acquire():
#         for i in range(100000):
#             num=num+1
#     print(num)
#     mutex.release()
# def test2():
#     global num
#     if mutex.acquire():
#         for i in range(100000):
#             num = num + 1
#     print(num)
#     mutex.release()
# if __name__=="__main__":
#     print(threading.current_thread().name)
#     mutex=threading.Lock()#一个锁对象
#     p1=threading.Thread(target=test1)
#     p1.start()
#     p2=threading.Thread(target=test2)
#     p2.start()
#     #p1.join()#主线程速度快于子线程
#     #p2.join()
#     print(num)
# from queue import Queue
# import threading
# import time
# class Pro(threading.Thread):
#     def run(self):
#         global qu
#         count=0
#         while True:
#             if qu.qsize()<100:
#                 for i in range(100):
#                     count+=1
#                     msg="生成产品"+str(count)
#                     qu.put(msg)
#                     print(msg)
#             time.sleep(1)
# class Con(threading.Thread):
#     def run(self):
#         global qu
#         while True:
#             if qu.qsize()>50:
#                 for i in range(3):
#                     msg=self.name+"消费了"+qu.get()
#                     print(msg)
#             time.sleep(1)
# if __name__=="__main__":
#     qu=Queue()
#     for i in range(60):
#         qu.put('初始产品'+str(i))
#     for i in range(2):
#         p=Pro()
#         p.start()
#     for i in range(5):
#         p=Con()
#         p.start()

#本地线程变量(ThreadLocal)
import threading
#创建全局ThreadingLocal对象
threadLocal=threading.local()

class Student:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return "<Student %s>"%self.name
def deal_student():
    #获取当前线程相关联的student
    std=threadLocal.student
    print("hello,",threading.current_thread().name)

def deal_thread(name):
    print("线程{0}执行任务，参数为{1}".format(threading.current_thread().name,name))
    #当前线程绑定student对象到ThreadLocal
    std=Student(name)
    threadLocal.student=std
    deal_student()

if __name__=="__main__":
    t1=threading.Thread(target=deal_thread,args=("KiKi",),name="Thread_KiKi")
    t2 = threading.Thread(target=deal_thread, args=("HaoHao",), name="Thread_HaoHao")
    t1.start()
    t2.start()