import psycopg2
import random
import string
import time
from threading import Thread

# Database connection parameters
db_host = 'your_database_host'
db_name = 'your_database_name'
db_user = 'your_database_user'
db_password = 'your_database_password'

#Could also use connection string
#db_connection_string = "your_connection_string"

# Function to generate random strings
def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

# Function to execute SQL queries
def execute_sql_query(sql_query):
    try:
        conn = psycopg2.connect(host=db_host, dbname=db_name, user=db_user, password=db_password)
        #conn = psycopg2.connect(db_connection_string)
        cursor = conn.cursor() 
        cursor.execute(sql_query) 
        conn.commit() 
    except Exception as e:
        print("Error executing SQL query:", e)
    finally:
        cursor.close()
        conn.close()

# Function to simulate workload
def simulate_write_workload(num_queries):
    for _ in range(num_queries):
        # Generate a random SQL query
        random_string = generate_random_string(10)
        sql_query = f"INSERT INTO your_table_name (column1) VALUES ('{random_string}')"
        execute_sql_query(sql_query)
        # Sleep for a random interval to simulate variable workload
        time.sleep(random.uniform(0.1, 0.5))

#def simulate_read_workload(num_queries):

def setup_table():
    # Create a table in the database
    create_table_query = """
    CREATE TABLE your_table_name (
        id SERIAL PRIMARY KEY,
        column1 VARCHAR(255)
    )
    """
    execute_sql_query(create_table_query)

    # Create an index on the table
    create_index_query = """
    CREATE INDEX idx_column1 ON your_table_name (column1)
    """
    execute_sql_query(create_index_query)

def drop_table():
    # Drop the table from the database
    drop_table_query = """
    DROP TABLE IF EXISTS your_table_name
    """
    execute_sql_query(drop_table_query)

# Main function
def main():
    # Setup table for workload simulation
    setup_table()

    # Define parameters for workload simulation
    num_threads = 10  # Number of concurrent threads
    num_queries_per_thread = 10000  # Number of queries to execute per thread

    # Start multiple threads to simulate concurrent workload
    threads = []
    for _ in range(num_threads):
        thread = Thread(target=simulate_write_workload, args=(num_queries_per_thread,))
        thread.start()
        threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    # Drop table after workload simulation
    drop_table()

if __name__ == "__main__":
    main()
