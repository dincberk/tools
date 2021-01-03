import speedtest
import pandas as pd
import sys
import numpy as np
import threading 
import time

st=speedtest.Speedtest()

def speed():
    while True:
        time.sleep(1000)
        d=st.download()/1000000
        u=st.upload()/1000000
        print(d)
        print(u)
        print('------------------')
    else:
        print('NO CONNECTION!')
speed()

