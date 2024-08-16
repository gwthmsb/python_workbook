"""
The Birthday Paradox, also called the
Birthday Problem, is the surprisingly high
probability that two people will have the
same birthday even in a small group of people.
In a group of 70 people, there’s a 99.9 percent chance
of two people having a matching birthday. But even
in a group as small as 23 people, there’s a 50 percent
chance of a matching birthday. This program performs
several probability experiments to determine
the percentages for groups of different sizes. We call these types of experiments,
in which we conduct multiple random trials to understand the
likely outcomes, Monte Carlo experiments.

"""

import random
import itertools


months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
days = [i for i in range(1, 32)]


def random_day_of_a_month(month):
    months_with_30_days = list(itertools.chain(months[1:7:2], months[8::2]))

    if month == "feb":
        return random.choice(days[:29])
    elif month in months_with_30_days:
        return random.choice(days[:30])
    else:
        return random.choice(days)
    

def generate_birthday():
    month = random.choice(months)
    day = random_day_of_a_month(month)    
    return " ".join([month, str(day)])


def generate_n_birthdays(num):
    birthdays = []
    for _ in range(num):
        birthdays.append(generate_birthday())
    return birthdays


def check_for_matching_birthday(birthdays):
    total_bds = len(birthdays)
    unique_bds = set(birthdays)

    if total_bds == len(unique_bds):
        return False
    return True


def run_simulation(sim_num=1000, num_of_bds=10):
    matching_bds_count = 0

    for i in range(sim_num):
        bds = generate_n_birthdays(num_of_bds)
        matching = check_for_matching_birthday(bds)
        if matching:
            matching_bds_count += 1
        
        if(i > 0 and i % 10000 == 0):
            print(f"Simulation ran {i} times")
    
    return matching_bds_count


def main():
    print("Welcome to birthday simulator")
    print("Enter the num of birthdays")
    bds_num = int(input())
    print("Enter the num of simulations to run")
    sims = int(input())

    matching_bds_count = run_simulation(sims, bds_num)
    print(f"Out of {sims} simulations of {bds_num} people, there was a matching birthdays in that group {matching_bds_count} times")
    print(f"This means that {bds_num} people have {matching_bds_count*100/sims}% chance of having same birthday in their group")


if __name__ == "__main__":
    main()

# Tests

def test_check_for_matching_birthday():
    unique_birthdays = ["jan 10", "feb 10", "jan 10"]
    non_unique_birthdays = ["jan 10", "feb 10", "jan 9"]

    assert check_for_matching_birthday(unique_birthdays)
    assert not check_for_matching_birthday(non_unique_birthdays)


def test_generate_n_birthdays():
    assert len(generate_n_birthdays(10)) == 10
    assert len(generate_n_birthdays(100)) == 100
    assert len(generate_n_birthdays(1)) == 1


def test_random_day_of_a_month():
    months_with_30_days = list(itertools.chain(months[1:7:2], months[8::2]))
    months_with_31_days = list(itertools.chain(months[:8:2], months[7::2]))
    
    for _ in range(0, 1000):
        month = random.choice(months)
        day = random_day_of_a_month(month)
        
        if month == "feb":
            assert day < 30

        if month in months_with_30_days:
            assert day < 31

        if month in months_with_31_days:
            assert day < 32
    

def test_generate_birthday():
    for _ in range(0, 1000):
        birthday = generate_birthday()
        m, d = birthday.split(" ", 2)
        if m not in months:
            assert False
        if int(d) not in days:
            assert False


