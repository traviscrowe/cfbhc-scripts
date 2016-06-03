"""
Utility functions for wikitable stat parsing
"""
import sys
import requests
from lxml import etree


def parse_table_header(query_data):
    """
    Parses out the header of the stat table
    """
    page = requests.get(query_data.page_link)
    tree = etree.fromstring(page.text)
    table_header = tree.xpath(query_data.table_path + '//th')

    return table_header


def parse_table_data(query_data):
    """
    Parses out the data of the stat table
    """
    page = requests.get(query_data.page_link)
    tree = etree.fromstring(page.text)
    table_data = tree.xpath(query_data.table_path + '//tr/td')

    return table_data


def chunk_player_data(table_data=[], cols=int):
    """
    Chunks out rows from stat table
    """
    players = []

    for _ in range(0, len(table_data), cols):
        player = table_data[_:_+cols]
        players.append(player)

    return players


def get_csv_file(query_data):
    """
    Generates CSV file to save data set to
    """
    file = 'data/' + str(query_data.year) + '_' + str(query_data.league)
    if query_data.table == 1:
        return  file + '_quarterbacks.csv'
    elif query_data.table == 2:
        return file + '_running_backs.csv'
    elif query_data.table == 3:
        return file + '_wide_receivers.csv'
    elif query_data.table == 4:
        return file + '_defenders.csv'
    elif query_data.table == 5:
        return file + '_kickers.csv'
    elif query_data.table == 6:
        return file + '_returners.csv'


def update_progress(progress):
    """
    Progress bar
    """
    sys.stdout.write('\r[{0}] {1}%'.format('#'*(progress/10), progress))
