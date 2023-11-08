import os
import random

def elimina_righe_da_file(lista_file_filtrata, perc_lines):
    for file_ in lista_file_filtrata:
        with open(file_, "r") as file:
            contenuto = file.readlines()
            len_perc_righe_da_rimuovere = int(len(contenuto) * perc_lines / 100)
            r_int_index = []
            while len(r_int_index) < len_perc_righe_da_rimuovere:
                r_int_index.append(random.randint(0,len(contenuto)-1))
            for r in r_int_index:
                contenuto.remove(contenuto[r])
            lista_righe_risultato = "".join(contenuto)
            file.close()
        with open(file_.split(".")[0]+"_modificato."+file_.split(".")[1], "w") as file:
            file.write(lista_righe_risultato)
            file.close()
    return lista_file_filtrata

def elimina_caratteri_da_file(lista_file_filtrata, perc_chars):
    for file_ in lista_file_filtrata:
        with open(file_.split(".")[0]+"_modificato."+file_.split(".")[1], "r") as file:
            contenuto = file.readlines()
            nuova_lista_righe=[]
            for r in contenuto:
                len_perc_char_da_rimuovere = int(len(r) * perc_chars / 100)
                r_int_index = []
                while len(r_int_index) < len_perc_char_da_rimuovere:
                  r_int_index.append(random.randint(0,len(r)-1))
                nuova_riga = ""
                for c in range(len(r)):
                    if c not in r_int_index:
                        nuova_riga=nuova_riga+r[c]
                nuova_lista_righe.append(nuova_riga)
                # print("dopo-----> ",len(r),"-",len(r_int_index),"=",len(nuova_riga),"\n",r,"\n",nuova_riga)
            lista_righe_risultato = "".join(nuova_lista_righe)
            file.close()

        with open(file_.split(".")[0]+"_modificato."+file_.split(".")[1], "w") as file:
            file.write(lista_righe_risultato)
            file.close()
    return lista_file_filtrata


def estrai_file(directory):
    lista_file_risultato = []
    for root, _, files in os.walk(directory):
        for file in files:
            lista_file_risultato.append(os.path.join(root, file))
    return lista_file_risultato

def filtra_estensioni(lista_file,estensioni):
    lista_file_filtrata = []
    for x in lista_file:
        if ("." + x.split(".")[1] in estensioni) or (len(estensioni)==0):
            lista_file_filtrata.append(x)
    return lista_file_filtrata

def filtra_modificati(lista_file):
    lista_file_filtrata = []
    for x in lista_file:
        if (x.split(".")[0][-10:] != "modificato"):
            lista_file_filtrata.append(x)
    return lista_file_filtrata

def cancella_righe(estensioni=[], perc_lines=5, perc_chars=5, directory=""):
    lista_file = []
    lista_file = lista_file + estrai_file(directory)

    lista_file_filtrata=filtra_estensioni(lista_file,estensioni)
    lista_file_filtrata=filtra_modificati(lista_file_filtrata)

    lista_file_filtrata_ridotta_riga = elimina_righe_da_file(lista_file_filtrata, perc_lines)
    lista_file_filtrata_ridotta_carattere = elimina_caratteri_da_file(lista_file_filtrata_ridotta_riga, perc_chars)

cancella_righe(estensioni= [".js",".txt"], perc_lines = 4, perc_chars = 6, directory= "directory_example_da_modificare/")
