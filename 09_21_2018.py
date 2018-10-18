def num_unique_routes(x_distance,y_distance):
    if (x_distance == 0 and y_distance == 0):
        out = 0
    elif (x_distance == 0 or y_distance == 0):
        out = 1
    else:
        out = num_unique_routes(x_distance-1, y_distance) + num_unique_routes(x_distance, y_distance-1)
    return out
    
print(num_unique_routes(5,10))    