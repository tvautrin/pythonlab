class ProductRepository:

    def create(self, product):
        print("Creation du produit {0}".format(product.name))