import csv
from itertools import islice

with open("data/raw/All_Players_1992-2025.csv", newline="", encoding="utf-8") as f:
    first_2000 = list(islice(csv.DictReader(f), 2000))

print("Rows read: ", len(first_2000))
print("Columns: ", list(first_2000[0].keys())[:10], "...")

players = {r["Player"] for r in first_2000}
squads = {r["Squad"] for r in first_2000}
top_scorers = [r["Player"] for r in first_2000
               if r["Gls"] not in ("", None) and float (r["Gls"])>=10 ]

unique_players = list(dict.fromkeys(players))
unique_squads = list(dict.fromkeys(squads))
print("There are", len(unique_players), "different players in the first 2000 lines!")
print("And", len(unique_squads), "different clubs." )
print("These are the 10 first scorers with more than 10 goals:")
print(list(dict.fromkeys(top_scorers))[:10])