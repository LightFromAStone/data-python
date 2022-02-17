import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


open_file = open('CupcakeInvoices.csv')

# test = '"first_name","last_name","flavor","quantity","unit_price"'
# print(len(test))

total_cost = 0
open_file.seek(59,0)
# print(open_file.tell())
# print(open_file.readline())
for line in open_file:
   items = line.split(',')
   print(items[2])
   invoice_total = float(items[3]) * float(items[4])
   print(format(invoice_total, '.2f'))
   total_cost += invoice_total

print(format(total_cost, '.2f'))

cc = pd.read_csv('CupcakeInvoices.csv')

sns.barplot(x='flavor', y='quantity', palette="ch:.25", data=cc)
plt.show()

open_file.close()