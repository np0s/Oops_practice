# 8. Create an ATM class with hidden PIN and verification method.
class ATM:
    def __init__(self, account_holder, pin):
        self.account_holder = account_holder
        self.__pin = pin  

    def verify_pin(self, pin):
        return self.__pin == pin
atm = ATM("Charlie", "1234")
print(f"Account Holder: {atm.account_holder}")
print(f"PIN Verified: {atm.verify_pin('1234')}")