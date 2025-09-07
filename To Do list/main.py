
while True:
    user_action=input("Type add, show, check, edit, remove all or exit: ")
    user_action=user_action.strip()

    def w_r_todo():
        with open("todos.txt", "r") as file:
            t = file.readlines()
            return t
    

    match user_action:
        case "add":
            try:
                todo=input("Enter a todo: ") + "\n"

                file = open("todos.txt", "a")
                todos = file.write(todo)
                file.close()

                print(todo.strip("\n")) 
            except ValueError:
                print("Something went wrong! Please, try again.") 
                continue             
            
        case "show":
            try:                            
                t = w_r_todo()
                if t:
                    for i, items in enumerate(t):
                        print(f"{i+1}. {items.strip("\n")}")
                else:        
                    print("add a todo first.") 
            except ValueError:
                print("Something went wrong! Please, try again.")      
                continue                
                        
        case "check":  #in the app, user will be asked to 'click' on the task they want to check
            try:
                t = w_r_todo()
                number = int(input("Enter the todo number, you want to check: "))
                if number <= 0:
                    print("You can only use natural numbers e.g. 1,2,3...")
                else:
                    num = number - 1
                    t.pop(num)   
                    with open("todos.txt", "w") as file:
                        file.writelines(t)
                    print("Checked Your Task!")  
            except ValueError:
                print("Something went wrong! Please, try again.")
                continue

        case "remove all":
            try:    

                with open("todos.txt", "w") as file:
                    file.writelines([])
            except ValueError:
                print("Something went wrong! Please, try again.")
                continue

        case "edit":
            try:
                t = w_r_todo()       
                number = int(input("Enter the todo number, you want to edit: "))
                if number < 0 or number > len(t):
                    print("invalid number, try again.")
                else:
                    new_item = input("Add a new todo here: ")
                    t[number - 1] = new_item + "\n"
                    with open("todos.txt", "w") as file:
                        file.writelines(t)
                    print(f"No. {number} task has been edited!")
            except ValueError:
                print("Something went wrong! Please, try again.")
                continue
                
        case "exit":
            try:
                break
            except ValueError:
                print("Something went wrong! Please, try again.")
                continue

        case _:
            print("Unknown Command!")