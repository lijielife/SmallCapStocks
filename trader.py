#!/usr/bin/env python2
# coding: utf-8

import re
import easytrader

PLATFORM = 'ht'
CONFIG_FILE = 'account.json'

class trader:
    def __init__(self):
        self.user = easytrader.use(PLATFORM)
        self.user.prepare(CONFIG_FILE)
        self.holding = {i['stock_code']:i for i in self.user.position} 
        self.balance = self.user.balance[0]
        self.enable_balance = self.balance['enable_balance']

    def buy(self, stock, amount, price):
        print 'Buy stock: %s, amount: %s, price: %s' % (stock, amount, price)
        result = self.user.buy(stock, amount=amount, price=price)

    def sell(self, stock, amount, price):
        print 'Sell stock: %s, amount: %s, price: %s' % (stock, amount, price)
        result = self.user.sell(stock, amount=amount, price=price)

if __name__ == '__main__':
    t = trader()
