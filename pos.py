#importing date and time module.
import datetime
now = datetime.datetime.now()
date_time = now.strftime("%d-%m-%Y  %H:%M:%S")
#function decison which displays menu aptions takes you where you want to go according to your decision.
def decision():
    k="="
    print(f"\n{k * 60}")
    print("WELCOME TO C*4 INVESTMENTS")
    print("""
    Enter 1. To create account if you are new.
          2. To login if you already have account.
          q. To quit.
    """)
    #code to catch errors if user enter data that is not a string
    try:
        choice = input("Input your choice:\n")

        if choice == "1":
            create_username()
        elif choice == "2":
            log_in()
        elif choice == "q":
            quit()

        else:
            print("Invalid option")
            decision()

    except ValueError:
        print("Invalid input.")
        decision()

#a function create_username which allows us to create account if new to the system.
def create_username():
    x="="

    print(f"\n{x*60}")
    print("WELCOME TO C*4 INVESTMENTS")

    # catching value error to avoid the program from crushing
    try:
        print("Create Account")

        username = input("\nEnter username: \n")
        password = input("Enter password: \n")

        #writing the login details to the text file
        with open("login.txt", "a") as f:
            f.write(username + "," + password + "\n")

            print("Account created successfully. Now open the system again and login.")

            #closing the system to save the login details.
            quit()

    except ValueError:
        print("Invalid input error")
        create_username()

#creating class Pos_system
class Pos_system:

    def __init__(self, total=0, receive=0, change=0):

        print("\nWELCOME TO C*4 INVESTMENTS")

        self.total = total
        self.receive = receive
        self.change = change

    # defining function foods
    def foods(self):
        print("\nC*4 INVESTMENTS STARTING UP..")
        print("\nREADY TO TAKE ORDERS NOW..")
        print("\nONE AT A TIME PLEASE..")

        print("""
    1.Nivea Shower Gel------>$5.40
    2.Nivea Q10------>$7.90
    3.Lux Shower Gel------>$6.00
    4.Avon Lotion------>$9.65

    *. To complete purchase.
    q. To quit.
                                     """)
        #creating lists
        prod = ["Nivea Shower Gel", "Nivea Q10", "Lux Shower Gel", "Avon Lotion"]
        pri = ["$5.40", "$7.90", "$6.00", "$9.65"]
        items = ""
        # the program is going to run until the condition becomes false
        while True:
            try:
                choice = input("Enter your choice:\n")

                # if statements to check the condition of the choice
                if (choice == "1"):

                    quantity = int(input("Enter the quantity:\n"))
                    items += "{:27}{:17}{}\n".format(prod[0], str(quantity), pri[0])
                    self.total = self.total + 5.40 * quantity

                elif (choice == "2"):
                    quantity = int(input("Enter the quantity:\n"))
                    items += "{:27}{:17}{}\n".format(prod[1], str(quantity), pri[1])
                    self.total = self.total + 7.90 * quantity
                elif (choice == "3"):
                    quantity = int(input("Enter the quantity:\n"))
                    items += "{:27}{:17}{}\n".format(prod[2], str(quantity), pri[2])
                    self.total = self.total + 6.00 * quantity
                elif (choice == "4"):
                    quantity = int(input("Enter quantity:\n"))
                    items += "{:27}{:17}{}\n".format(prod[3], str(quantity), pri[3])
                    self.total = self.total + 9.65 * quantity


                elif (choice == "*"):
                    total = self.total
                    if total <= 0:
                        break

                    sub_total = self.total
                    tax = (0.002) * sub_total
                    grand_total = sub_total + tax


                    print("\nTotal:  ${:.2f} ".format(grand_total))
                    # writing to a text file sold.txt
                    f = open("sold.txt", "a")
                    x = "="
                    v = "-"
                    f.write(f"\n{x * 49}")
                    f.write(f"\nNEW SALE\t\t\t\t\t{date_time}")
                    f.write(f"\n{x * 49}")
                    f.write(f"\nItem                      Quantity     Unit Price \n\n{items}")
                    f.write(f"{v * 49}\n")
                    f.write("Total:                                     ${:.2f}".format(total))
                    f.write(f"\n{x * 49}\n\n")
                    f.close()

                    receive = int(input("Input Amount Tendered:\n"))
                    if (receive >= self.total):

                        change = receive - grand_total
                        print("Change: ${:.2f}\n\n\n".format(change))

                        # printing the customer receipt
                        print("=" * 50)
                        print("\t\t\t\tC*4 INVESTMENTS")
                        print("\t\t\tNo. 150, GillChrist WestGate")
                        print("\t\t\t\t(+263) 773 649 006")
                        print("Cashier: ")
                        print(f"{date_time[0:10]}\t\t\t\t\t\t\t\t{date_time[10:]}")
                        print("=" * 50)
                        "\n"
                        print("Item\t\t\t\tQuantity\t\t\tUnit Price")
                        print("-" * 50)
                        print(items)
                        print("")

                        print(
                            f"Sub Total:                                  ${round(sub_total, 2)} ")
                        print(f"Tax:                                         ${round(tax, 2)} ")
                        print(
                            f"Grand Total:                                ${round(grand_total, 2)} ")
                        print("")
                        print(f"Amount Tendered:                            ${round(receive)}.00 ")
                        print(f"Change:                                      ${round(change, 2)}")
                        print("=" * 50)
                        print("\t\t\tTHANK YOU FOR SHOPPING WITH US.\n\t\t\t\t\tCOME AGAIN.")
                        print("=" * 50)
                    #this code runs if the operator enter amount less than amount to be paid
                    else:
                        print("Insufficient funds..")
                # shutting down the system
                elif (choice == "Q".lower()):
                    print("C*4 INVESTMENTS SHUTTING DOWN.")
                    print("GOODBYE!!!")
                    quit()
                else:
                    print("Invalid option")

            # exception error if value input is not a string
            except ValueError:
                print("Invalid input!!...")
                print("Try again.")

#the function login which allows users to login to the system.
def log_in():
    x = "="

    print(f"\n{x * 60}")

    print("WELCOME TO C*4 INVESTMENTS")
    print("\nENTER USERNAME AND PASSWORD TO LOGIN..")


    try:
        success=False
        username = input("\nEnter username: \n")
        password = input("Enter password: \n")

        file=open("login.txt", "r")
        for i in file:
            a,b=i.split(",")
            b=b.strip()
            if (a == username) and (b == password):
                success=True
        file.close()

        file.close()
        if success:
            print("Approved")
            with open("sold.txt", "a") as f:
                f.write(f"\n@ {username}")

            def main():
                a = Pos_system()

                while True:
                    a.foods()

            main()



        else:
            print("Wrong username or password try again")
            log_in()


    except ValueError:
        print("Invalid input.")
        log_in()


#calling the functions
decision()
create_username()
log_in()