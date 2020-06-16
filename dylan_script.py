import csv
import sqlite3

try:
    # Connect database
    sqliteConnection = sqlite3.connect('db.sqlite')
    cursor = sqliteConnection.cursor()
    sqliteConnection.text_factory = str
    print("Database created and Successfully Connected to SQLite")

    sql_delete_query = """DELETE from branchproducts"""
    cursor.execute(sql_delete_query)
    sqliteConnection.commit()

    sql_delete_query = """DELETE from products"""
    cursor.execute(sql_delete_query)
    sqliteConnection.commit()

    with open('prices_stock_modified.csv', 'r') as file:
        reader = csv.reader(file)
        index = 0
        for row in reader:
            if index == 0:
                index = index + 1
                continue

            id = row[0]
            productId = row[1]
            branch = row[2]
            stock = row[3]
            price = row[4]

            # Execute query
            count = cursor.execute("INSERT INTO branchproducts (id, product_id, branch, stock, price) VALUES(?, ?, ?, ?, ?)", (id, productId, branch, stock, price))

            print("INSERT branchproducts SUCCESS")
            sqliteConnection.commit()

    with open('products_modified.csv', 'rU') as file:
        reader = csv.reader(file)
        index = 0
        for row in reader:
            if index == 0:
                index = index + 1
                continue

            id = row[0]
            sku = row[1]
            barcodes = row[2]
            name = row[3]
            description = row[4]
            imageUrl = row[5]
            caterogy = row[6]
            brand = row[7]

            # Execute query
            count = cursor.execute("INSERT INTO products (id, store, sku, barcodes, brand, name, description, package, image_url, category, url) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (id, "", sku, barcodes, brand, name, description, "", imageUrl, caterogy, ""))

            print("INSERT SUCCESS")
            sqliteConnection.commit()

    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")
