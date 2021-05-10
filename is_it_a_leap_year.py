#!/usr/bin/env python3

# Created by: Luke Beausoleil
# Created on: May 2021
# This program determines whether inputted year is a leap year


def main():
    # this function determines if the year is a leap year

    # input
    year_as_string = input("Enter the year: ")

    # process & output
    try:
        year = int(year_as_string)
        if year > 0:
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        print("\nIt is not a leap year.")
                    else:
                        print("\nIt is a leap year.")
                else:
                    print("\nIt is a leap year.")
            else:
                print("\nIt is not a leap a year.")
        else:
            print("\nInvalid Input.")
    except (Exception):
        print("\nInvalid Input.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
