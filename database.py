import sqlite3
from datetime import datetime

import pandas as pd

import data_scraper

#ds = data_scraper()



class Database():

    def __init__(self, c_name):
        self.table_name = c_name
        self.conn = sqlite3.connect('stocks.db')
        self.insert_data_cmd = "INSERT INTO {} (Date, Open, High, Low, Close, Volume) VALUES (?, ?, ?, ?, ?, ?)".format(self.table_name)
        self.fetch_data_cmd = "SELECT * FROM {} ORDER BY id DESC LIMIT 200".format(self.table_name)
        self.insert_preds_cmd = "INSERT INTO {}_Preds (Date, Open, High, Low, Close) VALUES (?, ?, ?, ?, ?)".format(self.table_name)
        self.fetch_preds_cmd = "SELECT Date, Open , High, Low , Close FROM {}_Preds WHERE ID = ?".format(self.table_name)

        self.fetch_data_to_plot = "SELECT * FROM {} ORDER BY id DESC LIMIT 100".format(self.table_name)
        self.fetch_preds_to_plot = "SELECT * FROM {}_Preds ORDER BY id DESC LIMIT 100".format(self.table_name)
        self.current_date = datetime.now().strftime("%d-%m-%Y")


    def insert_data_to_db(self,data):

        self.conn.execute(self.insert_data_cmd, (self.current_date, data[0], data[1], data[2], data[4], data[3]))
        self.conn.commit()



    def fetch_data_from_db(self,limit):
        cursor = self.conn.cursor()
        cursor.execute(self.fetch_data_cmd)
        data = cursor.fetchall()
        return data



    def insert_preds_to_db(self,data):
        self.conn.execute(self.insert_preds_cmd, (self.current_date, float(data[0]), float(data[1]), float(data[2]),float(data[3])))
        self.conn.commit()



    def fetch_preds_from_db(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT MAX(id) FROM {}_preds".format(self.table_name))

        # Fetch the result (max 'id' value)
        max_id = cursor.fetchone()[0]

        cursor.execute(self.fetch_preds_cmd, (max_id,))
        data = cursor.fetchall()
        return data

    def fetch_ploting_data(self):
        cursor = self.conn.cursor()
        cursor.execute(self.fetch_data_to_plot)
        actual_data = cursor.fetchall()
        actual_data.pop()
        actual_data = pd.DataFrame(actual_data).sort_index(ascending=False)

        dates = actual_data[1].values
        actual_data.drop(columns=[0,1])



        cursor.execute(self.fetch_preds_to_plot)
        predicted_data = cursor.fetchall()
        predicted_data.pop(0)
        predicted_data = pd.DataFrame(predicted_data).sort_index(ascending=False)

        return actual_data, predicted_data

db = Database("ADAMS")
db.fetch_ploting_data()