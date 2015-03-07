import os
import re

def quitar_ceros(numero):
  while numero[0]=="0":
    numero=numero[1:]
    try:
      temp=numero[0]
    except:
      numero="---"
      break
  return numero

def buscar_casos(data,fname,numlin):
  casos=0
  caller = quitar_ceros(data[121])
  called = quitar_ceros(data[116])
  duration = quitar_ceros(data[19])
  print " numlinea:" + str(numlin)+ " (1)" + data[0] + \
        " (7)" + data[6] + " (19)"+ data[18] + \
        " (20)"+ duration + \
        " (54)" + data[53] + " (55)"+ data[54] + \
        " (122)" + caller + " (117)"+ called + \
        " (366)"+ data[365]
  #casos=casos+1

  return casos

path="."
dirList=os.listdir(path)
for fname in dirList:
  es_txt=re.search("\.csv$",fname)
  if es_txt:
    f = open(fname, "r")
    numlinea=0
    casos=0
    while True:
      linea = f.readline()
      numlinea=numlinea+1
      if not linea: break
      data = linea.split(",")
      
      campo366_ok1 = data[365] != ""
      campo366_ok2 = not re.search("..002",data[365])
      campo366_ok3 = not re.search("..001",data[365])
      campo366_ok = campo366_ok1 and campo366_ok2 and campo366_ok3
      
      opcion1_ok= data[0] == "005"
      opcion2_ok= data[0] == "006"
      opcion3_ok= (data[0] == "240") and (campo366_ok)
      
      if opcion1_ok or opcion2_ok or opcion3_ok:
        casos_linea = buscar_casos(data,fname,numlinea)
        if casos_linea:
          casos=casos+1
    
    if casos>0:
      print fname, "==========================================", casos, "\n"
