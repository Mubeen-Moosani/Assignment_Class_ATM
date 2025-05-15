class ATM():
    Balance=5000
    Pin=1234
    def __init__(self,Balance,PIN):
        self.Balance=Balance
        self.Pin=PIN
        
    def __check_pin(self,input_pin:int):
        if(input_pin == self.Pin):
            return True 

        else:
            return False 
    def check_balance(self,input_pin:int):
        if(self.__check_pin(input_pin)):
          print("Current Balance:",self.Balance)
        else:
            print("Invalid PIN")  
    def deposit(self,input_pin:int,amount):
        if(self.__check_pin(input_pin)):
            self.Balance=self.Balance+amount
            print("Amount Added")   
        else:
            print("Invalid PIN")
    def withdraw(self,input_pin:int,amount:int):
         if(self.__check_pin(input_pin)):
             if(self.Balance>=amount and amount>0):
                 self.Balance=self.Balance-amount
                 print("Amount Withdrawal SuccessFully")
             elif(amount<0):
                 print("Please Enter Valid Amount")
             else:
                 print("Insufficient Balance") 
         else:
             print("Invalid PIN")   
mubeen=ATM(6000,4567)
mubeen.deposit(4567,8000)
mubeen.check_balance(4567)
mubeen.withdraw(4567,9000)
mubeen.check_balance(4567)
