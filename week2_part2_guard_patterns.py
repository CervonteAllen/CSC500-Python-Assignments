# Week 2 - Part 2: Guard patterns using short-circuiting
def safe_divide(a, b):
    # If b is zero, the right side won't run; return None
    return (b != 0) and (a / b) or None

def has_valid_name(user):
    return (user is not None) and bool(getattr(user, "name", ""))

class User:
    def __init__(self, name):
        self.name = name

def main():
    print("Safe divide examples:")
    print("10 / 2 ->", safe_divide(10, 2))
    print("5 / 0  ->", safe_divide(5, 0))
    print()

    print("Validate user name safely:")
    u1 = User("Alex")
    u2 = None
    print("u1 has name? ->", has_valid_name(u1))
    print("u2 has name? ->", has_valid_name(u2))

if __name__ == "__main__":
    main()
