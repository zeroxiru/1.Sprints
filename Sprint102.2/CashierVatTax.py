def getting_total_amount_and_received_amount(prompt):
    user_input = input(prompt)
    return float(user_input)


def calculate_tax(total_amount, tax_rate):
    tax_amount_of_price = total_amount * tax_rate

    return tax_amount_of_price


def calculate_change_amount(total_amount, total_receive_amount, tax_amount_of_price):
    change_amount = total_receive_amount - total_amount - tax_amount_of_price
    return change_amount


def output_results(tax_amount_of_price, change ):
    print(f"Tax amount: {tax_amount_of_price:.2f}$")
    print(f"Change: {change:.2f}$")


def main():
    total_amount = getting_total_amount_and_received_amount("Enter the Total Amount: ")
    total_receive_amount = getting_total_amount_and_received_amount("Enter the Total Received Amount: ")

    # Calculate tax amount
    tax_rate = 0.115  # 11.5%
    tax_amount = calculate_tax(total_amount, tax_rate)

    # Calculate change
    change = calculate_change_amount(total_amount, total_receive_amount, tax_amount)

    # Output results
    output_results(tax_amount, change)


if __name__ == "__main__":
    main()

