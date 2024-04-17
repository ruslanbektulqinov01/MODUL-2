import sqlite3
import sys


class FinanceManager:
    def __init__(self, db):
        self.db = db
        self.create_table()

    def create_table(self):
        cursor = self.db.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                type TEXT,
                amount REAL
            )
            """
        )
        self.db.commit()

    def earn(self, amount):
        cursor = self.db.cursor()
        cursor.execute(
            """
            INSERT INTO transactions (type, amount)
            VALUES (?, ?)
            """,
            ('earn', amount)
        )
        self.db.commit()

    def spend(self, amount):
        cursor = self.db.cursor()
        cursor.execute(
            """
            INSERT INTO transactions (type, amount)
            VALUES (?, ?)
            """,
            ('spend', amount)
        )
        self.db.commit()

    def balance(self):
        cursor = self.db.cursor()
        cursor.execute(
            """
            SELECT SUM(CASE WHEN type='earn' THEN amount ELSE -amount END) AS balance
            FROM transactions
            """
        )
        result = cursor.fetchone()
        return result[0] if result[0] is not None else 0.0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit("Usage: python finance.py <command> [amount]")

    command = sys.argv[1]
    if command not in ('earn', 'spend', 'balance'):
        sys.exit("Invalid command. Available commands: earn, spend, balance")

    with sqlite3.connect("finance.db") as db:
        manager = FinanceManager(db)

        if command == 'earn':
            if len(sys.argv) != 3:
                sys.exit("Usage: python finance.py earn <amount>")
            amount = float(sys.argv[2])
            manager.earn(amount)
            print(f"Earned ${amount}")

        elif command == 'spend':
            if len(sys.argv) != 3:
                sys.exit("Usage: python finance.py spend <amount>")
            amount = float(sys.argv[2])
            manager.spend(amount)
            print(f"Spent ${amount}")

        elif command == 'balance':
            current_balance = manager.balance()
            print(f"Current Balance: ${current_balance}")
