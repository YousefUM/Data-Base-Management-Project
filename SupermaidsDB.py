import sqlite3
import pandas as pd
from tabulate import tabulate

db_connect = sqlite3.connect('cleaning_services.db')
cursor = db_connect.cursor()

### Part A. Creating Tables ###
# Drop the existing tables if they exist
cursor.execute("DROP TABLE IF EXISTS Client;")
cursor.execute("DROP TABLE IF EXISTS Service;")
cursor.execute("DROP TABLE IF EXISTS Employee;")
cursor.execute("DROP TABLE IF EXISTS Equipment;")
cursor.execute("DROP TABLE IF EXISTS Assigned;")
cursor.execute("DROP TABLE IF EXISTS EquipmentRequirements;")

# Create Client table
query = """
CREATE TABLE Client (
    clientNo INTEGER NOT NULL PRIMARY KEY,
    fName TEXT NOT NULL,
    lName TEXT NOT NULL,
    address TEXT NOT NULL,
    tel TEXT NOT NULL
);
"""
cursor.execute(query)

# Create Service table
query = """
CREATE TABLE Service (
    serviceNo INTEGER NOT NULL PRIMARY KEY,
    clientNo INTEGER NOT NULL,
    startDate DATE NOT NULL,
    startTime TIME NOT NULL,
    duration INTEGER NOT NULL,
    comments TEXT,
    FOREIGN KEY (clientNo) REFERENCES Client(clientNo) ON DELETE CASCADE
);
"""
cursor.execute(query)

# Create Employee table
query = """
CREATE TABLE Employee (
    staffNo INTEGER NOT NULL PRIMARY KEY,
    fName TEXT NOT NULL,
    lName TEXT NOT NULL,
    address TEXT NOT NULL,
    salary DECIMAL(10, 2) NOT NULL,
    tel TEXT NOT NULL
);
"""
cursor.execute(query)

# Create Equipment table
query = """
CREATE TABLE Equipment (
    equipNo INTEGER NOT NULL PRIMARY KEY,
    description TEXT NOT NULL,
    usage TEXT,
    cost DECIMAL(10, 2) NOT NULL
);
"""
cursor.execute(query)

# Create Assigned table
query = """
CREATE TABLE Assigned (
    serviceNo INTEGER NOT NULL,
    staffNo INTEGER NOT NULL,
    PRIMARY KEY (serviceNo, staffNo),
    FOREIGN KEY (serviceNo) REFERENCES Service(serviceNo) ON DELETE CASCADE,
    FOREIGN KEY (staffNo) REFERENCES Employee(staffNo) ON DELETE CASCADE
);
"""
cursor.execute(query)

# Create EquipmentRequirements table
query = """
CREATE TABLE EquipmentRequirements (
    serviceNo INTEGER NOT NULL,
    equipNo INTEGER NOT NULL,
    PRIMARY KEY (serviceNo, equipNo),
    FOREIGN KEY (serviceNo) REFERENCES Service(serviceNo) ON DELETE CASCADE,
    FOREIGN KEY (equipNo) REFERENCES Equipment(equipNo) ON DELETE CASCADE
);
"""
cursor.execute(query)

### Part B. Insert Data into Tables ###
# Client table
query = """
INSERT INTO Client VALUES
(1001, 'John', 'Doe', '123 Ludlam Rd', '555-1234'),
(2002, 'Jane', 'Smith', '456 Killian Dr', '555-5678'),
(3003, 'Oblaw', 'Boblob', '789 Flagami Blvd', '555-3333'),
(4004, 'Maya', 'Mi', '101 Graham Dairy Rd', '555-4444'),
(5005, 'Hiaya', 'Leah', '222 Opa Locka Blvd', '555-5555');
"""
cursor.execute(query)

# Insert data into Service table
query = """
INSERT INTO Service VALUES
(1, 1001, '2023-01-01', '10:00', 60, 'Regular cleaning'),
(2, 2002, '2023-02-01', '14:00', 120, 'Deep cleaning'),
(3, 3003, '2023-03-01', '09:00', 90, 'Regular cleaning'),
(4, 4004, '2023-03-15', '15:00', 120, 'Deep cleaning'),
(5, 4004, '2023-04-01', '10:30', 60, 'Regular cleaning');

"""
cursor.execute(query)

# Insert data into Employee table
query = """
INSERT INTO Employee VALUES
(101, 'Alicia', 'Rodriguez', '789 Miller Dr', 50000.00, '555-1111'),
(102, 'Roberto', 'Perez', '101 Bird Rd', 60000.00, '555-2222'),
(103, 'Emily', 'Correa', '456 Kendall Dr', 55000.00, '555-6666'),
(104, 'James', 'Izquierdo', '789 Miller Dr', 60000.00, '555-7777'),
(105, 'Valerie', 'Gallego', '101 Kendall Rd', 52000.00, '555-8888');
"""
cursor.execute(query)

# Insert data into Equipment table
query = """
INSERT INTO Equipment VALUES
(10101, 'Vacuum Cleaner', 'Carpet cleaning', 200.00),
(20202, 'Floor Scrubber', 'Floor cleaning', 50.00),
(30303, 'Shopvac', 'Floor cleaning', 30.00),
(40404, 'Yellow Mop Bucket', 'Mop cleaning', 25.00),
(50505, 'Scrapper', 'General cleaning', 20.00);
"""
cursor.execute(query)

