from account import Account
from savings_account import SavingsAccount 


class  BankingApp:

    def __init__(self):

           self.accounts = {}
           self._seed_accounts()


    def run(self):

           print("╔══════════════════════════════════╗")
           print("║    Python Banking Simulator      ║")
           print("╚══════════════════════════════════╝")

           while True:

               self._print_menu()
               choice = self._read_int(" Choose option: ")

               match choice:
                   case 1: self._create_account()
                   case 2: self._deposit()
                   case 3: self._withdraw()
                   case 4: self._check_balance()
                   case 5: self._view_history()
                   case 6: self._list_accounts()
                   case 7: self._apply_interest()
                   case 0: 
                        print("\n  Goodbye! Thank you for banking with us.")
                        break
                   case -:
                        print(" [!] Invalid option. Try again.")


    def _create_account(self):
            print("\n --- Create Account ---")
            acc_type  = self._read_int("   Type (1) Checking (2) Savings -> ")
            name      = self._read_text("  Owner name: ")
            opening   = self._read_float(" Opening deposit (KES): ")

            if acc_type ==2:
            rate    = self._read_float("Interest rate (e.g. 0.05 for 5%"):
            account = SavingsAccount(name, opening, rate)

            else: 
                account = Account(name, opening )


            self.accounts[ account.account_id ] = account
            print(f"  [✓] Account created: {account.account_id}")

     def _deposit(self):
         account = self._find_account()
         if not account: 
             return

        acc_desc = self._read_text("Add description? (y/n): ").lower()

        if acc_desc == "y":
            desc     = self._read_text("description (e.g. Salary): ")
            amount   = self._read_float("Amount (KES): ")

            amount.deposit(amount, desc)

        else:
            amount = self._read_float("Amount  (KES): ")
            account.deposit(amount)

    def _withdraw(self):
        account = self._find_account()
        if not account:
            return
        amount = self._read_float("  Amount (KES): ")
        account.withdraw(amount)

    def _check_balance(self):
        account = self._find_account()
        if not account:
            return
        print(f"\n Balance for {account.owner_name}: KES {account.balance:.2f}")

    def _view_history(self):
        account = self._find_account()
        if not account: 
            return
        account.print_history()

    def _list_accounts(self):
        print("\n  --- All Accounts ---")
        if not self.accounts:
            return

        for account in self.accounts.value():
            print(f" {account}")

    def _apply_interest(self):
        account = self._find_account()
        if not account:
            return

        if isintance(account, SavingsAccount):
            account._apply_interest()
        else:
            print("  [!] Interest only applies to savings accounts.")


    def _find_account(self):
        """ Prompt for an account ID and retrun the Account, or None."""
        account_id = self._read_text("\n Accounts ID (e.g. ACC-1001): ").upper()

        account= self.accounts.get(account_id)

        if account is None:
            print(f"  [!] Account not found: {account_id}")
        return account

    def _read_int(self, prompt: str ) -> int:
        """Keep asking until the user types a valid integer."""
        while True:
            try:
                return int(input(prompt).strip())
            except ValueError:
                print("  [!] Please enter a whole number. ")

    def _read_float(self, prompt:str ) -> float:
        """Keep asking until the user types a valid number."""
        while True:
            try:
                return float(input(prompt).strip())
            except ValueError:
                print("  [!] Please enter a valid number.")

    def _read_text(self, prompt:str) -> str:
        """Keep asking until the user types something non-empty."""
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("  [!] Input cannot be empty.")

    def _print_menu(self):

        print("""
  ┌─────────────────────────────┐
  │  1. Create account          │
  │  2. Deposit                 │
  │  3. Withdraw                │
  │  4. Check balance           │
  │  5. Transaction history     │
  │  6. List all accounts       │
  │  7. Apply interest          │
  │  0. Exit                    │
  └─────────────────────────────┘""")
    def _seed_accounts(self):
        """Pre-load two demo accounts so the app isn't empty on launch."""
        alice = Account("Alice Kamau", 5000.00)
        alice.deposit(2500.00, "Salary")
        alice.withdraw(800.00)

        bob = SavingsAccount("Bob Otieno", 10000.00, 0.05)
        bob.deposit(3000.00)

        self.accounts[alice.account_id] = alice
        self.accounts[bob.account_id]   = bob
        print("  [seed] Two demo accounts loaded. Use option 6 to list them.\n")

if __name__ = "__main__":
    BankingApp().run()
























