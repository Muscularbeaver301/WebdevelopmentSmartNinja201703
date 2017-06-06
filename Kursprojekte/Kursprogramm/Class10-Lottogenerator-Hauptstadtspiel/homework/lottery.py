
import random

print("###############################################")
print("## Welcome to the Lottery numbers generator. ##")
print("###############################################\n")

def randomlotterynumbers(quantity):
    result = []

    for x in range(0, quantity):
        num = random.randint(1, 50)
        while num in result:
            num = random.randint(1, 50)
        result.append(num)

    return result


def main():
    askquantity = None
    while askquantity is None:
        try:
            askquantity = int(raw_input("Please enter how many random numbers you would like to have: "))
        except ValueError:
            print("You didn't enter an integer number, please try again.")

    print("Your %i random numbers are: %s\n" % (askquantity, randomlotterynumbers(askquantity)))
    print("###################################")
    print("## Thanks for using - Good luck! ##")
    print("###################################")


if __name__ == '__main__':
    main()