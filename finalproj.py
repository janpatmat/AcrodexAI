from openpyxl import workbook, load_workbook

print("Print kag shit lods?: Y/N")

x = input()

if x == 'Y' or x == 'y':
        
    nwb = load_workbook('final.xlsx')
    ws = nwb.active
    print("Namae wa?: ")
    name = input()
    print("Edad?: ")
    age = input()

    ws.append(['Name' , 'Age', 'Address'])
    ws.append([name , age, "Some random address"])
    nwb.save('final.xlsx')
    print("Human na lods")
else:
    print("aw")

