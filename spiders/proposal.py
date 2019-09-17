
POSITION_POINTS = {'1': 25, '2': 20, '3': 16, 'vr': 5, 'pole': 10, 'pi': 5, 'm2': 15, 'm3': 15}


class Proposal(object):

    def __init__(self, pilot_name, position):
        if pilot_name and isinstance(pilot_name, (list, tuple)):
            pilot_name = pilot_name[0]
        if position and isinstance(position, (list, tuple)):
            position = position[0]
        self.pilot_name = pilot_name
        self.position = str(position).lower()

    def __eq__(self, other):
        return self.pilot_name.lower() == other.pilot_name.lower()

    def __repr__(self):
        return '{pilot_name} - {position}'.format(**self.__dict__)

    def get_points(self):
        return POSITION_POINTS[self.position]


class ProposalUser(Proposal):

    def __init__(self, username, pilot_name, position):
        self.username = username
        super(ProposalUser, self).__init__(pilot_name, position)

    def __repr__(self):
        return 'USERNAME {username} VOTED: {pilot_name} FOR {position}'.format(**self.__dict__)
