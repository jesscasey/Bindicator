import csv


# Return the local authority for the entered postcode.
def find_council(postcode):
    print(f"Finding the local authority for {postcode}...")
    
    # Most postcodes begin with two letters followed by a number (e.g. "AB1") 
    # but some begin with only one (e.g. "B1"). This if-statement checks for 
    # this and adjusts the search term accordingly.
    if postcode[1].isnumeric:
        filename_search = postcode[0]
    else:
        filename_search = postcode[:1]

    # Search the appropriate dataset for the postcode.
    with open(f"dataset/pcd_lad_aug_2023_{filename_search}.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == postcode:
                print(f"The local authority for {postcode} is {row[2]}.")
                next_bin_day(postcode, row[2])
            print("Postcode not found.")


# Return the next bin collection day for the entered postcode.
def next_bin_day(postcode, council):
    print(f"Finding the next bin collection day for {postcode}...")

    # Get the web page containing the council's bin collection information.
    with open("dataset/council_bin_collection_websites.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == council:
                council_website = row[1]
                return
        print(f"Bin collection information for {council} could not be found.")


if __name__ == "__main__":
    postcode = input("Please enter your postcode: ")
    house_no = input("Please enter your house name or number: ")
    find_council(postcode)