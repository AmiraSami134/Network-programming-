import _thread                             # calling the thread module
import time                                   # for printing and giving delay in our functions
 # Define a function for the thread with the name (print_time) and define two arguments (the name of the thread and delay)
def print_time(threadName,delay):
 count = 0                                     # create a counter and initialize it with 0
 while count < 3:                          # make a loop and inside it provide a delay (sec) to be
  time.sleep(delay)                    # able to show the thread execution because the
  count += 1                               # execution is fast and it difficult to see it without delay
  print(threadName,"-----------",time.ctime())    #check the thread running
 # Create two threads and execute the function inside them as follow:
 # start_new_threadis a function inside a thread module
try:
  _thread.start_new_thread(print_time,("Thread 1",1))                # the first thread
  _thread.start_new_thread(print_time,("Thread 2",2))                # the second thread
except:
  print("this is an error")
while 1: 
  pass
