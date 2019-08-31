import requests
import csv

def scrape_fly_atlas2():
    pass

def read_in_file(gene_list: str)->list:
    with open(gene_list) as csv_file:
        reader = csv.reader(csv_file)
        gene_name_list = [row[0] for row in reader if row[0][:4]=='FBgn']
        return gene_name_list

def get_gene_data(gene_name: str)->str:
    url = f"http://flyatlas.gla.ac.uk/FA2Direct/index.html?fbgn={gene_name}&tableOut=gene"
    r = requests.get(url)
    r.raise_for_status()
    return r.text