
#======================
# imports
#======================
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
import tkinter as Tkinter
from datetime import datetime
from tkinter import messagebox
import time
from typing import Coroutine, Counter

# Create instance
win = tk.Tk()   

# Add a title       
win.title("Baking Monitor")  

tabControl = ttk.Notebook(win)          # Create Tab Control

tab1 = ttk.Frame(tabControl)            # Create a tab 
tabControl.add(tab1, text='AOC Baking Monitor')      # Add the tab
# tab2 = ttk.Frame(tabControl)            # Add a second tab
# tabControl.add(tab2, text='Tab 2')      # Make second tab visible

tabControl.pack(expand=1, fill="both")  # Pack to make visible


image = Tkinter.PhotoImage(file="O-net.png")
label_image = Tkinter.Label(image=image)
label_image.pack(side=LEFT,fill=X)

# LabelFrame using tab1 as the parent
# CellA = ttk.LabelFrame(tab1, text=' Cell 1')
# CellA.grid(column=0, row=0)

# # Modify adding a Label using mighty as the parent instead of win
# a_label = ttk.Label(CellA, text="Scan ST barcode")
# a_label.grid(column=0, row=0, sticky='W')


Date_stamp = datetime.now().strftime('%H:%M:%S')


def clock():    #Clock
    my_clock = ''
    hour = time.strftime("%H")
    minute =time.strftime("%M")
    second = time.strftime("%S")
    my_clock.config(text= hour + ":" + minute + ":" + second)
    my_clock.after(1000,clock)

common_time = ''
clock = Label(win, font=('times', 15))
clock.pack(fill=BOTH, expand=1)

def tick():
    global common_time
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != common_time:
        common_time = time2
        clock.config(text=time2)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
    clock.after(1000, tick)
    print(common_time)
    return common_time

def compare_time(x):
    global common_time
    if common_time < x:
        print ("Good job")
    



#!-------- Cell 2
Cell_2 = ttk.LabelFrame(tab1, text=' Cell_2')
Cell_2.grid(column=0, row=1, padx=8, pady=4)     

name = tk.StringVar()
name_entered = ttk.Entry(Cell_2, width=12, textvariable=name)
name_entered.grid(column=0, row=1, sticky='W')

