# Currency exchange library
Library for getting UAH( Ukrainian hryvnia) exchange prices.  
Time period and currency, according to which UAH will be rated has to be specified by user.  
Library offers two entities to work with - one based on data from privatbank (https://api.privatbank.ua/#p24/exchangeArchive) , and another - on data from NBU( National Bank of Ukraine) - (https://bank.gov.ua/ua/open-data/api-dev).   
 
# Privatbank data 
  
**Get UAH exchange rate to selected currency for selected time period:**  
object = PrivatbankData(start_time, end_time, currency)  
start_time - string, dd.mm.yyyy  
end_time - string, dd.mm.yyyy  
currency - string, currency code  
**Example:**  
hryvnia = PrivatbankData("5.05.2020", "13.05.2020", "USD")  
  
**Print obtained data:**  
object.print_rates()  

**Plot obtained data:**  
object.plot_rates()  

**Save obtained data to csv file:**  
object.to_csv()  

**Save obtained data to json file:**  
object.to_json()  
  
**Note:**  
Privatbank api is slow to respond, so processing big portions of data using this model might take some time.  

# NBU data 
  
**Get UAH exchange rate to selected currency for selected time period:**  
object = NBUData(start_time, end_time, currency)  
start_time - string, dd.mm.yyyy  
end_time - string, dd.mm.yyyy  
currency - string, currency code  
**Example:**  
tuhryk = NBUData("5.05.2020", "13.05.2020", "NOK")  
  
**Print obtained data:**  
object.print_rates()  

**Plot obtained data:**  
object.plot_rates()  

**Save obtained data to csv file:**  
object.to_csv()  

**Save obtained data to json file:**  
object.to_json()  
  
 **Note:**  
Using this method, obtained dates will be in yyyymmdd format.  

# How to run it  
1. 

