import os
import re

def buscar_casos(data,fname,numlin):
  casos=0
  # busqueda de caso 1
  if data[12]!="986" and re.search("..008",data[365]):
    print " numlinea:" + str(numlin) + " :: test 1.1:: campo1:" + data[0] + " campo13:" + data[12] + " campo366:"+ data[365]
    casos=casos+1
  if data[12]!="986" and re.search("..025",data[365]):
    print " numlinea:" + str(numlin)+ " :: test 1.2:: campo1:" + data[0] + " campo13:" + data[12] + " campo366:"+ data[365]
    casos=casos+1
  if data[12]=="986" and (not re.search("..025",data[365])) and (not re.search("..008",data[365])):
    print " numlinea:" + str(numlin)+ " :: test 1.3:: campo1:" + data[0] + " campo13:" + data[12] + " campo366:"+ data[365]
    casos=casos+1
  if data[12]=="986" and re.search("..008",data[365]):
    print " numlinea:" + str(numlin)+ " :: test 1.4:: campo1:" + data[0] + " campo13:" + data[12] + " campo366:"+ data[365]
    casos=casos+1
  if data[12]=="986" and re.search("..025",data[365]):
    print " numlinea:" + str(numlin)+ " :: test 1.5:: campo1:" + data[0] + " campo13:" + data[12] + " campo366:"+ data[365]
    casos=casos+1

	# busqueda de caso 2
  if re.search("019",data[116]) and ( re.search("..008",data[365]) or re.search("..008",data[365]) ):
    print " numlinea:" + str(numlin)+ " :: test 2.1:: campo1:" + data[0] + " campo13:" + data[12] + " campo117:" + data[116] + " campo366:"+ data[365]
    casos=casos+1
  if re.search("019",data[116]) and re.search("986",data[12]):
    print " numlinea:" + str(numlin)+ " :: test 2.2:: campo1:" + data[0] + " campo13:" + data[12] + " campo117:" + data[116] + " campo366:"+ data[365]
    casos=casos+1


	# busqueda de caso 3
  if re.search("012",data[12]):
    print " numlinea:" + str(numlin)+ " :: test 3.1:: campo1:" + data[0] + " campo13:" + data[12] + " campo366:"+ data[365]
    casos=casos+1
  if re.search("014",data[12]):
    print " numlinea:" + str(numlin)+ " :: test 3.2:: campo1:" + data[0] + " campo13:" + data[12] + " campo366:"+ data[365]
    casos=casos+1
	
	# busqueda de caso 4
  if re.search("000",data[170]):
    print " numlinea:" + str(numlin)+ " :: test 4.1:: campo1:" + data[0] + " campo171:" + data[170] + " campo366:"+ data[365]
    casos=casos+1

	# busqueda de caso 5
  if re.search("503",data[170]):
    print " numlinea:" + str(numlin)+ " :: test 5.6:: campo1:" + data[0] + " campo171:" + data[170] + " campo366:"+ data[365]
    casos=casos+1

  return casos

path="."
dirList=os.listdir(path)
for fname in dirList:
  es_txt=re.search("\.txt$",fname)
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
  else:
    print fname + " no se trata de un archivo de CDRs"