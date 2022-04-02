import os

def getDate():
	""" This function shows the time """
	import time
	a = time.asctime(time.localtime(time.time()))
	return a

def Naam():
	"""THis function returns list of names, which would be helpful """
	a = str(os.listdir(path="C:/Exercise Logger/ExLog/"))
	a = a.replace(".txt", "")
	a = a.replace("'", "")
    # print(a)
	res = a.strip('][').split(', ')
	return res

def create_new_usr():
    """Creates New user and files"""
    name = input(("Enter Your username: "))

    f = open(f"C:/Exercise Logger/ExLog/{name}.txt", 'x')
    f.close()

def del_usr():
    """Deletes Username file"""
    User_name_shower()
    _inp = int(input("Enter username to delete (c to cancel): "))
    lis = Naam()
    filename = lis[_inp]
    if _inp != "c":
        os.remove(f"C:/Exercise Logger/ExLog/{filename}.txt")
    else:
    	exit()

def Exlog(a, ExerciseName:str):
	""" This function writes exercise log to the file  """
	my_lis = Naam()
	my_name = my_lis[a]
	f = open(f"C:\\Exercise logger\\ExLog\\{my_name}.txt", 'a')
	time = getDate()
	f.write(time)
	f.write(" Exercise: ")
	f.write(ExerciseName)
	f.write("\n")
	f.close

def DietLog(a, FoodName:str):
	""" This function writes diet log to the file  """

	my_lis = Naam()
	my_name = my_lis[a]
	f = open(f"C:\\Exercise logger\\DietLog\\{my_name}.txt", 'a')
	time = getDate()
	f.write(time)
	f.write(" Diet: ")
	f.write(FoodName)
	f.write("\n")
	f.close

def Retrieve(a, FyaE): # 1 = exercise, 2 = diet
	""" This function reads log from the file """
	lis = Naam()
	_name = lis[a]
	if FyaE==1:
		f = open(f"C:\\Exercise logger\\ExLog\\{_name}.txt")
		content = f.read()
		print("The Logs are:\n", content)
		f.close()

	elif FyaE==2:
		f = open(f"C:\\Exercise logger\\DietLog\\{_name}.txt")
		content = f.read()
		print("The Logs are:\n", content)
		f.close()
	
def create_new_usr():
    """Creates New user and files"""
    name = input(("Enter Your username: "))

    f = open(f"C:/Exercise Logger/ExLog/{name}.txt", 'x')
    f = open(f"C:/Exercise Logger/DietLog/{name}.txt", 'x')
    
    f.close()

def User_name_shower():
    """This function the name of user"""
    i = 0
    a = str(os.listdir(path="C:/Exercise Logger/ExLog/"))
    a = a.replace(".txt", "")
    a = a.replace("'", "")
    # print(a)
    res = a.strip('][').split(', ')

    print("Names:")
    for namee in res:
    		print(i, ": ",namee)
    		i = i+1
			     	
    # print(res)
    # print(type(res))
    # print(f"{res[0]}.txt")

# main programme :

print("Welcome!, Please enter number corresponding to your name  ")
User_name_shower()
print("404: Delete User     999: Add User\n")
a = int(input())

if a==404:
	del_usr()

elif a==999:
	create_new_usr()

print("What do you wanna do? \n1: Log\n2: Retrieve\n")
choice = int(input())

if choice==1:
	inp_ = int(input("What do you wanna log\n1 : Exercise\n2 : Diet\n3 : Exit\n"))
	if inp_ ==1:
		Exercise_name = input("Enter the Exercise Name: ")
		Exlog(a, Exercise_name)

	elif inp_ ==2:
		Food_name = input("Enter the Food Name: ")
		DietLog(a, Food_name)
else:
	Ret = int(input("What you wanna Retrieve\n1: Exercise Logs\n2: Diet Logs\n"))
	if Ret==1:
		Retrieve(a, Ret)
		
	else:
		Retrieve(a, Ret)
