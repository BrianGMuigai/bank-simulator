from account import Account
from transaction import Transaction



class SavingsAccount(Account)

    MINIMUM_BALANCE = 500.00

    def __init__(self, owner_name:str, intial_deposit:float, interest_rate:float ):

        super().__init__(owner_name, intial_deposit)

        if interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        self.interest_rate = interest_rate

    def withdrawal(self, amount:float) -> bool:
        if self._balance - amount < self._balance - self.MINIMUM_BALANCE:

            max_withdrawal = self._balance - self.MINIMUM_BALANCE
            
            print(f"  [!] Savings accounts require a minimum balance"
                  f"of KES {self.MINIMUM_BALANCE:.2F}.")
            
            print(f"      Max you can withdraw:KES {max_withdrawal:.2f}")
            
            return False

        return super().withdrawal(amount)

    def apply_interest(self):
        """ Add interest to the balance."""
        
        interest = self._balance * self.interest_rate

        self.transactions.append(
            Transaction("INTEREST", interest, self._balance)
        )

        print(f" [%] Interest applied:KES {interest:.2f}"
              f"({self.interest_rate * 100:.1f}%) -> "
              f"New balance:KES {self.-balance:.2f}")

    def __str__(self) -> str:
        return f"[SAVINGS] {super().__str__()} Rate: {self.interest_rate * 100:.1f }%"

