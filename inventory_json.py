import json
from product import Product

class Inventory:
    def __init__(self, filename="products.json"):
        self.filename = filename
        self.products = self.load_products()
        
    def load_products(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [Product(**item) for item in data]
        except FileNotFoundError:
            return []
        
    def save_products(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump([p.__dict__ for p in self.products], f, ensure_ascii=False,indent=4)
            
    def add_product(self, name, price, stock):
        product = Product(name, price, stock)
        self.products.append(product)
        self.save_products()
        print(f"{name} başarıyla eklendi ve kaydedildi.")
        
    def list_products(self):
        if not self.products:
            print("Hiç ürün bulunmamaktadır.")
            return
        print("\n---Ürün Listesi---")
        for i, product in enumerate(self.products, start=1):
            print(f"{i}. {product.name} - Fiyat: {product.price} TL - Stok: {product.stock}")
            
if __name__ == "__main__":
    inventory = Inventory()
    
    while True:
        print("\n1. Ürün Ekle\n2. Ürünleri Listele\n3. Çıkış")
        secim = input("Seçiminiz: ")
        
        if secim == "1":
            name = input("Ürün Adı: ")
            price = float(input("Fiyat: "))
            stock = int(input("Stok Miktarı: "))
            inventory.add_product(name, price, stock)
        elif secim == "2":
            inventory.list_products()
        elif secim == "3":
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")