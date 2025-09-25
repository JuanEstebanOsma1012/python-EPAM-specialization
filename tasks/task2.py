def get_total(costs, items, tax):
    total = sum(costs[item] for item in items if item in costs)
    total += total * tax
    return round(total + 1e-8, 2)