import requests

def get_stock_data(ticker):
    api_key = '396b50ec957e8582dad78eb37675d3d5'

    endpoints = [
        f'https://financialmodelingprep.com/api/v3/profile/{ticker}?apikey={api_key}',
        f'https://financialmodelingprep.com/api/v3/financial-growth/{ticker}?apikey={api_key}',
        f'https://financialmodelingprep.com/api/v3/ratios/{ticker}?apikey={api_key}'
    ]

    try:
        for endpoint in endpoints:
            response = requests.get(endpoint)
            data = response.json()
            if 'error' in data:
                print(f"Error: {data['error']}")
                return
            else:
                if '/profile/' in endpoint:
                    profile = data[0]
                    print(f"Symbol: {profile['symbol']}")
                    print(f"Company Name: {profile['companyName']}")
                    print(f"Price: {profile['price']}")
                    print(f"Exchange: {profile['exchange']}")
                elif '/financial-growth/' in endpoint:
                    if isinstance(data, list):  # Check if data is a list
                        for item in data:
                            print(f"Year: {item['date']}")
                            print(f"Revenue Growth: {item['revenueGrowth']}")
                            print(f"Operating Cash Flow Growth: {item['operatingCashFlowGrowth']}")
                            print(f"Free Cash Flow Growth: {item['freeCashFlowGrowth']}")
                            print()
                elif '/ratios/' in endpoint:
                    ratios = data[0]
                    print(f"Current Ratio: {ratios['currentRatio']}")
                    print(f"Quick Ratio: {ratios['quickRatio']}")
                    print(f"Free Cash Flow per Share: {ratios['freeCashFlowPerShare']}")
                    print(f"P/E Ratio: {ratios['priceEarningsRatio']}")
                print()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

def main():
    while True:
        ticker = input("Enter a stock ticker symbol (type 'exit' to quit): ").upper()
        if ticker == 'EXIT':
            break
        get_stock_data(ticker)

if __name__ == "__main__":
    main()