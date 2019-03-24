class Edge:
    pesoTotale = 0
    def __init__(self, orarioPartenza, orarioArrivo, idCorsa, idLinea, idStazionePartenza, idStazioneArrivo):
        """
        :param orarioPartenza: quando parte
        :param orarioArrivo: quando il bus arriva
        :param idCorsa: 01031
        :param idLinea: AVL
        :param idStazionePartenza: stazione di partenza del bus
        :param idStazioneArrivo: stazione in cui il bus arriva
        """
        self.orarioPartenza = orarioPartenza
        self.orarioArrivo = orarioArrivo
        self.idCorsa = idCorsa
        self.idLinea = idLinea
        self.idStazionePartenza = idStazionePartenza
        self.idStazioneArrivo = idStazioneArrivo
        #self.pesoTotale = minutesCounter(orarioPartenza, orarioArrivo)

    def extractTime(self, orario):
        return orario[0:2], orario[2:]

    def minutesCounter(self, orarioPartenza, orarioArrivo):
        orarioP= orarioPartenza[1:]
        orarioA = orarioArrivo[1:]
        ore_arrivo, minuti_arrivo = extractTime(orarioA)
        ore_partenza, minuti_partenza = extractTime(orarioP)
        if ore_partenza < ore_arrivo:   #non posso prendere la coincidenza
            print("ERRORE!!!!!!!!")
        else:
            minuti = (ore_partenza-ore_arrivo)*60 + (minuti_partenza - minuti_arrivo)
        return minuti


