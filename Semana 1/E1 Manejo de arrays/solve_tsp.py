def order_crossover(parent1, parent2, lower_bound, upper_bound):
    child1 = parent1[lower_bound:upper_bound]
    p2 = parent2[upper_bound:] + parent2[0:upper_bound]
    
    for number in p2:
        if number not in child1:
            child1.append(number)
    
    longitud_mitad = (upper_bound - lower_bound) + (len(parent1) - upper_bound)

    return child1[longitud_mitad:] + child1[0:longitud_mitad]
