class Hydrogen():
    def __init__(self):
        self.ryd_constant = 13.6
        self.num_of_possible_states = 10
        self.energies = self.states()

    def states(self):
        energies_H = list()
        for n in range(1, self.num_of_possible_states + 1):
            energies_H.append(-self.ryd_constant / n**2)
        return energies_H

    def __call__(self):
        n = int(input('Waht is the principal quantum number?\n'))
        if n <= self.num_of_possible_states and n > 0:
            print(f'The energy of the state of hydrogen is {self.energies[n-1]}.')
        else:
            print('I can not tell you the energy of the state.')

    def __str__(self):
        return f'The {self.num_of_possible_states} energy states of the hydrogen atom: \n' + \
                ' '.join([str(energy) for energy in self.energies])


if __name__ == '__main__':
    h = Hydrogen()
    h()
    print(h)