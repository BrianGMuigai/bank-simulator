from datetime import datetime

class Transaction:
     
     def __init__(self, transaction_type: str, amount:float, balance_after:float ):

        self.transaction_type = transaction_type
        self.amount = amount
        self.balance_after= balance_after
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self) -> str:
        return(f"[{self.timestamp}]"
               f"{self.transaction_type:<18}"
               f"KES{self.amount:> 10.2f}"
               f"Balance: KES {self.balance_after:.2f}"
               )

