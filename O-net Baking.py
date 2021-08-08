
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
from typing import Coroutine, Counter, get_origin

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


Date_stamp = datetime.now().strftime('%H:%M %p')

common_time = ''
clock = Label(win, font=('times', 15))
clock.pack(fill=BOTH, expand=1)

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
    #print(common_time)
    return common_time
    

#!----------------------------------------limit count--------------------------------------------!
countlim_set = 3600 #Sec = 1 hr
#!----------------------------------------limit count--------------------------------------------!
#
defult_color_delay = 500
result_color_delay = 1500


#!----------------------------- cell 1--------------------------------------------
cell1_slot_a = False
cell1_slot_b = False
cell1_slot_c = False
cell1_slot_d = False


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



cell_1_label=Label(cell_1,text="Baking slot B",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
cell_1_label.grid(column=0, row=6, padx=8, pady=4)
cell_1_label=Label(cell_1,text="Baking slot C",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
cell_1_label.grid(column=0, row=7, padx=8, pady=4)
cell_1_label=Label(cell_1,text="Baking slot D",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
cell_1_label.grid(column=0, row=8, padx=8, pady=4)




cell_1_label=Label(cell_1,text="Baking slot A",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
cell_1_label.grid(column=0, row=5, padx=8, pady=4)



def cell_1_main_start():
    global defult_color_delay
    global result_color_delay
    #cell #1 A
    cell1_start_aca = ttk.Button(cell_1,width=12, text="Start A",command= lambda:[cell1_dis_buttom_start_a(True),mes_box_A()])
    cell1_start_aca.grid(column=1, row=5)
    cell1_stop_a = ttk.Button(cell_1,width=12, text="Stop A",command= lambda:[cell1_dis_buttom_start_a(FALSE),cell1_a_stop(True)])
    cell1_stop_a.grid(column=5, row=5,padx=2, pady=2) 
    #cell #1 b
    cell1_start_acb = ttk.Button(cell_1,width=12, text="Start B",command= lambda:[cell1_dis_buttom_start_b(True),mes_box_B()])
    cell1_start_acb.grid(column=1, row=6)
    cell1_stop_b = ttk.Button(cell_1,width=12, text="Stop B",command= lambda:[cell1_dis_buttom_start_b(FALSE),cell1_b_stop(True)])
    cell1_stop_b.grid(column=5, row=6,padx=2, pady=2) 
    #cell #1 c
    cell1_start_acc = ttk.Button(cell_1,width=12, text="Start C",command= lambda:[cell1_dis_buttom_start_c(True),mes_box_C()])
    cell1_start_acc.grid(column=1, row=7)
    cell1_stop_c = ttk.Button(cell_1,width=12, text="Stop C",command= lambda:[cell1_dis_buttom_start_c(FALSE),cell1_c_stop(True)])
    cell1_stop_c.grid(column=5, row=7,padx=2, pady=2) 

    cell1_start_acd = ttk.Button(cell_1,width=12, text="Start D",command= lambda:[cell1_dis_buttom_start_d(True),mes_box_D()])
    cell1_start_acd.grid(column=1, row=8)
    cell1_stop_d = ttk.Button(cell_1,width=12, text="Stop D",command= lambda:[cell1_dis_buttom_start_d(FALSE),cell1_d_stop(True)])
    cell1_stop_d.grid(column=5, row=8,padx=2, pady=2) 


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
            # cell_1_butt=Button(cell_1, text=" ", width =12,fg='white',font = ('tahoma 7 bold'))
            # cell_1_butt.grid(column=9, row=5, padx=0, pady=2)
            
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
        mes_a = messagebox.askokcancel('OK','Please make sure a')
        #print(mes_a)
        if mes_a == True:
            cell1_slot_a_running = True
            start_cell1_a(cell1_slot_a_running)
        else:
            cell1_start_aca['state'] = NORMAL
    
    def mes_box_B():
        global cell1_slot_b_running
        mes_b = messagebox.askokcancel('OK','Please make sure b')
        #print(mes_b)
        if mes_b == True:
            cell1_slot_b_running = True
            start_cell1_b(cell1_slot_b_running)
        else:
            cell1_start_acb['state'] = NORMAL

    def mes_box_C():
        global cell1_slot_c_running
        mes_c = messagebox.askokcancel('OK','Please make sure b')
        #print(mes_c)
        if mes_c == True:
            cell1_slot_c_running = True
            start_cell1_c(cell1_slot_c_running)
        else:
            cell1_start_acc['state'] = NORMAL
        
    def mes_box_D():
        global cell1_slot_d_running
        mes_d = messagebox.askokcancel('OK','Please make sure b')
        #print(mes_d)
        if mes_d == True:
            cell1_slot_d_running = True
            start_cell1_d(cell1_slot_d_running)
        else:
            cell1_start_acd['state'] = NORMAL
        

    def start_cell1_a(cell1_slot_a_running):
        #print ("status cell1_slot_a =",cell1_slot_a)
        cell_1_label=Label(cell_1,text= common_time,fg='black',bg='white',font=("arial", 10))
        cell_1_label.grid(column=3, row=5, padx=8, pady=4)

        def count_a():
            global cell1_slot_a_running
            global cell1_cycle_time_a
            global cell1_slot_a
        
            if cell1_slot_a_running:
                #print('cell1_slot_a_running:',cell1_slot_a_running)
                cell_1_countlb_a.after(1000,count_a)
                cell1_cycle_time_a += 1
                remain_time = cell1_cycle_time_a
                cell_1_countlb_a.config(text=str(cell1_cycle_time_a)) 
                #print("This is remain_time A:",remain_time)
                LED_show_a()
                if cell1_cycle_time_a >= countlim_set :
                    unit_pass()
                return cell1_cycle_time_a
            else :
                cell1_cycle_time_a = 0
                cell_1_countlb_a.config(text=str(cell1_cycle_time_a))
                
                return cell1_cycle_time_a                     
        
        def LED_show_a():
                cell_1_butt=Button(cell_1, text=" ", width =12,fg='white',font = ('tahoma 7 bold'))
                cell_1_butt.grid(column=9, row=5, padx=0, pady=2)
                cell_1_butt=Button(cell_1, text=" ", width =12,bg="Yellow",fg='white',font = ('tahoma 7 bold')) 
                cell_1_butt.grid(column=9, row=5, padx=0, pady=2)
                # cell_1.after(defult_color_delay, lambda: cell_1_butt.configure(background="white"))
                # cell_1.after(result_color_delay, lambda: cell_1_butt.configure(background="yellow"))
        
        def unit_pass():
            cell_1_butt=Button(cell_1, text=" ", width =12,fg='black',font = ('tahoma 7 bold'))
            cell_1_butt.grid(column=9, row=5, padx=0, pady=2)
            cell_1_butt=Button(cell_1, text=" Done ", width =12,bg="lawn green",fg='white',font = ('tahoma 7 bold')) 
            cell_1_butt.grid(column=9, row=5, padx=0, pady=2)
            cell_1.after(defult_color_delay, lambda: cell_1_butt.configure(background="white"))
            cell_1.after(result_color_delay, lambda: cell_1_butt.configure(background="lawn green"))
                
        count_a()

    def start_cell1_b(cell1_slot_b_running):
        #print ("status cell1_slot_b =",cell1_slot_b)
        cell_1_label=Label(cell_1,text= common_time,fg='black',bg='white',font=("arial", 10))
        cell_1_label.grid(column=3, row=6, padx=8, pady=4)
        def count_a():
            global cell1_slot_b_running  # True /False
            global cell1_cycle_time_b
            global cell1_slot_b
        
            if cell1_slot_b_running:
                #print('cell1_slot_b_running:',cell1_slot_b_running)
                cell_1_countlb_b.after(1000,count_a)
                cell1_cycle_time_b += 1
                remain_time = cell1_cycle_time_b
                cell_1_countlb_b.config(text=str(cell1_cycle_time_b)) 
                #print("This is remain_time B:",remain_time)
                LED_show_a()
                if cell1_cycle_time_b >= countlim_set :
                    unit_pass()
                return cell1_cycle_time_b
            else :
                cell1_cycle_time_b = 0
                cell_1_countlb_b.config(text=str(cell1_cycle_time_b))
                
                return cell1_cycle_time_b
                            
        def LED_show_a():
                cell_1_butt=Button(cell_1, text=" ", width =12,fg='white',font = ('tahoma 7 bold'))
                cell_1_butt.grid(column=9, row=6, padx=0, pady=2)
                cell_1_butt=Button(cell_1, text=" ", width =12,bg="Yellow",fg='white',font = ('tahoma 7 bold')) 
                cell_1_butt.grid(column=9, row=6, padx=0, pady=2)
                # cell_1.after(defult_color_delay, lambda: cell_1_butt.configure(background="white"))
                # cell_1.after(result_color_delay, lambda: cell_1_butt.configure(background="yellow"))
        def unit_pass():
            cell_1_butt=Button(cell_1, text=" ", width =12,fg='white',font = ('tahoma 7 bold'))
            cell_1_butt.grid(column=9, row=6, padx=0, pady=2)
            cell_1_butt=Button(cell_1, text=" Done ", width =12,bg="lawn green",fg='white',font = ('tahoma 7 bold')) 
            cell_1_butt.grid(column=9, row=6, padx=0, pady=2)
            cell_1.after(defult_color_delay, lambda: cell_1_butt.configure(background="white"))
            cell_1.after(result_color_delay, lambda: cell_1_butt.configure(background="lawn green"))
                
        count_a()
    
    def start_cell1_c(cell1_slot_c_running):
        #print ("status cell1_slot_c =",cell1_slot_c_running)
        cell_1_label=Label(cell_1,text= common_time,fg='black',bg='white',font=("arial", 10))   # start time label
        cell_1_label.grid(column=3, row=7, padx=8, pady=4)
        def count_a():
            global cell1_slot_c_running  # True /False
            global cell1_cycle_time_c
            global cell1_slot_c
        
            if cell1_slot_c_running:
                #print('cell1_slot_c_running:',cell1_slot_c_running)
                cell_1_countlb_c.after(1000,count_a)
                cell1_cycle_time_c += 1
                remain_time = cell1_cycle_time_c
                cell_1_countlb_c.config(text=str(cell1_cycle_time_c)) 
                ####print("This is remain_time c:",remain_time)
                LED_show_a()
                if cell1_cycle_time_c >= countlim_set :
                    unit_pass()
                return cell1_cycle_time_c
            else :
                cell1_cycle_time_c = 0
                cell_1_countlb_c.config(text=str(cell1_cycle_time_c))
                
                return cell1_cycle_time_c
                            
        def LED_show_a():
                cell_1_butt=Button(cell_1, text=" ", width =12,fg='white',font = ('tahoma 7 bold'))
                cell_1_butt.grid(column=9, row=7, padx=0, pady=2)
                cell_1_butt=Button(cell_1, text=" ", width =12,bg="Yellow",fg='white',font = ('tahoma 7 bold')) 
                cell_1_butt.grid(column=9, row=7, padx=0, pady=2)
                # cell_1.after(defult_color_delay, lambda: cell_1_butt.configure(background="white"))
                # cell_1.after(result_color_delay, lambda: cell_1_butt.configure(background="yellow"))
        def unit_pass():
            cell_1_butt=Button(cell_1, text=" ", width =12,fg='white',font = ('tahoma 7 bold'))
            cell_1_butt.grid(column=9, row=7, padx=0, pady=2)
            cell_1_butt=Button(cell_1, text=" Done ", width =12,bg="lawn green",fg='white',font = ('tahoma 7 bold')) 
            cell_1_butt.grid(column=9, row=7, padx=0, pady=2)
            cell_1.after(defult_color_delay, lambda: cell_1_butt.configure(background="white"))
            cell_1.after(result_color_delay, lambda: cell_1_butt.configure(background="lawn green"))
                
        count_a()
    
    def start_cell1_d(cell1_slot_d_running):
        ##print ("status cell1_slot_c =",cell1_slot_d_running)
        cell_1_label=Label(cell_1,text= common_time,fg='black',bg='white',font=("arial", 10))   # start time label
        cell_1_label.grid(column=3, row=8, padx=8, pady=4)
        def count_a():
            global cell1_slot_d_running  # True /False
            global cell1_cycle_time_d
            global cell1_slot_d
        
            if cell1_slot_d_running:
                ##print('cell1_slot_d_running:',cell1_slot_d_running)
                cell_1_countlb_d.after(1000,count_a)
                cell1_cycle_time_d += 1
                remain_time = cell1_cycle_time_d
                cell_1_countlb_d.config(text=str(cell1_cycle_time_d)) 
                #####print("This is remain_time c:",remain_time)
                LED_show_a()
                if cell1_cycle_time_d >= countlim_set :
                    unit_pass()
                return cell1_cycle_time_d
            else :
                cell1_cycle_time_d = 0
                cell_1_countlb_d.config(text=str(cell1_cycle_time_d))
                
                return cell1_cycle_time_d
                            
        def LED_show_a():
                cell_1_butt=Button(cell_1, text=" ", width =12,fg='white',font = ('tahoma 7 bold'))
                cell_1_butt.grid(column=9, row=8, padx=0, pady=2)
                cell_1_butt=Button(cell_1, text=" ", width =12,bg="Yellow",fg='white',font = ('tahoma 7 bold')) 
                cell_1_butt.grid(column=9, row=8, padx=0, pady=2)
                # cell_1.after(defult_color_delay, lambda: cell_1_butt.configure(background="white"))
                # cell_1.after(result_color_delay, lambda: cell_1_butt.configure(background="yellow"))
        def unit_pass():
            cell_1_butt=Button(cell_1, text=" ", width =12,fg='white',font = ('tahoma 7 bold'))
            cell_1_butt.grid(column=9, row=8, padx=0, pady=2)
            cell_1_butt=Button(cell_1, text=" Done ", width =12,bg="lawn green",fg='white',font = ('tahoma 7 bold')) 
            cell_1_butt.grid(column=9, row=8, padx=0, pady=2)
            # cell_1.after(defult_color_delay, lambda: cell_1_butt.configure(background="white"))
            # cell_1.after(result_color_delay, lambda: cell_1_butt.configure(background="lawn green"))
                
        count_a()
    

cell_1_label=Label(cell_1,text="Start time :",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
cell_1_label.grid(column=2, row=5, padx=8, pady=4)
cell_1_label=Label(cell_1,text="Start time :",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
cell_1_label.grid(column=2, row=6, padx=8, pady=4)
cell_1_label=Label(cell_1,text="Start time :",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
cell_1_label.grid(column=2, row=7, padx=8, pady=4)
cell_1_label=Label(cell_1,text="Start time :",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
cell_1_label.grid(column=2, row=8, padx=8, pady=4)



cell_1_countlb_a=Label(cell_1,text=" ",fg='black',bg='white',font=("arial", 10))
cell_1_countlb_a.grid(column=4, row=5, padx=8, pady=4)
cell_1_countlb_b=Label(cell_1,text=" ",fg='black',bg='white',font=("arial", 10))
cell_1_countlb_b.grid(column=4, row=6, padx=8, pady=4)
cell_1_countlb_c=Label(cell_1,text=" ",fg='black',bg='white',font=("arial", 10))
cell_1_countlb_c.grid(column=4, row=7, padx=8, pady=4)
cell_1_countlb_d=Label(cell_1,text=" ",fg='black',bg='white',font=("arial", 10))
cell_1_countlb_d.grid(column=4, row=8, padx=8, pady=4)


#!---------------------------------------------------------End cell 1------------------------------------!

#!-------------------------------------------------------- cell 2--------------------------------------------
cell2_slot_a = False
cell2_slot_b = False
cell2_slot_c = False
cell2_slot_d = False

cell2_cycle_time_a = 0
cell2_cycle_time_b = 0
cell2_cycle_time_c = 0
cell2_cycle_time_d = 0

remain_time = 0

cell2_slot_a_running = False
cell2_slot_b_running = False
cell2_slot_c_running = False
cell2_slot_d_running = False


#--------------------------------------------------------------

cell_2 = ttk.LabelFrame(tab1, text=' Cell_2')
cell_2.grid(column=0, row=2, padx=8, pady=4)   

# cell_2_name = tk.StringVar()
# cell_2_name_entered = ttk.Entry(cell_2, width=12, textvariable=cell_2_name)
# cell_2_name_entered.grid(column=0, row=1, sticky='W')



cell_2_label=Label(cell_2,text="Baking slot A",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
cell_2_label.grid(column=0, row=5, padx=8, pady=4)
cell_2_label=Label(cell_2,text="Baking slot B",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
cell_2_label.grid(column=0, row=6, padx=8, pady=4)
cell_2_label=Label(cell_2,text="Baking slot C",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
cell_2_label.grid(column=0, row=7, padx=8, pady=4)
cell_2_label=Label(cell_2,text="Baking slot D",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
cell_2_label.grid(column=0, row=8, padx=8, pady=4)





def cell_2_main_start():
    global result_color_delay
    global defult_color_delay
    #cell #1 A
    cell2_start_aca = ttk.Button(cell_2,width=12, text="Start A",command= lambda:[cell2_dis_buttom_start_a(True),mes_box_A()])
    cell2_start_aca.grid(column=1, row=5)
    cell2_stop_a = ttk.Button(cell_2,width=12, text="Stop A",command= lambda:[cell2_dis_buttom_start_a(FALSE),cell2_a_stop(True)])
    cell2_stop_a.grid(column=5, row=5,padx=2, pady=2) 
    #cell #1 b
    cell2_start_acb = ttk.Button(cell_2,width=12, text="Start B",command= lambda:[cell2_dis_buttom_start_b(True),mes_box_B()])
    cell2_start_acb.grid(column=1, row=6)
    cell2_stop_b = ttk.Button(cell_2,width=12, text="Stop B",command= lambda:[cell2_dis_buttom_start_b(FALSE),cell2_b_stop(True)])
    cell2_stop_b.grid(column=5, row=6,padx=2, pady=2) 
    #cell #1 c
    cell2_start_acc = ttk.Button(cell_2,width=12, text="Start C",command= lambda:[cell2_dis_buttom_start_c(True),mes_box_C()])
    cell2_start_acc.grid(column=1, row=7)
    cell2_stop_c = ttk.Button(cell_2,width=12, text="Stop C",command= lambda:[cell2_dis_buttom_start_c(FALSE),cell2_c_stop(True)])
    cell2_stop_c.grid(column=5, row=7,padx=2, pady=2) 

    cell2_start_acd = ttk.Button(cell_2,width=12, text="Start D",command= lambda:[cell2_dis_buttom_start_d(True),mes_box_D()])
    cell2_start_acd.grid(column=1, row=8)
    cell2_stop_d = ttk.Button(cell_2,width=12, text="Stop D",command= lambda:[cell2_dis_buttom_start_d(FALSE),cell2_d_stop(True)])
    cell2_stop_d.grid(column=5, row=8,padx=2, pady=2) 


    def cell2_dis_buttom_start_a(status_butt):
        if status_butt == True:
            cell2_start_aca['state'] = DISABLED
            cell2_slot_a = True
            return  cell2_slot_a
        elif status_butt == FALSE :
            cell2_start_aca['state'] = NORMAL

    def cell2_dis_buttom_start_b(status_butt):
        if status_butt == True:
            cell2_start_acb['state'] = DISABLED
            cell2_slot_b = True
            return  cell2_slot_b
        elif status_butt == FALSE :
            cell2_start_acb['state'] = NORMAL

    def cell2_dis_buttom_start_c(status_butt):
        if status_butt == True:
            cell2_start_acc['state'] = DISABLED
            cell2_slot_c = True
            return  cell2_slot_c
        elif status_butt == FALSE :
            cell2_start_acc['state'] = NORMAL
    
    def cell2_dis_buttom_start_d(status_butt):
        if status_butt == True:
            cell2_start_acd['state'] = DISABLED
            cell2_slot_d = True
            return  cell2_slot_d
        elif status_butt == FALSE :
            cell2_start_acd['state'] = NORMAL
        
        


    def cell2_a_stop(stop_butt):
        global cell2_slot_a_running
        if stop_butt == True :
            cell2_slot_a_running = False
            cell2_cycle_time_a = 0
            start_cell2_a(cell2_slot_a_running)
            
            return cell2_cycle_time_a

    def cell2_b_stop(stop_butt):
        global cell2_slot_b_running
        if stop_butt == True :
            cell2_slot_b_running = False
            cell2_cycle_time_b = 0
            start_cell2_b(cell2_slot_b_running)
            
            return cell2_cycle_time_b

    def cell2_c_stop(stop_butt):
        global cell2_slot_c_running
        if stop_butt == True :
            cell2_slot_c_running = False
            cell2_cycle_time_c = 0
            start_cell2_c(cell2_slot_c_running)
            
            return cell2_cycle_time_c

    def cell2_d_stop(stop_butt):
        global cell2_slot_d_running
        if stop_butt == True :
            cell2_slot_d_running = False
            cell2_cycle_time_d = 0
            start_cell2_d(cell2_slot_d_running)
            
            return cell2_cycle_time_d

            

    def mes_box_A():
        global cell2_slot_a_running
        mes_a = messagebox.askokcancel('OK','Please make sure a')
        ##print(mes_a)
        if mes_a == True:
            cell2_slot_a_running = True
            start_cell2_a(cell2_slot_a_running)
        else:
            cell2_start_aca['state'] = NORMAL
    
    def mes_box_B():
        global cell2_slot_b_running
        mes_b = messagebox.askokcancel('OK','Please make sure b')
        ##print(mes_b)
        if mes_b == True:
            cell2_slot_b_running = True
            start_cell2_b(cell2_slot_b_running)
        else:
            cell2_start_acb['state'] = NORMAL

    def mes_box_C():
        global cell2_slot_c_running
        mes_c = messagebox.askokcancel('OK','Please make sure b')
        ##print(mes_c)
        if mes_c == True:
            cell2_slot_c_running = True
            start_cell2_c(cell2_slot_c_running)
        else:
            cell2_start_acc['state'] = NORMAL
        
    def mes_box_D():
        global cell2_slot_d_running
        mes_d = messagebox.askokcancel('OK','Please make sure b')
        ##print(mes_d)
        if mes_d == True:
            cell2_slot_d_running = True
            start_cell2_d(cell2_slot_d_running)
        else:
            cell2_start_acd['state'] = NORMAL
        

    def start_cell2_a(cell2_slot_a_running):
        ##print ("status cell2_slot_a =",cell2_slot_a)
        cell_2_label=Label(cell_2,text= common_time,fg='black',bg='white',font=("arial", 10))
        cell_2_label.grid(column=3, row=5, padx=8, pady=4)

        def count_a():
            global cell2_slot_a_running
            global cell2_cycle_time_a
            global cell2_slot_a
        
            if cell2_slot_a_running:
                ##print('cell2_slot_a_running:',cell2_slot_a_running)
                cell_2_countlb_a.after(1000,count_a)
                cell2_cycle_time_a += 1
                remain_time = cell2_cycle_time_a
                cell_2_countlb_a.config(text=str(cell2_cycle_time_a)) 
                ##print("This is remain_time A:",remain_time)
                LED_show_a()
                if cell2_cycle_time_a >= countlim_set :
                    unit_pass()
                return cell2_cycle_time_a
            else :
                cell2_cycle_time_a = 0
                cell_2_countlb_a.config(text=str(cell2_cycle_time_a))
                
                return cell2_cycle_time_a                     
        
        def LED_show_a():
                cell_2_butt=Button(cell_2, text=" ", width =12,fg='white',font = ('tahoma 7 bold'))
                cell_2_butt.grid(column=9, row=5, padx=0, pady=2)
                cell_2_butt=Button(cell_2, text=" ", width =12,bg="Yellow",fg='white',font = ('tahoma 7 bold')) 
                cell_2_butt.grid(column=9, row=5, padx=0, pady=2)
                # cell_2.after(defult_color_delay, lambda: cell_2_butt.configure(background="white"))
                # cell_2.after(result_color_delay, lambda: cell_2_butt.configure(background="yellow"))
        
        def unit_pass():
            cell_2_butt=Button(cell_2, text=" ", width =12,fg='white',font = ('tahoma 7 bold'))
            cell_2_butt.grid(column=9, row=5, padx=0, pady=2)
            cell_2_butt=Button(cell_2, text=" Done ", width =12,bg="lawn green",fg='white',font = ('tahoma 7 bold')) 
            cell_2_butt.grid(column=9, row=5, padx=0, pady=2)
            cell_2.after(defult_color_delay, lambda: cell_2_butt.configure(background="white"))
            cell_2.after(result_color_delay, lambda: cell_2_butt.configure(background="lawn green"))
                
        count_a()

    def start_cell2_b(cell2_slot_b_running):
        ##print ("status cell2_slot_b =",cell2_slot_b)
        cell_2_label=Label(cell_2,text= common_time,fg='black',bg='white',font=("arial", 10))
        cell_2_label.grid(column=3, row=6, padx=8, pady=4)
        def count_a():
            global cell2_slot_b_running  # True /False
            global cell2_cycle_time_b
            global cell2_slot_b
        
            if cell2_slot_b_running:
                ##print('cell2_slot_b_running:',cell2_slot_b_running)
                cell_2_countlb_b.after(1000,count_a)
                cell2_cycle_time_b += 1
                remain_time = cell2_cycle_time_b
                cell_2_countlb_b.config(text=str(cell2_cycle_time_b)) 
                ##print("This is remain_time B:",remain_time)
                LED_show_a()
                if cell2_cycle_time_b >= countlim_set :
                    unit_pass()
                return cell2_cycle_time_b
            else :
                cell2_cycle_time_b = 0
                cell_2_countlb_b.config(text=str(cell2_cycle_time_b))
                
                return cell2_cycle_time_b
                            
        def LED_show_a():
                cell_2_butt=Button(cell_2, text=" ", width =12,fg='white',font = ('tahoma 7 bold'))
                cell_2_butt.grid(column=9, row=6, padx=0, pady=2)
                cell_2_butt=Button(cell_2, text=" ", width =12,bg="Yellow",fg='white',font = ('tahoma 7 bold')) 
                cell_2_butt.grid(column=9, row=6, padx=0, pady=2)
                # cell_2.after(defult_color_delay, lambda: cell_2_butt.configure(background="white"))
                # cell_2.after(result_color_delay, lambda: cell_2_butt.configure(background="yellow"))
        def unit_pass():
            cell_2_butt=Button(cell_2, text=" ", width =12,fg='white',font = ('tahoma 7 bold'))
            cell_2_butt.grid(column=9, row=6, padx=0, pady=2)
            cell_2_butt=Button(cell_2, text=" Done ", width =12,bg="lawn green",fg='white',font = ('tahoma 7 bold')) 
            cell_2_butt.grid(column=9, row=6, padx=0, pady=2)
            cell_2.after(defult_color_delay, lambda: cell_2_butt.configure(background="white"))
            cell_2.after(result_color_delay, lambda: cell_2_butt.configure(background="lawn green"))
                
        count_a()
    
    def start_cell2_c(cell2_slot_c_running):
        ##print ("status cell2_slot_c =",cell2_slot_c_running)
        cell_2_label=Label(cell_2,text= common_time,fg='black',bg='white',font=("arial", 10))   # start time label
        cell_2_label.grid(column=3, row=7, padx=8, pady=4)
        def count_a():
            global cell2_slot_c_running  # True /False
            global cell2_cycle_time_c
            global cell2_slot_c
        
            if cell2_slot_c_running:
                ##print('cell2_slot_c_running:',cell2_slot_c_running)
                cell_2_countlb_c.after(1000,count_a)
                cell2_cycle_time_c += 1
                remain_time = cell2_cycle_time_c
                cell_2_countlb_c.config(text=str(cell2_cycle_time_c)) 
                #####print("This is remain_time c:",remain_time)
                LED_show_a()
                if cell2_cycle_time_c >= countlim_set :
                    unit_pass()
                return cell2_cycle_time_c
            else :
                cell2_cycle_time_c = 0
                cell_2_countlb_c.config(text=str(cell2_cycle_time_c))
                
                return cell2_cycle_time_c
                            
        def LED_show_a():
                cell_2_butt=Button(cell_2, text=" ", width =12,fg='white',font = ('tahoma 7 bold'))
                cell_2_butt.grid(column=9, row=7, padx=0, pady=2)
                cell_2_butt=Button(cell_2, text=" ", width =12,bg="Yellow",fg='white',font = ('tahoma 7 bold')) 
                cell_2_butt.grid(column=9, row=7, padx=0, pady=2)
                # cell_2.after(defult_color_delay, lambda: cell_2_butt.configure(background="white"))
                # cell_2.after(result_color_delay, lambda: cell_2_butt.configure(background="yellow"))
        def unit_pass():
            cell_2_butt=Button(cell_2, text=" ", width =12,fg='white',font = ('tahoma 7 bold'))
            cell_2_butt.grid(column=9, row=7, padx=0, pady=2)
            cell_2_butt=Button(cell_2, text=" Done ", width =12,bg="lawn green",fg='white',font = ('tahoma 7 bold')) 
            cell_2_butt.grid(column=9, row=7, padx=0, pady=2)
            cell_2.after(defult_color_delay, lambda: cell_2_butt.configure(background="white"))
            cell_2.after(result_color_delay, lambda: cell_2_butt.configure(background="lawn green"))
                
        count_a()
    
    def start_cell2_d(cell2_slot_d_running):
        ##print ("status cell2_slot_c =",cell2_slot_d_running)
        cell_2_label=Label(cell_2,text= common_time,fg='black',bg='white',font=("arial", 10))   # start time label
        cell_2_label.grid(column=3, row=8, padx=8, pady=4)
        def count_a():
            global cell2_slot_d_running  # True /False
            global cell2_cycle_time_d
            global cell2_slot_d
        
            if cell2_slot_d_running:
                ##print('cell2_slot_d_running:',cell2_slot_d_running)
                cell_2_countlb_d.after(1000,count_a)
                cell2_cycle_time_d += 1
                remain_time = cell2_cycle_time_d
                cell_2_countlb_d.config(text=str(cell2_cycle_time_d)) 
                #####print("This is remain_time c:",remain_time)
                LED_show_a()
                if cell2_cycle_time_d >= countlim_set :
                    unit_pass()
                return cell2_cycle_time_d
            else :
                cell2_cycle_time_d = 0
                cell_2_countlb_d.config(text=str(cell2_cycle_time_d))
                
                return cell2_cycle_time_d
                            
        def LED_show_a():
                cell_2_butt=Button(cell_2, text=" ", width =12,fg='white',font = ('tahoma 7 bold'))
                cell_2_butt.grid(column=9, row=8, padx=0, pady=2)
                cell_2_butt=Button(cell_2, text=" ", width =12,bg="Yellow",fg='white',font = ('tahoma 7 bold')) 
                cell_2_butt.grid(column=9, row=8, padx=0, pady=2)
                # cell_2.after(defult_color_delay, lambda: cell_2_butt.configure(background="white"))
                # cell_2.after(result_color_delay, lambda: cell_2_butt.configure(background="yellow"))
        def unit_pass():
            cell_2_butt=Button(cell_2, text=" ", width =12,fg='white',font = ('tahoma 7 bold'))
            cell_2_butt.grid(column=9, row=8, padx=0, pady=2)
            cell_2_butt=Button(cell_2, text=" Done ", width =12,bg="lawn green",fg='white',font = ('tahoma 7 bold')) 
            cell_2_butt.grid(column=9, row=8, padx=0, pady=2)
            cell_2.after(defult_color_delay, lambda: cell_2_butt.configure(background="white"))
            cell_2.after(result_color_delay, lambda: cell_2_butt.configure(background="lawn green"))
                
        count_a()
    


#!----------cell Mess box

cell_2_label=Label(cell_2,text="Start time :",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
cell_2_label.grid(column=2, row=5, padx=8, pady=4)
cell_2_label=Label(cell_2,text="Start time :",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
cell_2_label.grid(column=2, row=6, padx=8, pady=4)
cell_2_label=Label(cell_2,text="Start time :",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
cell_2_label.grid(column=2, row=7, padx=8, pady=4)
cell_2_label=Label(cell_2,text="Start time :",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
cell_2_label.grid(column=2, row=8, padx=8, pady=4)


cell_2_countlb_a=Label(cell_2,text=" ",fg='black',bg='white',font=("arial", 10))
cell_2_countlb_a.grid(column=4, row=5, padx=8, pady=4)
cell_2_countlb_b=Label(cell_2,text=" ",fg='black',bg='white',font=("arial", 10))
cell_2_countlb_b.grid(column=4, row=6, padx=8, pady=4)
cell_2_countlb_c=Label(cell_2,text=" ",fg='black',bg='white',font=("arial", 10))
cell_2_countlb_c.grid(column=4, row=7, padx=8, pady=4)
cell_2_countlb_d=Label(cell_2,text=" ",fg='black',bg='white',font=("arial", 10))
cell_2_countlb_d.grid(column=4, row=8, padx=8, pady=4)



#!------------------------------------------------------------------End cell 2----------------------------!

#!-------------------------------------------------------- cell 3--------------------------------------------
cell3_slot_a = False
cell3_slot_b = False
cell3_slot_c = False
cell3_slot_d = False


cell3_cycle_time_a = 0
cell3_cycle_time_b = 0
cell3_cycle_time_c = 0
cell3_cycle_time_d = 0

remain_time = 0


cell3_slot_a_running = False
cell3_slot_b_running = False
cell3_slot_c_running = False
cell3_slot_d_running = False


#--------------------------------------------------------------

cell_3 = ttk.LabelFrame(tab1, text=' Cell_3')
cell_3.grid(column=0, row=3, padx=8, pady=4)   

# cell_3_name = tk.StringVar()
# cell_3_name_entered = ttk.Entry(cell_3, width=12, textvariable=cell_3_name)
# cell_3_name_entered.grid(column=0, row=1, sticky='W')






def cell_3_main_start():
        
    cell_3_label=Label(cell_3,text="Baking slot A",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
    cell_3_label.grid(column=0, row=5, padx=8, pady=4)
    cell_3_label=Label(cell_3,text="Baking slot B",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
    cell_3_label.grid(column=0, row=6, padx=8, pady=4)
    cell_3_label=Label(cell_3,text="Baking slot C",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
    cell_3_label.grid(column=0, row=7, padx=8, pady=4)
    cell_3_label=Label(cell_3,text="Baking slot D",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
    cell_3_label.grid(column=0, row=8, padx=8, pady=4)

    
    cell_3_label=Label(cell_3,text="Start time :",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
    cell_3_label.grid(column=2, row=5, padx=8, pady=4)
    cell_3_label=Label(cell_3,text="Start time :",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
    cell_3_label.grid(column=2, row=6, padx=8, pady=4)
    cell_3_label=Label(cell_3,text="Start time :",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
    cell_3_label.grid(column=2, row=7, padx=8, pady=4)
    cell_3_label=Label(cell_3,text="Start time :",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
    cell_3_label.grid(column=2, row=8, padx=8, pady=4)




    cell_3_countlb_a=Label(cell_3,text=" ",fg='black',bg='white',font=("arial", 10))
    cell_3_countlb_a.grid(column=4, row=5, padx=8, pady=4)
    cell_3_countlb_b=Label(cell_3,text=" ",fg='black',bg='white',font=("arial", 10))
    cell_3_countlb_b.grid(column=4, row=6, padx=8, pady=4)
    cell_3_countlb_c=Label(cell_3,text=" ",fg='black',bg='white',font=("arial", 10))
    cell_3_countlb_c.grid(column=4, row=7, padx=8, pady=4)
    cell_3_countlb_d=Label(cell_3,text=" ",fg='black',bg='white',font=("arial", 10))
    cell_3_countlb_d.grid(column=4, row=8, padx=8, pady=4)


    #cell #1 A
    cell3_start_aca = ttk.Button(cell_3,width=12, text="Start A",command= lambda:[cell3_dis_buttom_start_a(True),mes_box_A()])
    cell3_start_aca.grid(column=1, row=5)
    cell3_stop_a = ttk.Button(cell_3,width=12, text="Stop A",command= lambda:[cell3_dis_buttom_start_a(FALSE),cell3_a_stop(True)])
    cell3_stop_a.grid(column=5, row=5,padx=2, pady=2) 
    #cell #1 b
    cell3_start_acb = ttk.Button(cell_3,width=12, text="Start B",command= lambda:[cell3_dis_buttom_start_b(True),mes_box_B()])
    cell3_start_acb.grid(column=1, row=6)
    cell3_stop_b = ttk.Button(cell_3,width=12, text="Stop B",command= lambda:[cell3_dis_buttom_start_b(FALSE),cell3_b_stop(True)])
    cell3_stop_b.grid(column=5, row=6,padx=2, pady=2) 
    #cell #1 c
    cell3_start_acc = ttk.Button(cell_3,width=12, text="Start C",command= lambda:[cell3_dis_buttom_start_c(True),mes_box_C()])
    cell3_start_acc.grid(column=1, row=7)
    cell3_stop_c = ttk.Button(cell_3,width=12, text="Stop C",command= lambda:[cell3_dis_buttom_start_c(FALSE),cell3_c_stop(True)])
    cell3_stop_c.grid(column=5, row=7,padx=2, pady=2) 

    cell3_start_acd = ttk.Button(cell_3,width=12, text="Start D",command= lambda:[cell3_dis_buttom_start_d(True),mes_box_D()])
    cell3_start_acd.grid(column=1, row=8)
    cell3_stop_d = ttk.Button(cell_3,width=12, text="Stop D",command= lambda:[cell3_dis_buttom_start_d(FALSE),cell3_d_stop(True)])
    cell3_stop_d.grid(column=5, row=8,padx=2, pady=2) 


    def cell3_dis_buttom_start_a(status_butt):
        if status_butt == True:
            cell3_start_aca['state'] = DISABLED
            cell3_slot_a = True
            return  cell3_slot_a
        elif status_butt == FALSE :
            cell3_start_aca['state'] = NORMAL

    def cell3_dis_buttom_start_b(status_butt):
        if status_butt == True:
            cell3_start_acb['state'] = DISABLED
            cell3_slot_b = True
            return  cell3_slot_b
        elif status_butt == FALSE :
            cell3_start_acb['state'] = NORMAL

    def cell3_dis_buttom_start_c(status_butt):
        if status_butt == True:
            cell3_start_acc['state'] = DISABLED
            cell3_slot_c = True
            return  cell3_slot_c
        elif status_butt == FALSE :
            cell3_start_acc['state'] = NORMAL
    
    def cell3_dis_buttom_start_d(status_butt):
        if status_butt == True:
            cell3_start_acd['state'] = DISABLED
            cell3_slot_d = True
            return  cell3_slot_d
        elif status_butt == FALSE :
            cell3_start_acd['state'] = NORMAL
        
        


    def cell3_a_stop(stop_butt):
        global cell3_slot_a_running
        if stop_butt == True :
            cell3_slot_a_running = False
            cell3_cycle_time_a = 0
            start_cell3_a(cell3_slot_a_running)
            
            return cell3_cycle_time_a

    def cell3_b_stop(stop_butt):
        global cell3_slot_b_running
        if stop_butt == True :
            cell3_slot_b_running = False
            cell3_cycle_time_b = 0
            start_cell3_b(cell3_slot_b_running)
            
            return cell3_cycle_time_b

    def cell3_c_stop(stop_butt):
        global cell3_slot_c_running
        if stop_butt == True :
            cell3_slot_c_running = False
            cell3_cycle_time_c = 0
            start_cell3_c(cell3_slot_c_running)
            
            return cell3_cycle_time_c

    def cell3_d_stop(stop_butt):
        global cell3_slot_d_running
        if stop_butt == True :
            cell3_slot_d_running = False
            cell3_cycle_time_d = 0
            start_cell3_d(cell3_slot_d_running)
            
            return cell3_cycle_time_d

            

    def mes_box_A():
        global cell3_slot_a_running
        mes_a = messagebox.askokcancel('OK','Please make sure a')
        ##print(mes_a)
        if mes_a == True:
            cell3_slot_a_running = True
            start_cell3_a(cell3_slot_a_running)
        else:
            cell3_start_aca['state'] = NORMAL
    
    def mes_box_B():
        global cell3_slot_b_running
        mes_b = messagebox.askokcancel('OK','Please make sure b')
        ##print(mes_b)
        if mes_b == True:
            cell3_slot_b_running = True
            start_cell3_b(cell3_slot_b_running)
        else:
            cell3_start_acb['state'] = NORMAL

    def mes_box_C():
        global cell3_slot_c_running
        mes_c = messagebox.askokcancel('OK','Please make sure b')
        ##print(mes_c)
        if mes_c == True:
            cell3_slot_c_running = True
            start_cell3_c(cell3_slot_c_running)
        else:
            cell3_start_acc['state'] = NORMAL
        
    def mes_box_D():
        global cell3_slot_d_running
        mes_d = messagebox.askokcancel('OK','Please make sure b')
        ##print(mes_d)
        if mes_d == True:
            cell3_slot_d_running = True
            start_cell3_d(cell3_slot_d_running)
        else:
            cell3_start_acd['state'] = NORMAL
        

    def start_cell3_a(cell3_slot_a_running):
        ##print ("status cell3_slot_a =",cell3_slot_a)
        cell_3_label=Label(cell_3,text= common_time,fg='black',bg='white',font=("arial", 10))
        cell_3_label.grid(column=3, row=5, padx=8, pady=4)

        def count_a():
            global cell3_slot_a_running
            global cell3_cycle_time_a
            global cell3_slot_a
        
            if cell3_slot_a_running:
                ##print('cell3_slot_a_running:',cell3_slot_a_running)
                cell_3_countlb_a.after(1000,count_a)
                cell3_cycle_time_a += 1
                remain_time = cell3_cycle_time_a
                cell_3_countlb_a.config(text=str(cell3_cycle_time_a)) 
                ##print("This is remain_time A:",remain_time)
                LED_show_a()
                if cell3_cycle_time_a >= countlim_set :
                    unit_pass()
                return cell3_cycle_time_a
            else :
                cell3_cycle_time_a = 0
                cell_3_countlb_a.config(text=str(cell3_cycle_time_a))
                
                return cell3_cycle_time_a                     
        
        def LED_show_a():
                cell_3_butt=Button(cell_3, text=" ", width =12,fg='white',font = ('tahoma 7 bold'))
                cell_3_butt.grid(column=9, row=5, padx=0, pady=2)
                cell_3_butt=Button(cell_3, text=" ", width =12,bg="Yellow",fg='white',font = ('tahoma 7 bold')) 
                cell_3_butt.grid(column=9, row=5, padx=0, pady=2)
                # cell_3.after(defult_color_delay, lambda: cell_3_butt.configure(background="white"))
                # cell_3.after(result_color_delay, lambda: cell_3_butt.configure(background="yellow"))
        
        def unit_pass():
            cell_3_butt=Button(cell_3, text=" ", width =12,fg='white',font = ('tahoma 7 bold'))
            cell_3_butt.grid(column=9, row=5, padx=0, pady=2)
            cell_3_butt=Button(cell_3, text=" Done ", width =12,bg="lawn green",fg='white',font = ('tahoma 7 bold')) 
            cell_3_butt.grid(column=9, row=5, padx=0, pady=2)
            cell_3.after(defult_color_delay, lambda: cell_3_butt.configure(background="white"))
            cell_3.after(result_color_delay, lambda: cell_3_butt.configure(background="lawn green"))
                
        count_a()

    def start_cell3_b(cell3_slot_b_running):
        ##print ("status cell3_slot_b =",cell3_slot_b)
        cell_3_label=Label(cell_3,text= common_time,fg='black',bg='white',font=("arial", 10))
        cell_3_label.grid(column=3, row=6, padx=8, pady=4)
        def count_a():
            global cell3_slot_b_running  # True /False
            global cell3_cycle_time_b
            global cell3_slot_b
        
            if cell3_slot_b_running:
                ##print('cell3_slot_b_running:',cell3_slot_b_running)
                cell_3_countlb_b.after(1000,count_a)
                cell3_cycle_time_b += 1
                remain_time = cell3_cycle_time_b
                cell_3_countlb_b.config(text=str(cell3_cycle_time_b)) 
                ##print("This is remain_time B:",remain_time)
                LED_show_a()
                if cell3_cycle_time_b >= countlim_set :
                    unit_pass()
                return cell3_cycle_time_b
            else :
                cell3_cycle_time_b = 0
                cell_3_countlb_b.config(text=str(cell3_cycle_time_b))
                
                return cell3_cycle_time_b
                            
        def LED_show_a():
                cell_3_butt=Button(cell_3, text=" ", width =12,fg='white',font = ('tahoma 7 bold'))
                cell_3_butt.grid(column=9, row=6, padx=0, pady=2)
                cell_3_butt=Button(cell_3, text=" ", width =12,bg="Yellow",fg='white',font = ('tahoma 7 bold')) 
                cell_3_butt.grid(column=9, row=6, padx=0, pady=2)
                # cell_3.after(defult_color_delay, lambda: cell_3_butt.configure(background="white"))
                # cell_3.after(result_color_delay, lambda: cell_3_butt.configure(background="yellow"))
        def unit_pass():
            cell_3_butt=Button(cell_3, text=" ", width =12,fg='white',font = ('tahoma 7 bold'))
            cell_3_butt.grid(column=9, row=6, padx=0, pady=2)
            cell_3_butt=Button(cell_3, text=" Done ", width =12,bg="lawn green",fg='white',font = ('tahoma 7 bold')) 
            cell_3_butt.grid(column=9, row=6, padx=0, pady=2)
            cell_3.after(defult_color_delay, lambda: cell_3_butt.configure(background="white"))
            cell_3.after(result_color_delay, lambda: cell_3_butt.configure(background="lawn green"))
                
        count_a()
    
    def start_cell3_c(cell3_slot_c_running):
        ##print ("status cell3_slot_c =",cell3_slot_c_running)
        cell_3_label=Label(cell_3,text= common_time,fg='black',bg='white',font=("arial", 10))   # start time label
        cell_3_label.grid(column=3, row=7, padx=8, pady=4)
        def count_a():
            global cell3_slot_c_running  # True /False
            global cell3_cycle_time_c
            global cell3_slot_c
        
            if cell3_slot_c_running:
                ##print('cell3_slot_c_running:',cell3_slot_c_running)
                cell_3_countlb_c.after(1000,count_a)
                cell3_cycle_time_c += 1
                remain_time = cell3_cycle_time_c
                cell_3_countlb_c.config(text=str(cell3_cycle_time_c)) 
                #####print("This is remain_time c:",remain_time)
                LED_show_a()
                if cell3_cycle_time_c >= countlim_set :
                    unit_pass()
                return cell3_cycle_time_c
            else :
                cell3_cycle_time_c = 0
                cell_3_countlb_c.config(text=str(cell3_cycle_time_c))
                
                return cell3_cycle_time_c
                            
        def LED_show_a():
                cell_3_butt=Button(cell_3, text=" ", width =12,fg='white',font = ('tahoma 7 bold'))
                cell_3_butt.grid(column=9, row=7, padx=0, pady=2)
                cell_3_butt=Button(cell_3, text=" ", width =12,bg="Yellow",fg='white',font = ('tahoma 7 bold')) 
                cell_3_butt.grid(column=9, row=7, padx=0, pady=2)
                # cell_3.after(defult_color_delay, lambda: cell_3_butt.configure(background="white"))
                # cell_3.after(result_color_delay, lambda: cell_3_butt.configure(background="yellow"))
        def unit_pass():
            cell_3_butt=Button(cell_3, text=" ", width =12,fg='white',font = ('tahoma 7 bold'))
            cell_3_butt.grid(column=9, row=7, padx=0, pady=2)
            cell_3_butt=Button(cell_3, text=" Done ", width =12,bg="lawn green",fg='white',font = ('tahoma 7 bold')) 
            cell_3_butt.grid(column=9, row=7, padx=0, pady=2)
            cell_3.after(defult_color_delay, lambda: cell_3_butt.configure(background="white"))
            cell_3.after(result_color_delay, lambda: cell_3_butt.configure(background="lawn green"))
                
        count_a()
    
    def start_cell3_d(cell3_slot_d_running):
        ##print ("status cell3_slot_c =",cell3_slot_d_running)
        cell_3_label=Label(cell_3,text= common_time,fg='black',bg='white',font=("arial", 10))   # start time label
        cell_3_label.grid(column=3, row=8, padx=8, pady=4)
        def count_a():
            global cell3_slot_d_running  # True /False
            global cell3_cycle_time_d
            global cell3_slot_d
        
            if cell3_slot_d_running:
                ##print('cell3_slot_d_running:',cell3_slot_d_running)
                cell_3_countlb_d.after(1000,count_a)
                cell3_cycle_time_d += 1
                remain_time = cell3_cycle_time_d
                cell_3_countlb_d.config(text=str(cell3_cycle_time_d)) 
                #####print("This is remain_time c:",remain_time)
                LED_show_a()
                if cell3_cycle_time_d >= countlim_set :
                    unit_pass()
                return cell3_cycle_time_d
            else :
                cell3_cycle_time_d = 0
                cell_3_countlb_d.config(text=str(cell3_cycle_time_d))
                
                return cell3_cycle_time_d
                            
        def LED_show_a():
                cell_3_butt=Button(cell_3, text=" ", width =12,fg='white',font = ('tahoma 7 bold'))
                cell_3_butt.grid(column=9, row=8, padx=0, pady=2)
                cell_3_butt=Button(cell_3, text=" ", width =12,bg="Yellow",fg='white',font = ('tahoma 7 bold')) 
                cell_3_butt.grid(column=9, row=8, padx=0, pady=2)
                # cell_3.after(defult_color_delay, lambda: cell_3_butt.configure(background="white"))
                # cell_3.after(result_color_delay, lambda: cell_3_butt.configure(background="yellow"))
        def unit_pass():
            cell_3_butt=Button(cell_3, text=" ", width =12,fg='white',font = ('tahoma 7 bold'))
            cell_3_butt.grid(column=9, row=8, padx=0, pady=2)
            cell_3_butt=Button(cell_3, text=" Done ", width =12,bg="lawn green",fg='white',font = ('tahoma 7 bold')) 
            cell_3_butt.grid(column=9, row=8, padx=0, pady=2)
            cell_3.after(defult_color_delay, lambda: cell_3_butt.configure(background="white"))
            cell_3.after(result_color_delay, lambda: cell_3_butt.configure(background="lawn green"))
                
        count_a()




#!------------------------------------------------------------------End cell 3----------------------------!

#!-------------------------------------------------------- cell 4--------------------------------------------
cell4_slot_a = False
cell4_slot_b = False
cell4_slot_c = False
cell4_slot_d = False


cell4_cycle_time_a = 0
cell4_cycle_time_b = 0
cell4_cycle_time_c = 0
cell4_cycle_time_d = 0

remain_time = 0


cell4_slot_a_running = False
cell4_slot_b_running = False
cell4_slot_c_running = False
cell4_slot_d_running = False


#--------------------------------------------------------------

cell_4 = ttk.LabelFrame(tab1, text=' Cell_4')
cell_4.grid(column=0, row=4, padx=8, pady=4)   
# cell_4_name = tk.StringVar()
# cell_4_name_entered = ttk.Entry(cell_4, width=12, textvariable=cell_4_name)
# cell_4_name_entered.grid(column=0, row=1, sticky='W')



def cell_4_main_start():
    cell_4_label=Label(cell_4,text="Baking slot A",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
    cell_4_label.grid(column=0, row=5, padx=8, pady=4)
    cell_4_label=Label(cell_4,text="Baking slot B",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
    cell_4_label.grid(column=0, row=6, padx=8, pady=4)
    cell_4_label=Label(cell_4,text="Baking slot C",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
    cell_4_label.grid(column=0, row=7, padx=8, pady=4)
    cell_4_label=Label(cell_4,text="Baking slot D",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
    cell_4_label.grid(column=0, row=8, padx=8, pady=4)



    cell_4_label=Label(cell_4,text="Start time :",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
    cell_4_label.grid(column=2, row=5, padx=8, pady=4)
    cell_4_label=Label(cell_4,text="Start time :",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
    cell_4_label.grid(column=2, row=6, padx=8, pady=4)
    cell_4_label=Label(cell_4,text="Start time :",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
    cell_4_label.grid(column=2, row=7, padx=8, pady=4)
    cell_4_label=Label(cell_4,text="Start time :",fg='white',bg='DeepSkyBlue4',font=("arial", 10))
    cell_4_label.grid(column=2, row=8, padx=8, pady=4)


    cell_4_countlb_a=Label(cell_4,text=" ",fg='black',bg='white',font=("arial", 10))
    cell_4_countlb_a.grid(column=4, row=5, padx=8, pady=4)
    cell_4_countlb_b=Label(cell_4,text=" ",fg='black',bg='white',font=("arial", 10))
    cell_4_countlb_b.grid(column=4, row=6, padx=8, pady=4)
    cell_4_countlb_c=Label(cell_4,text=" ",fg='black',bg='white',font=("arial", 10))
    cell_4_countlb_c.grid(column=4, row=7, padx=8, pady=4)
    cell_4_countlb_d=Label(cell_4,text=" ",fg='black',bg='white',font=("arial", 10))
    cell_4_countlb_d.grid(column=4, row=8, padx=8, pady=4)



    #cell #1 A
    cell4_start_aca = ttk.Button(cell_4,width=12, text="Start A",command= lambda:[cell4_dis_buttom_start_a(True),mes_box_A()])
    cell4_start_aca.grid(column=1, row=5)
    cell4_stop_a = ttk.Button(cell_4,width=12, text="Stop A",command= lambda:[cell4_dis_buttom_start_a(FALSE),cell4_a_stop(True)])
    cell4_stop_a.grid(column=5, row=5,padx=2, pady=2) 
    #cell #1 b
    cell4_start_acb = ttk.Button(cell_4,width=12, text="Start B",command= lambda:[cell4_dis_buttom_start_b(True),mes_box_B()])
    cell4_start_acb.grid(column=1, row=6)
    cell4_stop_b = ttk.Button(cell_4,width=12, text="Stop B",command= lambda:[cell4_dis_buttom_start_b(FALSE),cell4_b_stop(True)])
    cell4_stop_b.grid(column=5, row=6,padx=2, pady=2) 
    #cell #1 c
    cell4_start_acc = ttk.Button(cell_4,width=12, text="Start C",command= lambda:[cell4_dis_buttom_start_c(True),mes_box_C()])
    cell4_start_acc.grid(column=1, row=7)
    cell4_stop_c = ttk.Button(cell_4,width=12, text="Stop C",command= lambda:[cell4_dis_buttom_start_c(FALSE),cell4_c_stop(True)])
    cell4_stop_c.grid(column=5, row=7,padx=2, pady=2) 

    cell4_start_acd = ttk.Button(cell_4,width=12, text="Start D",command= lambda:[cell4_dis_buttom_start_d(True),mes_box_D()])
    cell4_start_acd.grid(column=1, row=8)
    cell4_stop_d = ttk.Button(cell_4,width=12, text="Stop D",command= lambda:[cell4_dis_buttom_start_d(FALSE),cell4_d_stop(True)])
    cell4_stop_d.grid(column=5, row=8,padx=2, pady=2) 


    def cell4_dis_buttom_start_a(status_butt):
        if status_butt == True:
            cell4_start_aca['state'] = DISABLED
            cell4_slot_a = True
            return  cell4_slot_a
        elif status_butt == FALSE :
            cell4_start_aca['state'] = NORMAL

    def cell4_dis_buttom_start_b(status_butt):
        if status_butt == True:
            cell4_start_acb['state'] = DISABLED
            cell4_slot_b = True
            return  cell4_slot_b
        elif status_butt == FALSE :
            cell4_start_acb['state'] = NORMAL

    def cell4_dis_buttom_start_c(status_butt):
        if status_butt == True:
            cell4_start_acc['state'] = DISABLED
            cell4_slot_c = True
            return  cell4_slot_c
        elif status_butt == FALSE :
            cell4_start_acc['state'] = NORMAL
    
    def cell4_dis_buttom_start_d(status_butt):
        if status_butt == True:
            cell4_start_acd['state'] = DISABLED
            cell4_slot_d = True
            return  cell4_slot_d
        elif status_butt == FALSE :
            cell4_start_acd['state'] = NORMAL
        
        


    def cell4_a_stop(stop_butt):
        global cell4_slot_a_running
        if stop_butt == True :
            cell4_slot_a_running = False
            cell4_cycle_time_a = 0
            start_cell4_a(cell4_slot_a_running)
            
            return cell4_cycle_time_a

    def cell4_b_stop(stop_butt):
        global cell4_slot_b_running
        if stop_butt == True :
            cell4_slot_b_running = False
            cell4_cycle_time_b = 0
            start_cell4_b(cell4_slot_b_running)
            
            return cell4_cycle_time_b

    def cell4_c_stop(stop_butt):
        global cell4_slot_c_running
        if stop_butt == True :
            cell4_slot_c_running = False
            cell4_cycle_time_c = 0
            start_cell4_c(cell4_slot_c_running)
            
            return cell4_cycle_time_c

    def cell4_d_stop(stop_butt):
        global cell4_slot_d_running
        if stop_butt == True :
            cell4_slot_d_running = False
            cell4_cycle_time_d = 0
            start_cell4_d(cell4_slot_d_running)
            
            return cell4_cycle_time_d

            

    def mes_box_A():
        global cell4_slot_a_running
        mes_a = messagebox.askokcancel('OK','Please make sure a')
        ##print(mes_a)
        if mes_a == True:
            cell4_slot_a_running = True
            start_cell4_a(cell4_slot_a_running)
        else:
            cell4_start_aca['state'] = NORMAL
    
    def mes_box_B():
        global cell4_slot_b_running
        mes_b = messagebox.askokcancel('OK','Please make sure b')
        ##print(mes_b)
        if mes_b == True:
            cell4_slot_b_running = True
            start_cell4_b(cell4_slot_b_running)
        else:
            cell4_start_acb['state'] = NORMAL

    def mes_box_C():
        global cell4_slot_c_running
        mes_c = messagebox.askokcancel('OK','Please make sure b')
        ##print(mes_c)
        if mes_c == True:
            cell4_slot_c_running = True
            start_cell4_c(cell4_slot_c_running)
        else:
            cell4_start_acc['state'] = NORMAL
        
    def mes_box_D():
        global cell4_slot_d_running
        mes_d = messagebox.askokcancel('OK','Please make sure b')
        ##print(mes_d)
        if mes_d == True:
            cell4_slot_d_running = True
            start_cell4_d(cell4_slot_d_running)
        else:
            cell4_start_acd['state'] = NORMAL
        

    def start_cell4_a(cell4_slot_a_running):
        ##print ("status cell4_slot_a =",cell4_slot_a)
        cell_4_label=Label(cell_4,text= common_time,fg='black',bg='white',font=("arial", 10))
        cell_4_label.grid(column=3, row=5, padx=8, pady=4)

        def count_a():
            global cell4_slot_a_running
            global cell4_cycle_time_a
            global cell4_slot_a
        
            if cell4_slot_a_running:
                ##print('cell4_slot_a_running:',cell4_slot_a_running)
                cell_4_countlb_a.after(1000,count_a)
                cell4_cycle_time_a += 1
                remain_time = cell4_cycle_time_a
                cell_4_countlb_a.config(text=str(cell4_cycle_time_a)) 
                ##print("This is remain_time A:",remain_time)
                LED_show_a()
                if cell4_cycle_time_a >= countlim_set :
                    unit_pass()
                return cell4_cycle_time_a
            else :
                cell4_cycle_time_a = 0
                cell_4_countlb_a.config(text=str(cell4_cycle_time_a))
                
                return cell4_cycle_time_a                     
        
        def LED_show_a():
                cell_4_butt=Button(cell_4, text=" ", width =12,fg='white',font = ('tahoma 7 bold'))
                cell_4_butt.grid(column=9, row=5, padx=0, pady=2)
                cell_4_butt=Button(cell_4, text=" ", width =12,bg="Yellow",fg='white',font = ('tahoma 7 bold')) 
                cell_4_butt.grid(column=9, row=5, padx=0, pady=2)
                # cell_4.after(defult_color_delay, lambda: cell_4_butt.configure(background="white"))
                # cell_4.after(result_color_delay, lambda: cell_4_butt.configure(background="yellow"))
        
        def unit_pass():
            cell_4_butt=Button(cell_4, text=" ", width =12,fg='white',font = ('tahoma 7 bold'))
            cell_4_butt.grid(column=9, row=5, padx=0, pady=2)
            cell_4_butt=Button(cell_4, text=" Done ", width =12,bg="lawn green",fg='white',font = ('tahoma 7 bold')) 
            cell_4_butt.grid(column=9, row=5, padx=0, pady=2)
            cell_4.after(defult_color_delay, lambda: cell_4_butt.configure(background="white"))
            cell_4.after(result_color_delay, lambda: cell_4_butt.configure(background="lawn green"))
                
        count_a()

    def start_cell4_b(cell4_slot_b_running):
        ##print ("status cell4_slot_b =",cell4_slot_b)
        cell_4_label=Label(cell_4,text= common_time,fg='black',bg='white',font=("arial", 10))
        cell_4_label.grid(column=3, row=6, padx=8, pady=4)
        def count_a():
            global cell4_slot_b_running  # True /False
            global cell4_cycle_time_b
            global cell4_slot_b
        
            if cell4_slot_b_running:
                ##print('cell4_slot_b_running:',cell4_slot_b_running)
                cell_4_countlb_b.after(1000,count_a)
                cell4_cycle_time_b += 1
                remain_time = cell4_cycle_time_b
                cell_4_countlb_b.config(text=str(cell4_cycle_time_b)) 
                ##print("This is remain_time B:",remain_time)
                LED_show_a()
                if cell4_cycle_time_b >= countlim_set :
                    unit_pass()
                return cell4_cycle_time_b
            else :
                cell4_cycle_time_b = 0
                cell_4_countlb_b.config(text=str(cell4_cycle_time_b))
                
                return cell4_cycle_time_b
                            
        def LED_show_a():
                cell_4_butt=Button(cell_4, text=" ", width =12,fg='white',font = ('tahoma 7 bold'))
                cell_4_butt.grid(column=9, row=6, padx=0, pady=2)
                cell_4_butt=Button(cell_4, text=" ", width =12,bg="Yellow",fg='white',font = ('tahoma 7 bold')) 
                cell_4_butt.grid(column=9, row=6, padx=0, pady=2)
                # cell_4.after(defult_color_delay, lambda: cell_4_butt.configure(background="white"))
                # cell_4.after(result_color_delay, lambda: cell_4_butt.configure(background="yellow"))
        def unit_pass():
            cell_4_butt=Button(cell_4, text=" ", width =12,fg='white',font = ('tahoma 7 bold'))
            cell_4_butt.grid(column=9, row=6, padx=0, pady=2)
            cell_4_butt=Button(cell_4, text=" Done ", width =12,bg="lawn green",fg='white',font = ('tahoma 7 bold')) 
            cell_4_butt.grid(column=9, row=6, padx=0, pady=2)
            cell_4.after(defult_color_delay, lambda: cell_4_butt.configure(background="white"))
            cell_4.after(result_color_delay, lambda: cell_4_butt.configure(background="lawn green"))
                
        count_a()
    
    def start_cell4_c(cell4_slot_c_running):
        ##print ("status cell4_slot_c =",cell4_slot_c_running)
        cell_4_label=Label(cell_4,text= common_time,fg='black',bg='white',font=("arial", 10))   # start time label
        cell_4_label.grid(column=3, row=7, padx=8, pady=4)
        def count_a():
            global cell4_slot_c_running  # True /False
            global cell4_cycle_time_c
            global cell4_slot_c
        
            if cell4_slot_c_running:
                ##print('cell4_slot_c_running:',cell4_slot_c_running)
                cell_4_countlb_c.after(1000,count_a)
                cell4_cycle_time_c += 1
                remain_time = cell4_cycle_time_c
                cell_4_countlb_c.config(text=str(cell4_cycle_time_c)) 
                #####print("This is remain_time c:",remain_time)
                LED_show_a()
                if cell4_cycle_time_c >= countlim_set :
                    unit_pass()
                return cell4_cycle_time_c
            else :
                cell4_cycle_time_c = 0
                cell_4_countlb_c.config(text=str(cell4_cycle_time_c))
                
                return cell4_cycle_time_c
                            
        def LED_show_a():
                cell_4_butt=Button(cell_4, text=" ", width =12,fg='white',font = ('tahoma 7 bold'))
                cell_4_butt.grid(column=9, row=7, padx=0, pady=2)
                cell_4_butt=Button(cell_4, text=" ", width =12,bg="Yellow",fg='white',font = ('tahoma 7 bold')) 
                cell_4_butt.grid(column=9, row=7, padx=0, pady=2)
                # cell_4.after(defult_color_delay, lambda: cell_4_butt.configure(background="white"))
                # cell_4.after(result_color_delay, lambda: cell_4_butt.configure(background="yellow"))
        def unit_pass():
            cell_4_butt=Button(cell_4, text=" ", width =12,fg='white',font = ('tahoma 7 bold'))
            cell_4_butt.grid(column=9, row=7, padx=0, pady=2)
            cell_4_butt=Button(cell_4, text=" Done ", width =12,bg="lawn green",fg='white',font = ('tahoma 7 bold')) 
            cell_4_butt.grid(column=9, row=7, padx=0, pady=2)
            cell_4.after(defult_color_delay, lambda: cell_4_butt.configure(background="white"))
            cell_4.after(result_color_delay, lambda: cell_4_butt.configure(background="lawn green"))
                
        count_a()
    
    def start_cell4_d(cell4_slot_d_running):
        ##print ("status cell4_slot_c =",cell4_slot_d_running)
        cell_4_label=Label(cell_4,text= common_time,fg='black',bg='white',font=("arial", 10))   # start time label
        cell_4_label.grid(column=3, row=8, padx=8, pady=4)
        def count_a():
            global cell4_slot_d_running  # True /False
            global cell4_cycle_time_d
            global cell4_slot_d
        
            if cell4_slot_d_running:
                #print('cell4_slot_d_running:',cell4_slot_d_running)
                cell_4_countlb_d.after(1000,count_a)
                cell4_cycle_time_d += 1
                remain_time = cell4_cycle_time_d
                cell_4_countlb_d.config(text=str(cell4_cycle_time_d)) 
                ####print("This is remain_time c:",remain_time)
                LED_show_a()
                if cell4_cycle_time_d >= countlim_set :
                    unit_pass()
                return cell4_cycle_time_d
            else :
                cell4_cycle_time_d = 0
                cell_4_countlb_d.config(text=str(cell4_cycle_time_d))
                
                return cell4_cycle_time_d
                            
        def LED_show_a():
                cell_4_butt=Button(cell_4, text=" ", width =12,fg='white',font = ('tahoma 7 bold'))
                cell_4_butt.grid(column=9, row=8, padx=0, pady=2)
                cell_4_butt=Button(cell_4, text=" ", width =12,bg="Yellow",fg='white',font = ('tahoma 7 bold')) 
                cell_4_butt.grid(column=9, row=8, padx=0, pady=2)
                # cell_4.after(defult_color_delay, lambda: cell_4_butt.configure(background="white"))
                # cell_4.after(result_color_delay, lambda: cell_4_butt.configure(background="yellow"))
        def unit_pass():
            cell_4_butt=Button(cell_4, text=" ", width =12,fg='white',font = ('tahoma 7 bold'))
            cell_4_butt.grid(column=9, row=8, padx=0, pady=2)
            cell_4_butt=Button(cell_4, text=" Done ", width =12,bg="lawn green",fg='white',font = ('tahoma 7 bold')) 
            cell_4_butt.grid(column=9, row=8, padx=0, pady=2)
            cell_4.after(defult_color_delay, lambda: cell_4_butt.configure(background="white"))
            cell_4.after(result_color_delay, lambda: cell_4_butt.configure(background="lawn green"))
                
        count_a()
    



#!------------------------------------------------------------------End cell 3----------------------------!

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
cell_1_main_start()
# cell_1_name_entered.focus()      # Place cursor into name Entry
cell_2_main_start()
# cell_2_name_entered.focus() 
cell_3_main_start()
# cell_3_name_entered.focus()      # Place cursor into name Entry
cell_4_main_start()
# cell_4_name_entered.focus()      # Place cursor into name Entry

#======================
# Start GUI
#======================
win.mainloop()