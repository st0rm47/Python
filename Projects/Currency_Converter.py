class CurrencyConverter:
    def __init__(self):
        # Dictionary to store exchange rates
        self.exchange_rates = {
            1: ("USD to INR", 86.20),
            2: ("USD to EUR", 0.98),
            3: ("USD to GBP", 0.82),
            4: ("USD to NPR", 138.30),
            5: ("EUR to USD", 1.03),
            6: ("GBP to USD", 1.22),
            7: ("INR to USD", 0.012),
            8: ("NPR to USD", 0.0072),
        }

    def convert_currency(self, rate, amount):
        return amount * rate

    def display_menu(self):
        print("\nAvailable currency pairs:")
        for key, value in self.exchange_rates.items():
            print(f"{key}. {value[0]}")

    def run(self):
        while True:
            print("\nCurrency Converter")
            print("===================")
            self.display_menu()
            print("Type '0' to exit.")
            
            # Get user selection
            try:
                choice = int(input("Enter the number corresponding to your choice: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue
            
            if choice == 0:
                print("Exiting the Currency Converter. Goodbye!")
                break

            if choice in self.exchange_rates:
                amount = input("Enter the amount to convert: ")
                if amount.replace('.', '', 1).isdigit():
                    amount = float(amount)
                    rate = self.exchange_rates[choice][1]
                    result = self.convert_currency(rate, amount)
                    print(f"{amount} in {self.exchange_rates[choice][0].split()[0]} is {result:.2f} in {self.exchange_rates[choice][0].split()[-1]}.")
                else:
                    print("Invalid input! Please enter a numeric value for the amount.")
            else:
                print("Invalid choice! Please select a valid option from the menu.")

if __name__ == "__main__":
    converter = CurrencyConverter()
    converter.run()
