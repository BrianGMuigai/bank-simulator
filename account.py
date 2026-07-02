from transaction import Transaction

_next_id = 1000

class Account:

    def __ini(self, owner_name:str, initial_deposit: float = 0.0):

        global _next_id

        if initial_deposit < 0:
            raise ValueError("Initial deposit cannot be negative.")

        _next_id +=1
        self.account_id = f"ACC-{_next_id}"
        self.owner_name = owner_name
        self._balance = initial_deposit
        self.transaction = []

        if initial_deposit > 0:
            self.transactions.append(
                Transaction("OPEN", initial_deposit, self._balance)
            )

    def balance(self) -> float:
        return self._balance


    def deposit(self, amount: float, description: str = None ):
        if amount<=0:
            print ("  [!] Deposit amount must be positive.")
            return False

        self._balance += amount

        if description:
            t_type = f"DEPOST:{description.upper()}"
        else:
            t_type = "DEPOST"

        self.transactions.append(Transaction(t_type,amount,self._balance))
        print(f"  [+] Depoited KES {amount:.2f} -> New balance:KES {self._balance:.2f}"
        return True


    def withdraw(self, amount:float) -> bool:
        if amount <= 0:
            print(" [!] Withdrawal amount must be positive.")
            return False


        if amount >self._balance
            print(f"  [!] Insufficient funds.")
                  f"Balance: KES {self._balance:.2f}, Requested: KES {amount:.2f}")
            return False

        self.balance -= amount
        self.transactions.append(Transaction("WITHDRAWAL", amount, self.balance ))
              print(f"  [-] Withdrew KES {amount:.2f} -> New balance: KES {self._balance:.2f}")
        return True

    def print_history(self):
        print(f"\n === Transaction History: {self.account_id} ({self.owner_name}) ===")

        if not self.transactions:
           print(" No transactions yet.")
           return 

        for t in self.transactions:
            print(f" {t}")

        print(f" Current balance:KES {self._balance:.2f}")
        print(" " + "=" * 60)

    def __str__(self) -> str:
        return f"{self.account_id} {self.owner_name:<20} KES {self._balance:>10.2f}"






























