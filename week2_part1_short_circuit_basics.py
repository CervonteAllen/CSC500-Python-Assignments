# Week 2 - Part 1: Short-circuit basics with AND / OR
def left_true():
    print("left_true() ran")
    return True

def left_false():
    print("left_false() ran")
    return False

def right_side():
    print("right_side() ran")
    return True

def main():
    print("Case 1: AND stops on first False")
    result_and = left_false() and right_side()
    print("Result AND:", result_and)
    print()

    print("Case 2: OR stops on first True")
    result_or = left_true() or right_side()
    print("Result OR:", result_or)
    print()

    print("Case 3: OR when left is False -> must check right")
    result_or2 = left_false() or right_side()
    print("Result OR2:", result_or2)

if __name__ == "__main__":
    main()
