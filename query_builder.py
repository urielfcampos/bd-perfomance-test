import binary_algs as bn
import os
import threading
import time
size = os.stat("bdb.bin").st_size

class ThreadControl:
    numberThreads:int
    threadArray =[]
    results = []
    def thread_init(self,numberOfThreads,functionName,functionArgs):
        self.numberThreads = numberOfThreads
        for x in range(numberOfThreads):
            t = threading.Thread(target=functionName,kwargs={'file':functionArgs[0],'offset':functionArgs[1][x]})
            self.threadArray.append(t)
    def start_threads(self):
        '''
        Function to start all thread objects in the thread_array variable=
        :return:
        '''
        for x in range(len(self.threadArray)):
            print("starting thread",x)
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
        '''
        Function to read the binary file and save the result in a global class variable
        :param file: a file name
        :param offset: the range of values to read from the file
        :return:
        '''
        temp = 0
        temp_value=()
        print(threading.currentThread(),offset)
        offsetValue = offset[0]
        for x in range(offset[1]):
            temp_value = bn.r_file(file,offsetValue)
            temp = temp_value[1]
            offsetValue = temp
            self.results.append([temp_value,threading.currentThread()])


def create_file_ranges(file,numberThreads):
    range_list = []
    temp_range_init = 0
    temp_range_final= size//numberThreads
    while temp_range_final < size:
        range_list.append([temp_range_init,temp_range_final])
        temp = temp_range_final
        temp_range_final += temp_range_final
        temp_range_init = temp
    range_list.append([temp_range_init,size])
    return range_list

def main():
    FirstControl = ThreadControl()
    range_file = create_file_ranges("bdb.bin",8)
    print(range_file)
    FirstControl.thread_init(4,FirstControl.bReadline,["bdb.bin",range_file])
    FirstControl.start_threads()
    for process in FirstControl.threadArray:
        process.join()
    with open("test.txt","a") as f:
        for x in FirstControl.results:
            f.write(str(x))

main()