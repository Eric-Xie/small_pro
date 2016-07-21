# encoding = utf-8
from random import uniform


def dispatch_money(total, n_person, min_m, max_m):
    person_dispatched = 0
    money_dispatched = 0
    list_dispatched = []
    for i in range(n_person):
        tmp_top = total-money_dispatched-\
                  min_m*(n_person-person_dispatched-1)
        top = tmp_top if not tmp_top >= 12 else max_m
        tmp_bottom = total-money_dispatched-\
                  max_m*(n_person-person_dispatched-1)
        bottom = tmp_bottom if not tmp_bottom <= 12 else min_m
        next_m = uniform(bottom, top)
        person_dispatched += 1
        money_dispatched += next_m
        list_dispatched.append(next_m)
    return list_dispatched




def main():
    print("Dispatch 100RMB to 10 person at random."
          "The area of RMB which each person got MUST be [6, 12].")
    print(dispatch_money(100, 10, 6, 12))
    print(sum(dispatch_money(100, 10, 6, 12)))



if __name__ == '__main__':
    main()


