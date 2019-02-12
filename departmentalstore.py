import datetime
def readDealerInfo():
    file=open("dealers.txt","r")
    rawData=file.read()
    lines=rawData.split("\n")
    lines.pop()
    finalList=[]
    for i in lines:
        splitted=i.split(",")
        temp=[splitted[0],int(splitted[1])]
        finalList.append(temp)
    return finalList
def readQuantity():
    file=open("quantity.txt","r")
    rawData=file.read()
    lines=rawData.split("\n")
    lines=lines[1:]
    lines.pop()
    quantityList=[]
    for i in lines:
        tmpStr=i.split(",")
        tmpList=[]
        for j in tmpStr:
            tmpList.append(int(j))
        quantityList.append(tmpList)
    return quantityList
def buyFromDealer(managerName):
    listOfAllItems=readItemsFromDisk()
    quantityList=readQuantity()
    inp=input("Enter product name or barcode: ")
    currentItem=[]
    for i in listOfAllItems:
        if i[0]==inp or inp in i[1]:
            currentItem=i
            break
    dealers=readDealerInfo()
    if not len(currentItem)==0:
        print("Product details are as follows: ")
        print("Barcode: ",currentItem[0])
        print("Name: ",currentItem[1])
        print("Purchase Price: ",currentItem[2])
        for j in dealers:
            if j[1]==int(currentItem[4]):
                print("Dealer Code: ",j[1])
                print("Dealer Name: ",j[0])
                break
        for j in quantityList:
            if int(j[0])==int(currentItem[0]):
                print("Available Quantity: ",j[1])
                print("Threshold Quantity: ",j[2])
                break
        quan=int(input("How much quantity do you want to buy? "))
        availableMoney=int((open("money.txt","r")).read())
        totalPrice=quan*int(currentItem[2])
        if availableMoney>=quan:
            availableMoney-=totalPrice
            (open("money.txt","w")).write(str(availableMoney))
            for i in quantityList:
                if i[0]==int(currentItem[0]):
                    i[1]+=quan
            file=open("quantity.txt","w")
            file.write("barcode,availblequantity,threshold,delaercode\n")
            for i in range(0,len(quantityList)):
                #print(quantityList[i])
                writeString=str(quantityList[i][0])+","+str(quantityList[i][1])+","+str(quantityList[i][2])+","+str(quantityList[i][3])
                if not i==len(quantityList):
                    writeString+="\n"
                file.write(writeString)
            file.close()
            print("Item purchase successful")
            print("Money Spent: ",totalPrice)
            print()
        else:
            print("This much money is not available")
    else:
        print("Product not found")
def listItems():
    allItems=readItemsFromDisk()
    quantityList=readQuantity()
    fullDetail=[]
    for i in allItems:
        temp=[]
        temp.extend(i)
        for j in quantityList:
            if int(j[0])==int(i[0]):
                temp.extend(j)
                break
        fullDetail.append(temp)
    print(99*"-")
    print("Barcode |Product Name       |Purchase Price |Sale Price |Available Quantity |Threshold |Dealer Code")
    for i in fullDetail:
        print(str(i[0])+(9-len(str(i[0])))*" ",end="")
        print(str(i[1])+(20-len(str(i[1])))*" ",end="")
        print(str(i[2])+(16-len(str(i[2])))*" ",end="")
        print(str(i[3])+(12-len(str(i[3])))*" ",end="")
        print(str(i[6])+(20-len(str(i[6])))*" ",end="")
        print(str(i[7])+(11-len(str(i[7])))*" ",end="")
        print(str(i[4])+(11-len(str(i[4])))*" ",end="")
        print()
    print(99*"-")
    print()
        
def listShortage():
    allItems=readItemsFromDisk()
    quantityList=readQuantity()
    fullDetail=[]
    for i in allItems:
        temp=[]
        temp.extend(i)
        for j in quantityList:
            if int(j[0])==int(i[0]):
                temp.extend(j)
                break
        fullDetail.append(temp)
    print(99*"-")
    print("Barcode |Product Name       |Purchase Price |Sale Price |Available Quantity |Threshold |Dealer Code")
    for i in fullDetail:
        if int(i[6])<int(i[7]):
            print(str(i[0])+(9-len(str(i[0])))*" ",end="")
            print(str(i[1])+(20-len(str(i[1])))*" ",end="")
            print(str(i[2])+(16-len(str(i[2])))*" ",end="")
            print(str(i[3])+(12-len(str(i[3])))*" ",end="")
            print(str(i[6])+(20-len(str(i[6])))*" ",end="")
            print(str(i[7])+(11-len(str(i[7])))*" ",end="")
            print(str(i[4])+(11-len(str(i[4])))*" ",end="")
            print()
    print(99*"-")
    print()
    
