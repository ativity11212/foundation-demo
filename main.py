def riel_to_one_currency():
    try:
        riel = float(input("Enter amount in Riel: "))
        if riel < 0:
            print("Amount must be positive!!!")
            return

        print("\nChoose currency to exchange to:")
        print("1. USD")
        print("2. AUD")
        print("3. Thai Baht (THB)")
        choice = input("Enter your choice : ")

        if choice == '1':
            rate = float(input("Enter exchange rate : "))
            result = riel / rate
            print(f"{riel} Riel = {result:.2f} USD")
        elif choice == '2':
            rate = float(input("Enter exchange rate : "))
            result = riel / rate
            print(f"{riel} Riel = {result:.2f} AUD")
        elif choice == '3':
            rate = float(input("Enter exchange rate : "))
            result = riel / rate
            print(f"{riel} Riel = {result:.2f} THB")
        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter valid numbers.")


def usd_to_one_currency():
    try:
        usd = float(input("Enter amount in USD: "))
        if usd < 0:
            print("Amount must be positive.")
            return

        print("\nChoose currency to exchange to:")
        print("1. Riel")
        print("2. AUD")
        print("3. Thai Baht (THB)")
        choice = input("Enter your choice : ")

        if choice == '1':
            rate = float(input("Enter exchange rate: "))
            result = usd * rate3
            print(f"{usd} USD = {result:.2f} Riel")
        elif choice == '2':
            rate = float(input("Enter exchange rate: "))
            result = usd * rate
            print(f"{usd} USD = {result:.2f} AUD")
        elif choice == '3':
            rate = float(input("Enter exchange: "))
            result = usd * rate
            print(f"{usd} USD = {result:.2f} THB")
        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter valid numbers.")


def main():
    while True:
        print("\n=== Currency Exchange Menu ===")
        print("1. Exchange from Riel to one currency (USD, AUD, THB)")
        print("2. Exchange from USD to one currency (Riel, AUD, THB)")
        print("3. Exit")

        choice = input("Select an option (1-3): ")

        if choice == '1':
            riel_to_one_currency()
        elif choice == '2':
            usd_to_one_currency()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
