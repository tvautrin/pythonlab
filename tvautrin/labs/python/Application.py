from tvautrin.labs.python.domain.Product import Product
from tvautrin.labs.python.services.ProductService import ProductService

productService = ProductService()


def main():
    product = Product()
    product.name = "Ordinateur"
    product.id = 1
    productService.create(product)


if __name__ == '__main__':
    main()
