# Polymorphism - Real World Payment System
class Payment:
    def __init__(self, amount, currency="INR"):
        self.amount = amount
        self.currency = currency

    def process_payment(self):
        pass

    def receipt(self):
        print(f"\n{'=' * 40}")
        print(f"  PAYMENT RECEIPT")
        print(f"{'=' * 40}")
        print(f"  Amount   : {self.currency} {self.amount}")
        self.process_payment()
        print(f"{'=' * 40}\n")


class CreditCard(Payment):
    def __init__(self, amount, card_number, holder_name):
        super().__init__(amount)
        self.card_number = f"**** **** **** {card_number[-4:]}"
        self.holder_name = holder_name

    def process_payment(self):
        print(f"  Method   : Credit Card")
        print(f"  Card     : {self.card_number}")
        print(f"  Holder   : {self.holder_name}")
        print(f"  Status   : ✅ Payment Approved")


class UPI(Payment):
    def __init__(self, amount, upi_id):
        super().__init__(amount)
        self.upi_id = upi_id

    def process_payment(self):
        print(f"  Method   : UPI")
        print(f"  UPI ID   : {self.upi_id}")
        print(f"  Status   : ✅ Payment Successful")


class NetBanking(Payment):
    def __init__(self, amount, bank_name, account_number):
        super().__init__(amount)
        self.bank_name = bank_name
        self.account_number = f"XX{account_number[-3:]}"

    def process_payment(self):
        print(f"  Method   : Net Banking")
        print(f"  Bank     : {self.bank_name}")
        print(f"  Account  : {self.account_number}")
        print(f"  Status   : ✅ Transfer Complete")


class Crypto(Payment):
    def __init__(self, amount, wallet_address, coin):
        super().__init__(amount, currency=coin)
        self.wallet_address = wallet_address[:6] + "..." + wallet_address[-4:]

    def process_payment(self):
        print(f"  Method   : Crypto")
        print(f"  Wallet   : {self.wallet_address}")
        print(f"  Coin     : {self.currency}")
        print(f"  Status   : ✅ Transaction Confirmed on Blockchain")


transactions = [
    CreditCard(5000, "1234567890123456", "Amit Aswal"),
    UPI(1500, "amit@okicici"),
    NetBanking(12000, "HDFC Bank", "987654321"),
    Crypto(0.005, "1A2b3C4d5E6f7G8h9I", "BTC"),
]

print("\n Processing all payments...\n")

for transaction in transactions:
    transaction.receipt()
