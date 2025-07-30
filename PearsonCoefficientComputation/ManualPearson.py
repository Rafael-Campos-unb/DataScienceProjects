import math

physics_scores = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
history_scores = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]


def PearsonCoefficient(x_values: list, y_values: list)-> float:
    """
    -Args:
    x_values = list
    y_values = list
    -Returns:
    r coefficient = float
    
    """
    mean_x = sum(x_values) / len(x_values)
    mean_y = sum(y_values) / len(y_values)
    delta_x_list = list()
    delta_y_list = list()
    delta_x2_list = list()
    delta_y2_list = list()
    
    for j, x in enumerate(x_values):
        delta_x = x - mean_x
        delta_x2 = (x - mean_x)**2
        delta_x_list.append(delta_x)
        delta_x2_list.append(delta_x2)
    for k, y in enumerate(y_values):
        delta_y = y - mean_y
        delta_y2 = (y - mean_y)**2
        delta_y_list.append(delta_y)
        delta_y2_list.append(delta_y2)
        
    return print(f'{sum([x*y for x, y in zip(delta_x_list, delta_y_list)]) /  math.sqrt(sum(delta_x2_list) * sum(delta_y2_list)):.3f}')

if __name__== '__main__':
    PearsonCoefficient(physics_scores, history_scores)


