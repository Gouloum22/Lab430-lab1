from daos.product_dao import ProductDAO
from models.product import Product

dao = ProductDAO()

def test_product_select():
    product = Product(None, 'Select Test Product', 'Test Brand', 9.99)
    assigned_id = dao.insert(product)

    products = dao.select_all()
    names = [p.name for p in products]

    assert product.name in names

    dao.delete(assigned_id)

def test_product_insert():
    product = Product(None, 'Test Product', 'Test Brand', 9.99)
    assigned_id = dao.insert(product)
    product_list = dao.select_all()
    names = [p.name for p in product_list]
    assert product.name in names
    dao.delete(assigned_id)

def test_product_update():
    product = Product(None, 'Test Product', 'Test Brand', 9.99)
    assigned_id = dao.insert(product)

    corrected_name = 'Updated Product'
    product.id = assigned_id
    product.name = corrected_name
    dao.update(product)

    product_list = dao.select_all()
    names = [p.name for p in product_list]
    assert corrected_name in names

    dao.delete(assigned_id)

def test_product_delete():
    product = Product(None, 'Test Product', 'Test Brand', 9.99)
    assigned_id = dao.insert(product)
    dao.delete(assigned_id)
    product_list = dao.select_all()
    names = [p.name for p in product_list]
    assert product.name not in names