from guitar import Guitar


def read_file():
    """Reads guitar data from guitars CSV file"""
    guitars = []
    with open("guitars.csv", "r") as guitars_information:
        for line in guitars_information:
            parts = line.strip().split(",")
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)
    return guitars


def main():
    """Reads guitars from CSV, sorts them, and prints the results."""
    guitars = read_file()
    for no_sort_guitar in guitars:
        print(no_sort_guitar)
    guitars.sort()
    print("Sorted Guitars:")
    for guitar in guitars:
        print(guitar)


if __name__ == '__main__':
    main()
