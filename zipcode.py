from banner import banner
banner("ZIP CODE SORTER", "Gavin Orcutt")

print("Welcome to the Newaygo County zip code sorter")

zip_book = {
    "49309": "Bitely",
    "49312": "Brohman",
    "49337": "Croton",
    "49412": "Fremont",
    "49413": "Fremont",
    "49327": "Grant",
    "49337": "Newaygo",
    "49349": "White Cloud",
}

def main():
    contin = "Y"
    while contin.capitalize() != "N" and contin.capitalize() != "NO":
        test_zip(get_zip())
        contin = ask_for_continue()
    print("Thank you for using Newaygo County Zip Code Sorter. Goodbye!")

def get_zip():
    return input("Please enter a zip code: ")

def test_zip(zipcode):
    if zipcode in zip_book:
        print(f"The zipcode {zipcode} is for {zip_book[zipcode]}.")
    else:
        print(f"The zipcode {zipcode} is not in Newaygo County.")

def ask_for_continue():
    return input("Would you like to enter another zip code (Y/N)? ")

main()