def profitAdd(add):
    file=open("profit.txt","r")
    data=int(file.read())
    data+=add
    data=str(data)
    file=open("profit.txt","w")
    file.write(data)
    file.close()
def moneyRecord(purchasedItems,quantityList):
    file=open("money.txt","r")
    money=int(file.read())
    for i in range(0,len(purchasedItems)):
        money+=int(purchasedItems[i][3])*int(quantityList[i])
    file=open("money.txt","w")
    file.write(str(money))
    file.close()

def recordBill(purchasedItems,quantityList):
    moneyRecord(purchasedItems,quantityList)
    file=open("quantity.txt","r")
    rawData=file.read()
    lines=rawData.split("\n")
    lines=lines[1:]
    lines.pop()
    fullData=[]
    for i in lines:
        tmpStr=i.split(",")
        #print(tmpStr)
        tmpList=[]
        for j in tmpStr:
            tmpList.append(int(j))
        fullData.append(tmpList)
    for i in fullData:
        for j in range(0,len(purchasedItems)):
            if i[0]==int(purchasedItems[j][0]):
                i[1]-=int(quantityList[j])
    file=open("quantity.txt","w")
    file.write("barcode,availblequantity,threshold,delaercode\n")
    for i in range(0,len(fullData)):
        #print(fullData[i])
        writeString=str(fullData[i][0])+","+str(fullData[i][1])+","+str(fullData[i][2])+","+str(fullData[i][3])
        if not i==len(fullData):
            writeString+="\n"
        file.write(writeString)
    file.close()
    allBills=[]
    file=open("bills.txt")
    rawData=file.read()
    splittedData=rawData.split("\n")
    splittedData.pop()
    for i in splittedData:
        allBills.append(i)
    currentDT = datetime.datetime.now()
    date=str(currentDT)
    allBills.append("t;"+date)
    for i in range(0,len(purchasedItems)):
        temp="i;"
        for j in purchasedItems[i]:
            temp+=str(j)+","
        temp+=str(quantityList[i])
        allBills.append(temp)
    
    file=open("bills.txt","w")
    for i in range(0,len(allBills)):
        file.write(allBills[i])
        if not i==len(allBills):
            file.write("\n")
    file.close()
    pass
def quantityCheck(barcode,quantity):
    file=open("quantity.txt","r")
    rawData=file.read()
    lines=rawData.split("\n")
    lines=lines[1:]
    lines.pop()
    fullData=[]
    for i in lines:
        tmpStr=i.split(",")
        tmpStr.pop()
        tmpList=[]
        for j in tmpStr:
            tmpList.append(int(j))
        fullData.append(tmpList)
    for i in fullData:
        if i[0]==int(barcode):
            if i[1]>=int(quantity):
                return True
            return False
    return False

def readItemsFromDisk():
    itemDetails=[]
    file=open("products.txt","r")
    rawData=file.read()
    broken=rawData.split("\n")
    brokenRef=broken[1:len(broken)-1]
    finalList=[]
    for i in brokenRef:
        finalList.append(i.split(","))
    return finalList
    
    
