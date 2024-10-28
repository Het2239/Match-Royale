from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import Toplevel, Frame, Label, messagebox, Scrollbar, VERTICAL, HORIZONTAL, BOTH, RIGHT, Y, X
import file_handle
import os
import csv

root = Tk()
root.title("Match Royale")  # Title of the screen
ico = Image.open('images//Naruto.jpg')  # ICON IMAGE
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)
root.geometry('500x500')  # ceometry of home screen
image = Image.open("images/match royale promo.jpg")
background_image = ImageTk.PhotoImage(image)  # home screen background image

# function called on pressing play button
def clk_play():
    player_name = name_input.get()
    if player_name.strip() == "":    # strip would remove any blankspaces before the first characher and after the last character.
        messagebox.showwarning("Input Error", "Please enter a player name.")  # error messagebox shown when name is not entered
    else:
        root.destroy()
        from my_game_logic import GameLogic
        
        timetaken=GameLogic.gametime() # stores the elapsed time
        moves=GameLogic.mmoves()  # stores the no. of moves
        file_handle.scoreUpdate(player_name.strip(), moves//2 , timetaken,len(file_handle.scoreDataonNo())+1)  # command for making an entry in the csv file
        


def view_history():
    try:
        # Check if the CSV file exists
        if os.path.exists("score.csv"):
            with open("score.csv", newline='') as file:
                reader = csv.reader(file)
                history = list(reader)

            if len(history) > 1:  # Ensure there's data beyond the header
                history_window = Toplevel(root)
                history_window.title("Game History")
                history_window.geometry("820x500")
                history_window.iconbitmap("images\\Naruto.ico")

                # Create a frame for the table
                table_frame = Frame(history_window)
                table_frame.pack(padx=10, pady=10, fill=BOTH, expand=True)

                # Create a canvas for adding a scrollbar
                canvas = Canvas(table_frame)
                canvas.pack(side=LEFT, fill=BOTH, expand=True)

                # Add a vertical scrollbar to the canvas
                v_scrollbar = Scrollbar(table_frame, orient=VERTICAL, command=canvas.yview)
                v_scrollbar.pack(side=RIGHT, fill=Y)

                # Add a horizontal scrollbar if needed
                h_scrollbar = Scrollbar(table_frame, orient=HORIZONTAL, command=canvas.xview)
                h_scrollbar.pack(side=BOTTOM, fill=X)

                # Configure the canvas to use the scrollbars
                canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
                canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

                # Create another frame inside the canvas to hold the table content
                content_frame = Frame(canvas)
                canvas.create_window((0, 0), window=content_frame, anchor="nw")

                # Add table headers
                headers = ["Name", "Moves", "Time","Game No."]
                for col, header in enumerate(headers):
                    header_label = Label(content_frame, text=header,padx=60, pady=5, font=("Helvetica", 12, "bold"), borderwidth=1, relief="solid")
                    header_label.grid(row=0, column=col, padx=5, pady=5, sticky="nsew")

                # Populate table rows with data
                for row_num, row in enumerate(history[1:], start=1):
                    if len(row) == 4:
                        for col_num, value in enumerate(row):
                            cell_label = Label(content_frame, text=value, font=("Helvetica", 12), borderwidth=1, relief="solid")
                            cell_label.grid(row=row_num, column=col_num, padx=5, pady=5, sticky="nsew")

                # Configure column and row weights for equal spacing
                for col_num in range(len(headers)):
                    content_frame.grid_columnconfigure(col_num, weight=1)
                for row_num in range(1, len(history)):
                    content_frame.grid_rowconfigure(row_num, weight=1)

            else:
                messagebox.showinfo("History", "No game history found.")
        else:
            messagebox.showinfo("History", "No game history found.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

frame1 = Frame(root, border=5)
background_label = Label(frame1, image=background_image)
background_label.place(relwidth=1, relheight=1)
frame1.pack(expand=True, fill="both")

frame2 = Frame(frame1, border=2, bg="lightblue")
frame2.pack(expand=True)

# Function to automatically convert entry text to uppercase
def convert_to_uppercase(*args):
    entry_text.set(entry_text.get().upper())
def credit():
    
    credits=Toplevel(root)
    credits.title('Credits')
    icox = Image.open('images//Naruto.jpg')  # ICON IMAGE
    photox = ImageTk.PhotoImage(icox)
    credits.wm_iconphoto(False, photox)
    name=Label(credits,text='Name',borderwidth=1,padx=60, pady=5, font=("Helvetica", 12))
    name1=Label(credits,text='Het Chavadia',border=1,padx=60, pady=5, font=("Helvetica", 12))
    name2=Label(credits,text='Puchakayala Jaya Raghunandhan Reddy',border=1,padx=60, pady=5, font=("Helvetica", 12))
    name3=Label(credits,text='Manne Rohith Sai',borderwidth=1,padx=60, pady=5, font=("Helvetica", 12))
    name4=Label(credits,text='Chovatiya Laksh Vipulbhai',borderwidth=1,padx=60, pady=5, font=("Helvetica", 12))
    roll_no=Label(credits,text='Roll No.',borderwidth=1,padx=60, pady=5, font=("Helvetica", 12))
    roll_no1=Label(credits,text='BT2024052',borderwidth=1,padx=60, pady=5, font=("Helvetica", 12))
    roll_no2=Label(credits,text='BT2024029',borderwidth=1,padx=60, pady=5, font=("Helvetica", 12))
    roll_no3=Label(credits,text='BT2024144',borderwidth=1,padx=60, pady=5, font=("Helvetica", 12))
    roll_no4=Label(credits,text='BT2024056',borderwidth=1,padx=60, pady=5, font=("Helvetica", 12))
    task=Label(credits,text='Task',borderwidth=1,padx=60, pady=5, font=("Helvetica", 12))
    task1=Label(credits,text='UI Design and game logic',borderwidth=1,padx=60, pady=5, font=("Helvetica", 12))
    task2=Label(credits,text='CSV file handling',borderwidth=1,padx=60, pady=5, font=("Helvetica", 12))
    task3=Label(credits,text='UI Design and testing',borderwidth=1,padx=60, pady=5, font=("Helvetica", 12))
    task4=Label(credits,text='Integration and Testing',borderwidth=1,padx=60, pady=5, font=("Helvetica", 12))
    email=Label(credits,text='Email',borderwidth=1,padx=60, pady=5, font=("Helvetica", 12))
    email1=Label(credits,text='Het.Chavadia@iiitb.ac.in',borderwidth=1,padx=60, pady=5, font=("Helvetica", 12))
    email2=Label(credits,text='Raghunandhan.P@iiitb.ac.in',borderwidth=1,padx=60, pady=5, font=("Helvetica", 12))
    email3=Label(credits,text='Rohith.Sai@iiitb.ac.in',borderwidth=1,padx=60, pady=5, font=("Helvetica", 12))
    email4=Label(credits,text='Laksh.Chovatiya@iiitb.ac.in',borderwidth=1,padx=60, pady=5, font=("Helvetica", 12))
    name.grid(row=0,column=0)
    name1.grid(row=1,column=0)
    name2.grid(row=2,column=0)
    name3.grid(row=3,column=0)
    name4.grid(row=4,column=0)
    

    roll_no.grid(row=0,column=1)
    roll_no1.grid(row=1,column=1)
    roll_no2.grid(row=2,column=1)
    roll_no3.grid(row=3,column=1)
    roll_no4.grid(row=4,column=1)

    task.grid(row=0,column=2)
    task1.grid(row=1,column=2)
    task2.grid(row=2,column=2)
    task3.grid(row=3,column=2)
    task4.grid(row=4,column=2)

    email.grid(row=0,column=3)
    email1.grid(row=1,column=3)
    email2.grid(row=2,column=3)
    email3.grid(row=3,column=3)
    email4.grid(row=4,column=3)
entry_text = StringVar()
entry_text.trace("w", convert_to_uppercase)  # Trace changes to the StringVar
name_input = Entry(frame2, textvariable=entry_text, border=1, width=17, font='Helvetica 20', bg="lightgreen")

player_name_label = Label(root, width=17, text="Enter Player Name:", font=("OCR A Extended", 17))
but1 = Button(frame2, text='Play', command=clk_play, font='Helvetica 28 bold', bg='Red', pady=15)
but2 = Button(frame2, text='Player History', background='orange', font='bold', command=view_history)
but3 = Button(frame2, text='Credits', bg='orange', font='bold', padx=25,command=credit)

name_input.grid(row=0, column=0, columnspan=4)
but1.grid(row=1, column=1, columnspan=2)
but2.grid(row=2, column=0, columnspan=2)
but3.grid(row=2, column=2, columnspan=2)

root.mainloop()
