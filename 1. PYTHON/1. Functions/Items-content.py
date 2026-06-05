def items_cost(cart):
    total_cost = 0;
    for item in cart:
        total_cost += item['price']*item['quantity']
        
    print("Total cost of items in the cart is: ", total_cost);
    
cart = [{"name":"Item 1" ,"price": 10, "quantity": 2}, {"name":"Item 2", "price": 5, "quantity": 3},{"name":"Item 3", "price": 15, "quantity": 1}]

items_cost(cart)