from Resources.automaton import Automaton
from GUI.GUI import GUI


def main():
    base = 5
    automaton = Automaton()
    comb = automaton.createBase(base)
    automaton.createCell(comb, 10, base - 1, ['Bajo', 'Guitarra', 'Voz'])
    GUI(automaton)
    # bajo, caja musical, campana,
    #drum, flauta, guitarra, organeta, timbales, violin, voz


main()
