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
        #print("orario partenza ",orarioPartenza, " orario arrivo ", orarioArrivo )
        minuti = 0
        orarioP= orarioPartenza[1:]
        orarioA = orarioArrivo[1:]
        ore_arrivo, minuti_arrivo = self.extractTime(orarioA)
        ore_partenza, minuti_partenza = self.extractTime(orarioP)
        #print("ora partenza ", ore_partenza ," ora arrivo ",ore_arrivo)
        if ore_partenza <= ore_arrivo:   #non posso prendere la coincidenza
            minuti = (int(ore_arrivo)-int(ore_partenza))*60 + int(minuti_arrivo) - int(minuti_partenza)
        else:
            #print(float(ore_partenza),float(ore_arrivo),float(minuti_partenza),float(minuti_arrivo))
            print("ERRORE!!!!!!!")
            #print(" minuti ", minuti)



        return minuti

    #TODO Aggiunto metodo per il confronto degli orari
    def isLaterThan(self, orarioPartenza, orario):
        oreOrario, minutiOrario = self.extractTime(orario)
        orePartenza, minutiPartenza = self.extractTime(orarioPartenza)
        if oreOrario < orePartenza or (oreOrario == orePartenza and minutiOrario <= minutiPartenza):
            return True
        else:
            return False


