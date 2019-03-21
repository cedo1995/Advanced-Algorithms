import fileinput
import glob
import errno

def main():
    pathInfo = "./Files/Info/"      #da vedere il formato del file
    pathLinee = "./Files/Linee/*.LIN"
    id_corsa = ""
    id_linea = ""
    files = glob.glob(pathLinee)
    for name in files:
        print(name)
        with open(name) as f:
            line = f.readline()
            print(line)
            count = 1
            while(line):
                #print(line)
                orario_arrivo= ""
                orario_partenza=""
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
                print(f, count)
                line = f.readline()







if __name__ == '__main__':
        main()
