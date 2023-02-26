# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 09:39:14 2023

@author: Evandro Rhari
"""

glossary = {
            'pep8': 'Guia de estilo de código para facilitar sua leitura',
            
            'metodo': 'Um método é uma sub-rotina que é executada por um ' +
            'objeto ao receber uma mensagem. Os métodos determinam o ' +
            'comportamento dos objetos de uma classe e são análogos a ' + 
            'funções ou procedimentos da programação estruturada. O envio de '+
            'mensagens (chamada de métodos) pode alterar o estado de um objeto',
    
            'dicionario': 'Coleções que guardam valores multidimensionais '+
            'para cada indice',
            
            'tupla': 'Sequência imutável, porém sobreescrevivel, de dados de '+
            'qualquer tipo.',
            
            'zen de python': 'Coleção de 19 princípios orientadores escrito'+
            'por Tim Peters, na forma de poema, com uma série de aforismos, '+
            'para escrever programas de computador que influenciam o design '+
            'da linguagem de programação Python.',
    }

for key, value in glossary.items():
    print(key.title())
    print(f'{value}\n')