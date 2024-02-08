def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    print("Temperature Converter Program\n")
    while True:
        try:
            choice = int(input("Choose conversion direction:\n1. Fahrenheit to Celsius\n2. Celsius to Fahrenheit\n3. Exit\n"))
            if choice == 1:
                f_temp = float(input("Enter temperature in Fahrenheit: "))
                c_temp = fahrenheit_to_celsius(f_temp)
                print(f"{f_temp}°F is equal to {c_temp:.2f}°C\n")
            elif choice == 2:
                c_temp = float(input("Enter temperature in Celsius: "))
                f_temp = celsius_to_fahrenheit(c_temp)
                print(f"{c_temp}°C is equal to {f_temp:.2f}°F\n")
            elif choice == 3:
                print("Exiting program...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.\n")
        except ValueError:
            print("Invalid input. Please enter a valid temperature value.\n")

if __name__ == "__main__":
    main()