# Insert data into Assigned table
query = """
INSERT INTO Assigned VALUES
(1, 101),
(2, 102),
(3, 103),
(4, 104),
(5, 104);
"""
cursor.execute(query)

# Insert data into EquipmentRequirements table
query = """
INSERT INTO EquipmentRequirements VALUES
(1, 10101),
(2, 20202),
(3, 30303),
(4, 40404),
(5, 50505);
"""
cursor.execute(query)

# Commit any changes to the database
db_connect.commit()

# Print the Client table
query = "SELECT * FROM Client"
cursor.execute(query)
client_data = cursor.fetchall()
client_df = pd.DataFrame(client_data, columns=[desc[0] for desc in cursor.description])
print("Client Table")
print(tabulate(client_df, headers='keys', tablefmt='pretty'))
print()

# Print the Service table
query = "SELECT * FROM Service"
cursor.execute(query)
service_data = cursor.fetchall()
service_df = pd.DataFrame(service_data, columns=[desc[0] for desc in cursor.description])
print("Service Table")
print(tabulate(service_df, headers='keys', tablefmt='pretty'))
print()

# Print the Employee table
query = "SELECT * FROM Employee"
cursor.execute(query)
employee_data = cursor.fetchall()
employee_df = pd.DataFrame(employee_data, columns=[desc[0] for desc in cursor.description])
print("Employee Table")
print(tabulate(employee_df, headers='keys', tablefmt='pretty'))
print()

# Print the Equipment table
query = "SELECT * FROM Equipment"
cursor.execute(query)
equipment_data = cursor.fetchall()
equipment_df = pd.DataFrame(equipment_data, columns=[desc[0] for desc in cursor.description])
print("Equipment Table")
print(tabulate(equipment_df, headers='keys', tablefmt='pretty'))
print()

# Print the Assigned table
query = "SELECT * FROM Assigned"
cursor.execute(query)
assigned_data = cursor.fetchall()
assigned_df = pd.DataFrame(assigned_data, columns=[desc[0] for desc in cursor.description])
print("Assigned Table")
print(tabulate(assigned_df, headers='keys', tablefmt='pretty'))
print()

# Print the EquipmentRequirements table
query = "SELECT * FROM EquipmentRequirements"
cursor.execute(query)
equipment_req_data = cursor.fetchall()
equipment_req_df = pd.DataFrame(equipment_req_data, columns=[desc[0] for desc in cursor.description])
print("EquipmentRequirements Table")
print(tabulate(equipment_req_df, headers='keys', tablefmt='pretty'))
print()

### Part C: Develop 5 SQL queries using embedded SQL ###
# Query 1: List all clients and the details of the services they have requested.
query1 = """
SELECT c.clientNo, c.fName, c.lName, s.serviceNo, s.startDate, s.startTime, s.duration, s.comments
FROM Client c
JOIN Service s ON c.clientNo = s.clientNo;
"""
cursor.execute(query1)
result1 = cursor.fetchall()
result_df1 = pd.DataFrame(result1, columns=[desc[0] for desc in cursor.description])
print("Query 1: List all clients and the details of the services they have requested.")
print(tabulate(result_df1, headers='keys', tablefmt='pretty'))
print()

# Query 2: Find the total cost of special equipment used in each service.
query2 = """
SELECT er.serviceNo, SUM(e.cost) AS totalEquipmentCost
FROM EquipmentRequirements er
JOIN Equipment e ON er.equipNo = e.equipNo
GROUP BY er.serviceNo;
"""
cursor.execute(query2)
result2 = cursor.fetchall()
result_df2 = pd.DataFrame(result2, columns=[desc[0] for desc in cursor.description])
print("Query 2: Find the total cost of special equipment used in each service.")
print(tabulate(result_df2, headers='keys', tablefmt='pretty'))
print()

# Query 3: Identify employees who are not currently assigned to any service.
query3 = """
SELECT e.staffNo, e.fName, e.lName
FROM Employee e
LEFT JOIN Assigned a ON e.staffNo = a.staffNo
WHERE a.staffNo IS NULL;
"""
cursor.execute(query3)
result3 = cursor.fetchall()
result_df3 = pd.DataFrame(result3, columns=[desc[0] for desc in cursor.description])
print("Query 3: Identify employees who are not currently assigned to any service.")
print(tabulate(result_df3, headers='keys', tablefmt='pretty'))
print()

# Query 4: List clients who have requested cleaning services more than once.
query4 = """
SELECT c.clientNo, c.fName, c.lName, COUNT(s.serviceNo) AS numServiceRequests
FROM Client c
JOIN Service s ON c.clientNo = s.clientNo
GROUP BY c.clientNo
HAVING COUNT(s.serviceNo) > 1;
"""
cursor.execute(query4)
result4 = cursor.fetchall()
result_df4 = pd.DataFrame(result4, columns=[desc[0] for desc in cursor.description])
print("Query 4: List clients who have requested cleaning services more than once.")
print(tabulate(result_df4, headers='keys', tablefmt='pretty'))
print()

# Query 5: Find and list employees that make below the average salary.
query5 = """
SELECT e.fName, e.lName, e.salary
FROM Employee e
WHERE e.salary < (SELECT AVG(e.salary) FROM Employee e);
"""
cursor.execute(query5)
result5 = cursor.fetchall()
result_df5 = pd.DataFrame(result5, columns=[desc[0] for desc in cursor.description])
print("Query 5: Find and list employees that make below the average salary.")
print(tabulate(result_df5, headers='keys', tablefmt='pretty'))
print()

# Close the connection
db_connect.close()




