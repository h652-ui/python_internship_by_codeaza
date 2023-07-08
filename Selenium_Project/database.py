import mysql.connector
import logging

# Connect to the MySQL database
cnx = mysql.connector.connect(
    host="localhost",    # Replace with your MySQL server host
    user="root",     # Replace with your MySQL username
    password="1234", # Replace with your MySQL password
    database="daraz"  # Replace with your MySQL database name
)

# Function to insert data into the database
def insert_data(data):
    cursor = cnx.cursor()
    # Insert data into the Laptops table
    insert_laptop_query = "INSERT INTO Laptops (title, price, rating) VALUES (%s, %s, %s)"
    laptop_data = (data[0], data[1], data[2])
    cursor.execute(insert_laptop_query, laptop_data)
    laptop_id = cursor.lastrowid
    logging.info(f'ID: {laptop_id} Data Entering!!!')

    # Insert data into the LaptopDetails table
    insert_detail_query = "INSERT INTO LaptopDetails (laptop_id, detail) VALUES (%s, %s)"
    for detail in data[3]:
        detail_data = (laptop_id, detail)
        cursor.execute(insert_detail_query, detail_data)

    # Insert data into the LaptopReviews table
    insert_review_query = "INSERT INTO LaptopReviews (laptop_id, comment, reply) VALUES (%s, %s, %s)"
    for review in data[4]:
        if len(review)==1:
            review.append('')
        review_data = (laptop_id, review[0], review[1])
        cursor.execute(insert_review_query, review_data)
    logging.info(f'ID: {laptop_id} Data Entered!!!')

    cnx.commit()
    cursor.close()
    return