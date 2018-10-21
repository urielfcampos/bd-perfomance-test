
import os
import random
import datetime
import csv
import threading
import time
import binary_algs as bn

random.seed(os.urandom(16))

pessoa = {"sexo": [0,1],
          "idade":[x for x in range(128)],
          "renda":[x for x in range(1024)],
          "escolaridade":[0,1,2,3],
          "idioma":[x for x in range(4096)],
          "pais":[x for x in range(256)],
          "localizador":[x for x in range(15)]}

def generate_data():
        with open("test.csv",'a',newline='') as file:
            datawriter = csv.writer(file, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for x in range(10**5):
                data = [pessoa["sexo"][random.randint(0, 1)], random.randint(0, 127),
                        random.randint(0, 1023),random.randint(0, 3),random.randint(0, 4095),
                        random.randint(0, 255),pessoa["localizador"][random.randint(0, 14)],
                        pessoa["localizador"][random.randint(0, 14)]]
                dataByteArray = bytearray(os.urandom(8))
                datawriter.writerow(data)
def generate_bin():
    with open("bdb.bin", "ab+") as f:
        for x in range(10**8):
            f.write(os.urandom(8))

print(datetime.datetime.now())
t1=threading.Thread(target=generate_bin)
t2=threading.Thread(target=generate_bin)
t3=threading.Thread(target=generate_bin)
t4=threading.Thread(target=generate_bin)
t5=threading.Thread(target=generate_bin)
t6=threading.Thread(target=generate_bin)
t7=threading.Thread(target=generate_bin)
t8=threading.Thread(target=generate_bin)
t9=threading.Thread(target=generate_bin)
t10=threading.Thread(target=generate_bin)

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
