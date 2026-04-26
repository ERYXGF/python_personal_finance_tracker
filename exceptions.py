"""
This file contains all the exceptions used in the project.
"""

class FinanceTrackerError(Exception):
    """Raised when the input is invalid."""
    pass

class NotFoundError(FinanceTrackerError):
    """raised when looking up an account by name or ID that does not exist. 
    Stores the account name/ID as an attribute so the error message can include it."""
    
    def __init__(self, item_id):
        self.item_id = item_id
        super().__init__(f"Item with ID {item_id} not found.")

class DuplicateError(FinanceTrackerError):
    """Raised when creating an account with a name that already exists. 
    Stores the conflicting name."""
    
    def __init__(self, name):
        self.name = name
        super().__init__(f"An account with the name '{name}' already exists.")

class InsufficientFundsError(FinanceTrackerError):
    """raised when an expense transaction would take an account balance below zero. 
    Store the account name, the attempted amount and the current balance as separate attributes. 
    The message should clearly state all three"""

    def __init__(self, account_name, attempted_amount, current_balance):
        self.account_name = account_name
        self.attempted_amount = attempted_amount
        self.current_balance = current_balance
        super().__init__(f"Cannot process transaction for account '{account_name}' as the attempted amount({attempted_amount}) exceeds the current balance({current_balance}).")

class InvalidTransactionError(FinanceTrackerError):
    """Raised when transaction data fails validation. 
    Stores the field that failed and the value that was rejected."""

    def __init__(self, field_name, invalid_value):
        self.field_name = field_name
        self.invalid_value = invalid_value
        super().__init__(f"Invalid value '{invalid_value}' for field '{field_name}'.")

class InvalidAmountError(InvalidTransactionError):
    """More specific subclass for when the amount specifically is wrong (negative, zero, non-numeric). 
    Inherits from InvalidTransactionError."""

    def __init__(self, invalid_value):
        self.invalid_value = invalid_value
        super().__init__(f"The value '{invalid_value}' was invalid because of its negative, non-numeric or null nature.")

class CategoryNotFoundError(FinanceTrackerError):
    """Raised when a category name is not in the known categories list."""

    def __init__(self, category_name):
        self.category_name = category_name
        super().__init__(f"Category '{category_name}' not found in known categories.")

class DataCorruptionError(FinanceTrackerError):
    """raised when the JSON data file exists but cannot be parsed or has unexpected structure. Store the filepath and the underlying cause."""
    
    def __init__(self, filepath, cause):
        self.filepath = filepath
        self.cause = cause
        super().__init__(f"Data corruption error for file '{filepath}': {cause}")

class ImportError(FinanceTrackerError):
    """Raised when a CSV import fails. Store the filepath, the line number where failure occurred and the reason. Note: name it CSVImportError to avoid shadowing Python's built-in ImportError."""

    def __init__(self, filepath, line_number, reason):
        self.filepath = filepath
        self.line_number = line_number
        self.reason = reason
        super().__init__(f"Import error for file '{filepath}' at line {line_number}: {reason}")

class BackupError(FinanceTrackerError):
    """Raised when a backup operation fails. Store the source path and destination path."""

    def __init__(self, source_path, destination_path, reason):
        self.source_path = source_path
        self.destination_path = destination_path
        self.reason = reason
        super().__init__(f"Backup error from '{source_path}' to '{destination_path}': {reason}")

class ExportError(FinanceTrackerError):
    """Raised when a CSV export fails. Store the destination path and reason."""

    def __init__(self, destination_path, reason):
        self.destination_path = destination_path
        self.reason = reason
        super().__init__(f"Export error for file '{destination_path}': {reason}")
