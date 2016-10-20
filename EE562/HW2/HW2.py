"""
Last update: 2016-10-19 01:31
Maintainer: Cunzhi Ren <renc@uw.edu>
Environment: python 3.5.2
HomeWork1 of EE562 Artificial Intelligence for Engineers:
A* Search   refer to
http://homes.cs.washington.edu/~shapiro/EE562/hw2/index.html
***************************************************************
BTW the data set files is supposed store in the same directory
as this program. Or you might change the file path from line
134 to 136
***************************************************************

"""
from math import sqrt, pow
import operator


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
        self.successors = []

    def calculate_h(self, goal):
        """
        This method calculate h of vertex
        :param goal: the goal point
        :return: h
        """
        h = self.distance(goal, self)
        return h

    def calculate_g(self, previous_node):
        """
        This method calculates g of vertex
        :param previous_node: the node before this vertex
        :return: g of this vertex = previous_g + current_increase
        """
        previous_g = previous_node.g
        current_increase = self.distance(previous_node, self)
        return previous_g + current_increase

    def calculate_f(self):
        """
        This method calculate f
        :return: None
        """
        self.f = self.h + self.g

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

    def is_on_open(self, open):
        """
        This method checks if node is on open list
        :param open: current open list
        :return: Boolean
        """
        for node in open:
            if node.x == self.x and node.y == self.y:
                return node
        return False

    def is_on_closed(self, closed):
        """
        This method checks if node is on closed list
        :param closed: current closed list
        :return: Boolean
        """
        for node in closed:
            if node.x == self.x and node.y == self.y:
                return node
        return False

    def remove_vertex(self, list):
        """
        This method removes node from a list
        :param list:
        :return: None
        """
        for node in list:
            if node.x == self.x and node.y == self.y:
                list.remove(node)


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
    data_set1, data_set2 and data_set3 represent their paths respectively
    """

    data_set1 = './data_set1'
    data_set2 = './data_set2'
    data_set3 = './data_set3'
    output_format = "({0},{1})\t\t\t{2}"
    index_format = "{0}\t\t\t{1}"

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
        self.diagonals = self.get_diagonals
        self.successors_init()

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

    @property
    def get_diagonals(self):
        """
        This method gets all the diagonals of obstacles in the map
        :return: diagonals
        """
        diagonals = []
        for o in self.obstacle:
            for i in range(2):
                diagonal = [[o.vertex[i].x, o.vertex[i].y], [o.vertex[i + 2].x, o.vertex[i + 2].y]]
                diagonals.append(diagonal)
        return diagonals

    @staticmethod
    def line_intersection(line1, line2):
        """
        This static method figure out the intersection of
        line1 and line2 using Cramer's rule
        :return: intersection
        """
        x_diff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
        y_diff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]

        div = det(x_diff, y_diff)
        if div == 0:
            return False

        d = (det(*line1), det(*line2))
        x = det(d, x_diff) / div
        y = det(d, y_diff) / div
        return [x, y]

    def is_successor_legal(self, current_node, successor):
        """
        This method checks if successor is a legal successor of
        current node
        :param current_node:
        :param successor:
        :return:
        """
        for diagonal in self.diagonals:
            line = [[current_node.x, current_node.y], [successor.x, successor.y]]
            intersection = self.line_intersection(diagonal, line)
            if not intersection:
                continue
            elif (diagonal[0][0] < intersection[0] < diagonal[1][0] or diagonal[1][0] < intersection[0] < diagonal[0][
                0]) \
                    and (line[0][0] < intersection[0] < line[1][0] or line[1][0] < intersection[0] < line[0][0]):
                return False
        return True

    def successors_init(self):
        """
        This method gathers all the legal successors of
        each node in the map
        :return: None
        """
        for current_node in self.all_vertex:
            for successor in self.all_vertex:
                if self.is_successor_legal(current_node, successor):
                    current_node.successors.append(successor)

    def search_path(self):
        """
        This method implements A* algorithm to find the shortest
        path from start point to goal point
        :return: current_node when it is the goal
        """
        open_list = []
        self.start.g = 0
        self.start.calculate_f()
        open_list.append(self.start)
        closed = []
        while len(open_list):
            current_node = self.min_f_node_on_open(open_list)
            if self.is_goal(current_node):
                return current_node
            open_list.remove(current_node)
            closed.append(current_node)
            for successor in current_node.successors:
                if successor.is_on_closed(closed):
                    continue
                tentative_g = successor.calculate_g(current_node)
                if not successor.is_on_open(open_list):
                    open_list.append(successor)
                elif tentative_g > successor.g:
                    continue
                successor.parent = current_node
                successor.g = tentative_g
                successor.calculate_f()
        return False

    @staticmethod
    def min_f_node_on_open(open_list):
        """
        This static method finds the node with min f
        on open list
        :param open_list: current open list
        :return: min_f_node_on_open
        """
        open_sorted_by_f = sorted(open_list, key=operator.attrgetter('g'))
        min_f_node_on_open = open_sorted_by_f[0]
        return min_f_node_on_open

    def is_goal(self, node):
        """
        This method checks if node is the goal. Return True if it is
        the goal, or else return False
        :param node: current node
        :return: Boolean
        """
        return node.x is self.goal.x and node.y is self.goal.y

    def generate_path(self, node):
        """
        This method generates solution path
        :param node: goal point
        :return: path
        """
        temp_stack = []
        path = []
        while node.parent:
            temp_stack.append(node)
            node = node.parent
        temp_stack.append(self.start)
        while len(temp_stack):
            path.append(temp_stack.pop())
        return path

    def solution(self):
        """
        This method uses A* algorithm solves mini cost path problem
        and print the solution path with cumulative cost of
        each node in path
        :return: None
        """
        path = self.generate_path(self.search_path())
        print(self.index_format.format('Point', 'Cumulative Cost'))
        for i in range(len(path)):
            print(self.output_format.format(path[i].x, path[i].y, round(path[i].g, 3)))
        print("################################\n")


if __name__ == '__main__':
    # This is your simple data set solution
    print("#######Data set1 solution#######")
    pm1 = ProblemMap(ProblemMap.data_set1)
    pm1.solution()
    # This is your complex data set solution
    print("#######Data set2 solution#######")
    pm2 = ProblemMap(ProblemMap.data_set2)
    pm2.solution()
    # This is my data set with 7 obstacles solution
    print("#######Data set3 solution#######")
    pm3 = ProblemMap(ProblemMap.data_set3)
    pm3.solution()
