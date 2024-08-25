import matplotlib.pylab as plt
import numpy as np
import matplotlib.animation as animation
import pandas as pd
import time 
import collections
import serial
import threading


class arduino(object):#serial_port,baud_rate=baud_rate):
    
    def __init__(self,serial_port='/dev/cu.usbmodem14201',baud_rate=9600,vector_lenght=5000):
        
        self.serial_port   = serial_port
        self.baud_rate     = baud_rate
    
        self.vector_lenght = vector_lenght
        
        self.time = collections.deque([0]*vector_lenght, maxlen=vector_lenght)
        self.raw_data = collections.deque([np.NaN]*vector_lenght, maxlen=vector_lenght)

        self.arduinoData = serial.Serial(self.serial_port, self.baud_rate) 

        self.t_start = np.copy(time.time())

    def read_serial_monitor(self,arduinoData):
    
        arduinoString = arduinoData.readline()
        arduinoString = arduinoString.decode("utf-8")
        arduinoString = arduinoString.strip()

        self.char_list     = arduinoString.split('\t')  
        

        return float(arduinoString)
   
    def read(self):

        while True:
            t = time.time()-self.t_start
            x = self.read_serial_monitor(self.arduinoData)
            #print("{:>30}".format(x),end="")
            self.raw_data.append(x)
            self.time.append(t)


def mean_update(mean,x,n):
    mean = (mean*n+x)/(n+1)
    n = n+1
    return mean,n


def main():

    print('running..')

    start_time = time.time()

    my_arduino = arduino(vector_lenght=2500)
    #Loops the in_background function
    try:
        thread = threading.Thread(target = my_arduino.read)
        thread.start() 

    except KeyboardInterrupt:
        thread._Thread_stop() 
        #sys.exit()

    n = my_arduino.vector_lenght
        
    fig, ax3 = plt.subplots(1,1,figsize=[6.4,4.8])

    raw_data, = ax3.plot(np.array(my_arduino.raw_data)[-n:],np.arange(n))

    mean = np.mean(my_arduino.raw_data)
    std = np.std(my_arduino.raw_data)
    mean_bar, = ax3.plot([0,mean],[-20,-20],lw=5,marker='o')
    std_bar,  = ax3.plot([mean-2*std,mean+2*std],[-10,-10],lw=5,marker='o')

    #Text = ax3.text(0,0,my_arduino.Roll['Complementary'][-1])
    Text = ax3.set_title("{:.2f}\n{:.0f} s".format(my_arduino.raw_data[-1],start_time))

    #lim = [-np.pi*1.1,np.pi*1.1]
    #ax1.set_ylim(lim);ax2.set_ylim(lim);ax3.set_ylim(lim)

    ax3.set_xticks([-16,-5,0,5,16])
    #ax3.set_xlim([-np.deg2rad(20),np.deg2rad(20)])
    ax3.set_xlim([-20,20])
    ax3.grid(True)


    def animate(i,):
        
        vector = my_arduino.raw_data
        x = vector[-1]

        mean = np.mean(vector)
        std  = np.std(vector)

        time_from_start = time.time()-start_time
        #mean,n = mean_update(mean,x,n)
        

        raw_data.set_xdata(np.array(my_arduino.raw_data)[-n:])
        #raw_data.set_ydata(my_arduino.time)
        mean_bar.set_xdata([0,mean])
        
        std_bar.set_xdata([mean-2*std,mean+2*std])

        title = "{:.1f}".format(x)
        title += "\nmean: {:.1f} | 2std: {:.1f}".format(mean,2*std)
        title += "\n{:.0f} s".format(time_from_start)
        Text.set_text(title)

        return raw_data,mean_bar,std_bar,Text
        

    ani = animation.FuncAnimation(fig, animate, interval=200)
    plt.show()
    


if __name__ == "__main__":
    main()