import sys

def procuraLista(lst,elem):
    
    for i in range(len(lst)):
        
        if(lst[i] == elem):
            return 1
    return 0

def montaEstadosMoore(estadosNormal,estadosMultSimbolos):

    estadosMoore    = []

    for i in range (len(estadosNormal)):

        estadosMoore.append(estadosNormal[i])

        for j in range (len(estadosMultSimbolos)):
            
            if(estadosMultSimbolos[j][0] == estadosNormal[i]):
                
                tam = len(estadosMultSimbolos[j][1])
                stringAUX = estadosMultSimbolos[j][0]
            
                for i in range (tam-1):
                    stringAUX += "'"
                    estadosMoore.append(stringAUX)

 
    return estadosMoore

def montaEstadosEndMoore(estadosNormal,estadosMultSimbolos,estadosFinais):

    estadosFinaisMoore = []

    for i in range (len(estadosFinais)):

        estadosFinaisMoore.append(estadosFinais[i])

        for j in range (len(estadosMultSimbolos)):
            
            if(estadosMultSimbolos[j][0] == estadosFinais[i]):
                
                tam = len(estadosMultSimbolos[j][1])
                stringAUX = estadosMultSimbolos[j][0]
            
                for i in range (tam-1):
                    stringAUX += "'"
                    estadosFinaisMoore.append(stringAUX)

    
    return estadosFinaisMoore

def montaTransicoesMoore(estadosMoore,transicoes):
    
    transicoesMoore     = []
    lstNos              = []
    no                  = [None,None]
    noMoore             = [None,None,None]

    e_inicial           = ""
    s_entrada           = ""
    e_final             = ""

    for i in range (len(estadosMoore)):

        no = [estadosMoore[i],None]

        if(i == 0):
            lstNos.append(no)            

        else:
            for j in range(len(transicoes)):

                if(transicoes[j][2] == no[0]):
                
                    if no[1] == None:
                    
                        no[1] = transicoes[j][3]
                        lstNos.append(no)
                
                    else:
                        if (i+1 < len(estadosMoore)):
                            no = [estadosMoore[i+1],transicoes[j][3]]
                            lstNos.append(no)
    
    
    
    
    for i in range(len(transicoes)):
        
        for j in range(len(lstNos)):
            
            if(transicoes[i][2] == lstNos[j][0]):

                if (transicoes[i][3] == lstNos[j][1]):
                    
                    e_inicial = transicoes[i][0]
                    s_entrada = transicoes[i][1]
                    e_final   = lstNos[j][0]

                    noMoore = [e_inicial,s_entrada,e_final] 
                    transicoesMoore.append(noMoore)
                
                else:

                    if j + 1 < len(lstNos):

                        if(transicoes[i][3] == lstNos[j+1][1]):
                            
                            e_inicial = transicoes[i][0]
                            s_entrada = transicoes[i][1]
                            e_final   = lstNos[j+1][0]

                            noMoore = [e_inicial,s_entrada,e_final] 
                            transicoesMoore.append(noMoore)

    return transicoesMoore,lstNos  



def montaMoore(estadosNormal,estadosMultSimbolos,transicoes,simbolos,estadoInic,estadosFinais,alfabetoSaida,nomearqsaida):

    print("=========== Conversão: Mealy para Moore ============")

    estadosMooreInic    = []
    estadosMoore        = []
    simbolosMoore       = []
    alfabetoSaidaMoore  = []
    transicoesMoore     = []
    definicao           = []

    estadosMoore = montaEstadosMoore(estadosNormal,estadosMultSimbolos);

    print("Estados Moore: ",estadosMoore)

    estadosFinaisMoore = montaEstadosEndMoore(estadosNormal,estadosMultSimbolos,estadosFinais)
    
    print("Estados end Moore",estadosFinaisMoore)

    simbolosMoore = simbolos;

    estadosMooreInic.append(estadoInic)

    print("Simbolos Moore: ",simbolosMoore)

    alfabetoSaidaMoore = alfabetoSaida;

    print("Alfabeto saida Moore: ",alfabetoSaidaMoore);
    
    transicoesMoore,definicao = montaTransicoesMoore(estadosMoore,transicoes)

    print("Transicoes Moore: ")

    for i in range(len(transicoesMoore)):
        print(transicoesMoore[i])
    
    print("Definicões: ")

    for i in range(len(definicao)):
        print(definicao[i])

    salvaMooreArq(nomearqsaida,estadosMoore,estadosFinaisMoore,simbolosMoore,alfabetoSaidaMoore,transicoesMoore,estadosMooreInic,definicao)
    
    print("Arquivo salvo.")

