# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 18:33:48 2023

@author: Evandro Rhari
"""

from collections import OrderedDict

glossary = OrderedDict()
glossary['pep8']  = 'Guia de estilo de código para facilitar sua leitura'

glossary['metodo'] = 'Um método é uma sub-rotina que é executada por um '
glossary['metodo'] +='objeto ao receber uma mensagem. Os métodos determinam o '
glossary['metodo'] +='comportamento dos objetos de uma classe e são análogos a '
glossary['metodo'] +='funções ou procedimentos da programação estruturada. O '
glossary['metodo'] +='envio de  mensagens (chamada de métodos) pode alterar o '
glossary['metodo'] += 'estado de um objeto'

glossary['dicionario'] = 'Coleções que guardam valores multidimensionais '
glossary['dicionario'] +='para cada indice'
            
glossary['tupla'] = 'Sequência imutável, porém sobreescrevivel, de dados de '
glossary['tupla'] +='qualquer tipo.'
            
glossary['zen de python'] = 'Ccoleção de 19 princípios orientadores escrito'
glossary['zen de python'] +='por Tim Peters, na forma de poema, com uma série '
glossary['zen de python'] +='de aforismos, para escrever programas de '
glossary['zen de python'] +='computador que influenciam o design da linguagem '
glossary['zen de python'] +='de programação Python.'


for key, value in glossary.items():
    print(key.title())
    print(f'{value}\n')