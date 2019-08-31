import AtlasScraper as AttScr

def test_read_in_file():
    output = AttScr.read_in_file('test_data/test_data_1_file_reading.csv')

    # Check that output is a list
    assert isinstance(output, list)

    # Check that contents of list are all strings
    assert all(isinstance(item, str) for item in output)

    # Check that all gene_names start with FBgn
    assert all([item[:4] == 'FBgn' for item in output])

def test_get_gene_data():
    # Check that output is a list
    assert isinstance(AttScr.get_gene_data('FBgn0030313'), str)
    assert isinstance(AttScr.get_gene_data('hello'), str)
    assert isinstance(AttScr.get_gene_data('1234'), str)