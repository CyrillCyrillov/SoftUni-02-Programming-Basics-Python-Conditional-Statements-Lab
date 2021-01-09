prise = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())
sum = number_of_puzzles * 2.6 + number_of_dolls * 3 + number_of_bears * 4.1 + number_of_minions * 8.2 + number_of_trucks * 2

if (number_of_puzzles + number_of_dolls + number_of_bears + number_of_minions + number_of_trucks) >= 50:
    sum = sum * 0.75

sum = sum * 0.9

if (sum >= prise):
    print(f"Yes! {sum - prise:.2f} lv left.")
else:
    print(f"Not enough money! {prise - sum:.2f} lv needed.")
