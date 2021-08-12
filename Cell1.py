
#======================
# imports
#======================
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
import tkinter as Tkinter
from tkinter import messagebox
import time
from typing import Coroutine, Counter, get_origin
import datetime
# Create instance
win = tk.Tk()   

# Add a title       
win.title("AOC Baking Monitor V1")  

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
# cellA = ttk.LabelFrame(tab1, text=' cell 1')
# cellA.grid(column=0, row=0)

# # Modify adding a Label using mighty as the parent instead of win
# a_label = ttk.Label(cellA, text="Scan ST barcode")
# a_label.grid(column=0, row=0, sticky='W')


now = datetime.datetime.now()
print ('Start time ',now.hour, now.minute, now.second)

common_time = ''
clock = Label(win, font=('times', 15))
clock.pack(fill=BOTH, expand=1)
stop_time = ''
clock_stop = Label(win, font=('times', 15))
clock_stop.pack(fill=BOTH, expand=1)
  
def tick():
    global common_time
    
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S %p')
    
    
    # if time string has changed, update it
    if time2 != common_time:
        common_time = time2
        clock.config(text=time2)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
          
    clock.after(1000, tick)
    return common_time
    #--
    

#!----------------------------------------limit count--------------------------------------------!
countlim_set = 5 #Sec = 1 hr
#!----------------------------------------limit count--------------------------------------------!
#
defult_color_delay = 500
result_color_delay = 2000

#!----------------------------- cell 1--------------------------------------------

cell1_cycle_time_a = 0
cell1_cycle_time_b = 0
cell1_cycle_time_c = 0
cell1_cycle_time_d = 0

remain_time = 0

cell1_slot_a_running = False
cell1_slot_b_running = False
cell1_slot_c_running = False
cell1_slot_d_running = False

#--------------------------------------------------------------

cell_1 = ttk.LabelFrame(tab1, text=' Cell_1')
cell_1.grid(column=0, row=1, padx=8, pady=4)   
# cell_1_name = tk.StringVar()
# cell_1_name_entered = ttk.Entry(cell_1, width=12, textvariable=cell_1_name)
# cell_1_name_entered.grid(column=0, row=1, sticky='W')


