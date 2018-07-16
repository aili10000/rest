# class Hotel(object):
#     """docstring for Hotel"""
#
#     def __init__(self, room, cf=1.0, br=15):
#         self.room = room
#         self.cf = cf
#         self.br = br
#
#     def cacl_all(self,):
#         return '111'
#
#
# if __name__ == '__main__':
#     Hotel.cacl_all()


# import threading
import time
from concurrent.futures import ThreadPoolExecutor


def work(name):
    print("当前线程是,name是%s" % (name))
    name = name*2
    time.sleep(2)
    print("当前线程是,结果是%s" % ( name))

# def work(name):
#     print("当前线程是%s,name是%s" % (threading.current_thread(),name))
#     name = name*2
#     time.sleep(2)
#     print("当前线程是%s,结果是%s" % (threading.current_thread(), name))


# print('thread %s is running...' % threading.current_thread())
# for i in range(1,5):
#     t = threading.Thread(target=work,args=(i,))
#     t.start()
#
# print('ok')
# t.join()
#
# print("=====================")
#
#
# t1 = threading.Thread(target=work,args=(11,))
# t2 = threading.Thread(target=work,args=(22,))
# t3 = threading.Thread(target=work,args=(22,))
# t1.start()
# t2.start()
# t3.start()
# t1.join()
# t2.join()
# t3.join()

print("++++++++++++++++++++++++")
th = ThreadPoolExecutor(max_workers=3)
for s in range(1,10):
    th.submit(work,s)
th.shutdown()
print('````````````````````````````')