import json
import pandas as pd
import statistics as st

from logging import exception
from time import sleep
from datetime import datetime, timedelta


#fetch one day's exchange rate

def get_exchange_rate(date):
    url = "http://api.currencylayer.com/historical"
    access_key = "Rate_API_Key"

    params = {
        "access_key": access_key,
        "date": date, #strftime('%Y-%m-%d'),
        "source": "USD",
        "currencies": "CNY",
        "format": "1"
    }

    response = requests.get(url, params=params)
    parse_response = json.loads(response.text)
    try:
      return parse_response['quotes']['USDCNY']
    except Exception as err:
      print (err)
      print (parse_response)
      return None


# get a list of past 30 days' exchange rate
def get_past_thirty_days_rates(sleep_seconds=1):
    today = datetime.today()

    exchange_rates = []
    for i in range(30, 0, -1):  # Counting from 30 to 1
        date_to_fetch = today - timedelta(days=i)
        date_str = date_to_fetch.strftime('%Y-%m-%d')

        rate = get_exchange_rate(date_str)
        print(date_str, rate)
        exchange_rates.append({"date": date_str, "rate": rate}) # keep adding exchange rates to the lsit

        sleep(sleep_seconds)

    return exchange_rates


# get the exchange rate for today
today_date = datetime.today().strftime('%Y-%m-%d')
today_rate = get_exchange_rate(today_date)

# get the exchange rates for the past 30 days
rates = get_past_thirty_days_rates()

# convert list to dataframe
rates_df = DataFrame(rates)
print(rates)

# Calculate mean and standard deviation of the 'rate' column in rates_df
mean = rates_df['rate'].mean()
stdev = rates_df['rate'].std()

# Replace cny_rate with the specific rate you want to calculate the Z-score for
cny_rate =  # Put the value of the specific rate here

z_score = (today_rate - mean) / stdev

print("Mean:", mean)
print("Standard Deviation:", stdev)
print("Z-score:", z_score)

# email

from getpass import getpass
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = getpass("Email_API_Key")
SENDER_ADDRESS = getpass("Sender_Address")

def send_email(recipient_address=SENDER_ADDRESS, subject="[Notice] Low Exchange Rate", html_content="<p>Hello World</p>"):
    print("SENDING EMAIL TO:", recipient_address)
    print("SUBJECT:", subject)
    print("HTML:", html_content)

    client = SendGridAPIClient(SENDGRID_API_KEY)
    print("CLIENT:", type(client))

    message = Mail(from_email=SENDER_ADDRESS, to_emails=recipient_address, subject=subject, html_content=html_content)

    try:
        response = client.send(message)

        print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
        print(response.status_code) #> 202 indicates SUCCESS
        print(response.body)
        print(response.headers)
        return response.status_code

    except Exception as err:
        print(type(err))
        print(err)
        return None


if __name__ == "__main__":

    # only want to do if running this file from command line
    # not when importing a function from this file
    user_address= input("Please enter your email address:")

     # !!!! need to replace currency and exchange rate with variables!
     # could add a graph showing how rates changed

    my_content = """

        <h1> Low Exchange Rate Right Now </h1>


        <p> 1 USD = 7 RMB </p>

    """

if z_score<-1.5: # can change the standard upon further analysis
    send_email(html_content=my_content, recipient_address=user_address)
