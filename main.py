from produk import Produk
from stock import Stock

produk = Produk()
produk.get_harga()
print(produk.get_nama)

stock = Stock()
stock.get_qty()
print(stock.get_produk)