cell_1_label=Label(cell_1,text="Baking slot A",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
cell_1_label.grid(column=0, row=5, padx=8, pady=4)
cell_1_label=Label(cell_1,text="Baking slot B",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
cell_1_label.grid(column=0, row=6, padx=8, pady=4)
cell_1_label=Label(cell_1,text="Baking slot C",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
cell_1_label.grid(column=0, row=7, padx=8, pady=4)
cell_1_label=Label(cell_1,text="Baking slot D",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
cell_1_label.grid(column=0, row=8, padx=8, pady=4)


def cell_1_main_start():
    global defult_color_delay
    global result_color_delay
    #cell #1 A
    cell1_start_aca = ttk.Button(cell_1,width=12, text="Start A",command= lambda:[cell1_dis_buttom_start_a(True),mes_box_A()])
    cell1_start_aca.grid(column=1, row=5)
    cell1_stop_a = ttk.Button(cell_1,width=12, text="Stop A",command= lambda:[cell1_dis_buttom_start_a(FALSE),cell1_a_stop(True)])
    cell1_stop_a.grid(column=8, row=5,padx=2, pady=2) 
    #cell #1 b
    cell1_start_acb = ttk.Button(cell_1,width=12, text="Start B",command= lambda:[cell1_dis_buttom_start_b(True),mes_box_B()])
    cell1_start_acb.grid(column=1, row=6)
    cell1_stop_b = ttk.Button(cell_1,width=12, text="Stop B",command= lambda:[cell1_dis_buttom_start_b(FALSE),cell1_b_stop(True)])
    cell1_stop_b.grid(column=8, row=6,padx=2, pady=2) 
    #cell #1 c
    cell1_start_acc = ttk.Button(cell_1,width=12, text="Start C",command= lambda:[cell1_dis_buttom_start_c(True),mes_box_C()])
    cell1_start_acc.grid(column=1, row=7)
    cell1_stop_c = ttk.Button(cell_1,width=12, text="Stop C",command= lambda:[cell1_dis_buttom_start_c(FALSE),cell1_c_stop(True)])
    cell1_stop_c.grid(column=8, row=7,padx=2, pady=2) 

    cell1_start_acd = ttk.Button(cell_1,width=12, text="Start D",command= lambda:[cell1_dis_buttom_start_d(True),mes_box_D()])
    cell1_start_acd.grid(column=1, row=8)
    cell1_stop_d = ttk.Button(cell_1,width=12, text="Stop D",command= lambda:[cell1_dis_buttom_start_d(FALSE),cell1_d_stop(True)])
    cell1_stop_d.grid(column=8, row=8,padx=2, pady=2) 

    cell_1_butt=Button(cell_1, text=" ", width =12,fg='white',font = ('tahoma 13 bold'))
    cell_1_butt.grid(column=9, row=5, padx=5, pady=2)
    cell_1_butt=Button(cell_1, text=" ", width =12,fg='white',font = ('tahoma 13 bold'))
    cell_1_butt.grid(column=10, row=5, padx=5, pady=2)
    cell_1_butt=Button(cell_1, text=" ", width =12,fg="white",font = ('tahoma 13 bold')) 
    cell_1_butt.grid(column=11, row=5, padx=5, pady=2)

    cell_1_butt=Button(cell_1, text=" ", width =12,fg='white',font = ('tahoma 13 bold'))
    cell_1_butt.grid(column=9, row=6, padx=5, pady=2)
    cell_1_butt=Button(cell_1, text=" ", width =12,fg='white',font = ('tahoma 13 bold'))
    cell_1_butt.grid(column=10, row=6, padx=5, pady=2)
    cell_1_butt=Button(cell_1, text=" ", width =12,fg="white",font = ('tahoma 13 bold')) 
    cell_1_butt.grid(column=11, row=6, padx=5, pady=2)

    cell_1_butt=Button(cell_1, text=" ", width =12,fg='white',font = ('tahoma 13 bold'))
    cell_1_butt.grid(column=9, row=7, padx=5, pady=2)
    cell_1_butt=Button(cell_1, text=" ", width =12,fg='white',font = ('tahoma 13 bold'))
    cell_1_butt.grid(column=10, row=7, padx=5, pady=2)
    cell_1_butt=Button(cell_1, text=" ", width =12,fg="white",font = ('tahoma 13 bold')) 
    cell_1_butt.grid(column=11, row=7, padx=5, pady=2)

    cell_1_butt=Button(cell_1, text=" ", width =12,fg='white',font = ('tahoma 13 bold'))
    cell_1_butt.grid(column=9, row=8, padx=5, pady=2)
    cell_1_butt=Button(cell_1, text=" ", width =12,fg='white',font = ('tahoma 13 bold'))
    cell_1_butt.grid(column=10, row=8, padx=5, pady=2)
    cell_1_butt=Button(cell_1, text=" ", width =12,fg="white",font = ('tahoma 13 bold')) 
    cell_1_butt.grid(column=11, row=8, padx=5, pady=2)

    cell_1_butt_time=Label(cell_1, text=common_time, width =12,fg="white",bg='white',font = ('tahoma 13 bold')) 
    cell_1_butt_time.grid(column=3, row=5, padx=5, pady=2)

    


    def cell1_dis_buttom_start_a(status_butt):
        if status_butt == True:
            cell1_start_aca['state'] = DISABLED
            cell1_slot_a = True
            return  cell1_slot_a
        elif status_butt == FALSE :
            cell1_start_aca['state'] = NORMAL

    def cell1_dis_buttom_start_b(status_butt):
        if status_butt == True:
            cell1_start_acb['state'] = DISABLED
            cell1_slot_b = True
            return  cell1_slot_b
        elif status_butt == FALSE :
            cell1_start_acb['state'] = NORMAL

    def cell1_dis_buttom_start_c(status_butt):
        if status_butt == True:
            cell1_start_acc['state'] = DISABLED
            cell1_slot_c = True
            return  cell1_slot_c
        elif status_butt == FALSE :
            cell1_start_acc['state'] = NORMAL
    
    def cell1_dis_buttom_start_d(status_butt):
        if status_butt == True:
            cell1_start_acd['state'] = DISABLED
            cell1_slot_d = True
            return  cell1_slot_d
        elif status_butt == FALSE :
            cell1_start_acd['state'] = NORMAL
        

    def cell1_a_stop(stop_butt):
        global cell1_slot_a_running
        if stop_butt == True :
            cell1_slot_a_running = False
            cell1_cycle_time_a = 0
            start_cell1_a(cell1_slot_a_running)
       
            return cell1_cycle_time_a

    def cell1_b_stop(stop_butt):
        global cell1_slot_b_running
        if stop_butt == True :
            cell1_slot_b_running = False
            cell1_cycle_time_b = 0
            start_cell1_b(cell1_slot_b_running)
            
            return cell1_cycle_time_b

    def cell1_c_stop(stop_butt):
        global cell1_slot_c_running
        if stop_butt == True :
            cell1_slot_c_running = False
            cell1_cycle_time_c = 0
            start_cell1_c(cell1_slot_c_running)
            
            return cell1_cycle_time_c

    def cell1_d_stop(stop_butt):
        global cell1_slot_d_running
        if stop_butt == True :
            cell1_slot_d_running = False
            cell1_cycle_time_d = 0
            start_cell1_d(cell1_slot_d_running)
            
            return cell1_cycle_time_d

            
    def mes_box_A():
        global cell1_slot_a_running
        mes_a = messagebox.askokcancel('Re-check','Sure to start slot A')
        #print(mes_a)
        if mes_a == True:
            cell1_slot_a_running = True
            start_cell1_a(cell1_slot_a_running)
        else:
            cell1_start_aca['state'] = NORMAL
    
    def mes_box_B():
        global cell1_slot_b_running
        mes_b = messagebox.askokcancel('Re-check','Sure to start slot B')
        #print(mes_b)
        if mes_b == True:
            cell1_slot_b_running = True
            start_cell1_b(cell1_slot_b_running)
        else:
            cell1_start_acb['state'] = NORMAL

    def mes_box_C():
        global cell1_slot_c_running
        mes_c = messagebox.askokcancel('Re-check','Sure to start slot C')
        #print(mes_c)
        if mes_c == True:
            cell1_slot_c_running = True
            start_cell1_c(cell1_slot_c_running)
        else:
            cell1_start_acc['state'] = NORMAL
        
    def mes_box_D():
        global cell1_slot_d_running
        mes_d = messagebox.askokcancel('Re-check','Sure to start slot D')
        #print(mes_d)
        if mes_d == True:
            cell1_slot_d_running = True
            start_cell1_d(cell1_slot_d_running)
        else:
            cell1_start_acd['state'] = NORMAL
        

    def start_cell1_a(cell1_slot_a_running):
        global cell1_cycle_time_a
        #print ("status cell1_slot_a =",cell1_slot_a)
        cell_1_label=Label(cell_1,text= common_time,fg='black',bg='white',font=("arial", 10))
        cell_1_label.grid(column=3, row=5, padx=8, pady=4)

        cell1_defult_led_a()
        def count_a():
            global cell1_slot_a_running
            global cell1_cycle_time_a
            if cell1_slot_a_running:
                #print('cell1_slot_a_running:',cell1_slot_a_running)
                cell_1_countlb_a.after(1000,count_a)
                cell1_cycle_time_a += 1
                remain_time = cell1_cycle_time_a
                # cell_1_countlb_a.config(text=str(cell1_cycle_time_a)) 
                #print("This is remain_time A:",remain_time)
                if cell1_cycle_time_a == 1:
                    LED_show_a()
                elif cell1_cycle_time_a == countlim_set :
                    unit_pass()
                    print('------------------------unit_pass(Cell 1 a)-----------------------')
                return cell1_cycle_time_a
            else :
                cell1_cycle_time_a = 0
                # cell_1_countlb_a.config(text=str(cell1_cycle_time_a))
    
                return cell1_cycle_time_a 
            
        def LED_show_a():
            cell_1_butt=Button(cell_1, text=" ", width =12,font = ('tahoma 13 bold')) 
            cell_1_butt.grid(column=9, row=5, padx=5, pady=2)
            cell_1_butt=Button(cell_1, text="Baking", width =12,fg='white',bg='yellow',font = ('tahoma 13 bold')) 
            cell_1_butt.grid(column=10, row=5, padx=5, pady=2)
            cell_1_butt_D=Button(cell_1, text=" ", width =12,font = ('tahoma 13 bold')) 
            cell_1_butt_D.grid(column=11, row=5, padx=5, pady=2)
            # cell_1.after(result_color_delay, lambda: cell_1_butt.configure(background="yellow"))
            # cell_1.after(defult_color_delay, lambda: cell_1_butt.configure(background="yellow3")) 

                      
        def unit_pass():  
            cell_1_butt_Y=Button(cell_1, text=" ", width =12,font = ('tahoma 13 bold')) 
            cell_1_butt_Y.grid(column=9, row=5, padx=5, pady=2)
            cell_1_butt_Y=Button(cell_1, text=" ", width =12,font = ('tahoma 13 bold')) 
            cell_1_butt_Y.grid(column=10, row=5, padx=5, pady=2)
            cell_1_butt_G=Button(cell_1, text=" Done ", width =12,bg="firebrick1",fg='white',font = ('tahoma 13 bold')) 
            cell_1_butt_G.grid(column=11, row=5, padx=5, pady=2)
            cell_1.after(defult_color_delay, lambda: cell_1_butt_G.configure(background="firebrick4"))
            cell_1.after(result_color_delay, lambda: cell_1_butt_G.configure(background="firebrick1"))
        count_a()

    def start_cell1_b(cell1_slot_b_running):
        #print ("status cell1_slot_b =",cell1_slot_b)
        cell_1_label=Label(cell_1,text= common_time,fg='black',bg='white',font=("arial", 10))
        cell_1_label.grid(column=3, row=6, padx=8, pady=4)
        cell1_defult_led_b()
        def count_a():
            global cell1_slot_b_running  # True /Falsez
            global cell1_cycle_time_b
            
            if cell1_slot_b_running:
                #print('cell1_slot_b_running:',cell1_slot_b_running)
                cell_1_countlb_b.after(1000,count_a)
                cell1_cycle_time_b += 1
                remain_time = cell1_cycle_time_b
                # cell_1_countlb_b.config(text=str(cell1_cycle_time_b)) 
                #print("This is remain_time B:",remain_time)
                if cell1_cycle_time_b == 1:
                    LED_show_a()
                elif cell1_cycle_time_b == countlim_set :
                    unit_pass()
                    print('------------------------unit_pass(Cell 1 b)-----------------------')
                return cell1_cycle_time_b
            else :
                cell1_cycle_time_b = 0
                # cell_1_countlb_b.config(text=str(cell1_cycle_time_b))
                
                return cell1_cycle_time_b
                            
        def LED_show_a():
            cell_1_butt=Button(cell_1, text=" ", width =12,font = ('tahoma 13 bold')) 
            cell_1_butt.grid(column=9, row=6, padx=5, pady=2)
            cell_1_butt=Button(cell_1, text="Baking", width =12,fg='white',bg='yellow',font = ('tahoma 13 bold')) 
            cell_1_butt.grid(column=10, row=6, padx=5, pady=2)
            cell_1_butt_D=Button(cell_1, text=" ", width =12,font = ('tahoma 13 bold')) 
            cell_1_butt_D.grid(column=11, row=6, padx=5, pady=2)
            # cell_1.after(result_color_delay, lambda: cell_1_butt.configure(background="yellow"))
            # cell_1.after(defult_color_delay, lambda: cell_1_butt.configure(background="yellow3")) 
       
        def unit_pass():  
            cell_1_butt_Y=Button(cell_1, text=" ", width =12,font = ('tahoma 13 bold')) 
            cell_1_butt_Y.grid(column=9, row=6, padx=5, pady=2)
            cell_1_butt_Y=Button(cell_1, text=" ", width =12,font = ('tahoma 13 bold')) 
            cell_1_butt_Y.grid(column=10, row=6, padx=5, pady=2)
            cell_1_butt_G=Button(cell_1, text=" Done ", width =12,bg="firebrick1",fg='white',font = ('tahoma 13 bold')) 
            cell_1_butt_G.grid(column=11, row=6, padx=5, pady=2)
            cell_1.after(defult_color_delay, lambda: cell_1_butt_G.configure(background="firebrick4"))
            cell_1.after(result_color_delay, lambda: cell_1_butt_G.configure(background="firebrick1"))
                  
        count_a()
    
    def start_cell1_c(cell1_slot_c_running):
        #print ("status cell1_slot_c =",cell1_slot_c_running)
        cell_1_label=Label(cell_1,text= common_time,fg='black',bg='white',font=("arial", 10))   # start time label
        cell_1_label.grid(column=3, row=7, padx=8, pady=4)
        
        cell1_defult_led_c()
    
        def count_a():
            global cell1_slot_c_running  # True /False
            global cell1_cycle_time_c
            global cell1_slot_c
        
            if cell1_slot_c_running:
                #print('cell1_slot_c_running:',cell1_slot_c_running)
                cell_1_countlb_c.after(1000,count_a)
                cell1_cycle_time_c += 1
                remain_time = cell1_cycle_time_c
             
                if cell1_cycle_time_c == 1:
                    LED_show_a()
                elif cell1_cycle_time_c == countlim_set :
                    unit_pass()
                    print('------------------------unit_pass(Cell 1 c)-----------------------')
                return cell1_cycle_time_c
            else :
                cell1_cycle_time_c = 0
                # cell_1_countlb_c.config(text=str(cell1_cycle_time_c))
                return cell1_cycle_time_c
                            
        def LED_show_a():
            cell_1_butt=Button(cell_1, text=" ", width =12,font = ('tahoma 13 bold')) 
            cell_1_butt.grid(column=9, row=7, padx=5, pady=2)
            cell_1_butt=Button(cell_1, text="Baking", width =12,fg='white',bg='yellow',font = ('tahoma 13 bold')) 
            cell_1_butt.grid(column=10, row=7, padx=5, pady=2)
            cell_1_butt_D=Button(cell_1, text=" ", width =12,font = ('tahoma 13 bold')) 
            cell_1_butt_D.grid(column=11, row=7, padx=5, pady=2)
            # cell_1.after(result_color_delay, lambda: cell_1_butt.configure(background="yellow"))
            # cell_1.after(defult_color_delay, lambda: cell_1_butt.configure(background="yellow3")) 
       
        def unit_pass():  
            cell_1_butt_Y=Button(cell_1, text=" ", width =12,font = ('tahoma 13 bold')) 
            cell_1_butt_Y.grid(column=9, row=7, padx=5, pady=2)
            cell_1_butt_Y=Button(cell_1, text=" ", width =12,font = ('tahoma 13 bold')) 
            cell_1_butt_Y.grid(column=10, row=7, padx=5, pady=2)
            cell_1_butt_G=Button(cell_1, text=" Done ", width =12,bg="firebrick1",fg='white',font = ('tahoma 13 bold')) 
            cell_1_butt_G.grid(column=11, row=7, padx=5, pady=2)
            cell_1.after(defult_color_delay, lambda: cell_1_butt_G.configure(background="firebrick4"))
            cell_1.after(result_color_delay, lambda: cell_1_butt_G.configure(background="firebrick1"))
            

        count_a()
    
    def start_cell1_d(cell1_slot_d_running):
        ##print ("status cell1_slot_c =",cell1_slot_d_running)
        cell_1_label=Label(cell_1,text= common_time,fg='black',bg='white',font=("arial", 10))   # start time label
        cell_1_label.grid(column=3, row=8, padx=8, pady=4)
        cell1_defult_led_d()
        def count_a():
            global cell1_slot_d_running  # True /False
            global cell1_cycle_time_d

            if cell1_slot_d_running:
                ##print('cell1_slot_d_running:',cell1_slot_d_running)
                cell_1_countlb_d.after(1000,count_a)
                cell1_cycle_time_d += 1
                remain_time = cell1_cycle_time_d
                # cell_1_countlb_d.config(text=str(cell1_cycle_time_d)) 
                #####print("This is remain_time c:",remain_time)
                if cell1_cycle_time_d == 1:
                    LED_show_a()
                elif cell1_cycle_time_d == countlim_set :
                    unit_pass()
                    print('------------------------unit_pass(Cell 1 d)-----------------------')
                return cell1_cycle_time_d
            else :
                cell1_cycle_time_d = 0
                # cell_1_countlb_d.config(text=str(cell1_cycle_time_d))
                
                return cell1_cycle_time_d
                            
        def LED_show_a():
            cell_1_butt=Button(cell_1, text=" ", width =12,font = ('tahoma 13 bold')) 
            cell_1_butt.grid(column=9, row=8, padx=5, pady=2)
            cell_1_butt=Button(cell_1, text="Baking", width =12,fg='white',bg='yellow',font = ('tahoma 13 bold')) 
            cell_1_butt.grid(column=10, row=8, padx=5, pady=2)
            cell_1_butt_D=Button(cell_1, text=" ", width =12,font = ('tahoma 13 bold')) 
            cell_1_butt_D.grid(column=11, row=8, padx=5, pady=2)
            # cell_1.after(result_color_delay, lambda: cell_1_butt.configure(background="yellow"))
            # cell_1.after(defult_color_delay, lambda: cell_1_butt.configure(background="yellow3")) 
       
        def unit_pass():  
            cell_1_butt_Y=Button(cell_1, text=" ", width =12,font = ('tahoma 13 bold')) 
            cell_1_butt_Y.grid(column=9, row=8, padx=5, pady=2)
            cell_1_butt_Y=Button(cell_1, text=" ", width =12,font = ('tahoma 13 bold')) 
            cell_1_butt_Y.grid(column=10, row=8, padx=5, pady=2)
            cell_1_butt_G=Button(cell_1, text=" Done ", width =12,bg="firebrick1",fg='white',font = ('tahoma 13 bold')) 
            cell_1_butt_G.grid(column=11, row=8, padx=5, pady=2)
            cell_1.after(defult_color_delay, lambda: cell_1_butt_G.configure(background="firebrick4"))
            cell_1.after(result_color_delay, lambda: cell_1_butt_G.configure(background="firebrick1"))
        count_a()


    def cell1_defult_led_a():
                cell_1_butt_defult_led=Button(cell_1, text="Free", width =12,fg='white',bg='green',font = ('tahoma 13 bold')) 
                cell_1_butt_defult_led.grid(column=9, row=5, padx=5, pady=2)
                cell_1_butt_defult_led2=Button(cell_1, text=" ", width =12,fg='white',font = ('tahoma 13 bold')) 
                cell_1_butt_defult_led2.grid(column=10, row=5, padx=5, pady=2)
                cell_1_butt_defult_led3=Button(cell_1, text=" ", width =12,fg='white',font = ('tahoma 13 bold')) 
                cell_1_butt_defult_led3.grid(column=11, row=5, padx=5, pady=2)
                cell_1.after(defult_color_delay, lambda: cell_1_butt_defult_led.configure(background="lime green"))
                cell_1.after(result_color_delay, lambda: cell_1_butt_defult_led.configure(background="green"))        

    def cell1_defult_led_b():

                cell_1_butt_defult_led=Button(cell_1, text="Free", width =12,fg='white',bg='green',font = ('tahoma 13 bold')) 
                cell_1_butt_defult_led.grid(column=9, row=6, padx=5, pady=2)
                cell_1_butt_defult_led2=Button(cell_1, text=" ", width =12,fg='white',font = ('tahoma 13 bold')) 
                cell_1_butt_defult_led2.grid(column=10, row=6, padx=5, pady=2)
                cell_1_butt_defult_led3=Button(cell_1, text=" ", width =12,fg='white',font = ('tahoma 13 bold')) 
                cell_1_butt_defult_led3.grid(column=11, row=6, padx=5, pady=2)
                cell_1.after(defult_color_delay, lambda: cell_1_butt_defult_led.configure(background="lime green"))
                cell_1.after(result_color_delay, lambda: cell_1_butt_defult_led.configure(background="green"))   

    def cell1_defult_led_c():

                cell_1_butt_defult_led=Button(cell_1, text="Free", width =12,fg='white',bg='green',font = ('tahoma 13 bold')) 
                cell_1_butt_defult_led.grid(column=9, row=7, padx=5, pady=2)
                cell_1_butt_defult_led2=Button(cell_1, text=" ", width =12,fg='white',font = ('tahoma 13 bold')) 
                cell_1_butt_defult_led2.grid(column=10, row=7, padx=5, pady=2)
                cell_1_butt_defult_led3=Button(cell_1, text=" ", width =12,fg='white',font = ('tahoma 13 bold')) 
                cell_1_butt_defult_led3.grid(column=11, row=7, padx=5, pady=2)
                cell_1.after(defult_color_delay, lambda: cell_1_butt_defult_led.configure(background="lime green"))
                cell_1.after(result_color_delay, lambda: cell_1_butt_defult_led.configure(background="green"))     

    def cell1_defult_led_d():

                cell_1_butt_defult_led=Button(cell_1, text="Free", width =12,fg='white',bg='green',font = ('tahoma 13 bold')) 
                cell_1_butt_defult_led.grid(column=9, row=8, padx=5, pady=2)
                cell_1_butt_defult_led2=Button(cell_1, text=" ", width =12,fg='white',font = ('tahoma 13 bold')) 
                cell_1_butt_defult_led2.grid(column=10, row=8, padx=5, pady=2)
                cell_1_butt_defult_led3=Button(cell_1, text=" ", width =12,fg='white',font = ('tahoma 13 bold')) 
                cell_1_butt_defult_led3.grid(column=11, row=8, padx=5, pady=2)
                cell_1.after(defult_color_delay, lambda: cell_1_butt_defult_led.configure(background="lime green"))
                cell_1.after(result_color_delay, lambda: cell_1_butt_defult_led.configure(background="green"))   
    

cell_1_label=Label(cell_1,text="Start time :",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
cell_1_label.grid(column=2, row=5, padx=8, pady=4)
cell_1_label=Label(cell_1,text="Start time :",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
cell_1_label.grid(column=2, row=6, padx=8, pady=4)
cell_1_label=Label(cell_1,text="Start time :",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
cell_1_label.grid(column=2, row=7, padx=8, pady=4)
cell_1_label=Label(cell_1,text="Start time :",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
cell_1_label.grid(column=2, row=8, padx=8, pady=4)


cell_1_countlb_a=Label(cell_1,text=" ",fg='black',font=("arial", 10))
cell_1_countlb_a.grid(column=20, row=5, padx=8, pady=4)
cell_1_countlb_b=Label(cell_1,text=" ",fg='black',font=("arial", 10))
cell_1_countlb_b.grid(column=20, row=6, padx=8, pady=4)
cell_1_countlb_c=Label(cell_1,text=" ",fg='black',font=("arial", 10))
cell_1_countlb_c.grid(column=20, row=7, padx=8, pady=4)
cell_1_countlb_d=Label(cell_1,text="  ",fg='black',font=("arial", 10))
cell_1_countlb_d.grid(column=20, row=8, padx=8, pady=4)


#!---------------------------------------------------------End cell 1------------------------------------!






tick()
cell_1_main_start()
# cell_1_name_entered.focus()      # Place cursor into name Entry
# Start GUI
#======================
win.mainloop()