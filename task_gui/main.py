from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry # DateEntry widget
from datetime import datetime
import smtplib as s # For sending email

# SMTP Configuration and Email Function
def send_mail(task):
    sm = s.SMTP('smtp.gmail.com', 587)
    sm.ehlo()
    sm.starttls()
    sm.login('test@gmail.com', 'testpassword') # replace placeholder email, password with your own
    sender = 'test@gmail.com' # sender email address
    mail_receiver = 'receivertest@gmail.com' # receiver email address
    subject = "Task Manager - Task is not completed!" 
    body = f"Hi {mail_receiver},\n\nThis is a reminder that you have a {task} that is not completed yet!\n\n"
    msg = f"subject: {subject}\n\n{body}"
    sm.sendmail(sender, mail_receiver, msg)
    print("Email Sent Successfully.")
    sm.quit()

# Win Main Configurations
win = Tk()
win.title("Task Manager")
win.iconbitmap("images/task.ico")
win.geometry("1030x480")
win.resizable(False, False)

# Define Column
tree = ttk.Treeview(win, columns=('Name', 'Description', 'Date', 'Status'), height=13)
tree.column('#0', width=0, stretch=NO)
tree.column('Name', width=220, anchor=CENTER)
tree.column('Description', width=500, anchor=CENTER)
tree.column('Date', width=130, anchor=CENTER)
tree.column('Status', width=160, anchor=CENTER)

# Creating headings
tree.heading('#0', text='')
tree.heading('Name', text='Task Name', anchor=CENTER)
tree.heading('Description', text='Task Description', anchor=CENTER)
tree.heading('Date', text='Date', anchor=CENTER)
tree.heading('Status', text='Status', anchor=CENTER)

# Global Variables
current_row = 0 # For inserting new task
current_date = datetime.now().strftime("%d%m%Y") # current date format is 05052022

# Add Task Function
def add_task():
    global current_row
    current_row += 1
    tname = task_name.get()
    tdesc = task_desc.get('1.0', END)
    tdate = task_date.get()
    cdate = task_date.get().replace('/', '') # convert date in 06052022 format to compare with current date
    tstatus = task_chan_status.get()

    if (tstatus == 'to-do') and (cdate < current_date):
        tstatus = "It's not completed!"
        tree.insert('', current_row, text='', values=(tname, tdesc, tdate, tstatus),
                    tags=('todo_red'))
        send_mail(tname)
    elif (tstatus == 'to-do') and (cdate >= current_date):
        tree.insert('', current_row, text='', values=(tname, tdesc, tdate, tstatus),
                    tags=('todo'))
    elif (tstatus == 'in-progress') and (cdate < current_date):
        tstatus = "It's not completed!"
        tree.insert('', current_row, text='', values=(tname, tdesc, tdate, tstatus),
                    tags=('inprogress_red'))
        send_mail(tname)
    elif (tstatus == 'in-progress') and (cdate >= current_date):
        tree.insert('', current_row, text='', values=(tname, tdesc, tdate, tstatus),
                    tags=('inprogress'))
    else:
        tree.insert('', current_row, text='', values=(tname, tdesc, tdate, tstatus),
                    tags=('complete'))

    # For changing the color of the task status using tags
    tree.tag_configure('todo', background='blue', foreground='white')
    tree.tag_configure('todo_red', background='red', foreground='white')
    tree.tag_configure('inprogress', background='yellow', foreground='black')
    tree.tag_configure('inprogress_red', background='red', foreground='white')
    tree.tag_configure('complete', background='green', foreground='white')


# Update Task Function
def update_task():
    tname = task_name.get()
    tdesc = task_desc.get('1.0', END)
    tdate = task_date.get()
    cdate = task_date.get().replace('/', '') # convert date in 06052022 format to compare with current date
    tstatus = task_chan_status.get()
    
    for i in tree.selection():
        if (tstatus == 'to-do') and (cdate < current_date):
            tstatus = "It's not completed!"
            tree.item(i, values=(tname, tdesc, tdate, tstatus),
                    tags=('todo_red'))
            send_mail(tname)
        elif (tstatus == 'to-do') and (cdate >= current_date):
            tree.item(i, values=(tname, tdesc, tdate, tstatus),
                    tags=('todo'))
        elif (tstatus == 'in-progress') and (cdate < current_date):
            tstatus = "It's not completed!"
            tree.item(i, values=(tname, tdesc, tdate, tstatus),
                    tags=('inprogress_red'))
            send_mail(tname)
        elif (tstatus == 'in-progress') and (cdate >= current_date):
            tree.item(i, values=(tname, tdesc, tdate, tstatus),
                    tags=('inprogress'))
        else:
            tree.item(i, values=(tname, tdesc, tdate, tstatus),
                    tags=('complete'))

    # For changing the color of the task status using tags
    tree.tag_configure('todo_red', background='red', foreground='white')
    tree.tag_configure('todo', background='blue', foreground='white')
    tree.tag_configure('inprogress_red', background='red', foreground='white')
    tree.tag_configure('inprogress', background='yellow', foreground='black')
    tree.tag_configure('complete', background='green', foreground='white')


# Delete Task Function
def delete_task():
    for i in tree.selection():
        tree.delete(i)


# Layout of the Treeview
tree.grid(row = 0, column = 0, columnspan = 6, pady="10", padx="10")

# Scrollbar inside the treeview
sb = Scrollbar(win,orient=VERTICAL)
sb.grid(row=0, column=5, sticky=NS)

tree.config(yscrollcommand=sb.set)
sb.config(command=tree.yview)

# Define Entry, Text, DateEntry and Combobox widgets for Task
task_name = Entry(win, font="Lato 12 bold", borderwidth=2, relief="groove", width="25")
task_name.insert(0, "Task Name...")
task_name.grid(row = 1, column = 0, pady="10", padx="5")

task_desc = Text(win, font="Lato 12 bold", borderwidth=2, relief="groove", width=25, height=5)
task_desc.insert(0.0, "Task Description...")
task_desc.grid(row = 1, column = 1, pady="10", padx="5")

task_date = DateEntry(win, selectmode='day', date_pattern='dd/mm/yyyy', font="Lato 12 bold", borderwidth=2, relief="groove", width="15")
task_date.grid(row = 1, column = 2, pady="10", padx="5")

task_chan_status = ttk.Combobox(win, values=['to-do','in-progress','completed'], font="Lato 12 bold", width="15")
task_chan_status.set('to-do')
task_chan_status.grid(row = 1, column = 3, pady="10", padx="5")


# Buttons for adding, deleting and updating task buttons
add_task =Button(win, text="Add", command = add_task, bg="green", fg="#ffffff", font="Lato 12 bold", borderwidth="2", relief="groove", width="14")
add_task.grid(row = 2, column = 0, pady="10", padx="5")

del_task =Button(win, text="Delete", command = delete_task, bg="red", fg="#ffffff", font="Lato 12 bold", borderwidth="2", relief="groove", width="14")
del_task.grid(row = 2, column = 1, pady="10", padx="5")

upd_task = Button(win, text="Update", command = update_task, bg="blue", fg="#ffffff", font="Lato 12 bold", borderwidth="2", relief="groove", width="14")
upd_task.grid(row = 2, column = 2, pady="10", padx="5")

win.mainloop()