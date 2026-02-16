class product:
    def init (self, name, price, category = "laptop" ):
        self.name = name 
        self.price = price 

    def get_info(self):
        return f"produt name: {self.name }, Price: $ {self.price:.2f}"
    product = product("Laptop", 999.99, "Laptop")   
    print(product.get_info())
    