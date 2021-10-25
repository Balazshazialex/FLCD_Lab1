import re

from Parser import Parser
from SymbolTable import SymbolTable


class Tokenizer:
    def __init__(self, list_of_words):
        self._tokens = {}
        constants_table=SymbolTable()
        vars_table=SymbolTable()
        f = open("token.in", 'r')
        lines = f.readlines()
        f.close()
        for line in lines:
            line = line.split()
            self._tokens[line[0].upper()] = line[1]
        self._PIF = ""
        for elem in list_of_words:
            if elem in self._tokens:
                self._PIF += str(self._tokens[elem]) + '\n'
            else:
                if re.findall('(\".*\"|[0-9]+)',elem):
                    poz=constants_table.add(elem)
                    self._PIF+= "( 1, "+str(poz) +" )"+'\n'
                elif re.findall('([A-Z]+)',elem):
                    poz = vars_table.add(elem)
                    self._PIF += "( 0, " + str(poz) + " )" + '\n'
        f = open("1.txt", 'w')
        f.write(self._PIF)


f = open('p1.txt', 'r')
text = f.read()
p = Parser(text)
words = p.get_splitted()
t=Tokenizer(words)