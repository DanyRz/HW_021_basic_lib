import datetime
import requests
import json
import csv
from matplotlib import pyplot as plt


class BankData:

    def __init__(self, start_time, end_time, currency):
        self.daily_rates = {}
        self.start_time = start_time
        self.end_time = end_time
        self.currency = currency
        self.get_data()

    def get_data(self):
        pass

    def print_rates(self):
        print(f"UAH to {self.currency} from {self.start_time} to {self.end_time} :")
        for date, price in self.daily_rates.items():
            print("Date: " + str(date), " price: " + str(price))

    def plot_rates(self):
        dates = list(self.daily_rates.keys())
        prices = list(self.daily_rates.values())
        plt.plot(dates, prices)
        plt.title(f"UAH to {self.currency}")
        plt.xlabel("Date")
        plt.ylabel(f"UAH for 1 {self.currency}")
        plt.show()

    def to_csv(self):
        daily_rates = [{"date": date, "price": price} for (date, price) in self.daily_rates.items()]
        with open(f"UAH_to_{self.currency}_from_{self.start_time}_to_{self.end_time}.csv", 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["date", "price"])
            writer.writeheader()
            writer.writerows(daily_rates)

    def to_json(self):
        with open(f"UAH_to_{self.currency}_from_{self.start_time}_to_{self.end_time}.json", "w") as jsonfile:
            json.dump(self.daily_rates, jsonfile)


class PrivatbankData(BankData):

    def get_data(self):
        start_time = datetime.datetime.strptime(self.start_time, "%d.%m.%Y")
        end_time = datetime.datetime.strptime(self.end_time, "%d.%m.%Y")
        delta = datetime.timedelta(days=1)
        while start_time <= end_time:
            date = datetime.datetime.strftime(start_time, "%d.%m.%Y")
            url = f"https://api.privatbank.ua/p24api/exchange_rates?json&date={date}"
            rates = requests.get(url)
            uah_rates = rates.json()["exchangeRate"][1:]
            uah_to_currency_rate = [element for element in uah_rates if element['currency'] == self.currency]
            price = uah_to_currency_rate[0]["saleRate"]
            self.daily_rates[date] = price
            start_time += delta


class NBUData(BankData):

    def get_data(self):
        start_time = datetime.datetime.strptime(self.start_time, "%d.%m.%Y")
        end_time = datetime.datetime.strptime(self.end_time, "%d.%m.%Y")
        delta = datetime.timedelta(days=1)
        while start_time <= end_time:
            date = datetime.datetime.strftime(start_time, "%Y%m%d")
            url = f'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date={date}&json'
            rates = requests.get(url)
            uah_rates = rates.json()
            uah_to_currency_rate = [element for element in uah_rates if element['cc'] == self.currency]
            price = uah_to_currency_rate[0]["rate"]
            self.daily_rates[date] = price
            start_time += delta






