import AtlasScraper as AttScr
import pytest

@pytest.fixture
def test_data_1():
    return AttScr.read_in_file("test_data/test_data_1_file_reading.csv")

@pytest.fixture
def test_data_2():
    return AttScr.read_in_file("test_data/test_data_2_website_response.csv")

def test_read_in_file_is_list(test_data_1):
    assert isinstance(test_data_1, list)

def test_read_in_file_list_contents_are_string(test_data_1):
    assert all(isinstance(item, str) for item in test_data_1)

def test_read_in_file_list_contents_are_begin_with_FBgn(test_data_1):
    assert all([item[:4] == "FBgn" for item in test_data_1])

def test_get_gene_data_return_is_string():
    assert isinstance(AttScr.get_gene_data("FBgn0030313"), str)
    assert isinstance(AttScr.get_gene_data("hello"), str)
    assert isinstance(AttScr.get_gene_data("1234"), str)

def test_get_gene_data_has_correct_error():
    assert AttScr.get_gene_data("Random thing1") == "An error has occurred.\r\n"
    assert AttScr.get_gene_data("123413") == "An error has occurred.\r\n"
    assert AttScr.get_gene_data("xnnaiunas_wdsnak") == "An error has occurred.\r\n"






def test_request_all_gene_data(test_data_2):
    # Check that output is a dictionary
    assert isinstance(AttScr.request_all_gene_data(test_data_2), dict)


def test_request_all_gene_data_for_FBgn0000489_commas_removed():
    gene_name = ['FBgn0000489']
    gene_data = AttScr.request_all_gene_data(gene_name)
    assert gene_data['FBgn0000489'].count(',') == 0