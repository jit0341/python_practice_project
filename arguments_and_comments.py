def calculate_total_price(items, tax_rate):
    """
    Calculates the total price of items including tax.

    Args:
        items (list): A list of item prices (numbers).
        tax_rate (float): The tax rate as a decimal (e.g., 0.05 for 5%).

    Returns:
        float: The total price after applying tax.
    """
    subtotal = sum(items)
    # Calculate tax amount, ensuring it's rounded to two decimal places
    tax_amount = round(subtotal * tax_rate, 2)
    total = subtotal + tax_amount
    return total
