'''Complete the function printTransactions that takes a float m money left,
an integer k number of stocks, an integer d days left, 
a string array name of stock names, an integer array owned of stocks owned, 
and an 2d integer array prices of stock prices containing k arrays of length 5 
and print your output.'''

import math

def printTransactions(m, k, d, name, owned, prices):
    transactions = []
    for i in range(k):
        current_price = prices[i][-1]
        avg_price = sum(prices[i])/len(prices[i])
        if current_price > avg_price and m > 0:
            # sell the stock
            transactions.append((name[i], "SELL", owned[i]))
            m += current_price * owned[i]
            owned[i] = 0
        elif current_price < avg_price and m >= current_price:
            # buy the stock
            shares_to_buy = math.floor(m/current_price)
            transactions.append((name[i], "BUY", shares_to_buy))
            m -= current_price * shares_to_buy
            owned[i] += shares_to_buy
    num_transactions = len(transactions)
    print(num_transactions)
    for i in range(num_transactions):
        print(transactions[i][0], transactions[i][1], transactions[i][2])

# example usage with sample input
m = 90
k = 2
d = 400
name = ["iStreet", "HR"]
owned = [10, 0]
prices = [[4.54, 5.53, 6.56, 5.54, 7.60], [30.54, 27.53, 24.42, 20.11, 17.50]]
printTransactions(m, k, d, name, owned, prices)
