class Action(list):
    STOP = 5

    def __init__(self, group, direction):
        self.group = group
        self.direction = direction
