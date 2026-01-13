import logging

# Initialize logging system
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def determine_discount(product_category, discount_level):
    """
    Returns the total discount percentage for a product
    based on its category and pricing tier.
    """

    base_discount = 0
    extra_discount = 0

    match product_category:
        case "Electronics":
            base_discount = 10
        case "Clothing":
            base_discount = 15
        case "Books":
            base_discount = 5
        case "Home":
            base_discount = 12
        case _:
            base_discount = 0

    match discount_level:
        case "Premium":
            extra_discount = 5
        case "Budget":
            extra_discount = 2
        case _:
            extra_discount = 0

    return base_discount + extra_discount


def read_product_file(file_path):
    """
    Reads product data from file and returns
    a list of processed product records.
    """

    processed = []

    with open(file_path, "r") as source:
        for line_number, record in enumerate(source, start=1):
            fields = record.strip().split(",")

            if len(fields) != 4:
                logging.warning(
                    f"Line {line_number}: Expected 4 fields, found {len(fields)}"
                )
                continue

            name, price_text, category, tier = fields

            try:
                price = float(price_text)
            except ValueError:
                logging.error(
                    f"Line {line_number}: Invalid price value '{price_text}'"
                )
                continue

            discount_percentage = determine_discount(category, tier)
            discount_value = price * discount_percentage / 100
            final_price = price - discount_value

            processed.append(
                (
                    name,
                    price,
                    discount_percentage,
                    discount_value,
                    final_price
                )
            )

    return processed


def write_pricing_report(destination, product_data):
    """
    Writes formatted pricing report to an output file.
    """

    with open(destination, "w") as report:
        report.write("=" * 92 + "\n")
        report.write("PRODUCT PRICING ANALYSIS REPORT\n")
        report.write("=" * 92 + "\n")
        report.write(
            f"{'Product':<30}"
            f"{'Base Price':>14}"
            f"{'Total Discount %':>14}"
            f"{'Discount $':>16}"
            f"{'Final Price':>16}\n"
        )
        report.write("-" * 92 + "\n")

        for item in product_data:
            report.write(
                f"{item[0]:<30}"
                f"${item[1]:>13.2f}"
                f"{item[2]:>13.1f}%"
                f"${item[3]:>15.2f}"
                f"${item[4]:>15.2f}\n"
            )

        report.write("=" * 92 + "\n")


def display_summary(product_data):
    """
    Prints processing summary to the console.
    """

    count = len(product_data)
    avg_discount = (
        sum(item[2] for item in product_data) / count
        if count > 0 else 0
    )

    print("\nPricing Report Completed Successfully")
    print(f"Products processed: {count}")
    print(f"Average discount applied: {avg_discount:.2f}%")


def run_pricing_manager(input_file, output_file):
    """
    Main controller for pricing manager workflow.
    """

    try:
        products = read_product_file(input_file)
        write_pricing_report(output_file, products)
        display_summary(products)

        logging.info(f"Processed {len(products)} products successfully")

    except FileNotFoundError:
        logging.critical(f"Missing input file: {input_file}")
        print(f"Error: Input file '{input_file}' not found.")

    except PermissionError:
        logging.critical(f"Permission denied for output file: {output_file}")
        print(f"Error: Unable to write to '{output_file}'.")

    except Exception as error:
        logging.exception("Unexpected runtime error")
        print("Unexpected error occurred:", error)


if __name__ == "__main__":
    run_pricing_manager("products.txt", "pricing_report.txt")
