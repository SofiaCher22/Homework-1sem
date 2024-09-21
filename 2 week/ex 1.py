n, cards = int(input()), list(map(int, input().split()))
total_sum = sum(range(1, n + 1))
cards_sum = sum(cards)
print(total_sum - cards_sum)
