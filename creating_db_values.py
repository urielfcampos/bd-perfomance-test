
import os
import random
import datetime
import csv
import threading
import time
import binary_algs as bn
import pickle
import numpy as np
random.seed(os.urandom(32))

pessoa = {"sexo": [0,1],
          "idade":[x for x in range(128)],
          "renda":[x for x in range(1024)],
          "escolaridade":[0,1,2,3],
          "idioma":[x for x in range(4096)],
          "pais":[x for x in range(256)],
          "localizador":[x for x in range(15)]}

def generate_data():
        with open("test.csv",'a',newline='') as file:
            datawriter = csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            dataBuffer =[]
            for x in range(10**8):
                data = [pessoa["sexo"][random.randint(0, 1)], random.randint(0, 127),
                        random.randint(0, 1023),random.randint(0, 3),random.randint(0, 4095),
                        random.randint(0, 255),pessoa["localizador"][random.randint(0, 14)],
                        pessoa["localizador"][random.randint(0, 14)]]
                datawriter.writerow(data)

def generate_bin():
    with open("bdb2.bin", "ab") as f:
           f.write(os.urandom(8*(10**5)))





print(datetime.datetime.now())
t1=threading.Thread(target=generate_data)
t2=threading.Thread(target=generate_data)
t3=threading.Thread(target=generate_data)
t4=threading.Thread(target=generate_data)
t5=threading.Thread(target=generate_data)
t6=threading.Thread(target=generate_data)
t7=threading.Thread(target=generate_data)
t8=threading.Thread(target=generate_data)
t9=threading.Thread(target=generate_data)
t10=threading.Thread(target=generate_data)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
while (t10.isAlive()):
    print("Still going at it")
    time.sleep(5)
print(datetime.datetime.now())
