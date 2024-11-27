import mysql.connector
from mysql.connector import errorcode
import random

# Generate 100 sample health records
def generate_sample_records():
    first_names = ['John', 'Jane', 'Alice', 'Bob', 'Carol', 'Michael', 'Sara', 'Tom', 'Anna', 'David']
    last_names = ['Smith', 'Doe', 'Brown', 'Johnson', 'Davis', 'Wilson', 'Taylor', 'Anderson', 'Thomas', 'Lee']
    health_conditions = [
        'No significant medical history',
        'Mild allergies',
        'Diabetes type 2',
        'Hypertension',
        'Asthma',
        'Seasonal flu',
        'Migraine',
        'Chronic pain',
        'Healthy',
        'Arthritis'
    ]

    records = []
    for _ in range(100):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        gender = random.choice([1, 0])  # 1 for male, 0 for female
        age = random.randint(18, 70)
        weight = round(random.uniform(50.0, 100.0), 1)
        height = round(random.uniform(150.0, 200.0), 1)
        health_history = random.choice(health_conditions)

        records.append((first_name, last_name, gender, age, weight, height, health_history))
    return records

# Initialize the database and insert sample data
def initialize_database():
    try:
        # Connect to MySQL
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Homesh@99"
        )
        cursor = conn.cursor()

        # Create database and switch to it
        cursor.execute("CREATE DATABASE IF NOT EXISTS secure_health_db")
        cursor.execute("USE secure_health_db")

        # Create tables
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS health_info (
                id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                gender BOOLEAN,
                age INT,
                weight FLOAT,
                height FLOAT,
                health_history TEXT
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                username VARCHAR(50) PRIMARY KEY,
                password VARBINARY(60),
                user_group CHAR(1) CHECK (user_group IN ('H', 'R'))
            )
        """)

        # Insert predefined sample data
        predefined_data = [
            ('John', 'Smith', 1, 35, 75.5, 180.5, 'No significant medical history'),
            ('Jane', 'Doe', 0, 28, 62.3, 165.2, 'Mild allergies'),
            ('Alice', 'Brown', 0, 42, 68.0, 170.0, 'Diabetes type 2'),
            ('Bob', 'Johnson', 1, 50, 80.0, 175.0, 'Hypertension'),
            ('Carol', 'Davis', 0, 33, 55.0, 160.0, 'Asthma')
        ]

        cursor.executemany("""
            INSERT INTO health_info (first_name, last_name, gender, age, weight, height, health_history)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, predefined_data)

        # Insert dynamically generated sample data
        sample_records = generate_sample_records()
        cursor.executemany("""
            INSERT INTO health_info (first_name, last_name, gender, age, weight, height, health_history)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, sample_records)

        conn.commit()
        print(f"Database initialized with {len(predefined_data) + len(sample_records)} records.")
        
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    initialize_database()
