def calculate_discount(price, discount_percent):
    if discount_percent >=20:
        discount=price*(discount_percent/100)
        result= price-discount
        return result
    else:
        return price     
price=int(input("pls enter original price"))
discount_percent=int(input("pls enter the discount"))
calculate_discount(price,discount_percent)