def multSimboloEstado(lstEstados,lstTransicao,lstSimbolos):
    
    quantTransic    = len(lstTransicao) # Quantidade de Transicoes;
    quantEstados    = len(lstEstados)   # Quantidade de Estados;
    simbolos        = []                # Simbolos encontrados na transicao para um estado;
    estadosMult     = []                # Estados com mais de um simbolo
    pack            = []                # Pacote auxiliar
    megaPack        = []                # Pacote com estados finais com mais de um simbolo na transicao;

    #Passa por todos estados
    for i in range (quantEstados):
        quant = 0

        #Passa por todas as transicoes
        for j in range (quantTransic):

            # Se <estadoAtual> == <estadoFinalDaTransicao>
            if lstEstados[i] == lstTransicao[j][2]:
                
                # Procura se esse simbolo da trasicao já foi usado por outra transicao
                # 0 = False
                if (procuraLista(simbolos,lstTransicao[j][1]) == 0):
                    
                    estado = lstTransicao[j][2]         # Pega o estado atual
                    quant +=1                           # Um transicao com simbolo novo
                    simbolos.append(lstTransicao[j][1]) # Adciona esse simbolo na lista de simbolos
        
        if quant >= 2 :
                
            pack.append(estado)     # Adciona o estado atual
            pack.append(simbolos)   # Os simbolos que esse estado recebe
            megaPack.append(pack)   
        
        pack = []       
        quant = 0
        simbolos = []
     
    return megaPack

def salvaMooreArq(nomearqsaida,estadosMoore,estadosFinaisMoore,simbolosMoore,alfabetoSaidaMoore,transicoesMoore,estadosMooreInic,definicao):
    
    arq = open(nomearqsaida, 'w')
    arq.write("moore\n")


    for i in range (len(estadosMoore)):
        
        
        arq.write(str(estadosMoore[i]))

        if i+1 < len(estadosMoore):
            arq.write(" ")

    arq.write("\n")

    #========================================

    for i in range(len(simbolosMoore)):
        
        arq.write(str(simbolosMoore[i]))
        
        if i+1 < len(simbolosMoore):
            arq.write(" ")

    arq.write("\n")
    
    #=======================================

    for i in range (len(estadosMooreInic)):

        arq.write(str(estadosMooreInic[i]))
        
        if i+1 < len(estadosMooreInic):
            arq.write(" ")

    arq.write("\n")

    for i in range (len(estadosFinaisMoore)):

        arq.write(str(estadosFinaisMoore[i]))
        
        if i+1 < len(estadosFinaisMoore):
            arq.write(" ")

    arq.write("\n")

    for i in range (len(alfabetoSaidaMoore)):

        arq.write(str(alfabetoSaidaMoore[i]))
        
        if i+1 < len(alfabetoSaidaMoore):
            arq.write(" ")

    arq.write("\n")



    #========================================
    
    for i in range(len(transicoesMoore)):
        for j in range(len(transicoesMoore[i])):
            
            arq.write(str(transicoesMoore[i][j]))
            
            if j+1 < len(transicoesMoore[i]):
                arq.write(" ")
        arq.write("\n")

    arq.write("-----\n")

    #=========================================
    
    
    for i in range(len(definicao)):
        
        flag = False
     
        if (definicao[i][1] == None):
                
            arq.write(str(definicao[i][0]))
        else:
            arq.write(str(definicao[i][0]))
            arq.write(" ")
            arq.write(str(definicao[i][1]))
        
                
        

        
        arq.write("\n")

    arq.close()


