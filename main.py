from prettytable import PrettyTable
import csv
import os
import datetime

products = [                # [soort,maat,stock]
    ["maandverband",1,10], 
    ["maandverband",2,10],
    ["maandverband",3,10],
    ["maandverband",4,10],
    ["tampon",1,10],
    ["tampon",2,10],
    ["tampon",3,10],
]
with open ('transactions.csv','w',newline='') as f:
    writer = csv.writer(f,delimiter=",")
    reader = csv.reader(f,delimiter=",")

product_table = PrettyTable()
#==============================#
def file_setup():
    if not os.path.isfile("transaction.csv"):
        with open("transactions.csv", "w",newline="") as csvfile:
            writer = csv.DictWriter(csvfile,delimiter=",",fieldnames= ["ID","NAME","PRODUCT","PRICE","TIME"])
            writer.writeheader()

product_table.field_names = ["ID","soort","maat","stock"]
index = 0
for product in products:
        index+=1
        product_table.add_row([index,product[0],product[1],product[2]])
def get_trans():
    with open("transactions.csv","r") as csvfile:
        reader_data = csv.DictReader(csvfile,delimiter=",")
        for row in reader_data:
            print(row["ID"],row["NAME"],row["PRODUCT"],row["PRICE"],row["TIME"],sep=" | ")
file_setup()
get_trans()