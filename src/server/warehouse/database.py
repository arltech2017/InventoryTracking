#!/usr/bin/env python3.6
# coding=utf-8
import random
import json
from footwear import Boot, DressShoe, CasualShoe

import unqlite


def make_catalog(n):
    styles = (("Cowboy", "Hiking", "Rain", "Riding"),
              ("Loafer", "Oxford", "Pump", "Sling-back", "Wing-tip"),
              ("Athletic", "Hightop", "Moccasin", "Sandal"))

    sizes = (5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5,
             12, 12.5, 13, 13.5, 14)

    catalog = []

    for i in range(n):
        fwtype = random.randint(0, len(styles)-1)
        style = random.choice(styles[fwtype])
        size = random.choice(sizes)
        sku = "1234-" + str(i)

        if fwtype == 0:
            catalog.append(Boot(style, size, sku))
        elif fwtype == 1:
            catalog.append(DressShoe(style, size, sku))
        else:
            catalog.append(CasualShoe(style, size, sku))

    return catalog


def get_catalog(fname):
    """Read catalog from json encoded fname file."""
    f = open(fname, 'r')
    catdat = f.read()
    f.close()
    catalog = json.loads(catdat)
    for index, item in enumerate(catalog):
        style, size, sku = item['style'], item['size'], item['sku']
        if item['type'] == 'Boot':
            catalog[index] = Boot(style, size, sku)
        elif item['type'] == 'DressShoe':
            catalog[index] = DressShoe(style, size, sku)
        else:
            catalog[index] = CasualShoe(style, size, sku)

    return catalog


def save_catalog(catalog, fname):
    """Write catalog to json encoded fname file."""
    f = open(fname, 'w')
    catalog = [item.__dict__ for item in catalog]
    f.write(json.dumps(catalog))
    f.close()


class Warehouse_DB():
    def __init__(self, name):
        self.db = unqlite.UnQLite(name)
        self.bins = self.db.collection('bins')
        if not self.bins.exists():
            self.bins.create()
        self.shoes = self.db.collection('shoes')
        if not self.shoes.exists():
            self.shoes.create()

    def add_sku_to_bin(self, num, sku):
        """select style, size, sku, type from thing"""
        self.bins.store({'bin': num,
                         'sku': str(sku)})

    def del_sku_from_bin(self, num, sku):
        """ DELETE localhost/api/warehouse/bin{#}/{sku} """
        things = self.bins.filter(lambda bin: bin['bin'] == num and bin['sku'] ==
                str(sku))
        for bin in things:
            self.bins.delete(bin['__id'])

    def register_shoe(self, size, style, sku):
        """ PUT localhost/api/warehouse/{sku} """
        self.shoes.store({'sku': str(sku),
                          'size': size,
                          'style': style})

    def get_bin_info(self, num):
        """ GET localhost/api/warehouse/bin{#} """
        return [bin for bin in self.bins.all() if bin['bin'] == num]

    @property
    def warehouse(self):
        """ GET localhost/api/warehouse """
        real_bins = []
        for bin in self.bins.all():
            while bin['bin'] >= len(real_bins):
                real_bins.append([])
            real_bins[bin['bin']].append(bin['sku'])
        return real_bins
