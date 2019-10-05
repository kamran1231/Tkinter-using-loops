

import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.geometry('500x400+200+100')

#Create Label using for  using Loop:

label = ['Customer Name: ','Customer Age: ','Customer Salary: ',' Customer Address: ','Customer City: ',
         'Customer Country: ','Customer Gender: ']

for i in range(len(label)):
    current_label = 'label' + str(i)
    current_label = ttk.Label(root,text = label[i])
    current_label.grid(row = i, column = 0,sticky = tk.W)


#create EnterBox for using Loop:

user_info = {
    'Name': tk.StringVar(),
    'Age':tk.IntVar(),
    'Salary':tk.IntVar(),
    'Address':tk.StringVar(),
    'City':tk.StringVar(),
    'Country':tk.StringVar()
}
count = 0
for i in user_info:
    current_entryBox = 'entry' + i
    current_entryBox = ttk.Entry(root,width = 20,textvariable = user_info[i])
    current_entryBox.grid(row = count,column = 1)
    current_entryBox.focus()
    count += 1


#Create Radio Button
userType_var = tk.StringVar()
radiobutton1 = ttk.Radiobutton(root,text = 'Student',value = 'Student',variable = userType_var)
radiobutton1.grid(row = 7,column = 0)
radiobutton2 = ttk.Radiobutton(root,text = 'Employe',value = 'Employe',variable = userType_var)
radiobutton2.grid(row = 7,column = 1)


#Create Combo button:

gendertype_var = tk.StringVar()
combobtn = ttk.Combobox(root,width = 17,textvariable = gendertype_var,state = 'readonly')
combobtn['values'] = ('Male','Female','Other')
combobtn.grid(row = 6,column  = 1)






#create Submit Button:

def action():
    print(user_info.get('Name').get())
    print(user_info.get('Age').get())
    print(user_info.get('Salary').get())
    print(user_info.get('Address').get())
    print(user_info.get('City').get())
    print(user_info.get('Country').get())
    gendertype = gendertype_var.get()
    print(f'{gendertype}')
    typeofuser = userType_var.get()
    print(f'{typeofuser}')



    #2nd method for taking output
    # username = user_info.get('Name').get()
    # userage = user_info.get('Age').get()
    # usersalary = user_info.get('Salary').get()
    # useraddress = user_info.get('Address').get()
    # usercity = user_info.get('City').get()
    # usercountry = user_info.get('Country').get()
    # usertype = userType_var.get()
    #
    # print(f' Name: {username}\n Age: {userage}\n Salary: {usersalary}\n Address: {useraddress}'
    #       f'\n City: {usercity}\n Country: {usercountry}')




submitbtn = ttk.Button(root,text = 'Submit',command = action)
submitbtn.grid(row = 9 , column = 0,columnspan = 3)

root.mainloop()
