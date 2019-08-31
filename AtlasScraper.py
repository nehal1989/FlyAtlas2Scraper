import requests
import csv
from time import sleep


def scrape_fly_atlas2(gene_list_file: str, output_file: str):
    # Function takes fly atlas gene list to generate text containing scraped gene info.
    gene_name_list = read_in_file(gene_list_file)
    gene_data_dict = request_all_gene_data(gene_name_list)
    generate_output_text_file(gene_data_dict, output_file)


def read_in_file(gene_list: str) -> list:
    # Function reads in a csv file and outputs a gene list
    with open(gene_list) as csv_file:
        reader = csv.reader(csv_file)
        gene_name_list = [row[0] for row in reader if row[0][:4] == "FBgn"]
        return gene_name_list


def get_gene_data(gene_name: str) -> str:
    # Function accepts a gene name and requests the information rom flyatlas. Returns the text.
    url = (
        f"http://flyatlas.gla.ac.uk/FA2Direct/index.html?fbgn={gene_name}&tableOut=gene"
    )
    r = requests.get(url)
    r.raise_for_status()
    return r.text


def request_all_gene_data(gene_name_list: list) -> dict:
    # Function that accepts a cleaned up name of gene lists and returns the gene data as a dict
    # with gene name as key and gene data as value
    gene_data_dict = {}
    number_of_genes = len(gene_name_list)
    for idx, gene_name in enumerate(gene_name_list, 1):
        gene_data = get_gene_data(gene_name)
        sleep(1)
        gene_data_dict[gene_name] = gene_data
        print(
            f"{idx} of {number_of_genes} requested. {round(idx/number_of_genes*100,1)}% complete."
        )
    return gene_data_dict


def generate_output_text_file(gene_data_dict: dict, output_file_name: str):
    # Function which takes gene data dictionary and makes a big text file for parsing in Pandas.
    for gene_info in gene_data_dict.values():
        with open(output_file_name, "a", encoding="utf-8") as file:
            file.write(gene_info)
