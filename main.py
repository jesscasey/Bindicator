import csv

def find_council(postcode):
    print(f"Finding the local authority for {postcode}...")
    
    # Most postcodes begin with two letters followed by a number (e.g. "AB1") 
    # but some begin with only one (e.g. "B1"). This if-statement checks for 
    # this and adjusts the search term accordingly.
    if postcode[1].isnumeric:
        filename_search = postcode[0]
    else:
        filename_search = postcode[:1]

    with open(f"dataset/pcd_lad_aug_2023_{filename_search}.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == postcode:
                print(f"The local authority for {postcode} is {row[2]}.")
                return
            print("Postcode not found.")


if __name__ == "__main__":
    postcode = input("Please enter your postcode: ")
    find_council(postcode)