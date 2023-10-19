import numpy as np

# Задача #1

delta_x = 0.00001


def function_1(x):
    return np.cos(x) + 0.05 * x ** 3 + np.log2(x ** 2)


def derivation(x, function):
    return round((function(x + delta_x) - function(x)) / delta_x, 2)


result_1 = derivation(10, function_1)
print(result_1)

# Задача #2


def function_2(x):
    return ((x[0]**2) * np.cos(x[1])) + (0.05 * x[1] ** 3) + (3 * x[0] ** 3) * (np.log2(x[1] ** 2))


def gradient(x, function):
    return [round((function([x[0] + delta_x, x[1]]) - function(x)) / delta_x, 2),
            round((function([x[0], x[1] + delta_x]) - function(x)) / delta_x, 2)]


x = [10, 1]
result_2 = gradient(x, function_2)
print(result_2)

# Задача #3

epsilon = 0.001


def gradient_optimization_one_dim(function):
    value = 10
    for i in range(50):
        value = value - (epsilon * derivation(value, function))
    return round(value, 2)


result3 = gradient_optimization_one_dim(function_1)
print(result3)

# Задача #4


def gradient_optimization_multi_dim(function):
    result = [4, 10]
    for i in range(50):
        grad = np.array([round((function([result[0] + delta_x, result[1]]) - function(result)) / delta_x, 2),
                         round((function([result[0], result[1] + delta_x]) - function(result)) / delta_x, 2)])
        result = result - epsilon * grad
    return [round(value, 2) for value in result]


result4 = gradient_optimization_multi_dim(function_2)
print(result4)
