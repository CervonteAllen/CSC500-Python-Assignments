# Week 4 - ItemToPurchase (two items) and total
class ItemToPurchase:
    def __init__(self, name="none", price=0.0, quantity=0):
        self.item_name = name
        self.item_price = float(price)
        self.item_quantity = int(quantity)

    def print_item_cost(self):
        cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price:g} = ${cost:g}")

def main():
    print("Item 1")
    n1 = input("Enter the item name: ")
    p1 = float(input("Enter the item price: "))
    q1 = int(input("Enter the item quantity: "))
    item1 = ItemToPurchase(n1, p1, q1)

    print("\nItem 2")
    n2 = input("Enter the item name: ")
    p2 = float(input("Enter the item price: "))
    q2 = int(input("Enter the item quantity: "))
    item2 = ItemToPurchase(n2, p2, q2)

    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    total = item1.item_price*item1.item_quantity + item2.item_price*item2.item_quantity
    print(f"Total: ${total:g}")

if __name__ == "__main__":
    main()
