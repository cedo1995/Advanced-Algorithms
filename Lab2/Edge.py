import sys
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
        # print("orario partenza ",orarioPartenza, " orario arrivo ", orarioArrivo )
        minuti = sys.maxsize
        ore_arrivo, minuti_arrivo = self.extractTime(orarioArrivo[1:])
        ore_partenza, minuti_partenza = self.extractTime(orarioPartenza[1:])
        minuti_arrivo = int(ore_arrivo) * 60 + int(minuti_arrivo)
        minuti_partenza = int(ore_partenza) * 60 + int(minuti_partenza)
        # print("ora partenza ", ore_partenza ," ora arrivo ",ore_arrivo)
        if minuti_partenza <= minuti_arrivo:
            minuti = minuti_arrivo - minuti_partenza

        return minuti

    #TODO Aggiunto metodo per il confronto degli orari
    def isLaterThan(self, orarioPartenza, orario):
        oreOrario, minutiOrario = self.extractTime(orario)
        orePartenza, minutiPartenza = self.extractTime(orarioPartenza)
        if oreOrario < orePartenza or (oreOrario == orePartenza and minutiOrario <= minutiPartenza):
            return True
        else:
            return False


