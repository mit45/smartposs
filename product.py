class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        
    def __repr__(self):
        return f"Product(name={self.name}, price={self.price}, stock={self.stock})"
    
    def reduce_stock(self, amount):
        if amount > self.stock:
            return "Yetersiz stok"
        self.stock -= amount
        return f"Yeni stok miktarı: {self.stock}"
    
if __name__ == "__main__":
    urun1 = Product("Kalem", 5.0, 10)
    urun2 = Product("Defter", 20.0, 5)
    
    print(urun1)
    print(urun2)
    
    print(urun1.reduce_stock(3)) #Kalem stok azaltma
    print(urun2.reduce_stock(10)) #Defter stok azaltma