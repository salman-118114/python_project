from datetime import datetime
import csv

class Transaction:
    def __init__(self,date,category,amount,description):
        self.date = date
        self.category = category
        self.amount = amount
        self.description = description


class FinanceTracker():

    def __init__(self):
        self.transactions = []

    def add_transaction(self,transaction):
        self.transactions.append(transaction)
        print("transaction added")

    def view_transactions(self):
       if not self.transactions:
           print("No transactions")
       else:
           for t in self.transactions:
               print(f"Date:{t.date} | category: {t.category} | Amount:{t.amount} | Description:{t.description}")

    #filter by category
    def filter_by_category(self,category):
        filtered = [t for t in self.transactions if t.category.lower() == category.lower()]

        if not filtered:
            print("No transactions for this category")
        else:
            for t in filtered:
               print(f"Date:{t.date} | category: {t.category} | Amount:{t.amount} | Description:{t.description}")

    #generate financial report
    def generate_financial_report(self):

        total_income = sum([t.amount for t in self.transactions if t.category.lower() == 'income' ])
        total_expenses = sum([t.amount for t in self.transactions if t.category.lower() == 'expenses' ])

        Remaining_balance = total_income - total_expenses
        
        print("--Your financial report--")
        print(f"TOtal income so far: {total_income}")
        print(f"Total expenses so far: {total_expenses}")
        print(f"Remaining balance: {Remaining_balance}")
    
    #save transactions to csv file
    def save_to_csv(self,filename):

        with open(filename,'w',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["date","category","amount","description"])
            for i in self.transactions:
                writer.writerow([i.date,i.category,i.amount,i.description])
            
        print(f"transaction saved to csv file: {filename}")

    #load transactions from csv file
    def load_from_csv(self,filename):
        try:
            with open(filename,'r') as f:
                reader = csv.reader(f)
                next(reader) # skip header
                for row in reader:
                    date = row[0]
                    category = row[1]
                    amount = row[2]
                    description = row[3]
                    self.transactions.append(Transaction(date,category,amount,description))
            print(f"transactions loaded from file: {filename}" )
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except Exception as e:
            print(f"Error loading transactions: {e}")




#main function to execute code
def main():

    Tracker = FinanceTracker()

    while True:
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Filter by Category")
        print("4. Generate Financial Report")
        print("5. Save to CSV")
        print("6. load_from_csv")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = datetime.now()
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            Tracker.add_transaction(Transaction(date,category,amount,description))
        elif choice == "2":
            Tracker.view_transactions()
        elif choice == "3":
            category = input("Enter category: ")
            Tracker.filter_by_category(category)
        elif choice == "4":
            Tracker.generate_financial_report()
        elif choice == "5":
            filename = input("enter filename:")
            Tracker.save_to_csv(filename)
        elif choice == "6":
            filename = input("enter filename:")
            Tracker.load_from_csv(filename)
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

#run the program
if __name__ == "__main__":
    main()
