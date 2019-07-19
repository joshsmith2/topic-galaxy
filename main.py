import csv

def get_data_from_csv(csv_path):
    """
    Given a CSV path, return a dictionary containing its data
    :param csv_path: str: Path to CSV to load
    :return: dict: Dictionary containing that CSV's data
    """
    with open(csv_path, 'r', encoding='utf-8-sig') as csv_file:
        reader = csv.DictReader(csv_file)
        data = [line for line in reader]
    return data

def main():
    pass

if __name__ == "__main__":
    main()

