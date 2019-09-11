
POSITION_POINTS = {'1': 25, '2': 20, '3': 16, 'vr': 5, 'pole': 10, 'pi': 5, 'm2': 15, 'm3': 15}


class Proposal(object):

    def __init__(self, pilot_name, position):
        self.pilot_name = pilot_name
        self.position = position

    def __eq__(self, other):
        return self.pilot_name == other.pilot_name

    def get_points(self):
        return POSITION_POINTS[self.position]


class ProposalUser(Proposal):

    def __init__(self, username, pilot_name, position):
        self.username = username
        super(ProposalUser, self).__init__(pilot_name, position)

    def __eq__(self, other):
        return self.pilot_name.lower() == other.pilot_name.lower()

    def get_points(self):
        return POSITION_POINTS[self.position]

    def __repr__(self):
        return 'USERNAME {} VOTED: {} FOR {} '.format(self.username, self.pilot_name, self.position)
