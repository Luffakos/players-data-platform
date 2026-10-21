import duckdb
from pathlib import Path

print(Path("data/warehouse.duckdb").resolve())
con = duckdb.connect("data/warehouse.duckdb")
print(con.execute("SHOW TABLES").fetchall())

con.sql("""
 CREATE OR REPLACE TABLE players AS
 SELECT * FROM read_csv_auto('data/raw/All_Players_1992-2025.csv')
""")
# Example
con.sql("""
 SELECT Player, Squad, Season, Gls, xG
 FROM players
 WHERE Season = '2022-2023' AND Gls >= 15
 ORDER BY Gls DESC
 LIMIT 10
""").show()

# Top 20 goalscorers 2003-2004
con.sql('''
SELECT Player, Squad, Season, Gls
FROM players
WHERE Season = '2003-2004'
ORDER BY Gls DESC
LIMIT 20;
''').show()

# Number of Seasons, Teams and Leagues
con.sql('''
SELECT
    COUNT(DISTINCT Season) as number_of_seasons
    COUNT(DISTINCT League) as number_of_leagues
    COUNT(DISTINCT Squad) as number_of_teams
FROM players;
''')

# Attakers (Position = FW) over 35 who have scored more than 10 goals
con.sql('''
SELECT Player, Squad, Season, Age, Gls
FROM players
WHERE Gls > 9 and Age > 35 and Pos like '%FW%'
ORDER BY Gls DESC;
''')