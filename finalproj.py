from openpyxl import workbook, load_workbook

def generateSheet():
    print("Bot: Would you like to create a sheet?: Y/N")

    x = input()

    if x == 'Y' or x == 'y':
            
        nwb = load_workbook('final.xlsx')
        ws = nwb.active
        print("Bot: Add a name ")
        name = input("Name: ")
        print("Bot: Add an age ")
        age = input("Age: ")
        print("Bot: Add an address ")
        address = input("Address: ")

        ws.append(['Name' , 'Age', 'Address'])
        ws.append([name , age, address])
        nwb.save('final.xlsx')
        print("Bot: Process finished")
    else:
        print("Bot: Terminating process")


        


