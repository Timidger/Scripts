import sympy
from sympy.abc import x

#Fix float numbers ---> int

def derivative(function):
    """Returns the derivative of the function with respects to the given
    variable"""
    assert type(function) != str
    return function.diff()

def get_critical_values(derived_function):
    """Returns a set of the values in which the derived_function == 0"""
    return sympy.solve(derived_function)

def get_side_signs(derived_function, critical_values):
    """Returns the sides, in order, for each Critical Values for the
    given derived function"""
    critical_values = list(critical_values)
    signs = []
    for value in critical_values:
        if value == critical_values[-1]:
            signs.append(derived_function.evalf(
            subs = {x: value + 1}) > 0)
            break
        signs.append(derived_function.evalf(subs = {
        x: value - .00001}) > 0)
        #Wow, these magic numbers could break semi-easily
        signs.append(derived_function.evalf(subs = {
        x: value + .00001}) > 0)
    return signs

def interpret_behaviour(function):
    interval = get_critical_values(derivative(function))
    signs = get_side_signs(derivative(function), interval)
    print interval
    print signs
    for gap, sign in zip(interval, signs):
        print 'f(x) is {} over the interval {{{}}}'.format(
        'increasing' if sign else 'decreasing', gap)


if __name__ == "__main__":
    print interpret_behaviour(x**3 - 3/2*x**2)