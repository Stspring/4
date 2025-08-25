import pandas as pd
from datetime import datetime

class DataPayWork:
    def __init__(self, file_name):
        self.file_name = file_name
        self.df = pd.read_csv(file_name)

    def __pos__(self):
        total_lines = len(self.df)
        self.df = self.df.drop_duplicates()
        total_deleted = total_lines - len(self.df)
        print(f"Количество повторяющихся строк в наборе данных: {total_deleted}")

    def str_date(self, date_str):
        if pd.notna(date_str):
            return datetime.strptime(date_str, '%d-%m-%Y')
        return None

    def year_sp(self):
        self.df['Дата оплаты'] = self.df['Дата оплаты'].apply(self.str_date)
        self.df.dropna(subset=['Дата оплаты'], inplace=True)
        self.df['Год'] = self.df['Дата оплаты'].dt.year

        self.data_before = self.df[self.df['Год'] < 2014]
        self.data_after = self.df[self.df['Год'] >= 2014]

        self.data_before.to_csv("data_before_2014.csv", index=False)
        self.data_after.to_csv("data_after_2014.csv", index=False)



