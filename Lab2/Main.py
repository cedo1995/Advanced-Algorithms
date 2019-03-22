import fileinput
import glob
import errno
import codecs
#TODO: creare classe arco con orario arrivo e partenza e id corsa poi ci sarà una matrice delle adiacenze dove in corrispondenza delle stazioni collegate direttamente ci sarà un oggetto lista di archi
def main():
    pathInfo = "./Files/Info/"      #da vedere il formato del file
    fileStazioni = pathInfo + "bahnhof"
    stazioni = {}
    id_staz = 0
    nome_staz = ""
    matrice = []
    with codecs.open(fileStazioni, encoding='latin-1') as f:
        f.readline()    #salto la prima riga
        line = f.readline()
        count = 0       #contatore delle stazioni
        while(line):    #finchè il file non finisce
            id_staz = line[0:9]
            nome_staz = line[14:34]     #salta in tutti i modi la scritta CdT o CtF.. va bene?
            stazioni[id_staz] = [count, nome_staz]  #se cambio sopra devo mettere nome_staz[0:20]

            line = f.readline()     #passo alla linea successiva
            count += 1

    pathLinee = "./Files/Linee/*.LIN"

    files = glob.glob(pathLinee)
    i = 0

    for name in files:      #per ciascun file presente nella cartella Linee
        i += 1
        print("NOME DEL FILE: ",name,"\t File numero",i)      #primo file letto
        with codecs.open(name, encoding='latin-1') as f:    #FONDAMENTALE la codifica del file
            line = f.readline()     #leggo la prima riga
            id_corsa = ""
            id_linea = ""
            j = 0           #alla prima fermata sarà a 0, poi sarà un contatore
            orario_arrivo = []
            orario_partenza = []
            nome_stazione = []
            id_stazione = []
            while(line):        #finchè non finisce il file
                #print(line)

                if line.startswith("*Z"):       #identifica le righe che danno informazioni sulla corsa
                    id_corsa = line[3:8]        #utile per l'arco
                    id_linea = line[9:15]
                if line.startswith("*"):
                    j = 0

                else:        #se è una riga che contiene informazioni riguardo alle fermate
                    print(line[0:9])
                    id_stazione.append(line[0:9])          #inserisco l'id
                    print("ID: ", id_stazione[j])
                    nome_stazione.append(line[10:30])      #inserisco il nome
                    print("\t", nome_stazione[j])
                    if not (line[32:].startswith(" ") and line[32:].startswith("-")):
                        orario_arrivo.append(line[32:37])
                        print("Orario arrivo: ", str(orario_arrivo[j]))

                    orario_partenza.append(line[39:44])
                    print("Orario partenza: ", str(orario_partenza[j]))

                    j += 1    #incremento j

                line = f.readline()








if __name__ == '__main__':
        main()
