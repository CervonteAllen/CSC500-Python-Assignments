# Week 3 - Part 2: 24-hour alarm time
def main():
    print("24-hour Alarm Calculator")
    now = int(input("Enter current time (0-23): "))
    wait = int(input("Enter hours to wait: "))
    future = (now + wait) % 24
    print(f"Alarm will go off at: {future:02d}:00")

if __name__ == "__main__":
    main()
