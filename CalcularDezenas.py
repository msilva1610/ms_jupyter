import logging
class CalcularDezenas:
    '''classe base dos calculos das dezenas'''
    def __init__(self):
        self.impares = 0
        self.pares = 0
        self.SomaDezenas = 0
        self.obj = []

    def CalcMultiplosParaDezenas(self, m, dezenas):
        ''' Função interna'''
        TotalMultiplos = 0
        for d in dezenas:
            if d >= m:
                if d % m == 0:
                    TotalMultiplos += 1

        return TotalMultiplos


    def CalculaParImparSomaDez(self, dezenas):
        """[Calcula quantidade de dezenas par, impar e soma as dezenas.
        Retorna um obj dict ]

        Args:
            dezenas ([list]): [lista com as dezenas combinadas]

        Returns:
            [dict]: [description]
        """
        impares, pares, SomaDezenas = 0,0,0
        somadasdezenasOk = False
        try:
            for d in dezenas:
                if d % 2 != 0:
                    impares += 1
                else:
                    pares += 1
                SomaDezenas += d
            if impares not in (0,6):
                imparesok = True
            else:
                imparesok = False

            if pares not in (0,6):
                paresok = True
            else:
                paresok = False

            if (SomaDezenas >= 102 and SomaDezenas <= 268):
                somadasdezenasOk = True

            obj = {
                'impares': impares,
                'imparesok': imparesok,
                'pares': pares,
                'paresok': paresok,
                'SomaDezenas': SomaDezenas,
                'somadasdezenasOk': somadasdezenasOk
            }    
            return obj
        except Exception as e:
            logging.error(f'Ocorreu um erro: {e}') 
        finally:
            pass


    def RetornaArrDezenas (self, apostas):
        '''
        Recebe um objeto de apostas e retorna um arrray de dezenas
        '''
        dezenas = []
        dezenas.append(apostas['dez01'])
        dezenas.append(apostas['dez02'])
        dezenas.append(apostas['dez03'])
        dezenas.append(apostas['dez04'])
        dezenas.append(apostas['dez05'])
        dezenas.append(apostas['dez06'])
        return dezenas


    def CalculaPA(self, dezenas):
        '''
        Calcula progressão aritmética das dezenaas
        '''
        r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18,r19,r20 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 
        ParDePAs = 0
        delta1 = dezenas[1] - dezenas[0]
        for index in range(len(dezenas) - 1):
            if (dezenas[index + 1] - dezenas[index]) == delta1:
                ParDePAs += 1
            elif delta1 == 3:
                r3 = ParDePAs
                delta1 = 0
            elif delta1 == 4:
                r4 = ParDePAs
                delta1 = 0
            elif delta1 == 5:
                r5 = ParDePAs
                delta1 = 0
            elif delta1 == 6:
                r6 = ParDePAs
                delta1 = 0                        
            elif delta1 == 7:
                r7 = ParDePAs
                delta1 = 0                        
            elif delta1 == 8:
                r8 = ParDePAs
                delta1 = 0
            elif delta1 == 9:
                r9 = ParDePAs
                delta1 = 0
            elif delta1 == 10:
                r10 = ParDePAs
                delta1 = 0
            elif delta1 == 11:
                r11 = ParDePAs
                delta1 = 0
            elif delta1 == 12:
                r12 = ParDePAs
                delta1 = 0
            elif delta1 == 13:
                r13 = ParDePAs
                delta1 = 0
            elif delta1 == 14:
                r14 = ParDePAs
                delta1 = 0
            elif delta1 == 15:
                r15 = ParDePAs
                delta1 = 0
            elif delta1 == 16:
                r16 = ParDePAs
                delta1 = 0
            elif delta1 == 17:
                r17 = ParDePAs
                delta1 = 0
            elif delta1 == 18:
                r18 = ParDePAs
                delta1 = 0
            elif delta1 == 19:
                r19 = ParDePAs
                delta1 = 0
            elif delta1 == 20:
                r20 = ParDePAs
                delta1 = 0
        if (r3 in (2,3) or r4 in (1,2) or r5 in (1,2) or r6 in (1,2) or \
        r7 in (1,2) or r8 in (1,2) or r9 in (1,2) or r10 in (0,1,2) or \
        r11 in (0,1,2) or r12 in (0,1,2) or r13 in (0,1) or r14 in (0,1) or r15 in (0,1) or \
        r16 in (0,1) or r17 in (0,1) or r18 in (0,1) or r19 in (0,1) or r20 in (0,1)):
            razao = True            
        # return r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18,r19,r20
        return razao


    def SomaDigitosDezenas(self, dezenas):
        try:
            soma_dos_digitos_das_dezenas = 0
            somaok = False
            for d in dezenas:
                strdezena = str(d)
                for s in strdezena:
                    soma_dos_digitos_das_dezenas += int(s)

            if soma_dos_digitos_das_dezenas >= 27 and soma_dos_digitos_das_dezenas <= 58:
                somaok = True

            return  soma_dos_digitos_das_dezenas, somaok

        except:
            logging.error('error ocorreu em soma digitos dezenas...') 
        finally:
            del soma_dos_digitos_das_dezenas


    def CalculaDezenasEspelho(self, dezenas):
        '''
        Calcula dezenas espelho da aposta
        '''
        dez2d = []
        TotalParesDezenasEspelho = 0
        TotalParesDezenasEspelhoOk = False
        list(dezenas).sort()
        for d in (dezenas):
            temp = "{:02d}".format(d)
            dez2d.append(temp)
        for dig in dez2d:
            digespelho = dig[1]+dig[0]
            if digespelho in dez2d:
                TotalParesDezenasEspelho += 1

        if TotalParesDezenasEspelho <= 1:
            TotalParesDezenasEspelhoOk = True

        return (TotalParesDezenasEspelho/2, TotalParesDezenasEspelhoOk)


    def CalculaPresencaDigitos(self, dezenas):
        toatldigitosok = False
        digitos = []
        TotalDigitos = 0
        list(dezenas).sort()
        for d in dezenas:
            for digito in str(d):
                digitos.append(digito)
        TotalDigitos = list(dict.fromkeys(digitos))

        if len(TotalDigitos) in (5,6,7,8):
            toatldigitosok = True 

        return (len(TotalDigitos), toatldigitosok)


    def CalculaIntervaloDezena(self, dezenas):
        IntervalorDezenaOk = True
        dz = 0
        list(dezenas).sort()
        for d in dezenas:
            dz += 1
            if (d not in range(1,26) and dz == 1):
                IntervalorDezenaOk = False
            elif (d not in range(2,37) and dz == 2):
                IntervalorDezenaOk = False
            elif (d not in range(5,47) and dz == 3):
                IntervalorDezenaOk = False
            elif (d not in range(13,54) and dz == 4):
                IntervalorDezenaOk = False
            elif (d not in range(23,59) and dz == 5):
                IntervalorDezenaOk = False
            elif (d not in range(35,60) and dz == 6):
                IntervalorDezenaOk = False
        return IntervalorDezenaOk


    def CalculaConsecutivos(self, dezenas):
        numAnterior = 1
        totConsecutivos = 0
        totConsecutivosOk = False
        list(dezenas).sort()
        for d in dezenas:
            if (d - numAnterior) == 1:
                totConsecutivos += 1
            numAnterior = d

        if totConsecutivos in (0,1,2):
            totConsecutivosOk = True                
        
        return totConsecutivos, totConsecutivosOk


    def calculaColunas(self, dezenas):
        TotalColunas = 0
        TotalColunasOk = False
        for d in dezenas:
            if d in [1,11,21,31,41,51]:
                TotalColunas += 1
            elif d in [2,12,22,32,42,52]:
                TotalColunas += 1
            elif d in [3,13,23,33,43,53]:
                TotalColunas += 1
            elif d in [4,14,24,34,44,54]:
                TotalColunas += 1
            elif d in [5,15,25,35,45,55]:
                TotalColunas += 1
            elif d in [6,16,26,36,46,56]:
                TotalColunas += 1
            elif d in [7,17,27,37,47,57]:
                TotalColunas += 1
            elif d in [8,18,28,38,48,58]:
                TotalColunas += 1
            elif d in [9,19,29,39,49,59]:
                TotalColunas += 1
            elif d in [10,20,30,40,50,60]:
                TotalColunas += 1

    
        if TotalColunas in (4,5,6):
            TotalColunasOk = True

        return TotalColunas, TotalColunasOk


    def CalculaLinhas(self, dezenas):
        TotalLinhas = 0
        TotalLinhasOk = False
        for d in dezenas:
            if d in range(1,10):
                TotalLinhas += 1
            elif d in (range(11,20)):
                TotalLinhas += 1
            elif d in (range(21,30)):
                TotalLinhas += 1
            elif d in (range(31,40)):
                TotalLinhas += 1
            elif d in (range(41,50)):
                TotalLinhas += 1
            elif d in (range(51, 60)):
                TotalLinhas += 1

        if TotalLinhas in (4,5,6):
            TotalLinhasOk = True        
        return TotalLinhas, TotalLinhasOk


    def CalculaQuadraticos(self, dezenas):
        Numquadraticos = [1,4,9,16,25,36,49]
        TotNumquadraticos = 0
        TotNumquadraticosOk = False
        for d in dezenas:
            if d in Numquadraticos:
                TotNumquadraticos += 1

        if TotNumquadraticos not in (3,4,5,6):
            TotNumquadraticosOk = True        
        return TotNumquadraticos, TotNumquadraticosOk


    def CalculaMultiplos(self, dezenas):
        m = False
        m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16,m17,m18,m19,m20,m21,m22,m23,m24,m25,m26,m27,m28,m29,m30 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
        for m in (range(2,31)):
            if m == 3:
                m3 = self.CalcMultiplosParaDezenas(m,dezenas)
            elif m == 4:
                m4 = self.CalcMultiplosParaDezenas(m,dezenas)
            elif m == 5:
                m5 = self.CalcMultiplosParaDezenas(m,dezenas)
            elif m == 6:
                m6 = self.CalcMultiplosParaDezenas(m,dezenas)
            elif m == 7:
                m7 = self.CalcMultiplosParaDezenas(m,dezenas)
            elif m == 8:
                m8 = self.CalcMultiplosParaDezenas(m,dezenas)
            elif m == 9:
                m9 = self.CalcMultiplosParaDezenas(m,dezenas)
            elif m == 10:
                m10 = self.CalcMultiplosParaDezenas(m,dezenas)
            elif m == 11:
                m11 = self.CalcMultiplosParaDezenas(m,dezenas)
            elif m == 12:
                m12 = self.CalcMultiplosParaDezenas(m,dezenas)
            elif m == 13:
                m13 = self.CalcMultiplosParaDezenas(m,dezenas)
            elif m == 14:
                m14 = self.CalcMultiplosParaDezenas(m,dezenas)
            elif m == 15:
                m15 = self.CalcMultiplosParaDezenas(m,dezenas)
            elif m == 16:
                m16 = self.CalcMultiplosParaDezenas(m,dezenas)
            elif m == 17:
                m17 = self.CalcMultiplosParaDezenas(m,dezenas)
            elif m == 18:
                m18 = self.CalcMultiplosParaDezenas(m,dezenas)
            elif m == 19:
                m19 = self.CalcMultiplosParaDezenas(m,dezenas)
            elif m == 20:
                m20 = self.CalcMultiplosParaDezenas(m,dezenas)
            elif m == 21:
                m21 = self.CalcMultiplosParaDezenas(m,dezenas)
            elif m == 22:
                m22 = self.CalcMultiplosParaDezenas(m,dezenas)
            elif m == 23:
                m23 = self.CalcMultiplosParaDezenas(m,dezenas)
            elif m == 24:
                m24 = self.CalcMultiplosParaDezenas(m,dezenas)
            elif m == 25:
                m25 = self.CalcMultiplosParaDezenas(m,dezenas)
            elif m == 26:
                m26 = self.CalcMultiplosParaDezenas(m,dezenas)
            elif m == 27:
                m27 = self.CalcMultiplosParaDezenas(m,dezenas)
            elif m == 28:
                m28 = self.CalcMultiplosParaDezenas(m,dezenas)
            elif m == 29:
                m29 = self.CalcMultiplosParaDezenas(m,dezenas)
            elif m == 30:
                m30 = self.CalcMultiplosParaDezenas(m,dezenas)

        if (m3 in (1,2,3) or (m4 in (0,1,2,3)) or (m5 in (0,1,2)) or (m6 in (0,1,2)) \
        or  (m7 in (0,1,2)) or (m8 in (0,1,2)) or (m9 in (0,1)) or (m10 in (0,1,2)) \
        or  (m11 in (0,1)) or (m12 in (0,1,2)) or (m13 in (0,1,2)) or (m14 in (0,1,2)) \
        or  (m15 in (0,1)) or (m16 in (0,1)) or (m17 in (0,1)) or (m18 in (0,1)) \
        or  (m19 in (0,1)) or (m20 in (0,1)) or (m21 in (0,1)) or (m22 in (0,1)) \
        or  (m22 in (0,1)) or (m23 in (0,1)) or (m24 in (0,1)) or (m25 in (0,1)) \
        or  (m26 in (0,1)) or (m27 in (0,1)) or (m28 in (0,1)) or (m29 in (0,1)) \
        or  (m30 in (0,1))):
            m = True        
        # return m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16,m17,m18,m19,m20,m21,m22,m23,m24,m25,m26,m27,m28,m29,m30
        return m


    def ContaPrimos(self, dezenas):
        try:
            NumerosPrimos = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
            totPrimos = 0
            totPrimosOk = False
            for d in dezenas:
                if d in NumerosPrimos:
                    totPrimos += 1
            if totPrimos not in (4,5,6):
                totPrimosOk = True        
            return totPrimos, totPrimosOk
        except:
            logging.error('error ocorreu em conta primos...')
        finally:
            del NumerosPrimos
            del totPrimosOk


    def ValidaDezenaNoQuadrante(self, dezenas):
        try:
            quadranteOK = False
            qtde_q1, qtde_q2,qtde_q3, qtde_q4 = 0, 0, 0, 0
            quadrante = {}
            quadrante['quadrantes'] = []
            q = 0
            q1 = {1,2,3,4,5,11,12,13,14,15,21,22,23,24,25}
            q2 = {6,7,8,9,10,16,17,18,19,20,26,27,28,29,30}
            q3 = {31,32,33,34,35,41,42,43,44,45,51,52,53,54,55}
            q4 = {36,37,38,39,40,46,47,48,49,50,56,57,58,59,60}
            for d in dezenas:
                if d in q1:
                    qtde_q1 += 1
                elif d in q2:
                    qtde_q2 += 1
                elif d in q3:
                    qtde_q3 += 1
                else:
                    qtde_q4 += 1

                if qtde_q1 in (1,2,3):
                    q += 1
                if qtde_q2 in (1,2,3):
                    q += 1
                if qtde_q3 in (1,2,3):
                    q += 1 
                if qtde_q4 in (1,2,3):
                    q += 1
                # aceito um qudrante sem dezena(s)
                if q >= 3:
                    quadranteOK = True
            return qtde_q1, qtde_q2, qtde_q3, qtde_q4, quadranteOK
        except Exception as e:
            logging.error(f'error ocorreu em validaquadrante...{e}')
        finally:
            del quadrante
            del q1
            del q2
            del q3
            del q4


    def ValidaFibonacci(self, dezenas):
        try:
            totFiboOk = False
            totFibo = 0
            Fibonacci = [1, 2, 3, 5, 8, 13, 21, 34, 55]
            for d in dezenas:
                if d in Fibonacci:
                    totFibo += 1
            if  totFibo not in (3,4,5,6):
                totFiboOk = True            
            return totFibo, totFiboOk
        except:
            logging.error('error ocorreu em fibonacci...')
        finally:
            del totFibo
            del Fibonacci


    def DezenasQueMaisSaem(self, dezenas):
        """ Não estou usando no momento"""
        DezenasMais = [5,10,53,23,4,54]
        TotalDezenas = list(set(dezenas) & set(DezenasMais))  # Encontra os iguais
        return len(TotalDezenas)