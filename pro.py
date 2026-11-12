def format_product_details(product_id, name, quantity, price):
    """Returns product information as a well-formatted string."""
    return (
        f"Product ID: {product_id}\n"
        f"Product Name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: ${price:.2f}"
    )

if __name__ == "__main__":
    # Example usage
    result = format_product_details("P101", "Wireless Mouse", 15, 25.50)
    print(result)