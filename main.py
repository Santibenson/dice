import random
PURSE = 0
STAKE = 0


def deposit():
    global PURSE
    while True:
        bills = input("How much do you want to deposit? > ")
        if bills.isdigit():
            bills = int(bills)
            PURSE += bills
            if bills > 0:
                break
            else:
                print("You can't deposit such amount. Try again")
        else:
            print("Enter a valid amount")

    print(f"You have ${PURSE} in your purse currently")


def staking():
    global STAKE, PURSE
    while True:
        STAKE = input("How much do you want to stake? > ")
        if STAKE.isdigit():
            STAKE = int(STAKE)
            if STAKE > 0:
                PURSE += STAKE
                break
            else:
                print("You can't bet with that amount")
        else:
            print(f"Enter a valid amount. You have ${PURSE} in your purse")


def start():
    global PURSE, STAKE
    dice_diagram = {
        1: (
            "┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘",
        ),
        2: (
            "┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘",
        ),
        3: (
            "┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘",
        ),
        4: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        5: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        6: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
    }

    QUESTION = input("Do you want to play a dice game? (Y/N) > ").lower()
    while QUESTION == "y":
        staking()

        PURSE -= STAKE
        if STAKE == PURSE:
            print(
                "You'd be left with $0 if you stake this much. You'll need to top up after this game")
            cont = input("Do you want to continue with the stake? (Y/N) > ")
            if cont == "y":
                continue
            if cont == "n":
                staking()

        if STAKE > PURSE:
            print(
                f"You can't stake that amount. Your purse is ${PURSE} currently")
            print("Deposit some more money")
            isyeah = input("(Y/N) > ").lower()
            if isyeah == "y":
                deposit()
            else:
                quit()
        if PURSE == 0:
            print("No credit today")
            break

        first_roll = random.randint(1, 6)
        sec_roll = random.randint(1, 6)
        total_roll = first_roll + sec_roll
        if total_roll >= 10:
            print(f"You won. Total dice is {total_roll}")
            PURSE += (STAKE * 1/2)
        else:
            print(f"You lost. Total dice is {total_roll}")
            PURSE -= STAKE

        print(f"Dice rolled: {first_roll, sec_roll}")
        print("\n".join(dice_diagram[first_roll]))
        print("\n".join(dice_diagram[sec_roll]))
        print()
        print(f"Your current balance is {PURSE}")

        QUESTION2 = input("Do you want to roll again? (Y/N) > ").lower()
        if QUESTION2 != "y":
            break


deposit()
start()
