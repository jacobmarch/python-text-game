import sqlite3
from constants import DB_NAME

def create_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        """Create the teams table"""
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY,
            university_name TEXT NOT NULL,
            mascot TEXT NOT NULL,
            offense_rating INTEGER NOT NULL,
            defense_rating INTEGER NOT NULL
        )
        """)


        cursor.execute("""
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            number INTEGER CHECK (number >= 0 AND number <= 99),
            position TEXT CHECK (position IN ('PG', 'SG', 'SF', 'PF', 'C')),
            ath_rating INTEGER NOT NULL,
            off_rating INTEGER NOT NULL,
            def_rating INTEGER NOT NULL,
            int_rating INTEGER NOT NULL,
            team_id INT NOT NULL,
            FOREIGN KEY (team_id) REFERENCES teams(id) ON DELETE CASCADE
            )
            """)

        conn.commit()

def print_team_list():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        cursor.execute("""
        SELECT id, university_name, mascot
        FROM teams""")

        team_list = cursor.fetchall()

        for team in team_list:
            print(f"{team[0]}. {team[1]} {team[2]}")

'''def insert_init_data():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()


        cursor.execute("""
        INSERT INTO teams (university_name, mascot, offense_rating, defense_rating)
            VALUES
            ('University of Illinois', 'Fighting Illini', 80, 85),
            ('Indiana University', 'Hoosiers', 82, 83),
            ('University of Iowa', 'Hawkeyes', 86, 84),
            ('University of Maryland', 'Terrapins', 83, 81),
            ('University of Michigan', 'Wolverines', 88, 87),
            ('Michigan State University', 'Spartans', 85, 86),
            ('University of Minnesota', 'Golden Gophers', 81, 80),
            ('University of Nebraska', 'Cornhuskers', 79, 78),
            ('Northwestern University', 'Wildcats', 78, 77),
            ('Ohio State University', 'Buckeyes', 87, 86),
            ('Penn State University', 'Nittany Lions', 80, 79),
            ('Purdue University', 'Boilermakers', 84, 83),
            ('Rutgers University', 'Scarlet Knights', 82, 81),
            ('University of Wisconsin', 'Badgers', 86, 85);
        """)

        conn.commit()'''







