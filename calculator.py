def calculate_cost(base_price, part, color, paintMethod, part_coefficients, color_coefficients, paintMethod_coefficients):
    if part in part_coefficients and color in color_coefficients:
        total_cost = base_price * part_coefficients[part] * color_coefficients[color] * paintMethod_coefficients[paintMethod]
        return total_cost
    else:
        raise ValueError("Incorrect color or part")