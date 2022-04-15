from tkinter import *

def store():
    namee = name.get()
    pwd = pwdd.get()

    f = open("Data.txt", 'a')
    f.write(f"\n{namee}")
    f.write(f"\n{pwd}")
    f.close()
    print("Added new user")
    Succ = Label(text="Created New User!").grid(row=8, column=5)

def login():

    f =  open("Data.txt", 'r')
    num_lines = sum(1 for line in f if line.rstrip())
    f.close()
    print('Total lines:', num_lines)

    namee = name.get()
    pwd = pwdd.get()

    print(f"You Entered:\nName:{namee} \nPass:{pwd}\n\n")

    f = open("Data.txt", 'r')

    num_lines = num_lines/2
    for l in range(int(num_lines)):

        Naam = f.readline()
        Passs = f.readline()

        # Had to write below lines because python also reads '\n' newline character
        Naam = Naam.replace('\n', '')
        Passs = Passs.replace('\n', '')

        print(f"Actual:\nName:{Naam}Pass:{Passs}")

        if Naam == namee and Passs == pwd:
            print("Login success")
            gg = Label(text="Login Succesfull").grid(row=6, column=7)

        else:
            print("Invalid user")
            gfg = Label(text="Invalid User").grid(row=7, column=7)

    f.close()

if __name__ == '__main__':
    
    root = Tk()
    root.geometry("733x334")
    root.minsize(200, 200)

    # Inializing Variables
    name = StringVar()
    pwdd = StringVar()

    # Labels
    _ff = Label(text="Name:").grid(row=2, column=2)
    _fg = Label(text="Pass:").grid(row=3, column=2)

    # Making entries
    _name = Entry(root, textvariable=name).grid(row=2, column=3)
    _pwwd = Entry(root, textvariable=pwdd).grid(row=3, column=3)

    # Making Button
    Button(text="Add User", command=store).grid(row=4, column=3)
    Button(text="Login", command=login, bg='#ffffff').grid(row=5, column=5)

    root.mainloop()