def startBilling(cashiername):
    print("Billing started by: ",cashiername)
    currentDT = datetime.datetime.now()
    date=str(currentDT)
    print ("Billing Date/Time:",date)
    items=[]
    totalPayable=0
    listOfAllItems=readItemsFromDisk()
    purchasedItems=[]
    quantityList=[]
    #print(listOfAllItems)
    #barcode,name,purchaseprice,saleprice,dealercode
    while True:
        inp=input("Enter product name or barcode: ")
        productName=""
        if inp == "end":
            break
        productPurchasePrice=0
        productSalePrice=0
        currentItem=[]
        for i in listOfAllItems:
            if i[0]==inp or inp in i[1]:
                productName=i[1]
                productPurchasePrice=int(i[2])
                productSalePrice=int(i[3])
                currentItem=i
                #purchasedItems.append(i)
                break
        if (productName==""):
            print("Product Not Found")
        else:
            print("Product Name = ",productName)
            print("Price = ",productSalePrice)
            quan=int(input("Enter quantity: "))
            if quantityCheck(currentItem[0],quan):
                productPurchasePrice*=quan
                productSalePrice*=quan
                profitAdd(productSalePrice-productPurchasePrice)
                totalPayable+=productSalePrice
                quantityList.append(quan)
                purchasedItems.append(currentItem)
            else:
                print("Sorry, This much quantity of this product is not available")
                
    recordBill(purchasedItems,quantityList)
    print("\n")
    print("-"*67)
    print(" "*21,"SUNNY Deparmental Store")
    print("-"*67)
    currentDT = datetime.datetime.now()
    date=str(currentDT)
    print("Billing Date/Time: ",date)
    print("-"*67)
    print()
    print("Barcode | Product Name       | Item Price | Quantity | Total Price")
    for i in range(0,len(purchasedItems)):
        currentItem=purchasedItems[i]
        itemQuantity=quantityList[i]
        itemQuantityStr=str(itemQuantity)
        itemCode=currentItem[0]
        itemName=currentItem[1]
        itemPrice=int(currentItem[3])
        itemPriceStr=str(itemPrice)
        totalPrice=itemPrice*itemQuantity
        totalPriceStr=str(totalPrice)
        print(itemCode+" "*6+itemName+" "*(21-len(itemName))+itemPriceStr+" "*(13-len(itemPriceStr))+itemQuantityStr+" "*(11-len(itemQuantityStr))+totalPriceStr)
    print("-"*67)
    print(" "*42+"Grand Total: "+str(totalPayable))
    paidByCustomer=int(input("Paid by customer: "))
    change=paidByCustomer-totalPayable
    print("Balance: ",change)
    print("-"*67)
    print(" "*9+"Thanks for Shopping at SUNNY Departmental Store")
    print(" "*25+"Please Come Again")
    print("-"*67)
    print()
    print()
            
def registerNewDealer(dealerList):
    print("You are goint to register a new dealer")
    name=input("Enter the dealer name: ")
    code=0
    unique=False
    while not unique:
        code=int(input("Enter a code for this dealer: "))
        found=False
        for i in dealerList:
            if int(i[1])==code:
                found=True
        if found:
            print("Please select a unique code for the dealer")
        else:
            unique=True
            print(f"New dealer registered with name \"{name}\" and code \"{code}\"")
            print()
            input("Press enter to continue")
    dealerList.append([name,str(code)])
    file=open("dealers.txt","w")
    for i in range(0,len(dealerList)):
        writeStr=dealerList[i][0]+","+dealerList[i][1]
        if not i==len(dealerList):
            writeStr+="\n"
        file.write(writeStr)
    file.close()
    
def manageDealers():
    file=open("dealers.txt","r")
    rawData=file.read()
    lines=rawData.split("\n")
    lines.pop()
    allDealers=[]
    for i in lines:
        allDealers.append(i.split(","))
    print("What do you want to do?")
    print("1. View all dealers")
    print("2. Register a new dealer")
    choice=int(input("Enter the option number: "))
    if choice==2:
        registerNewDealer(allDealers)
    else:
        print()
        print("-"*40)
        print("Dealer Code |Dealer Name")
        for i in allDealers:
            print(i[1]+(13-len(i[1]))*" "+i[0])
        print("-"*40)
        print()
