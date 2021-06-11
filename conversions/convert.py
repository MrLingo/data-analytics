import mysql.connector
import csv
import sys
import datetime


csv_filename = 'dataset.csv'

# Connect to server.
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password"
)

# Get header/column names.
extracted_rows = []
column_names = []
data = []
with open(csv_filename, mode='r') as file:
    spamreader = csv.reader(file)
    for row in spamreader:
        extracted_rows.append(row)

cut_portion = len(extracted_rows)-1
column_names = extracted_rows[:-cut_portion]
data = extracted_rows[1:]

# Organize.
columns_clean = []
for x in column_names:
    for y in x:
        columns_clean.append(y)

# Ask user input for datatypes.
attributes = []
print('\n' + str(len(columns_clean)) + ' columns detected. Please assign datatype to each one.')
print('(int, varchar, datetime)\n')
for col in columns_clean:
    datatype = str(input("Datatype for column '" + str(col) + "'?:"))
    if datatype == 'int':
        col = col +' INT'
    elif datatype == 'varchar':
        char_range = str(input('Enter character range:'))
        col = col +' VARCHAR(' + char_range +')'
    elif datatype == 'datetime':
        col = col + ' DATETIME'
    else:
        print('Invalid data! Type one of the three possible choices.')
        sys.exit()
    attributes.append(col)

attributes = ', '.join(attributes)

# Dynamic values:
db_name = 'demo_db'
table_name = 'demo_table'
create_db_query = 'CREATE DATABASE IF NOT EXISTS {}'.format(db_name)
use_query = 'USE {}'.format(db_name)
create_table_query = 'CREATE TABLE IF NOT EXISTS {} (ID INT AUTO_INCREMENT, {}, PRIMARY KEY(ID));'.format(table_name, attributes)

mycursor = mydb.cursor(buffered=True)
mycursor.execute(create_db_query)
mycursor.execute(use_query)
mycursor.execute(create_table_query)

columns = ', '.join(columns_clean)
placeholders = []

# Get placeholder count.
for ph in range(len(data[0])):
    placeholders.append('%s')

placeholders = ', '.join(placeholders)

# Cast and insert data.
for values in data:
    values_clean = []   
    for x in values:
        # Different rule for datetime.
        try:
            x = datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
            values_clean.append(x)
            continue
        except:
            pass
        try:
            x = int(x)
            values_clean.append(x)
        except:
            x = str(x)
            values_clean.append(x)

    sql = "INSERT INTO {} ({}) VALUES ({})".format(table_name, columns, placeholders)
    print(values_clean)
    mycursor.execute(sql, tuple(values_clean))
    mydb.commit()

mycursor.execute('SELECT * FROM ' + str(table_name))
my_result = mycursor.fetchall()

#for x in my_result:
#    print(x)

print('All data successfully inserted. Check your database.')
