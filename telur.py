from abc import ABC
from produk import Produk

class Telur(Produk):
    
    def set_nama(self, nama):
        self.__nama = nama
    
    def get_nama(self, nama) ->str:
        return "produk", self.__nama
    
    def set_harga(self, harga):
        self.__harga = harga
        
    def get_harga(self, harga)->float:
        return "15000", self.__harga
    
    def show_produk(self):
        print(self.__nama)
        print(self.__harga)