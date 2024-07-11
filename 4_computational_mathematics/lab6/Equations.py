import numexpr as ne

EQUATIONS = {
    1: "y`=(x-y)**2",
    2: "y`=(x-y)**2+y**2",
    3: "y`=sin(x)+y",
    4: "y`=y+(1+x)*y**2"
}

ANSWERS = {
    1: "y=+1/(c*exp(2*x)+1/2)+x-1",
    2: "y=(x - c) - sqrt(c - x + c**2)",
    3: "y=c*exp(x)- sin(x)-cos(x)",
    4: "y=-1/(c-x-x**2/2)"
}

C = {
    1: "с=((y - x + 1)**(2) - 1)/exp(-2*x)",
    2: "c=x-y-sqrt(y**2 - (x - y)**2)",
    3: "c= y-sin(x)",
    4: "с=x+x**2/2-1/y"
}


def calculateFunction(xi, yi, function_number):
    return float(ne.evaluate(EQUATIONS[function_number].split('=')[1], local_dict={'x': xi, 'y': yi}))


def calculateAnswer(x0, y0, xi, function_number):
    c = calculateC(x0, y0, function_number)
    return float(
        ne.evaluate(ANSWERS[function_number].split('=')[1], local_dict={'x': xi, 'c': c}))


def calculateC(x0, y0, function_number):
    return float(ne.evaluate(C[function_number].split('=')[1], local_dict={'x': x0, 'y': y0}))


METHODS = ['Одношаговый. Усовершенствованный метод Эйлера',
           'Одношаговый. Метод Рунге-Кутта 4-го порядка',
           'Многошаговый. Метод Адамса']
