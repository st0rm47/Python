def km_to_miles(km):
    return km * 0.621371

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    while True:
        print("\nUnit Converter")
        print("=================")
        print("1. Kilometers to Miles")
        print("2. Celsius to Fahrenheit")
        print("3. Exit")
        
        try:
            option = int(input("Choose an option (1-3): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 3.")
            continue
        
        if option == 1:
            try:
                km = float(input("Enter the value in kilometers: "))
                miles = km_to_miles(km)
                print(f"{km} kilometers = {miles:.2f} miles.")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
                
        elif option == 2:
            try:
                celsius = float(input("Enter the value in Celsius: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"{celsius} Celsius = {fahrenheit:.2f} Fahrenheit.")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
                
        elif option == 3:
            print("Exiting the Unit Converter. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please select a valid option (1-3).")

if __name__ == "__main__":
    main()
