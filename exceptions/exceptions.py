class ReaderError(Exception):
    def __init__(self, message):
        super().__init__(message)


class PlotterError(Exception):
    def __init__(self, message):
        super().__init__(message)
