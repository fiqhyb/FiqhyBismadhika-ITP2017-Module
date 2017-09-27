from interface import combine1 as c

products = {"3121ab": "spoon", "1234ab": "fork", "2143ab": "knife", "3241ab": "plate", "2314ab": "bowl"}
list = []
code_list = []
search_found = False
def maina():
    def quit():
        c.mainc()
    while True:
        barcode = input("Enter barcode: ")
        search_found = False
        for keys, value in products.items():
            if barcode == keys:
                print("Product : ", value.title())
                print("Barcode : ", keys)
                list.append(value)
                code_list.append(keys)
                print(list)
                print(code_list)
                search_found = True
                break

        if search_found == False:
            print("No product found.")

        inpt = input("Search again?")
        if inpt == "yes":
            continue
        else:
            break
    quit()
