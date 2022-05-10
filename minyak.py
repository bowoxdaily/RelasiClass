
class Minyak(Produk):
    
    def set_nama(self, nama:str ) :
        self.__nama = nama
            
        
    def get_nama(self,nama )->str:
        return "produk ini Minyak",self.__nama   
    
    def set_harga(self,harga) :
        self.harga = harga
        
    def get_harga(self,harga)->float :
        return  "12000",self.__harga
    
    