from pro import format_product_details

def test_format_product_details():
    # Arrange: Define sample inputs and expected output
    product_id = "P101"
    name = "Wireless Mouse"
    quantity = 15
    price = 25.50
    
    expected_output = (
        "Product ID: P101\n"
        "Product Name: Wireless Mouse\n"
        "Quantity: 15\n"
        "Price: $25.50"
    )
    
    # Act: Call the function
    actual_output = format_product_details(product_id, name, quantity, price)
    
    # Assert: Verify the output matches expectations
    assert actual_output == expected_output
    