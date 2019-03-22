import fileinput
import glob
import errno
import codecs
#TODO: creare classe arco con orario arrivo e partenza e id corsa poi ci sarà una matrice delle adiacenze dove in corrispondenza delle stazioni collegate direttamente ci sarà un oggetto lista di archi
def main():
    pathInfo = "./Files/Info/"      #da vedere il formato del file
    fileStazioni = pathInfo + "bahnhof"
    stazioni = {}
    id_staz=0
    nome_staz=""
    with codecs.open(fileStazioni,encoding='latin-1') as f:
        f.readline() #salto la prima riga
        line = f.readline()
        count=0
        while(line):
            id_staz=line[0:9]
            nome_staz = line[14:34]
            stazioni[id_staz]=[count ,nome_staz]
            line = f.readline()
            count+=1
    pathLinee = "./Files/Linee/*.LIN"
    id_corsa = ""
    id_linea = ""
    files = glob.glob(pathLinee)
    i=0
    for name in files:
        i+=1
        print(name,i)
        with codecs.open(name,encoding='latin-1') as f:
            line = f.readline()
            #print(line)
            count = 1
            while(line):
                #print(line)
                orario_arrivo= ""
                orario_partenza=""
                nome_stazione=""
                id_stazione=""
                if line.startswith("*Z"):
                    id_corsa = line[3:8]
                    id_linea = line[9:15]
                if not line.startswith("*"):        #se è una riga utile
                    id_stazione = line[0:9]
                    nome_stazione = line[10:30]
                    if not line[32:].startswith(" "):
                        orario_arrivo = line[32:37]
                        if not line[39:].startswith(" "):
                             orario_partenza = line[39:44]
                    else:
                        orario_partenza = line[39:44]
                count += 1
                print(nome_stazione,id_stazione)
                line = f.readline()







if __name__ == '__main__':
        main()
