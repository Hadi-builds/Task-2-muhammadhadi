def expense_tracker():
    # 1. State Initialization (must be outside the loop to persist memory)
    total_spent = 0.0

    print("=== DecodeLabs Expense Tracker ===")
    print("Enter your expense amount or type 'quit' to finish.\n")

    # 2. Continuous Audit Loop
    while True:
        user_input = input("Enter expense ($): ").strip()

        # 3. Sentinel Value / Emergency Stop
        if user_input.lower() == 'quit':
            break

        # 4. Defensive Type Safety & Accumulator
        try:
            expense = float(user_input)
            
            if expense < 0:
                print("Expense cannot be negative. Please enter a valid amount.")
                continue

            total_spent += expense
            print(f"Added: ${expense:.2f} | Current Total: ${total_spent:.2f}\n")

        except ValueError:
            print("Invalid input! Please enter a numerical value (or 'quit' to exit).\n")

    # 5. Final Output Display
    print("\n" + "=" * 35)
    print(f"FINAL TOTAL SPENT: ${total_spent:.2f}")
    print("=" * 35)
if __name__ == "__main__":
    expense_tracker()