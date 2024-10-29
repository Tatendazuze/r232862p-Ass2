import matplotlib.pyplot as plt

def plot_data(my_file, scatter_plot=None):
    my_file = open('C:/Users/TEVES/Downloads/x_y_coordinates.txt', 'r')
    print(my_file.read())
    print(my_file.readline())
    for line in my_file.readlines():
        print(line)
    x_coords = []
    y_coords = []
    my_file.readline()
    for line in my_file.readlines():
        x_coords.append(float(line.split(',')[0]))
        y_coords.append(float(line.split(',')[1]))
        print(type(x_coords[0]))
    plt.scatter(x_coords, y_coords)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Scatterplot of Data')
    plt.show()
    return scatter_plot