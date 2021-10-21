class parkingLot():
    listofavailableslot = [1,2,3,4,5]
    usedslot = []

def parkmycar():
    print(f"Available parking slots : {parkingLot.listofavailableslot}")
    choice = input("Do you want to park car ? Press Y/y or M/m for main menu or any other key to exit :").lower()
    if choice == "y":
        slotchoice = int(input(f"choose from the available slots displayed above !"))
        if slotchoice in parkingLot.listofavailableslot:
            parkingLot.listofavailableslot.remove(slotchoice)
            parkingLot.usedslot.append(slotchoice)
            choice2 = input(f"Car parked successfully at slot {slotchoice}.Select M/m for main menu or any other key to exit :")
            if choice2 == "m":
                main()
            else:
                print("Thanks for Visiting !")
        else:
            choice2 = input("Invalid slot selected : For parking options type A/a or any other key to exit :")
            if choice2 == "a":
                parkmycar()
            else:
                print("Thanks for Visiting !")
    elif choice == "m":
        main()
    else:
        print("Thanks for Visiting !")

def checkoutcar():
    print(parkingLot.listofavailableslot)
    print(parkingLot.usedslot)
    if len(parkingLot.usedslot) == 0:
        print("Currently No Cars are parked")
        choice2 = input("Select M/m for main menu or any other key to exit :")
        if choice2 == "m":
            main()
        else:
            print("Thanks for Visiting !")
    else:
        slottoberemove = int(input("Plese provide your slot number: "))

        if slottoberemove in parkingLot.usedslot:
            parkingLot.usedslot.remove(slottoberemove)
            parkingLot.listofavailableslot.append(slottoberemove)
            choice2 = input(f"Car checked out successfully from slot {slottoberemove}.Select M/m for main menu or any other key to exit :")
            if choice2 == "m":
                main()
            else:
                print("Thanks for Visiting !")
        else:
            choice2 = input("Invalid slot selected : For car check out options type A/a or any other key to exit :")
            if choice2 == "a":
                checkoutcar()
            else:
                print("Thanks for Visiting !")

def main():
    print("Welcome to the Parking Lot !")
    firstoption = input("Press C for checking availability / O/o for car checkout any other key for exit/  :").lower()
    if firstoption == "c":
        if len(parkingLot.listofavailableslot) == 0:
            print("No slots available ... try again later")
        else:
            print()
            parkmycar()
    elif firstoption == "o":
        checkoutcar()
    else:
        print("Thanks for Visiting !")

main()
