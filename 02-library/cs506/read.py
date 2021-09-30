def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    results = []
    with open(csv_file_path, 'r') as f:
        for line in f:
            words = line.split(',')
            results.append(words)
    return results