Cell_2_label=Label(Cell_2,text="Baking slot A",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
Cell_2_label.grid(column=0, row=5, padx=8, pady=4)
Cell_2_label=Label(Cell_2,text="Baking slot B",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
Cell_2_label.grid(column=0, row=6, padx=8, pady=4)
Cell_2_label=Label(Cell_2,text="Baking slot C",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
Cell_2_label.grid(column=0, row=7, padx=8, pady=4)
Cell_2_label=Label(Cell_2,text="Baking slot D",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
Cell_2_label.grid(column=0, row=8, padx=8, pady=4)


cycle_time = 6
remain_time = 0
running = False
def start_cell1_a():
    Cell_2_label=Label(Cell_2,text= common_time,fg='black',bg='white',font=("arial", 10))
    Cell_2_label.grid(column=3, row=5, padx=8, pady=4)
    def count_a():
            global running
            running = True
            if running:
                global cycle_time
                print(cycle_time)
                SS = Cell_2_countlb_a.after(10000,count_a)
                cycle_time += 1
                remain_time = cycle_time
            Cell_2_countlb_a.config(text=str(cycle_time)) 
            print("This is remain_time:",remain_time)
            LED_show_a()
            return cycle_time
            
        
    def LED_show_a():
        if cycle_time <5 :
            cell_2_butt=Button(Cell_2, text=" ", width =12,fg='white',font = ('tahoma 7 bold'))
            cell_2_butt.grid(column=9, row=5, padx=0, pady=2)
            cell_2_butt=Button(Cell_2, text=" ", width =12,bg="Yellow",fg='white',font = ('tahoma 7 bold')) 
            cell_2_butt.grid(column=9, row=5, padx=0, pady=2)
            # cell_2_butt=Button(Cell_2, text=" ", width =12,fg='white',font = ('tahoma 7 bold')) 
            # cell_2_butt.grid(column=10, row=5, padx=0, pady=2)
            cell_2_butt.after(1000,LED_show_a)                 
        elif cycle_time == 0 :
            cell_2_butt=Button(Cell_2, text=" ", width =12,font = ('tahoma 7 bold'))
            cell_2_butt.grid(column=8, row=5, padx=0, pady=2)
            cell_2_butt=Button(Cell_2, text=" ", width =12,fg='white',font = ('tahoma 7 bold')) 
            cell_2_butt.grid(column=9, row=5, padx=0, pady=2)
            cell_2_butt=Button(Cell_2, text=" ", width =12,fg='red',font = ('tahoma 7 bold')) 
            cell_2_butt.grid(column=10, row=5, padx=0, pady=2)
            cell_2_butt.after(500,LED_show_a)  
            
        else :
            cell_2_butt=Button(Cell_2, text=" ", width =12,bg="green",fg='white',font = ('tahoma 7 bold')) 
            cell_2_butt.grid(column=10, row=5, padx=0, pady=2)
        

    
    count_a()

  
    

def start_cell1_b():
    Cell_2_label=Label(Cell_2,text=common_time,fg='black',bg='white',font=("arial", 10))
    Cell_2_label.grid(column=3, row=6, padx=8, pady=4)
def start_cell1_c():
    Cell_2_label=Label(Cell_2,text=common_time,fg='black',bg='white',font=("arial", 10))
    Cell_2_label.grid(column=3, row=7, padx=8, pady=4)
def start_cell1_d():
    Cell_2_label=Label(Cell_2,text=common_time,fg='black',bg='white',font=("arial", 10))
    Cell_2_label.grid(column=3, row=8, padx=8, pady=4)
        
#!----------Cell Mess box


def mes_boxA():
   mes_boxA = messagebox.askokcancel('OK','Please make sure')
   print(mes_boxA)
   if mes_boxA == True:
       start_cell1_a()
   else :
        print("--")

# def mainfunction():

    



cell2_start_acA = ttk.Button(Cell_2,width=12, text="Start A",command= mes_boxA)   
cell2_start_acA.grid(column=1, row=5)
cell2_start_acb = ttk.Button(Cell_2,width=12, text="Start B",command= start_cell1_b)   
cell2_start_acb.grid(column=1, row=6) 
cell2_start_acc = ttk.Button(Cell_2,width=12, text="Start C",command= start_cell1_c)   
cell2_start_acc.grid(column=1, row=7) 
cell2_start_acd = ttk.Button(Cell_2,width=12, text="Start D",command= start_cell1_d)   
cell2_start_acd.grid(column=1, row=8) 







Cell_2_label=Label(Cell_2,text="Start time :",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
Cell_2_label.grid(column=4, row=5, padx=8, pady=4)
Cell_2_label=Label(Cell_2,text="Start time :",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
Cell_2_label.grid(column=4, row=6, padx=8, pady=4)
Cell_2_label=Label(Cell_2,text="Start time :",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
Cell_2_label.grid(column=4, row=7, padx=8, pady=4)
Cell_2_label=Label(Cell_2,text="Start time :",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
Cell_2_label.grid(column=4, row=8, padx=8, pady=4)



Cell_2_label=Label(Cell_2,text="Stop time :",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
Cell_2_label.grid(column=4, row=5, padx=8, pady=4)
Cell_2_label=Label(Cell_2,text="Stop time  :",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
Cell_2_label.grid(column=4, row=6, padx=8, pady=4)
Cell_2_label=Label(Cell_2,text="Stop time  :",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
Cell_2_label.grid(column=4, row=7, padx=8, pady=4)
Cell_2_label=Label(Cell_2,text="Stop time  :",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
Cell_2_label.grid(column=4, row=8, padx=8, pady=4)

Cell_2_countlb_a=Label(Cell_2,text=" ",fg='black',bg='white',font=("arial", 10))
Cell_2_countlb_a.grid(column=5, row=5, padx=8, pady=4)
Cell_2_countlb_b=Label(Cell_2,text=" ",fg='black',bg='white',font=("arial", 10))
Cell_2_countlb_b.grid(column=5, row=6, padx=8, pady=4)
Cell_2_countlb_c=Label(Cell_2,text=" ",fg='black',bg='white',font=("arial", 10))
Cell_2_countlb_c.grid(column=5, row=7, padx=8, pady=4)
Cell_2_countlb_d=Label(Cell_2,text=" ",fg='black',bg='white',font=("arial", 10))
Cell_2_countlb_d.grid(column=5, row=8, padx=8, pady=4)





cell_2_butt=Button(Cell_2, text=" ", width =12,bg="red",fg='white',font = ('tahoma 7 bold')) 
cell_2_butt.grid(column=8, row=6, padx=0, pady=4)
cell_2_butt=Button(Cell_2, text=" ", width =12,bg="Yellow",fg='white',font = ('tahoma 7 bold')) 
cell_2_butt.grid(column=9, row=6, padx=0, pady=4)
cell_2_butt=Button(Cell_2, text=" ", width =12,bg="green",fg='white',font = ('tahoma 7 bold')) 
cell_2_butt.grid(column=10, row=6, padx=0, pady=4)



cell_2_butt=Button(Cell_2, text=" ", width =12,bg="red",fg='white',font = ('tahoma 7 bold')) 
cell_2_butt.grid(column=8, row=7, padx=0, pady=4)
cell_2_butt=Button(Cell_2, text=" ", width =12,bg="Yellow",fg='white',font = ('tahoma 7 bold')) 
cell_2_butt.grid(column=9, row=7, padx=0, pady=4)
cell_2_butt=Button(Cell_2, text=" ", width =12,bg="green",fg='white',font = ('tahoma 7 bold')) 
cell_2_butt.grid(column=10, row=7, padx=0, pady=4)



cell_2_butt=Button(Cell_2, text=" ", width =12,bg="red",fg='white',font = ('tahoma 7 bold')) 
cell_2_butt.grid(column=8, row=8, padx=0, pady=4)
cell_2_butt=Button(Cell_2, text=" ", width =12,bg="Yellow",fg='white',font = ('tahoma 7 bold')) 
cell_2_butt.grid(column=9, row=8, padx=0, pady=4)
cell_2_butt=Button(Cell_2, text=" ", width =12,bg="green",fg='white',font = ('tahoma 7 bold')) 
cell_2_butt.grid(column=10, row=8, padx=0, pady=4)





#!-------- Cell 3

# Cell_3 = ttk.LabelFrame(tab1, text=' Cell_3')
# Cell_3.grid(column=0, row=2, padx=8, pady=4)      

# action = ttk.Button(Cell_3,width=12, text="Start",)   
# action.grid(column=0, row=2)  

# name = tk.StringVar()
# name_entered = ttk.Entry(Cell_3, width=12, textvariable=name)
# name_entered.grid(column=0, row=1, sticky='W')

# Cell_3_label=Label(Cell_3,text="Baking slot A",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
# Cell_3_label.grid(column=0, row=5, padx=8, pady=4)
# Cell_3_label=Label(Cell_3,text="Baking slot B",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
# Cell_3_label.grid(column=0, row=6, padx=8, pady=4)
# Cell_3_label=Label(Cell_3,text="Baking slot C",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
# Cell_3_label.grid(column=0, row=7, padx=8, pady=4)
# Cell_3_label=Label(Cell_3,text="Baking slot D",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
# Cell_3_label.grid(column=0, row=8, padx=8, pady=4)

# Cell_3_label=Label(Cell_3,text= Date_stamp,fg='black',bg='white',font=("arial", 10))
# Cell_3_label.grid(column=2, row=5, padx=8, pady=4)
# Cell_3_label=Label(Cell_3,text=Date_stamp,fg='black',bg='white',font=("arial", 10))
# Cell_3_label.grid(column=2, row=6, padx=8, pady=4)
# Cell_3_label=Label(Cell_3,text=Date_stamp,fg='black',bg='white',font=("arial", 10))
# Cell_3_label.grid(column=2, row=7, padx=8, pady=4)
# Cell_3_label=Label(Cell_3,text=Date_stamp,fg='black',bg='white',font=("arial", 10))
# Cell_3_label.grid(column=2, row=8, padx=8, pady=4)


# Cell_3_label=Label(Cell_3,text="Start time :",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
# Cell_3_label.grid(column=1, row=5, padx=8, pady=4)
# Cell_3_label=Label(Cell_3,text="Start time :",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
# Cell_3_label.grid(column=1, row=6, padx=8, pady=4)
# Cell_3_label=Label(Cell_3,text="Start time :",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
# Cell_3_label.grid(column=1, row=7, padx=8, pady=4)
# Cell_3_label=Label(Cell_3,text="Start time :",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
# Cell_3_label.grid(column=1, row=8, padx=8, pady=4)

# cell_3_butt=Button(Cell_3, text=" ", width =12,bg="red",fg='white',font = ('tahoma 7 bold')) 
# cell_3_butt.grid(column=8, row=5, padx=0, pady=2)
# cell_3_butt=Button(Cell_3, text=" ", width =12,bg="Yellow",fg='white',font = ('tahoma 7 bold')) 
# cell_3_butt.grid(column=9, row=5, padx=0, pady=2)
# cell_3_butt=Button(Cell_3, text=" ", width =12,bg="green",fg='white',font = ('tahoma 7 bold')) 
# cell_3_butt.grid(column=10, row=5, padx=0, pady=2)


# cell_3_butt=Button(Cell_3, text=" ", width =12,bg="red",fg='white',font = ('tahoma 7 bold')) 
# cell_3_butt.grid(column=8, row=6, padx=0, pady=4)
# cell_3_butt=Button(Cell_3, text=" ", width =12,bg="Yellow",fg='white',font = ('tahoma 7 bold')) 
# cell_3_butt.grid(column=9, row=6, padx=0, pady=4)
# cell_3_butt=Button(Cell_3, text=" ", width =12,bg="green",fg='white',font = ('tahoma 7 bold')) 
# cell_3_butt.grid(column=10, row=6, padx=0, pady=4)



# cell_3_butt=Button(Cell_3, text=" ", width =12,bg="red",fg='white',font = ('tahoma 7 bold')) 
# cell_3_butt.grid(column=8, row=7, padx=0, pady=4)
# cell_3_butt=Button(Cell_3, text=" ", width =12,bg="Yellow",fg='white',font = ('tahoma 7 bold')) 
# cell_3_butt.grid(column=9, row=7, padx=0, pady=4)
# cell_3_butt=Button(Cell_3, text=" ", width =12,bg="green",fg='white',font = ('tahoma 7 bold')) 
# cell_3_butt.grid(column=10, row=7, padx=0, pady=4)



# cell_3_butt=Button(Cell_3, text=" ", width =12,bg="red",fg='white',font = ('tahoma 7 bold')) 
# cell_3_butt.grid(column=8, row=8, padx=0, pady=4)
# cell_3_butt=Button(Cell_3, text=" ", width =12,bg="Yellow",fg='white',font = ('tahoma 7 bold')) 
# cell_3_butt.grid(column=9, row=8, padx=0, pady=4)
# cell_3_butt=Button(Cell_3, text=" ", width =12,bg="green",fg='white',font = ('tahoma 7 bold')) 
# cell_3_butt.grid(column=10, row=8, padx=0, pady=4)

#!----------------------------------------------------------------------------------------

# Using a scrolled Text control    
# scrol_w  = 30
# scrol_h  =  3
# scr = scrolledtext.ScrolledText(Cell_2, width=scrol_w, height=scrol_h, wrap=tk.WORD)
# scr.grid(column=0, row=11, sticky='WE', columnspan=3)  

# Modified Button Click Function
def click_me(): 
    action.configure(text='Hello ' + name.get() + ' ' + 
                     number_chosen.get())

# Adding a Textbox Entry widget
# name = tk.StringVar()
# name_entered = ttk.Entry(CellA, width=12, textvariable=name)
# name_entered.grid(column=0, row=1, sticky='W')               # align left/West

# # Adding a Button
# action = ttk.Button(CellA, text="Stop", command=click_me)   
# action.grid(column=2, row=1)                                

# ttk.Label(mighty, text="Choose a number:").grid(column=1, row=0)
# number = tk.StringVar()
# number_chosen = ttk.Combobox(mighty, width=12, textvariable=number, state='readonly')
# number_chosen['values'] = (1, 2, 4, 42, 100)
# number_chosen.grid(column=1, row=1)
# number_chosen.current(0)


            


# # Tab Control 2 refactoring  ---------------------------------------------------------
# # We are creating a container frame to hold all other widgets -- Tab2

# mighty2 = ttk.LabelFrame(tab2, text=' The Snake ')
# mighty2.grid(column=0, row=0, padx=5, pady=4)

# # Creating three checkbuttons
# chVarDis = tk.IntVar()
# check1 = tk.Checkbutton(mighty2, text="Disabled", variable=chVarDis, state='disabled')
# check1.select()
# check1.grid(column=0, row=4, sticky=tk.W)

# chVarUn = tk.IntVar()
# check2 = tk.Checkbutton(mighty2, text="UnChecked", variable=chVarUn)
# check2.deselect()
# check2.grid(column=1, row=4, sticky=tk.W)                   

# chVarEn = tk.IntVar()
# check3 = tk.Checkbutton(mighty2, text="Enabled", variable=chVarEn)
# check3.deselect()
# check3.grid(column=2, row=4, sticky=tk.W)                     

# # GUI Callback function 
# def checkCallback(*ignoredArgs):
#     # only enable one checkbutton
#     if chVarUn.get(): check3.configure(state='disabled')
#     else:             check3.configure(state='normal')
#     if chVarEn.get(): check2.configure(state='disabled')
#     else:             check2.configure(state='normal') 

# # trace the state of the two checkbuttons
# chVarUn.trace('w', lambda unused0, unused1, unused2 : checkCallback())    
# chVarEn.trace('w', lambda unused0, unused1, unused2 : checkCallback())   


# # First, we change our Radiobutton global variables into a list
# colors = ["Blue", "Gold", "Red"]   

# # We have also changed the callback function to be zero-based, using the list 
# # instead of module-level global variables 
# # Radiobutton Callback
# def radCall():
#     radSel=radVar.get()
#     if   radSel == 0: win.configure(background=colors[0])  # zero-based
#     elif radSel == 1: win.configure(background=colors[1])  # using list
#     elif radSel == 2: win.configure(background=colors[2])

# # create three Radiobuttons using one variable
# radVar = tk.IntVar()

# # Next we are selecting a non-existing index value for radVar
# radVar.set(99)                                 
 
# # Now we are creating all three Radiobutton widgets within one loop
# for col in range(3):                             
#     curRad = tk.Radiobutton(mighty2, text=colors[col], variable=radVar, 
#                             value=col, command=radCall)          
#     curRad.grid(column=col, row=6, sticky=tk.W)             # row=6

# # Create a container to hold labels
# buttons_frame = ttk.LabelFrame(mighty2, text=' Labels in a Frame ')
# buttons_frame.grid(column=0, row=7)        
 
# # Place labels into the container element
# ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0, sticky=tk.W)
# ttk.Label(buttons_frame, text="Label2").grid(column=1, row=0, sticky=tk.W)
# ttk.Label(buttons_frame, text="Label3").grid(column=2, row=0, sticky=tk.W)

# Exit GUI cleanly
def _quit():
    win.quit()
    win.destroy()
    exit() 
    
# Creating a Menu Bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

# Add menu items
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=_quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add another Menu to the Menu Bar and an item
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About")
menu_bar.add_cascade(label="Help", menu=help_menu)


tick()
name_entered.focus()      # Place cursor into name Entry
#======================
# Start GUI
#======================
win.mainloop()