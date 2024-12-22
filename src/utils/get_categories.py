from models.transaction import TransactionCategory 


perdifinedCategories = {
            "Allowance": TransactionCategory(name="Allowance", type="Income"),
            "Bonus": TransactionCategory(name="Bonus", type="Income"),
            "Clothes": TransactionCategory(name="Clothes", type="Expense"),
            "Education": TransactionCategory(name="Education", type="Expense"),
            "Entertainment": TransactionCategory(name="Entertainment", type="Expense"),
            "Food & Drinks": TransactionCategory(name="Food & Drinks", type="Expense"),
            "Housing & Utilities": TransactionCategory(name="Housing & Utilities", type="Expense"),
            "Personal": TransactionCategory(name="Personal", type="Expense"),
            "Salary": TransactionCategory(name="Salary", type="Income"),
            "Transportation": TransactionCategory(name="Transportation", type="Expense"),
        }

class getCategories():
    
    def setUp(self):
        categories = TransactionCategory.predefined_categories().values()
        return categories