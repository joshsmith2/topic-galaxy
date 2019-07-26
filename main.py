import csv
import itertools


def get_term_edges(terms, data,
                   data_textfield='Text',
                   data_userfield=None):
    """
    Given terms to look for in a dataset, return an edges table describing
    connections between those terms. If 'data_userfield' is specified,
    return a table listing uses of each term by each user.

    :param terms: dict: Terms to look for in Dataset
    :param data: list: Source data
    :
    :return: dict: Gephi edge table formatted connections
    """
    terms_text = [term.lower() for term in terms]
    edges = []
    for document in data:
        text_to_search = document[data_textfield].lower()
        found_terms = [t for t in terms_text if t in text_to_search]
        if data_userfield:
            user_id = document[data_userfield]
            pairs = [(user_id, term) for term in found_terms]
        else:
            pairs = list(itertools.combinations(found_terms, 2))
        edges.extend([{'source': p[0], 'target':p[1]} for p in pairs])
    return edges


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

