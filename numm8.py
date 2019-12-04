class MoneyFmt:
    def __init__(self,cash):
        self.cash = cash

    def update(self,cash):
        self.cash = cash

    def repr(self,cash):
        self.cash = cash
        self.cash = float(input("Enter your integer: "))

    def str(self):
        if self.cash >= 0:
            return '${:,.2f}'.format(self.cash)
        else:
            return '-${:,.2f}'.format(-self.cash)


cash_user = MoneyFmt(1546547835.84739)
print(cash_user.str())
cash_user.update(137635.795)
print(cash_user.str())
cash_user.repr(436346)
print(cash_user.str())


