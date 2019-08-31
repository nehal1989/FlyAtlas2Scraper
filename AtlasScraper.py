import requests
import csv

def scrape_fly_atlas2():
    pass

def read_in_file(gene_list: str):
    with open(gene_list) as csv_file:
        reader = csv.reader(csv_file)
        gene_name_list = [row[0] for row in reader if row[0][:4]=='FBgn']
        return gene_name_list