def registerNewProduct():
    quantityList=readQuantity()
    itemList=readItemsFromDisk()
    dealers=readDealerInfo()
    currentDealer=[]
    while True:
        dlr=input("Enter dealer code or name: ")
        exists=False
        for i in dealers:
            if dlr in str(i[0]) or dlr in str(i[1]):
                currentDealer=i
                exists=True
                break
        if not exists:
            print("Wrong dealer info. Please try again")
        else:
            break
    print("Dealer name: ",currentDealer[0])
    print("Dealer code: ",currentDealer[1])
    barcode=0
    while True:
        bc=int(input("Enter a unique barcode: "))
        match=False
        for i in itemList:
            if bc==int(i[0]):
                match=True
        if match:
            print("This barcode already exists. Please select a unique barcode")
        else:
            barcode=bc
            break
    name=input("Enter product name: ")
    purchase=int(input("Enter product\'s purchase price: "))
    sale=int(input("Enter product\'s sale price: "))
    threshold=int(input("Enter the threshold value: "))
    itemAdd=[str(barcode),str(name),str(purchase),str(sale),str(currentDealer[1])]
    quanAdd=[int(barcode),0,int(threshold),int(currentDealer[1])]
    itemList.append(itemAdd)
    quantityList.append(quanAdd)
    file=open("quantity.txt","w")
    file.write("barcode,availblequantity,threshold,delaercode\n")
    for i in range(0,len(quantityList)):
        writeString=str(quantityList[i][0])+","+str(quantityList[i][1])+","+str(quantityList[i][2])+","+str(quantityList[i][3])
        if not i==len(quantityList):
            writeString+="\n"
        file.write(writeString)
    file.close()
    file=open("products.txt","w")
    file.write("barcode,productname,originalprice,saleprice,dealercode\n")
    for i in range(0,len(itemList)):
        writeString=str(itemList[i][0])+","+str(itemList[i][1])+","+str(itemList[i][2])+","+str(itemList[i][3])+","+str(itemList[i][4])
        if not i==len(itemList):
            writeString+="\n"
        file.write(writeString)
    file.close()
    
def addPerson():
    file=open("LoginData.txt","r")
    allFileData=file.read()
    process1=allFileData.split(":")
    ownerDataRaw=process1[2]
    ownerListRaw=ownerDataRaw.split("\n")
    ownerListRefined=ownerListRaw[1:len(ownerListRaw)-1]
    ownerLoginFinal=[]
    for i in ownerListRefined:
        ownerLoginFinal.append(i.split(","))
    managerDataRaw=process1[4]
    managerListRaw=managerDataRaw.split("\n")
    managerListRefined=managerListRaw[1:len(managerListRaw)-1]
    managerLoginFinal=[]
    for i in managerListRefined:
        managerLoginFinal.append(i.split(","))
    cashierDataRaw=process1[6]
    cashierListRaw=cashierDataRaw.split("\n")
    cashierListRefined=cashierListRaw[1:len(cashierListRaw)-1]
    cashierLoginFinal=[]
    for i in cashierListRefined:
        cashierLoginFinal.append(i.split(","))
    print("Choose the authority of the person you want to add")
    print("1. Owner")
    print("2. Manager")
    print("3. Cashier")
    option=int(input("Choose the option: "))
    username=input("Enter username for the person: ")
    password=input("Enter password for the person: ")
    if option==1:
        ownerLoginFinal.append([username,password])
    elif option==2:
        managerLoginFinal.append([username,password])
    elif option==3:
        cashierLoginFinal.append([username,password])
    file=open("LoginData.txt","w")
    file.write(":Owners:\n")
    for i in ownerLoginFinal:
        writeStr=i[0]+","+i[1]+"\n"
        file.write(writeStr)
    file.write(":Managers:\n")
    for i in managerLoginFinal:
        writeStr=i[0]+","+i[1]+"\n"
        file.write(writeStr)
    file.write(":Cashiers:\n")
    for i in range(0,len(cashierLoginFinal)):
        writeStr=cashierLoginFinal[i][0]+","+cashierLoginFinal[i][1]
        if not i==len(cashierLoginFinal):
            writeStr+="\n"
        file.write(writeStr)
        
    
    
    
def viewProfit():
    file=open("profit.txt","r")
    m=file.read()
    print(f"Total profit is {m}")
def viewMoney():
    file=open("money.txt","r")
    m=file.read()
    print(f"Total available money is {m}")
    return int(m)
def addMoney():
    money=viewMoney()
    add=int(input("How much money do you want to add? "))
    money+=add
    file=open("money.txt","w")
    file.write(str(money))
    file.close()
def removeMoney():
    money=viewMoney()
    sub=int(input("How much money do you want to extract? "))
    money-=sub
    file=open("money.txt","w")
    file.write(str(money))
    file.close()

    
