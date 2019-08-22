## Moloco SWE Q2 - Chirag Rao

import csv
import json
from collections import defaultdict


def MostPopularProduct(file):

    ## Implementing hashmaps

    qty = defaultdict(int)
    usr = defaultdict(set)

    for l in file:
        l = json.loads(l[0])
        usr[l["product_id"]].add(l["user_id"])
        qty[l["product_id"]] += l["quantity"]

    Customers = 0
    for u in usr:
        Customers = max(Customers,len(usr[u]))
    no_purchasers = []
    for u in usr:
        if len(usr[u]) == Customers:
            no_purchasers.append(u)

    Quantities = 0
    for q in qty:
        Quantities = max(Quantities, qty[q])
    qty_goods = []
    for q in qty:
        if qty[q] == Quantities:
            qty_goods.append(q)

    print("Most popular product(s) based on the number of purchasers:{0}".format(no_purchasers))
    print("Most popular product(s) based on the quantity of goods sold:{0}".format(qty_goods))

## Execution and reading of the input file
fread = open('SWE sample data - Q2 data.csv','r',encoding='utf-8')
file = csv.reader(fread, delimiter=' ',skipinitialspace=True)
MostPopularProduct(file)
