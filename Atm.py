import sys
class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber =  cardnumber
        self.pin = pin 

    def balanceinquiry(self):
        print("Your balance is: $10000")

    def cashwidthdrawal(self, amount):
        new_amount = 10000-amount
        print("You withdrawed: " + str(amount) + " Your remaining balance is: " + str(new_amount))

def main():
        name = input("Hello what is your name?")
        print("Hello, " + name)
        cardnumber = input("Insert your card number: ")
        pin = int(input("Enter your pin: "))
        new_user = Atm(cardnumber, pin)

        print("Choose your activity")
        print("1. Balance Inquiry")
        print("2. Cash Withdrawal")
        activity = int(input("Enter activity choice: "))
        
        if (activity == 1):
            new_user.balanceinquiry()
            sys.exit()
        elif (activity == 2):
            amount = int(input("How much d'ye need??: "))
            new_user.cashwidthdrawal(amount)
            sys.exit()
        if(amount>100):
         print("Lol no you don't need that much.. Enter amount below 100.")     
         sys.exit() 
        else:
            print("You stupid Fool")
            sys.exit()

if __name__ == "__main__":
    main()

