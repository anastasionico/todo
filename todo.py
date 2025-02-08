task = []

def main():
    i = 1  
    while i < 10: 
        operation = input('type what operation you want to perform [1] create a new task [2] show all the existing tasks [3] delete a task\n')

        operation = int(operation)

        process(operation)
        
        i += 1
    else:
        print("program concluded\n")


def delete_task():
    element = input("insert the number of the element you want to delete\n")
    
    if int(element) > len(task):
        print("the number needs to be under {len(task)}\n")
    else:
        task.pop(int(element))


def process(operation):
    if operation == 1:
        task.append(input("Insert the name of the task you want to add\n"))

    elif operation == 2:
        print(task)

    elif operation == 3:
       delete_task() 
    else:
        exit('program concluded\n')

main()
