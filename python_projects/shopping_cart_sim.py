def main():
    cart = {}
    while True:
        print("Choose any one of the options to continue:")
        print("1.Add items\n2.Update items\n3.Remove items\n4.View cart\n5.View Total\n6.Checkout")
        option = int(input())
        if option == 1:
            while True:
                items = input("Enter the item's name, to exit enter 'exit': ")
                if items == 'exit':
                    break
                price = int(input("Enter the price: "))
                quantity = int(input("Enter the quantity: "))
                if items in cart:
                    cart[items]["quantity"] = quantity
                    cart[items]["price"] = price
                else:
                    cart[items] = {"quantity": quantity, "price": price}
        elif option == 2:
            while True:
                u_item = input("Enter the item to be updated: ")
                if u_item in cart:
                    u_price = int(input("Price: "))
                    u_quantity = int(input("Quantity: "))
                    cart[u_item] = {"quantity": u_quantity, "price": u_price}
                    break
                else:
                    print("Enter the correct item.")
                    pass
        elif option == 3:
            while True:
                d_item = input("Enter the item to be deleted: ")
                if d_item in cart:
                    del cart[d_item]
                    print("Item deleted.")
                    break
                else:
                    print("Choose the correct item.")
                    pass
        elif option == 4:
            if cart:
                print("\nItems in your cart:")
                for item, details in cart.items():
                    print(f"{item.title()}: {details['quantity']},  price: {details['price']}")
            else:
                print("Your cart is empty.")
        elif option == 5:
            total_cost = 0
            for item in cart.values():
                total_cost += item["price"] * item["quantity"]
            print("Total cost:", total_cost)
        elif option == 6:
            print("Are you sure you want to checkout?")
            ans = input("(Yes/No): ").lower()
            if ans == ("y", "yes"):
                print("Thank you for your patience.")
                break
            break
        else:
            raise ValueError("Choose the correct option.")


if __name__ == "__main__":
    main()