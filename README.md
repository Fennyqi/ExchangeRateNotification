# ExchangeRateNotification

## Setup

Create and activate a virtual environment:

```sh
conda create -n my-env python=3.10

conda activate my-env
```


Install packages:

```sh
pip install -r requirements.txt
```

Obtain an [API Key from CurrencyLayer]( https://currencylayer.com) 

Follow the [setup instructions]( https://currencylayer.com/documentation) to create an account, verify your account, setup a single sender, and obtain an API Key.

Create a ".env" file and paste in the following contents:


# this is the ".env" file...

Email_API_Key  = "_________"

Sender_Address ="_________"

Rate_API_Key ="_________"

## Usage

Run the exchange rate fetch function:

```sh
python -m app.fetch
```