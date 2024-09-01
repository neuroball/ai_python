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

"""
In the data we just read in, the fourth column is the player
and the 8th column is the passing yards. Get the sum of
yards from column 8 where the 4th column value is
"Aaron Rodgers"
"""
def get_aaron_rogers_passing_yards(nfl_data):  
    aaron_rogers_passing_yards = 0
    for row in nfl_data:
        if row[3] == "Aaron Rodgers":
            aaron_rogers_passing_yards += int(row[7])
    
    return aaron_rogers_passing_yards

def main():
    nfl_data = read_nfl_data()
    print(get_aaron_rogers_passing_yards(nfl_data))

if __name__ == "__main__":
    main()
