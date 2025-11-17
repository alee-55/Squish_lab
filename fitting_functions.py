def linear(m,x,b):
    return (m*x)+b
def slope_units (x_units, y_units):
     print(y_units.rstrip('s') + '/' + x_units)
def print_equation(m,b,y_units,x_units):
    print('The equation of the line is: y =' + str(m) + slope_units(x_units, y_units) + '+' + str(b) + str(y_units))

    
