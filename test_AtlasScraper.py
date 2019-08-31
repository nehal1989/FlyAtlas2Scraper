import AtlasScraper as AttScr


def test_read_in_file():
    output = AttScr.read_in_file("test_data/test_data_1_file_reading.csv")

    # Check that output is a list
    assert isinstance(output, list)

    # Check that contents of list are all strings
    assert all(isinstance(item, str) for item in output)

    # Check that all gene_names start with FBgn
    assert all([item[:4] == "FBgn" for item in output])


def test_get_gene_data():
    # Check that output is a list
    assert isinstance(AttScr.get_gene_data("FBgn0030313"), str)
    assert isinstance(AttScr.get_gene_data("hello"), str)
    assert isinstance(AttScr.get_gene_data("1234"), str)

    # Check if bad input results in "An error has occurred."
    assert AttScr.get_gene_data("Random thing1") == "An error has occurred.\r\n"
    assert AttScr.get_gene_data("123413") == "An error has occurred.\r\n"
    assert AttScr.get_gene_data("xnnaiunas_wdsnak") == "An error has occurred.\r\n"


def test_request_all_gene_data():
    gene_list = AttScr.read_in_file("test_data/test_data_2_website_response.csv")

    # Check that output is a dictionary
    assert isinstance(AttScr.request_all_gene_data(gene_list), dict)
