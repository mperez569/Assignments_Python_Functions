#1. The Calculator App
def adds(sums):
    if not sums:
        print("No numbers were entered!!!")
        
    else:
        z = sums[0] 
        for i in range(1, len(sums)): 
            z += sums[i]
    
    return z
    
    #alternate code for summation
    #x = []
    #x.append(args)
    #return sum(args)

def subs(difference):
    if not difference:
        print("No numbers were entered!!!")
        
    else:
        z = difference[0] 
        for i in range(1, len(difference)): 
            z -= difference[i]
    
    return z

def mults(product):
    if not product:
        print("No numbers were entered!!!")
        
    else:
        z = product[0] 
        for i in range(1, len(product)): 
            z *= product[i]
    
    return z
    
def divs(quotient):
    if not quotient:
        print("No numbers were entered!!!")
        
    else:
        z = quotient[0] 
        for i in range(1, len(quotient)):
            try:
                z /= quotient[i]
            except ZeroDivisionError:
                print("Cannot divide by zero. Exit Operation")
    
    return z

def main():
    print("-----Welcome to Calculator APP-----\n")
    print("What would you like to do? \n")
    print("Select a number for whichever operation you would like to preform: \n")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division\n")
    try:
        choice = int(input("Enter choice here: "))
        if choice == 1:
            numbers = []
    
            while True:
                num = input("Enter an integer (enter 'exit' to stop): ")
                if num.lower() == 'exit':
                    break
                try:
                    num = int(num)  # Convert input to integer
                    numbers.append(num)  # Append to list
                except ValueError:
                    print("Please enter a valid integer or 'exit' to stop.")
            
            result = adds(numbers)
            print("Result: " + str(result))
            
        if choice == 2:
            numbers = []
    
            while True:
                num = input("Enter an integer (enter 'exit' to stop): ")
                if num.lower() == 'exit':
                    break
                try:
                    num = int(num)  # Convert input to integer
                    numbers.append(num)  # Append to list
                except ValueError:
                    print("Please enter a valid integer or 'exit' to stop.")
            
            result = subs(numbers)
            print("Result: " + str(result))
        
        if choice == 3:
            numbers = []
    
            while True:
                num = input("Enter an integer (enter 'exit' to stop): ")
                if num.lower() == 'exit':
                    break
                try:
                    num = int(num)  # Convert input to integer
                    numbers.append(num)  # Append to list
                except ValueError:
                    print("Please enter a valid integer or 'exit' to stop.")
            
            result = mults(numbers)
            print("Result: " + str(result))
        
        if choice == 4:
            numbers = []
    
            while True:
                num = input("Enter an integer (enter 'exit' to stop): ")
                if num.lower() == 'exit':
                    break
                try:
                    num = int(num)  # Convert input to integer
                    numbers.append(num)  # Append to list
                except ValueError:
                    print("Please enter a valid integer or 'exit' to stop.")
            
            result = divs(numbers)
            print("Result: " + str(result))
    except ValueError:
        print("Invalid choice. Program")
    
 
main()       
while True:
    cont = input("-----do you wish to preform another operation?: ")
    if cont == "y" or cont == "yes" or cont == "Yes":
        main()
    else:
        print("Thank You!!!")
        break

#####
#2. The Shopping List Maker
#####

print("----Welcome to Shopping List!----")

def add(items):
    item = input("Enter Item (enter 'exit' to quit): ")
    items.append(item)
    print("")
    
    
def remove(items):
    if len(items) == 0:
        print("There are no items to remove\n")
    elif len(items) > 0:
        for i in range(len(items)):
            print(str(i + 1) + ". " + items[i])
            
        item = input("which item do you want to remove?: (enter any key to stop): ")
        if item in items:
            items.remove(item.lower())
    print("")
        
def item_list(items):
    if len(items) > 0:
        for i in range(len(items)):
            print(str(i + 1) + ". " + items[i])
    else: 
        print("There is nothing in the list\n")
    print("")
        


items = []
while True:
    arl = input("Do you want to add, remove, or list the items?: (enter 'exit' to quit): ")
    if arl == "add":
        add(items)
        
    elif arl == "remove":
        remove(items)
    
    elif arl == "list":
        item_list(items)
    
    elif arl == "exit":
        print("Thank you, goodbye!")
        break
    
    else:
        print("Invalid selection. Enter valid choice.")
    
