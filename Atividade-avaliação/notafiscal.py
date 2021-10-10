"""
    Módulo notafiscal -
    Classe NotaFiscal - 
        Atributos :
            id        - informado.
            codigo    - informado.
            data      - informado.
            cliente   - informado.
            items     - informado
            valornota - calculado. 
"""
import datetime
from cliente        import Cliente
from produto        import Produto
from itemnotafiscal import ItemNotaFiscal


class NotaFiscal():         
    def __init__(self, Id, codigo, cliente):
        self._Id = Id
        self._codigo=codigo
        self._cliente=cliente 
        self._data=datetime.datetime.now()   
        self._itens=[]
        self._valorNota=0.0        
        
    def setCliente(self, cliente):
        if isinstance(cliente, Cliente):
            self._cliente=cliente    
            
    def adicionarItem(self, item): 
        if isinstance(item, ItemNotaFiscal):
            self._itens.append(item)
        
    def calcularNotaFiscal(self):
        valor=0.0
        for item in self._itens:
            valor = valor + item._valorItem
        self.valorNota=valor
     
    def imprimirNotaFiscal(self):
        Linhas = '-' * 111
        print(Linhas)
        print('{:101}{}'.format('NOTA FISCAL',datetime.datetime.now().strftime('%d-%m-%Y')))
        print('Cliente:{:<10}Nome:{}'.format(self._cliente._codigo, self._cliente._nome))
        print('CPF/CNPJ:{}'.format(self._cliente._cnpjcpf))
        print(Linhas)
        print('ITENS')
        print(Linhas)
        print('{:5s}     {:55s} {:>5s}         {:>10s}   {:>15s}'.format('Seq','Descrição','QTD','valor unit','preço'))
        print('{:^5s} {:^55s}      {:^5s}        {:^10s}      {:^15s}'.format('-'*5,'-'*55,'-'*5,'-'*10,'-'*15))
        for i in range (0,len(self._itens)):
            print('{:^5}{:^25}                                     {:^5}        {:^10}         {:^15}'.format(self._itens[i]._sequencial,
                                                             self._itens[i]._produto._descricao,
                                                             self._itens[i]._quantidade,
                                                             self._itens[i]._valorUnitario,
                                                             self._itens[i]._valorItem))
            print(Linhas)
