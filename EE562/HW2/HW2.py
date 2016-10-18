from math import sqrt, pow


class Vertex:
    """
    This class is vertex in our problem. In order to realizing A* algorithm,
    f,g,h are introduced.
    """

    def __init__(self, x, y, parent):
        """
        This method initializes a vertex
        g is sum of edge costs from start to n
        h is estimate of lowest cost path form n to goal
        :param x: the x coordinate of vertex
        :param y: the y coordinate of vertex
        :param parent: parent of vertex
        """
        self.x = x
        self.y = y
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = self.g + self.h

    def calculate_h(self, goal):
        """
        This method calculate h of vertex
        :param goal: the goal point
        :return: h
        """
        h = self.distance(goal, self)
        return h

    def calculate_g(self, previous_g):
        """
        This method calculates g of vertex
        :param previous_g: the g before this vertex
        :return: g of this vertex = previous_g + current_increase
        """
        current_increase = self.distance(self.parent, self)
        return previous_g + current_increase

    @staticmethod
    def distance(a, b):
        """
        This static method calculate the distance between
        point a and point b
        :param a: point a
        :param b: point b
        :return: distance between a and b
        """
        return sqrt(pow(a.x - b.x, 2) + pow(a.y - b.y, 2))


class Obstacle:
    """
    This class represents rectangle obstacle with its four
    vertex
    """

    def __init__(self, vertex1, vertex2, vertex3, vertex4):
        """
        This method initialize rectangle obstacle in the problem
        vertex1 and vertex3 are endpoints of a same diagonal
        so do vertex2 and vertex4
        """
        self.vertex = [vertex1, vertex2, vertex3, vertex4]


class ProblemMap:
    """
    This class maps start point, goal point and vertexes of all
    obstacles in the problem and provides solution
    """
    # the following data set represent their paths respectively
    data_set1 = './data_set1'
    data_set2 = './data_set2'
    data_set3 = './data_set3'

    def __init__(self, data_set):
        """
        This method initialize problemMap class
        :param data_set: the path of data set
        """
        self.start_point_line = 0
        self.goal_point_line = 1
        self.obstacle_num_line = 2
        self.first_obstacle_line = 3
        self.data_set = self.read_data_set(data_set)
        self.all_vertex = []
        self.start = self.start_init()
        self.goal = self.goal_init()
        self.obstacle_num = self.obstacle_num_init()
        self.obstacle = []
        self.obstacle_init()
        self.h_init()

    @staticmethod
    def read_data_set(file):
        """
        This method read data set from a txt file
        :param file: the data set file
        :return: data_set
        """
        data_set = []
        with open(file, 'r') as data_file:
            for line in data_file:
                data_set.append(line)
        return data_set

    @staticmethod
    def get_point(data_set, line_in_data_set, index_x, index_y):
        """
        This method get points (x,y) from data set
        :param data_set: data set describes problem
        :param line_in_data_set: line number of data set (start from 0)
        :param index_x: the index in line of x coordinate
        :param index_y: the index in line of y coordinate
        :return: point
        """
        point_data = data_set[line_in_data_set]
        point_data_list = point_data.split(' ')
        point_x = int(point_data_list[index_x])
        point_y = int(point_data_list[index_y])
        point = {'x': point_x, 'y': point_y}
        return point

    def start_init(self):
        """
        This method initialize start point
        :return: start
        """
        start_point = self.get_point(self.data_set, self.start_point_line, 0, 1)
        start = Vertex(start_point['x'], start_point['y'], None)
        self.all_vertex.append(start)
        return start

    def goal_init(self):
        """
        This method initialize goal point
        :return: goal
        """
        goal_point = self.get_point(self.data_set, self.goal_point_line, 0, 1)
        goal = Vertex(goal_point['x'], goal_point['y'], None)
        self.all_vertex.append(goal)
        return goal

    def obstacle_num_init(self):
        """
        This method initialize number of obstacles
        :return: number of obstacles
        """
        return self.get_point(self.data_set, self.obstacle_num_line, 0, 0)['x']

    def obstacle_init(self):
        """
        This method initialize the obstacles
        :return: None
        """
        obstacle_vertex = list()
        for i in range(self.obstacle_num):
            j = 0
            while j < 7:
                obstacle_vertex.append(self.get_point(self.data_set, self.first_obstacle_line + i, j, j + 1))
                j += 2
        i = 0
        while i < self.obstacle_num * 4:
            current_obstacle = Obstacle(Vertex(obstacle_vertex[i + 0]['x'], obstacle_vertex[i + 0]['y'], None),
                                        Vertex(obstacle_vertex[i + 1]['x'], obstacle_vertex[i + 1]['y'], None),
                                        Vertex(obstacle_vertex[i + 2]['x'], obstacle_vertex[i + 2]['y'], None),
                                        Vertex(obstacle_vertex[i + 3]['x'], obstacle_vertex[i + 3]['y'], None))
            self.obstacle.append(current_obstacle)
            for k in range(4):
                self.all_vertex.append(current_obstacle.vertex[k])
            i += 4

    def h_init(self):
        """
        This method initialize h of all the vertexes in problem
        including start and goal points
        :return: None
        """
        for vertex in self.all_vertex:
            vertex.h = vertex.calculate_h(self.goal)


if __name__ == '__main__':
    pass
