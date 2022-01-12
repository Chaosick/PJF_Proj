class AllExpenses:
    allExpenses = []

    def addExpense(self, exp):
        self.allExpenses.append(exp)

    def removeExpense(self, exp):
        self.allExpenses.remove(exp)
