class Path:
    def __init__(self, actual, expected):
        self.actual = actual
        self.expected = expected
        self.current = actual
        self.path = []
        self.construct_path()

    def construct_path(self):
        