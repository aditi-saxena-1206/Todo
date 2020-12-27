#importing libraries
import sys
from datetime import date

#=========================
# function to execute help command
def task_help():
    temp = "$ ./todo add \"todo item\""
    print("Usage :-")
    print(f"{temp : <26}{'# Add a new todo' : <16}")
    print(f"{'$ ./todo ls' : <26}{'# Show remaining todos' : <22}")
    print(f"{'$ ./todo del NUMBER' : <26}{'# Delete a todo' : <15}")
    print(f"{'$ ./todo done NUMBER' : <26}{'# Complete a todo' : <17}")
    print(f"{'$ ./todo help' : <26}{'# Show usage' : <12}")
    print(f"{'$ ./todo report' : <26}{'# Statistics' : <12}")

#===========================
# function to execute add command
def task_add(todo_file,cmd):
    try:
        item = cmd[2]
    except IndexError:
        print("Error: Missing todo string. Nothing added!")
        sys.exit()

    item = cmd[2]
    file = open(todo_file,"a")
    file.write(item+"\n")
    file.close()
    print("Added todo: \""+item.strip()+"\"")

#============================
# function to execute ls command
def task_list(todo_file):
    try:
        file = open(todo_file, "r")
    except IOError as e:
        #print(str(e))
        #print("Add some todos and try again")
        print("There are no pending todos!")
        sys.exit()
    todo_list = file.readlines()
    if len(todo_list) == 0:
        print("There are no pending todos!")
    else:
        for i, e in reversed(list(enumerate(todo_list))):
            print("["+str(i+1)+"]", e, end ="")

#+=============================
# function to execute delete command
def task_delete(todo_file,cmd):
    try:
        num = cmd[2]
    except IndexError:
        print("Error: Missing NUMBER for deleting todo.")
        sys.exit()
    
    try:
        file = open(todo_file,"r")
    except IOError as e:
        print(str(e))
        print("Add some todos and try again")
        sys.exit()
    
    

    num = int(cmd[2])
    todo_list = file.readlines()
    todo_list = [task.strip() for task in todo_list]
    file.close()
    if num > len(todo_list) or num == 0:
        print("Error: todo #"+str(num)+" does not exist. Nothing deleted.")
    else:
        del todo_list[num-1]
        file = open(todo_file, "w")
        todo_list = [task + "\n" for task in todo_list]
        file.writelines(todo_list)
        file.close()
        print("Deleted todo #"+str(num))

#================================
# function to execute done command
def task_done(todo_file,done_file,cmd):
    
    try:
        num = cmd[2]
    except IndexError:
        print("Error: Missing NUMBER for marking todo as done.")
        sys.exit()
    try:
        file = open(todo_file,"r")
    except IOError as e:
        print(str(e))
        print("Add some todos and try again")
        sys.exit()
    
    

    num = int(cmd[2])
    todo_list = file.readlines()
    todo_list = [task.strip() for task in todo_list]
    file.close()
    if num > len(todo_list) or num == 0:
        print("Error: todo #"+str(num)+" does not exist.")
    else:
        done_task = todo_list[num-1]
        del todo_list[num-1]
        file = open(todo_file,"w")
        todo_list = [task + "\n" for task in todo_list]
        file.writelines(todo_list)
        file.close()
        file = open(done_file,"a")
        file.write("x  "+ str(date.today())+"  "+done_task+"\n")
        file.close()
        print("Marked todo #"+str(num)+" as done.")

#====================================
# function to execute report command
def task_report(todo_file,done_file):
    try:
        file1 = open(todo_file,"r")
    except IOError as e:
        print(str(e))
        print("Add some todos and try again")
        sys.exit()
    try:
        file2 = open(done_file,"r")
    except IOError as e:
        print(str(e))
        print("No todos done till now. Better get to work")
        sys.exit()
    todo_list = file1.readlines()
    todo_list = [task.strip() for task in todo_list]
    done_list = file2.readlines()
    done_list = [task.strip() for task in done_list]
    print(str(date.today())+" Pending : "+str(len(todo_list))+" Completed : "+str(len(done_list)))
    file1.close()
    file2.close()

#=========================
#execution begins

#defining files
todo_file = "todo.txt"
done_file = "done.txt"

#defining functions
cmd = sys.argv
#print(cmd)
functions = ["add","ls","del","done","help","report"]

#handling errors

#if no arguments
try:
    task = cmd[1]
except IndexError:
    task_help()
    sys.exit()

task = cmd[1]
#if invalid argument
if task not in functions:
    print("I don't understand that. Try something else")
    sys.exit()

if task == "add":
    task_add(todo_file,cmd)
elif task == "ls":
    task_list(todo_file)
elif task == "del":
    task_delete(todo_file, cmd)
elif task == "done":
    task_done(todo_file,done_file,cmd)
elif task == "help":
    task_help()
else:
    task_report(todo_file,done_file)

#end



