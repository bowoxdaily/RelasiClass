from produk import Produk

class Stock :
    def __init__(self,produk : Produk, qty: int):
        self.produk=produk
        self.qty=qty
        
        
    def get_produk(self) -> Produk:
        return self.__produk
    
    def get_qty(self) -> int:
        return self.__qty        