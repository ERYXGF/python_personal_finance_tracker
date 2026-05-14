"""
This file defines the Category class, which represents a category of financial transactions
in the application.
"""

from exceptions import InvalidTransactionError, DataCorruptionError
from logger import logger

class Category:
    """
    Represents a financial transaction category.
    Has a type (income/expense), a name, and an optional description.
    Provides serialization (to_dict / from_dict).
    Provides a class-level factory for default categories.
    """
    DEFAULT_CATEGORIES = {
        "income":[
            "Salary",
            "Freelance",
            "Investment",
            "Gift",
            "Other Income"
            ],
        "expense":[
            "Food",
            "Transport",
            "Entertainment",
            "Health",
            "Education",
            "Rent",
            "Utilities",
            "Clothing",
            "Other Expense"
            ]
    }

    def __init__(self, name, category_type, description=""):

        if not isinstance(category_type, str) or category_type not in ("income", "expense"):
            logger.error(f"Invalid category_type: {category_type!r}")
            raise InvalidTransactionError("category_type", category_type)

        if not isinstance(name, str):
            logger.error(f"Invalid name: {name!r}")
            raise InvalidTransactionError("name", name)

        name = name.strip().title()

        if not name:
            logger.error(f"Invalid name: {name!r}")
            raise InvalidTransactionError("name", name)

        if not isinstance(description, str):
            logger.error(f"Invalid description: {description!r}")
            raise InvalidTransactionError("description", description)

        self.name = name
        self.category_type = category_type
        self.description = description.strip()
        logger.debug(f"Category created: {self.name}, {self.category_type}")

    def is_income(self):
        """
        Returns a boolean on whether the category is classified as income.
        """
        return self.category_type == "income"

    def is_expense(self):
        """
        Returns a boolean on whether the category is classified as expense.
        """
        return self.category_type == "expense"

    def __str__(self):
        return f"[{self.category_type.capitalize()}] {self.name}"

    def __repr__(self):
        return f"Category(name={self.name!r}, category_type={self.category_type!r}, description={self.description!r})"


    def to_dict(self):
        """
        Converts the Category object to a dict.
        """
        return {
            "name": self.name,
            "type": self.category_type,
            "description": self.description,
        }

    @classmethod
    def create_default_categories(cls):
        """
        Returns a list of the default categories.
        """
        result = []
        for name in cls.DEFAULT_CATEGORIES["income"]:
            result.append(cls(name=name, category_type="income"))
        for name in cls.DEFAULT_CATEGORIES["expense"]:
            result.append(cls(name=name, category_type="expense"))
        return result


    @classmethod
    def from_dict(cls, data):
        """
        Reconstructs from dictionary
        """
        if "name" not in data:
            raise DataCorruptionError(None, "Missing required key: 'name' in data")

        if "type" not in data:
            raise DataCorruptionError(None, "Missing required key: 'type' in data")

        return cls(
            name=data["name"],
            category_type=data["type"],
            description=data.get("description", "")
        )
