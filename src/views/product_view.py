"""
Product view
Auteurs : Dyaa Abou Arida, 2026
"""
from controllers.product_controller import ProductController
from models.product import Product

class ProductView:
    @staticmethod
    def show_options():
        """ Show menu with operation options which can be selected by the user """
        controller = ProductController()
        while True:
            print("\n1. Montrer la liste des produits" \
            "\n2. Ajouter un produit" \
            "\n3. Modifier un produit" \
            "\n4. Supprimer un produit" \
            "\n5. Supprimer tout les produits"
            "\n6. Quitter l'appli")
            choice = input("Choisissez une option: ")

            if choice == '1':
                products = controller.list_products()
                ProductView.show_products(products)
            elif choice == '2':
                name, brand, price = ProductView.get_inputs_create()
                product = Product(None, name, brand, price)
                controller.create_product(product)
            elif choice == '3':
                products = controller.list_products()
                ProductView.show_products(products)
                id, name, brand, price = ProductView.get_inputs_update()
                product = Product(id, name, brand, price)
                controller.update_product(product)
            elif choice == '4':
                products = controller.list_products()
                ProductView.show_products(products)
                product_id = ProductView.get_inputs_delete()
                controller.delete_product(product_id)
            elif choice == '5':
                controller.delete_all_products()
            elif choice == '6':
                controller.shutdown()
                break
            else:
                print("Cette option n'existe pas.")

    @staticmethod
    def show_products(products):
        """ List products """
        print("\n".join(f"{product.id}: {product.name} ({product.brand}) - ${product.price:.2f}" for product in products))

    @staticmethod
    def get_inputs_create():
        """ Prompt user for inputs necessary to add a new product """
        name = input("Nom du produit : ").strip()
        brand = input("Marque du produit : ").strip()
        price = float(input("Prix du produit : "))
        return name, brand, price

    @staticmethod
    def get_inputs_update():
        """ Prompt user for inputs necessary to modify a product """
        id = input("\nID du produit a modifier: ").strip()
        name = input("\nNouveau nom de produit: ").strip()
        brand = input("\nNouvelle marque de produit: ").strip()
        price = float(input("Nouveau prix: "))
        return id, name, brand, price

    @staticmethod
    def get_inputs_delete():
        """ Prompt user for inputs necessary to modify a product """
        product_id = input("\nID du produit a supprimer : ").strip()
        return product_id
    