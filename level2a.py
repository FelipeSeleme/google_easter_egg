from fractions import Fraction


def solution(pegs):
    gears_quant = len(pegs)
    if (not pegs) or gears_quant == 1:
        return [-1, -1]

    even = True if (gears_quant % 2 == 0) else False
    sum = (- pegs[0] + pegs[gears_quant - 1]) if even else (- pegs[0] - pegs[gears_quant -1])

    if gears_quant > 2:
        for index in range(1, gears_quant-1):
            sum += 2 * (-1)**(index+1) * pegs[index]

    first_gear_radius = Fraction(2 * (float(sum)/3 if even else sum)).limit_denominator()

    if first_gear_radius < 2:
        return [-1, -1]

    current_radius = first_gear_radius
    for index in range(0, gears_quant-2):
        center_distance = pegs[index+1] - pegs[index]
        next_radius = center_distance - current_radius
        if current_radius < 1 or next_radius < 1:
            return [-1, -1]
        else:
            current_radius = next_radius

    return [first_gear_radius.numerator, first_gear_radius.denominator]
