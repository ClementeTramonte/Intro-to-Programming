def print_menu():
    print("Taco Palace Menu")
    print("1. Taco")
    print("2. Burrito")
    print("3. Nachos")
    print("4. Soft Drink")
    print("5. Quit")


def get_price(selection):
    if selection == 1:
        return 2.50
    elif selection == 2:
        return 3.50
    elif selection == 3:
        return 4.00
    elif selection == 4:
        return 1.45
    return 0.00


def get_item_name(selection):
    if selection == 1:
        return "Taco"
    elif selection == 2:
        return "Burrito"
    elif selection == 3:
        return "Nachos"
    elif selection == 4:
        return "Soft Drink"
    return ""


def main():
    order_list = []
    total_price = 0.0

    print("Welcome to Taco Palace, please view the menu below and enter the number that represents your selection.")

    while True:
        print_menu()

        try:
            user_input = input("User entered: ")
            selection = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if selection == 5:
            break
        elif selection in [1, 2, 3, 4]:
            item_name = get_item_name(selection)
            price = get_price(selection)

            order_list.append(item_name)
            total_price += price

            print(f"You selected a {item_name}")
        else:
            print("Invalid selection. Please enter a number between 1 and 5.")

    if order_list:
        order_summary = ", ".join(order_list)
        print(f"You ordered a {order_summary}. Your total is ${total_price:.2f}")
    else:
        print("No items were ordered. Thank you for visiting Taco Palace!")


if __name__ == "__main__":
    main()