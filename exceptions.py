"""
Custom exception hierarchy for the Personal Finance Tracker.
All exceptions inherit from FinanceTrackerError to allow for unified error handling.
"""

class FinanceTrackerError(Exception):
    """Base exception class for all finance tracker related errors."""
    pass

class AccountNotFoundError(FinanceTrackerError):
    """Raised when looking up an account by name or ID that does not exist."""
    def __init__(self, identifier):
        self.identifier = identifier
        super().__init__(f"Account not found: {identifier}")

class DuplicateAccountError(FinanceTrackerError):
    """Raised when creating an account with a name that already exists."""
    def __init__(self, name):
        self.name = name
        super().__init__(f"Account with name '{name}' already exists.")

class InsufficientFundsError(FinanceTrackerError):
    """Raised when an expense transaction would take an account balance below zero."""
    def __init__(self, account_name, attempted_amount, current_balance):
        self.account_name = account_name
        self.attempted_amount = attempted_amount
        self.current_balance = current_balance
        message = (f"Insufficient funds in '{account_name}'. "
                   f"Attempted: {attempted_amount}, Available: {current_balance}")
        super().__init__(message)

class InvalidTransactionError(FinanceTrackerError):
    """Raised when transaction data fails validation."""
    def __init__(self, field, value):
        self.field = field
        self.value = value
        super().__init__(f"Invalid value '{value}' for field '{field}'.")

class InvalidAmountError(InvalidTransactionError):
    """More specific subclass for when the amount specifically is wrong."""
    def __init__(self, value):
        # Passes "amount" as the field name to the parent InvalidTransactionError
        super().__init__(field="amount", value=value)

class CategoryNotFoundError(FinanceTrackerError):
    """Raised when a category name is not in the known categories list."""
    def __init__(self, category_name):
        self.category_name = category_name
        super().__init__(f"Category '{category_name}' not found.")

class DataCorruptionError(FinanceTrackerError):
    """Raised when the JSON data file exists but cannot be parsed."""
    def __init__(self, filepath, cause):
        self.filepath = filepath
        self.cause = cause
        super().__init__(f"Data at {filepath} is corrupted or invalid. Cause: {cause}")

class CSVImportError(FinanceTrackerError):
    """Raised when a CSV import fails. Named to avoid shadowing built-in ImportError."""
    def __init__(self, filepath, line_number, reason):
        self.filepath = filepath
        self.line_number = line_number
        self.reason = reason
        super().__init__(f"Import failed for {filepath} at line {line_number}: {reason}")

class BackupError(FinanceTrackerError):
    """Raised when a backup operation fails."""
    def __init__(self, source_path, destination_path):
        self.source_path = source_path
        self.destination_path = destination_path
        super().__init__(f"Failed to backup from {source_path} to {destination_path}")

class ExportError(FinanceTrackerError):
    """Raised when a CSV export fails."""
    def __init__(self, destination_path, reason):
        self.destination_path = destination_path
        self.reason = reason
        super().__init__(f"Export to {destination_path} failed: {reason}")