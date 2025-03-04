# This is task 7
""" 7. Personal Budget Advisor
 ● Description   : Build a program to track expenses and income, analyze spending patterns,
                   and provide suggestions for saving money.
 ● Challenges:
                ○ Create a rule-based suggestion system for budgeting.
                ○ Summarize data using percentages and trends.
                ○ Implement error handling for incorrect user inputs.
 ● Skills      : Conditional logic, file I/O, and mathematical calculations.
● Restriction   : No pre-built financial or statistical libraries (e.g., pandas, numpy).
 ● Reason       : This forces students to implement their own methods for handling and
                analyzing financial data. While tools like pandas can make things easier, the goal is for
                students to learn how to manipulate data manually using basic structures like lists,
                dictionaries, and loops. By doing so, they will gain a deeper understanding of data
                analysis without relying on external packages.
 ● Learning Outcome: Students will develop skills in data manipulation, basic statistical
                        analysis, and budgeting algorithms, learning how to create effective financial
                        tracking tools without the aid of external libraries."""
class BudgetAdvisor:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, category, amount):
        self.transactions.append((category, amount))

    def summarize(self):
        summary = {}
        for category, amount in self.transactions:
            summary[category] = summary.get(category, 0) + amount
        return summary

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            for category, amount in self.transactions:
                f.write(f"{category}: {amount}\n")

# Example
advisor = BudgetAdvisor()
advisor.add_transaction("Food", 200)
advisor.add_transaction("Rent", 5000)
advisor.add_transaction("Food", 150)
print(advisor.summarize())
advisor.save_to_file("budget.txt")
