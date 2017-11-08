from tvautrin.labs.python.repository.ProductRepository import ProductRepository


class ProductService:
    productRepository = ProductRepository()

    def create(self, product):
        """ Create a product"""
        self.productRepository.create(product)
