from Resources.automaton import Automaton


def main():
    base = 3
    automaton = Automaton()
    comb = automaton.createBase(base)
    automaton.createCell(comb, 10, base - 1)


main()
