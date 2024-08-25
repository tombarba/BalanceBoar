from tkinter import*
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

def ask():

    # Function to handle the connection using the entered credentials
    def do_something():
        global cursor,user_id,password

        user_id = user_entry.get()
        password = password_entry.get()

        window.destroy()


    def on_closing():
        if tkMessageBox.askokcancel("Confirm Exit", "Are you sure you want to exit?"):
            # Close the database connection
        
            # Destroy the window (closing the application)
            window.destroy()


    # Create the main window
    window = Tk()
    window.title("Inserisci nome e password")
    screen_width=window.winfo_screenwidth()
    screen_height=window.winfo_screenheight()
    width=200
    height=200
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))
    #pipwindow.resizable(0, 0)


    # Create top frame for title (anchored to NW)
    top_frame = Frame(window)
    top_frame.pack(side="top", fill="x")

    txt_title = Label(top_frame, width=200, font=('arial', 12), text="")
    txt_title.pack(side="left", anchor="nw")

    # Create left frame for user input fields (anchored to NW)
    left_frame = Frame(window)
    left_frame.pack(side="left", fill="both", expand=True)

    # Create forms frame within left frame (anchored to NW and fill)
    forms_frame = Frame(left_frame)
    forms_frame.pack(side="top", fill="both", expand=True)


    user_label = Label(forms_frame, text="User ID:")
    user_label.grid(row=2, column=0, sticky="e")
    user_entry = Entry(forms_frame)
    user_entry.grid(row=2, column=1)

    password_label = Label(forms_frame, text="Password:")
    password_label.grid(row=3, column=0, sticky="e")
    password_entry = Entry(forms_frame, show="*")  # Hide password input
    password_entry.grid(row=3, column=1)

    # Create buttons frame within left frame (anchored to NW)
    buttons_frame = Frame(left_frame)
    buttons_frame.pack(side="bottom", fill="x")

    txt_result = Label(buttons_frame)
    txt_result.pack(side="top")

    connect_button = Button(buttons_frame, text="Enter", command=do_something)
    connect_button.pack(side="left")

    window.protocol("WM_DELETE_WINDOW", on_closing)

    window.mainloop()

    return user_id,password

ask()