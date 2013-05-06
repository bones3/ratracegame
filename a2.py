# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    def __init__(self, symbol, row, col):
        """ (Rat, str, int, int) -> NoneType

        Initialize the object with a symbol, row and column parameters
        Example Rat('P', 1, 4)
        """

        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0
        
    def set_location(self, row, col):
        """ (Rat, row, col) -> NonType

        Set the Rat's location by row and column
        """
        self.row = row
        self.col = col
        
    def eat_sprout(self):
        """(Rat) -> NoneType
        Rat counter for eating sprouts
        """
        self.num_sprouts_eaten +=1

    def __str__(self):
        """(Rat) -> str
        Print the rat, where is the location and how sprouts were eaten.
        example 'J at (4, 3) ate 2 sprouts.'
        """
        return '{0} at ({1}, {2}) ate {3} sprouts.'.format(
                self.symbol, self.row, self.col, self.num_sprouts_eaten)
        
      
class Maze:
    """ A 2D maze. """

    def __init__(self, maze, rat_1, rat_2):
        """(Maze, list of list of str, Rat, Rat) -> NoneType
        Initialize this maze's four instance variables:
        maze: a maze with contents specified by the second parameter.
        rat_1: the first rat in the maze.
        rat_2: the second rat in the maze.
        num_sprouts_left: the number of uneaten sprouts in this maze.
        example Maze([['#', '#', '#', '#', '#', '#', '#'], 
          ['#', '.', '.', '.', '.', '.', '#'], 
          ['#', '.', '#', '#', '#', '.', '#'], 
          ['#', '.', '.', '@', '#', '.', '#'], 
          ['#', '@', '#', '.', '@', '.', '#'], 
          ['#', '#', '#', '#', '#', '#', '#']], 
          Rat('J', 1, 1),
          Rat('P', 1, 4))
        """
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2
        self.num_sprouts_left = sum([s.count(SPROUT) for s in maze])
        self.maze[self.rat_1.row][self.rat_1.col] = self.rat_1.symbol
        self.maze[self.rat_2.row][self.rat_2.col] = self.rat_2.symbol

    def is_wall(self, row, col):
        """ (Maze, int, int) -> bool
        Return True if and only if there is a
        wall at the given row and column in the maze.
        """
        return self.maze[row][col] ==WALL

    def get_character(self, row, col):
        """(Maze, int, int) -> str
        Return the character in the maze at the given row and column.
        If a rat at the location than it should be return rather than HALL
        """
        return self.maze[row][col] if self.maze[row][col] != Rat else HALL

    def move(self, rat, vertical, horizontal):
        """ (Maze, Rat, int, int) -> bool
        Move the rat in the given direction, unless there is a wall in the way.
        Also, check for a Brussels sprout at that location and, if present:
        """
        row = rat.row + vertical
        col = rat.col + horizontal

        if self.is_wall(row, col) == False and (vertical != 0 or horizontal != 0):
            if self.maze[row][col] == SPROUT:
                if self.num_sprouts_left > 0:
                    rat.eat_sprout()
                    self.maze[row][col] = HALL
                    self.num_sprouts_left -= 1
            self.maze[row - vertical][col - horizontal] = HALL
            self.maze[row][col] = rat.symbol
            rat.set_location(row, col)
        return self.is_wall(row, col) != True

    def __str__(self):
        """ (Maze) -> str
        first parameter is the maze and return as a string in the format below
        example:
        #######
        #J..P.#
        #.###.#
        #..@#.#
        #@#.@.#
        #######
        J at (1, 1) ate 0 sprouts.
        P at (1, 4) ate 0 sprouts.
        """
        return "".join(["".join(x)+'\n' for x in self.maze]) + self.rat_1.__str__() + '\n' + self.rat_2.__str__()

    
        
    
