import matplotlib.pyplot as plt
def plot_data():
    my_file = open('C:/Users/user/Downloads/x_y_coordinates.txt','r')
    x_coords = []
    y_coords = []
    my_file.readline()
    for line in my_file.readlines():
        x_coords.append(float(line.split(',')[0]))
        y_coords.append(float(line.split(',')[1]))
    plt.scatter(x_coords, y_coords)
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('Coordinates ScatterPlot')
    plt.grid(True)
    plt.show()

plot_data()