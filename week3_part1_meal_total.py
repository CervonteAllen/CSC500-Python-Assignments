# Week 3 - Part 1: Meal total with tip and tax
def main():
    print("Meal Total Calculator (Tip 18%, Tax 7%)")
    food = float(input("Enter charge for the food: "))
    tip = food * 0.18
    tax = food * 0.07
    total = food + tip + tax
    print(f"Tip (18%): ${tip:.2f}")
    print(f"Tax (7%): ${tax:.2f}")
    print(f"Total: ${total:.2f}")

if __name__ == "__main__":
    main()
