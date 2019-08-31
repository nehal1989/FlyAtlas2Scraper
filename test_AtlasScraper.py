import AtlasScraper

def test_read_in_file():

    output = AtlasScraper.read_in_file('test_data/test_data1.csv')

    # Check that output is a list
    assert isinstance(output, list)

    # Check that contents of list are all strings
    assert all(isinstance(item, str) for item in output)

    # Check that all gene_names start with FBgn
    assert all([item[:4] == 'FBgn' for item in output])