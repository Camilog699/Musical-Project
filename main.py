from Resources.automaton import Automaton
from GUI.GUI import GUI


def main():
    base = 3
    automaton = Automaton()
    comb = automaton.createBase(base)
    automaton.createCell(comb, 10, base - 1, ['Bajo', 'Guitarra', 'saxo'])
    GUI(automaton)
    # bajo, caja musical, campana,
    #drum, flauta, guitarra, organeta, timbales, violin, voz


main()
