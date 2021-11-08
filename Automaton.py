class Automaton:
    def __init__(self, in_file):
        self._states = []
        self._final_states = []
        self._alphabet = []
        self._transitions = []
        self.parse(in_file)
        self._mapping = {}
        self.create_mapping()

    def parse(self, in_file):
        index = 1
        f = open(in_file)
        lines = f.readlines()
        for line in lines:
            if index == 1:
                self._states = line.split()
            elif index == 2:
                self._final_states = line.split()
            elif index == 3:
                self._alphabet = line.split()
            else:
                self._transitions.append(line.split())
            index += 1

    def get_states(self):
        return self._states

    def get_final_states(self):
        return self._final_states

    def get_alphabet(self):
        return self._alphabet

    def get_transitions(self):
        return self._transitions

    def create_mapping(self):
        for i in self._transitions:
            tuply = (i[0], i[1])
            if tuply in self._mapping:
                self._mapping[tuply].append(i[2])
            else:
                self._mapping[tuply] = [i[2]]

    def check_DFA(self):
        for elem in self._mapping:
            if len(self._mapping[elem]) > 1:
                return False
        return True

    '''
    sequence is a char sequence
    '''

    def check_sequence(self, sequence):
        if not self.check_DFA():
            return False
        start_state = self._states[0]
        for char in sequence:
            tuply = (start_state, char)
            if tuply in self._mapping:
                start_state = self._mapping[tuply][0]
            else:
                return False
        return True


a = Automaton("fa.in")
print("The states are " + str(a.get_states()))
print("The final states are " + str(a.get_final_states()))
print("The alphabet is " + str(a.get_alphabet()))
print("The transitions are " + str(a.get_transitions()))
print(a.check_DFA())
print(a.check_sequence("232"))
