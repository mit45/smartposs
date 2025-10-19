from product import Product

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, stock):
        product = Product(name, price, stock)
        self.products.append(product)
        print(f"{name} başarıyla eklendi.")
        
    def list_products(self):
        if not self.products:
            print("Henüz ürün yok.")
            return
        print("/n---Ürün Listesi---")
        for i, product in enumerate(self.products, start=1):
            print(f"{i}. {product.name} - Fiyat: {product.price} - Stok: {product.stock}")
            
if __name__ == "__main__":
    inventory = Inventory()
    
    while True:
        print("\n1. Ürün Ekle")
        print("2. Ürünleri Listele")
        print("3. Çıkış")
        
        secim = input("Seçiminiz: ")
        
        if secim == '1':
            name = input("Ürün Adı: ")
            price = float(input("Fiyat: "))
            stock = int(input("Stok Miktarı: "))
            inventory.add_product(name, price, stock)
        elif secim == '2':
            inventory.list_products()
        elif secim == '3':
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim!")