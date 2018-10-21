import binary_algs as bn
import os
import threading
import time
import queries as qr
import datetime
size = os.stat("bdb2.bin").st_size


class ThreadControl:
    numberThreads:int
    threadArray =[]
    results = []
    def thread_init(self,numberOfThreads,functionName,functionArgs):
        self.numberThreads = numberOfThreads
        start_range =0
        for x in range(numberOfThreads):
            t = threading.Thread(target=functionName,kwargs={'file':functionArgs[0],'offset':(start_range,functionArgs[1][x])})
            start_range = functionArgs[1][x]
            self.threadArray.append(t)
    def start_threads(self):
        '''
        Function to start all thread objects in the thread_array variable=
        :return:
        '''
        for x in range(len(self.threadArray)):
            #print("starting thread",x)
            self.threadArray[x].start()
    def check_threads(self):
        '''
        Function to check active threads
        :return:
        '''
        while threading.active_count() >1:
            print("Still alive)")
            print("Thread no",threading.active_count())
            time.sleep(15)
    def bReadline(self,file,offset):
        import pickle
        '''
        Function to read the binary file and save the result in a global class variable
        :param file: a file name
        :param offset: the range of values to read from the file
        :return:
        '''
        bn.r_file(offset[0],offset[1],file)
        threadName = threading.currentThread().getName()
        print("Starting query1", threadName)
        with open(f'tmp_cda{threadName}',"r")as f:
            data=f.read()
        print(bn.cdataline(data))
        print(qr.querie_1(data,"tmp.bin"),threadName)


def create_file_ranges(numberThreads):
    rangeList = []
    totalBlocks = size // 8
    blocksPerThread = totalBlocks//numberThreads
    finalValue = blocksPerThread*8
    for x in range(numberThreads):
        rangeList.append(finalValue)
        finalValue+= 8 * blocksPerThread

    return rangeList

def main():
    FirstControl = ThreadControl()
    range_file = create_file_ranges(10)
    #print(range_file)
    FirstControl.thread_init(10,FirstControl.bReadline,["bdb2.bin",range_file])
    FirstControl.start_threads()
    for process in FirstControl.threadArray:
        process.join()
print(datetime.datetime.now())
main()
print(datetime.datetime.now())
