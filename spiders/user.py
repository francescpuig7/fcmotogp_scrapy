
class User(object):
    def __init__(self, name, total_points=0, proposals=None):
        self.name = name
        self.total_points = total_points
        if proposals:
            self.proposals = proposals[:]

    @total_points.setter
    def total_points(self, points):
        self.total_points = points

    @total_points.deleter
    def total_points(self):
        del self.total_points
