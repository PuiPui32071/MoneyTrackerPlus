# src/models/transaction.py

from typing import Dict, Any
from datetime import datetime
from dataclasses import dataclass


class Transaction:
    """
    Class representing a single transaction record.
    """

    def __init__(self, id: int, amount: float, date: datetime, description: str, type: str, category: 'TransactionCategory'):

        """
        Initialize a Transaction instance.

        :param id: The unique identifier of the transaction.
        :type id: int
        :param amount: The amount of the transaction.
        :type amount: float
        :param date: The date of the transaction.
        :type date: datetime
        :param description: The description of the transaction.
        :type description: str
        :param type: The type of the transaction(Income/Expense).
        :type type: str
        :param category: The category of the transaction.
        :type category: TransactionCategory
        """
        self.id = id
        self.amount = amount
        self.date = date
        self.description = description
        self.type = type
        self.category = category

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the transaction to a dictionary format.

        :return: Dictionary representation of the transaction.
        :rtype: Dict[str, Any]
        """
        return {
            'id': self.id,
            'amount': self.amount,
            'date': self.date.isoformat(),
            'description': self.description,
            'type': self.type,
            'category': self.category.name
        }


@dataclass
class TransactionCategory:
    """
    Class representing a transaction category.
    """

    name: str
    type: str

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the transaction category to a dictionary format.

        :return: Dictionary representation of the transaction category.
        :rtype: Dict[str, Any]
        """
        return {
            'name': self.name,
            'type': self.type
        }

    @classmethod
    def from_json(cls, data: Dict[str, Any]) -> 'TransactionCategory':
        """
        Create a TransactionCategory instance from a JSON dictionary.

        :param data: JSON dictionary representing a transaction category.
        :type data: Dict[str, Any]
        :return: TransactionCategory instance.
        :rtype: TransactionCategory
        """
        return cls(name=data['name'], type=data['type'])
    
    @staticmethod
    def predefined_categories() -> Dict[str, 'TransactionCategory']:
        """
        Return a dictionary of predefined categories.

        :return: Dictionary of predefined transaction categories.
        :rtype: Dict[str, TransactionCategory]
        """
        return {
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
        
    def getIconPath(self) -> str:
        """
        Return the path to the icon image file for the transaction category.

        :return: Path to the icon image file.
        :rtype: str
        """
        return f"./images/categories/{self.name}.png"


if __name__ == "__main__":
    # Example usage
    categories = TransactionCategory.get_categories()
    transaction = Transaction(
        id=1,
        amount=50.0,
        date=datetime.now(),
        description="Dinner at a restaurant",
        type = "Expense",
        category=categories["Food & Drinks"]
    )

    print(transaction.to_dict())
