import random

MIN_PRICE = 1
MAX_PRICE = 10
MIN_TEMP = 17
MAX_TEMP = 42
CUSTOMERS_PER_DAY = 50


def determine_num_of_buyers(num_of_popsicles, num_of_customers, price, temperature):
    """
    determine the number of buyers, based on pre-existing information
    :param num_of_popsicles:
    :param num_of_customers:
    :param price:
    :return: the number of buyers
    """

    temperature_bias = MIN_PRICE + (temperature - MIN_TEMP) * ((MAX_PRICE - MIN_PRICE) / (MAX_TEMP - MIN_TEMP))
    num_of_buyers = 0
    customers = 0

    while num_of_buyers < num_of_popsicles and customers < CUSTOMERS_PER_DAY:
        willing_to_pay = random.triangular(MIN_PRICE, MAX_PRICE, temperature_bias)
        if willing_to_pay > price:
            num_of_buyers += 1
        customers += 1
    return num_of_buyers


def simulate_day(num_of_popsicles, price, num_of_customers=100):
    """

    :param num_of_popsicles:
    :param price:
    :param num_of_customers:
    :return:
    """
    temperature = random.randint(MIN_TEMP, MAX_TEMP)
    num_of_buyers = determine_num_of_buyers(num_of_popsicles, num_of_customers, price, temperature)
    print(f"Today's temperature: {temperature}C")
    print(f"Customers today: {num_of_buyers}")
    income = num_of_buyers * price  # Income for the day
    return income


def main():
    buying_price = 1
    while True:
        print(f"the price of each popsicles is: {buying_price}")
        print("Enter how many popsicles you want to buy (or 'q' to quit):")
        num_of_popsicles_input = input("> ")

        if num_of_popsicles_input.lower() == "q":
            break

        num_of_popsicles = int(num_of_popsicles_input)

        print("Enter the price in which you want to sell each popsicle:")
        price_input = input("> ")

        price = float(price_input)
        expense = buying_price * num_of_popsicles
        income = simulate_day(num_of_popsicles, price)
        print(f"Income for the day: ${income - expense}\n")

    # print(f"\nTotal income: ${total_income}")
    print("Game Over!")


if __name__ == "__main__":
    main()