def converteMealyparaMoore(arq,nomearqsai):

    estadoInit      = None
    lstEstados      = []
    lstSimbolos     = []
    lstAlfasai      = []
    lstTransicao    = []

    linha = arq.readline()
    linha = linha.strip()

    lstEstados = linha.split(" ")
    
    linha = arq.readline()
    linha = linha.strip()
    
    lstSimbolos = linha.split(" ")
    
    linha = arq.readline()
    linha = linha.strip()
    
    estadoInit = linha
    
    linha = arq.readline()
    linha = linha.strip()
    
    lstEstadosaida = linha.split(" ")
    linha = arq.readline()
    linha = linha.strip()
    
    lstAlfasai = linha.split(" ")

    linha = arq.readline()

    while linha!= "":
        
        linha = linha.strip()
        linha = linha.split()
        
        lstTransicao.append(linha)
        
        linha = arq.readline()


    estadosMultSimbolos = multSimboloEstado(lstEstados,lstTransicao,len(lstSimbolos))

    montaMoore(lstEstados,estadosMultSimbolos,lstTransicao,lstSimbolos,estadoInit,lstEstadosaida,lstAlfasai,nomearqsai)

  
#Funções Mooe pra Mealy;


def converteMooreparaMealy(arq,nomearqsai):
    
    print("=========== Conversão: Moore para Mealy ============")
    
    lstestadosMoore     = []
    alfabetoEntrada     = []
    estadoInicial       = ""
    estadosFinais       = []
    alfabetoSaida       = []
    transicoes          = []
    marca               = "-----"
    lstNos              = []

    lstestadosMealy     = []
    estadosfinaisMealy  = []
    transicoesMealy     = []


    linha = arq.readline()
    linha =linha.strip()
    lstestadosMoore = linha.split(" ")
    

    linha = arq.readline()
    linha = linha.strip()
    alfabetoEntrada = linha.split(" ")
    

    linha = arq.readline()
    linha = linha.strip()
    estadoInicial = linha
    

    linha = arq.readline()
    linha = linha.strip()
    estadosFinais = linha.split(" ")
    


    linha = arq.readline()
    linha = linha.strip()
    alfabetoSaida = linha.split(" ")
    

    linha = arq.readline()
    linha = linha.strip()

    while linha != marca:
        linha = linha.strip()
        linha = linha.split(" ")
        transicoes.append(linha)
        linha = arq.readline()
        linha = linha.strip()
    

    linha = arq.readline()
    while linha != "":
        linha = linha.strip()
        linha = linha.split(" ")
        lstNos.append(linha)
        linha = arq.readline()

    lstestadosMealy = montaEstadosMealy(lstestadosMoore)
   
    estadosfinaisMealy = montaEstadosfinaisMealy(estadosFinais)

    transicoesMealy = montaMealy(transicoes,lstNos)


    print("Estados Mealy: ", lstestadosMealy)
    print("Alfabeto Entrada: ", alfabetoEntrada)
    print("Estado Inicial: ", estadoInicial)
    print("Estados Finais: ", estadosfinaisMealy)
    print("Alfabeto Saida: ", alfabetoSaida)

    print("Transicoes: " )
    for i in range (len(transicoes)):
        print(transicoes[i])


    salvaMealyArq(nomearqsai,lstestadosMealy,estadoInicial,alfabetoEntrada,estadosfinaisMealy,alfabetoSaida,transicoesMealy)
    print("Arquivo salvo.")

