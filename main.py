import random


def add_git_branch():
    return "https://github.com/AssafBrown92/mego_game.git"


def determine_num_of_buyers(num_of_popsicles, num_of_customers, price):
    """
    determine the number of buyers, based on pre-existing information
    :param num_of_popsicles:
    :param num_of_customers:
    :param price:
    :return: the number of buyers
    """
    num_of_buyers = 0
    for customer in range(num_of_customers):
        willing_to_pay = random.uniform(1, 3)
        if willing_to_pay > price:
            if num_of_buyers < num_of_popsicles:
                num_of_buyers += 1
    return num_of_buyers


def simulate_day(num_of_popsicles, price, num_of_customers=100):
    """

    :param num_of_popsicles:
    :param price:
    :param num_of_customers:
    :return:
    """
    num_of_buyers = determine_num_of_buyers(num_of_popsicles, num_of_customers, price)
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
