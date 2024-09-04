import csv

def read_nfl_data():
    file_path = "data/nfl_offensive_stats.csv"
    data = []
    
    with open(file_path, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        
        for row in csv_reader:
            data.append(row)
    
    return data


def calculate_qb_passing_yards(data):
    qb_passing_yards = {}
    
    for row in data:
        position = row[2]
        player = row[3]
        yards = int(row[7])
        
        if position == "QB":
            if player in qb_passing_yards:
                qb_passing_yards[player] += yards
            else:
                qb_passing_yards[player] = yards
    
    return qb_passing_yards


def print_sorted_total_passing_yards(data):
    sorted_total_passing_yards = sorted(data.items(), key=lambda x: x[1], reverse=True)
    
    for player, yards in sorted_total_passing_yards:
        print(f"{player}: {yards} yards")


def main():
    data = read_nfl_data()
    qb_passing_yards = calculate_qb_passing_yards(data)
    print_sorted_total_passing_yards(qb_passing_yards)

if __name__ == "__main__":
    main()