def montaMealy(transicoes,lstNos):

    transicoesMealy     = []
    no_mealy            = [None,None,None,None]

    e_inicial           = "" # Estado inicial da Transicao
    e_final             = "" # Estado final da Transicao
    s_entrada           = "" # Simbolo inicial da Transicao
    s_saida             = "" # Simbolo final da Transicao
    estadoAux           = ""

    for i in range(len(transicoes)):
        
        
        s_entrada = transicoes[i][1]


        for j in range (len(lstNos)):
            

            
            if lstNos[j][0] == transicoes[i][2]:
                
                s_saida = lstNos[j][1]

             
        # Se i estado inicial foi um estado "qx'"
        if len(transicoes[i][0]) == 3:
            
            estadoAux += transicoes[i][0][0]
            estadoAux += transicoes[i][0][1] 
            
            e_inicial = estadoAux
            estadoAux = ""
        
        else:

            e_inicial = transicoes[i][0]


        if len(transicoes[i][2]) == 3:

            estadoAux += transicoes[i][2][0]
            estadoAux += transicoes[i][2][1] 
            
            e_final = estadoAux
            estadoAux = ""
        else:

            e_final = transicoes[i][2]

        no_mealy[0] = e_inicial
        no_mealy[1] = s_entrada
        no_mealy[2] = e_final
        no_mealy[3] = s_saida

        flag = False
        
        for x in range(len(transicoesMealy)):
            
            if transicoesMealy[x] == no_mealy:
                flag = True

        if flag == False:
            transicoesMealy.append(no_mealy)

        no_mealy = [None,None,None,None]

        e_inicial           = "" # Estado inicial da Transicao
        e_final             = "" # Estado final da Transicao
        s_entrada           = "" # Simbolo inicial da Transicao
        s_saida             = "" # Simbolo final da Transicao

    return transicoesMealy

def montaEstadosMealy(lstestadoMoore):
    
    lstestadosmealy = []
    
    for i in range(len(lstestadoMoore)):
        
        if len(lstestadoMoore[i]) == 2:
            lstestadosmealy.append(lstestadoMoore[i])

    return lstestadosmealy


def montaEstadosfinaisMealy(estadosFinais):
    
    estadosfinaismealy = []

    for i in range(len(estadosFinais)):
        
        if len(estadosFinais[i]) <= 2:
            estadosfinaismealy.append(estadosFinais[i])

    return estadosfinaismealy


def salvaMealyArq(nomearqsaida,lstestadosMealy,estadoInicial,alfabetoEntrada,estadosfinaisMealy,alfabetoSaida,transicoesMealy):
    
    arq = open(nomearqsaida, 'w')
    arq.write("mealy\n")

    # =============== ESTADO =============== #
    for i in range (len(lstestadosMealy)):
        
        arq.write(lstestadosMealy[i])

        if i+1 < len(lstestadosMealy):
            arq.write(" ")
    
    arq.write("\n")
    # ====================================== #

    
    # ========= Alfabeto de Entrada ======== #
    for i in range (len(alfabetoEntrada)):
        
        arq.write(alfabetoEntrada[i])

        if i+1 < len(alfabetoEntrada):
            arq.write(" ")
    
    arq.write("\n")
    # ====================================== #

    
    # ============ Estado Incial =========== #
    
    arq.write(estadoInicial)
    arq.write("\n")

    # ====================================== #


    # ============ Estado Finais  =========== #
    for i in range (len(estadosfinaisMealy)):
        arq.write(estadosfinaisMealy[i])

        if i+1 < len(estadosfinaisMealy):
            arq.write(" ")

    arq.write("\n")
    # ====================================== #

    # ============ Alfabeto de saida ======== #
    for i in range (len(alfabetoSaida)):
        arq.write(alfabetoSaida[i])

        if i+1 < len(alfabetoSaida):
            arq.write(" ")

    arq.write("\n")
    # ====================================== #

    # ============ Transicoes =========== #
    for i in range (len(transicoesMealy)):
        
        for j in range (len(transicoesMealy[i])):

            arq.write(transicoesMealy[i][j])


            if j+1 < len(transicoesMealy[i]):
                arq.write(" ")

        if i + 1 < len(transicoesMealy):
            arq.write("\n")

    # ====================================== #

def main(argv):

    
    nomearqentrada  = argv[1]
    nomearqsaida    = argv[2]

    arqentrada = open(nomearqentrada,"r")
    
    linha = arqentrada.readline()
    linha = linha.strip()
    
    if(linha == "mealy"):

        converteMealyparaMoore(arqentrada,nomearqsaida)

    elif(linha == "moore"):
        
        converteMooreparaMealy(arqentrada,nomearqsaida)

    return 0

if __name__ == '__main__':
    main(sys.argv)