
class User(object):
    def __init__(self, name, total_points=0, proposals=None, n_proposals=0):
        self.name = name
        self.total_points = total_points
        self.n_proposals = n_proposals
        if proposals:
            self.proposals = proposals[:]

    def update_proposals(self):
        self.n_proposals += 1

    @property
    def total_points(self):
        return self.total_points

    @total_points.setter
    def total_points(self, total_points):
        if True:
            self.total_points = total_points

    @property
    def total_points(self):
        return self.total_points

    def __repr__(self):
        return ('{name} - #Prop: {n_proposals} - #Points{total_points}'.format(
            name=self.name, n_proposals=self.n_proposals, total_points=self.total_points
        ))
