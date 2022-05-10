
class Minyak(Produk):
    
    def set_nama(self, nama:str ) :
        self.__nama = nama
            
        
    def get_nama(self,nama )->str:
        return self.__nama   
    
    def set_harga(self,harga) :
        self.harga = harga
        
    def get_harga(self,harga)->float :
        return  self.__harga
    
    