def ownerLoginDone(ownerName):
    print("In owner login method")
    while True:
        print("What do you want to do?")
        print("1. Manage Dealers")
        print("2. Register a new product")
        print("3. Add a person to the software")
        print("4. View Profit")
        print("5. View Money in the bank")
        print("6. Add investment to the business")
        print("7. Extract money from the bank")
        print("8. Make a bill")
        print("9. Buy things from dealers")
        print("10. View items in the store")
        print("11. View item shortage notification")
        print("12. Logout")
        choice=int(input("Enter option number: "))
        if choice==1:
            manageDealers()
        elif choice==2:
            registerNewProduct()
        elif choice==3:
            addPerson()
        elif choice==4:
            viewProfit()
            input("Press enter to continue")
        elif choice==5:
            viewMoney()
            input("Press enter to continue")
        elif choice==6:
            addMoney()
        elif choice==7:
            removeMoney()
        elif choice==8:
            startBilling(ownerName)
        elif choice==9:
            buyFromDealer(ownerName)
        elif choice==10:
            listItems()
        elif choice==11:
            listShortage()
        else:
            return


def managerLoginDone(managerName):
    while True:
        print("What do you want to do?")
        print("1. Make a bill")
        print("2. Buy things from dealers")
        print("3. View items in the store")
        print("4. View item shortage notification")
        print("5. Logout")
        choice=int(input("Enter option number: "))
        if choice==1:
            startBilling(managerName)
        elif choice==2:
            buyFromDealer(managerName)
        elif choice==3:
            listItems()
        elif choice==4:
            listShortage()
        else:
            return
        

def cashierLoginDone(cashiername):
    while True:
        print("What do you want to do?")
        print("1. Make a bill")
        print("2. Logout")
        choice=int(input("Enter option number: "))
        if choice==2:
            return
        startBilling(cashiername)
        
        


def main():
    file=open("LoginData.txt","r")
    allFileData=file.read()
    process1=allFileData.split(":")
    #print(process1)
    ownerDataRaw=process1[2]
    #print(ownerDataRaw)
    ownerListRaw=ownerDataRaw.split("\n")
    ownerListRefined=ownerListRaw[1:len(ownerListRaw)-1]
    #print(ownerListRefined)
    ownerLoginFinal=[]
    for i in ownerListRefined:
        ownerLoginFinal.append(i.split(","))
    #print(ownerLoginFinal)
    managerDataRaw=process1[4]
    #print(managerDataRaw)
    managerListRaw=managerDataRaw.split("\n")
    managerListRefined=managerListRaw[1:len(managerListRaw)-1]
    #print(managerListRefined)
    managerLoginFinal=[]
    for i in managerListRefined:
        managerLoginFinal.append(i.split(","))
    #print(managerLoginFinal)
    cashierDataRaw=process1[6]
    #print(cashierDataRaw)
    cashierListRaw=cashierDataRaw.split("\n")
    cashierListRefined=cashierListRaw[1:len(cashierListRaw)-1]
    #print(cashierListRefined)
    cashierLoginFinal=[]
    for i in cashierListRefined:
        cashierLoginFinal.append(i.split(","))
    #print(cashierLoginFinal)
    
    loginSuccessful=False
    while not loginSuccessful:
        username=input("Enter your username: ")
        password=input("Enter your password: ")
        loginType=""
        if not loginSuccessful:
            for a in ownerLoginFinal:
                if username==a[0] and password==a[1]:
                    loginSuccessful=True
                    loginType="owner"
        if not loginSuccessful:
            for b in managerLoginFinal:
                if username==b[0] and password==b[1]:
                    loginSuccessful=True
                    loginType="manager"
        if not loginSuccessful:
            for c in cashierLoginFinal:
                if username==c[0] and password==c[1]:
                    loginSuccessful=True
                    loginType="cashier"
        if loginSuccessful:
            print("Log in successfull, type=",loginType)
        else:
            print("Username or password incorrect, please retry")
        if loginType=="owner":
            ownerLoginDone(username)
            print("Logout Successfull")
        elif loginType=="manager":
            managerLoginDone(username)
            print("Logout Successfull")
        elif loginType=="cashier":
            cashierLoginDone(username)
            print("Logout Successfull")
        else:
            print("There was an error in processing the login")
    
main()
