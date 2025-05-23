def is_leap_year(year):
    if (year % 400 == 0) and (year % 100 == 0) or \
        (year % 4 == 0) and (year % 100 != 0):
        return True
    else:
        return False
    
def main():
    print("\n=== 📅 Leap Year 📅 ===\n")
    year = int(input("Enter a year: "))
    if is_leap_year(year):
        print(year, "is a leap year!\n")
    else:
        print(year, "is not a leap year.\n")

main()