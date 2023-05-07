import pytest
from pages.main_page import Main_page
from pages.product_page import Product_page
from pages.cart_page import Cart_page
from pages.checkout_page import Checkout_page


#
@pytest.mark.run(order=2)
def test_buy_product_1(set_up_for_buy_products):
    driver_g = set_up_for_buy_products
    mp = Main_page(driver_g)
    mp.select_filters()
    mp.click_button_buy("Петля")
    mp.click_button_go_to_catalog()




@pytest.mark.run(order=1)
def test_buy_product_2(set_up_for_buy_products):
    driver_g = set_up_for_buy_products
    mp = Main_page(driver_g)
    mp.select_filters()
    mp.find_specific_product("Битоку")
    pp = Product_page(driver_g)
    pp.input_field_quantity("3")
    pp.click_button_buy()
    pp.click_button_go_to_cart()
    cp = Cart_page(driver_g)
    cp.input_field_promocode("BGwithUS")
    cp.check_confirm_promocode()
    value_cart_price = cp.save_value_cart_price()
    print(f'Стоимость товаров в корзине равна: {value_cart_price}')
    mp.make_screenshots()
    cp.click_button_go_to_checkout()
    check_p = Checkout_page(driver_g)
    check_p.click_payment_method()
    check_p.click_method_dolyami()
    check_p.select_address_cdek()
    value_price_delivery = check_p.save_value_price_delivery()
    value_total_order_amount = check_p.save_value_total_order_amount()
    check_p.make_screenshots()
    check_p.order_amount_comparison(value_cart_price, value_price_delivery, value_total_order_amount)
    check_p.input_contact_form()
