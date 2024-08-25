from tkinter import*
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
from datetime import datetime
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk) 
import matplotlib.pylab as plt
import numpy as np



acquisition = False
foot = "Right"

def update_title():
    global cursor
    global acquisition
    global foot

    #global ax
    #ax.plot(np.random.random(10))
    #plot_frame.update()

    now = datetime.now()

    now_string = now.strftime("%Y-%m-%d %H:%M:%S")
    if acquisition :
        acquisition_string = "Running"
    else:
        acquisition_string = "Stopped"

    title = "{:}\nAcquisition: {:}\nFoot: {:}".format(now_string,acquisition_string,foot)

    txt_title.config(text = title)

# Function to handle the connection using the entered credentials
def start_stop_acquisition():
    global cursor
    global acquisition
    global foot

    if acquisition :
        acquisition = False
    else:
        acquisition = True

    update_title()

    return  acquisition

# Function to handle the connection using the entered credentials
def change_foot():
    global cursor
    global acquisition
    global foot

    if foot == 'Right':
        foot = 'Left'
    else:
        foot = 'Right'

    update_title()

def look_results():

    print('results to be added')

def on_closing():
    if tkMessageBox.askokcancel("Confirm Exit", "Are you sure you want to exit?"):
        # Close the database connection
    
        # Destroy the window (closing the application)
        window.destroy()


# Create the main window
window = Tk()
window.title("Balance Board")
screen_width=window.winfo_screenwidth()
screen_height=window.winfo_screenheight()
width=2000
height=1000
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
window.geometry('%dx%d+%d+%d' % (width, height, x, y))
#pipwindow.resizable(0, 0)


# Create top frame for title (anchored to NW)
top_frame = Frame(window)
top_frame.pack(side="top", fill="both")

txt_title = Label(top_frame, width=200, font=('arial', 24), text="Push the button to start the acquisition.",background="blue")
txt_title.pack(side="left", anchor="nw")

#plot_frame = Frame(window,background="red")

#fig,ax = plt.subplots()
#ax.plot()
# creating the Tkinter canvas 
# containing the Matplotlib figure 
#canvas = FigureCanvasTkAgg(fig, 
  #                          master = plot_frame)   
#canvas.draw() 



# placing the canvas on the Tkinter window 
#canvas.get_tk_widget().pack(padx=100,pady=100) 
#plot_frame.pack(fill='y')# fill="both", expand=True)# padx = 100, pady = 100

# Create left frame for user input fields (anchored to NW)
bottom_frame = Frame(window,background="green")
bottom_frame.pack(side="bottom", fill="both", expand=True)

# Create buttons frame within bottom_frame (anchored to NW)
buttons_frame = Frame(bottom_frame,background='orange')
buttons_frame.pack(side="bottom", fill="both")

start_stop_button = Button(buttons_frame, text="Start/Stop", command=start_stop_acquisition)
start_stop_button.pack(side="bottom")

change_foot_button = Button(buttons_frame, text="Change Foot", command=change_foot)
change_foot_button.pack(side="top")

window.protocol("WM_DELETE_WINDOW", on_closing)

fig,ax = plt.subplots()
ax.plot([12,3],[5,6])
plt.show()


window.mainloop()



#return user_id,password

