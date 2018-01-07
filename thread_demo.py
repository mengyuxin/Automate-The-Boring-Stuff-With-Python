#! python3
# thread_demo.py

import threading, time

def takeANap():
    time.sleep(5)
    print('wake up!')

thread_obj = threading.Thread(target=takeANap)
thread_obj.start()

print('End of Program.')
