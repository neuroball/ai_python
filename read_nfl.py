#!/usr/bin/env python3
"""
open the csv file called "data/nfl_offensive_stats.csv" and read in
the csv data from the file.
"""
import csv


def read_nfl_data():
    
    with open("data/nfl_offensive_stats.csv", "r") as csvfile:
        nfl_data = list(csv.reader(csvfile))
    
    return nfl_data


def main():
    nfl_data = read_nfl_data()
    print(nfl_data)
