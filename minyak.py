from abc import ABC
from produk import Produk

class Minyak(Produk):
    
    def set_nama(self, nama:str ) :
        self.__nama = nama
            
        
    def get_nama(self,nama )->str:
        return self.__nama   
    
    def set_harga(self,harga) :
        self.harga = harga
        
    def get_harga(self,harga)->float :
        return  self.__harga
    
    def show_produk (self,nama,harga):
        print(self.__nama)
        print(self.__harga)