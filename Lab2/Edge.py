class Edge:
    pesoTotale = 0
    def __init__(self, orarioPartenza, orarioArrivo, idCorsa, idLinea):
        """
        :param orarioArrivo: quando il bus arriva
        :param orarioPartenza: quando parte
        :param idCorsa: 01031
        :param idLinea: AVL
        """
        self.orarioPartenza = orarioPartenza
        self.orarioArrivo = orarioArrivo
        self.idCorsa = idCorsa
        self.idLinea = idLinea
        self.pesoTotale = minutesCounter(orarioPartenza, orarioArrivo)

    def extractTime(self, orario):
        return orario[0:2], orario[2:]

    def minutesCounter(self, orarioArrivo, orarioPartenza):
        orarioP= orarioPartenza[1:]
        orarioA = orarioArrivo[1:]
        ore_arrivo, minuti_arrivo = extractTime(orarioA)
        ore_partenza, minuti_partenza = extractTime(orarioP)
        if ore_partenza < ore_arrivo:   #non posso prendere la coincidenza
            print("ERRORE!!!!!!!!")
            break
        else:
            minuti = (ore_partenza-ore_arrivo)*60 + (minuti_partenza - minuti_arrivo)
        return minuti


