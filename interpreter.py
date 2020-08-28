import os
import glob 
from queue import deque
def inter(event_name):
    files = os.curdir + "/events/" + event_name
    print(files)
    with open(files,"r") as event:
        for f in event:
            word = ""
            for char in f:
                if char == " ":
                    word = ""
                    continue

                 

inter("caribbean_dynamism.txt")
                
