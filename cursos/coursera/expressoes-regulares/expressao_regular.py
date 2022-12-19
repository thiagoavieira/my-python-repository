# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto
import re

# findall search sub
# compile
# sub change occurencies

string = 'Este é um teste de expressões regulares. - teste'
print(re.search(r'teste', string)) # achará a 1ª ocorrência
print(re.findall(r'teste', string)) # retorna todas as ocorrências
print(re.sub(r'teste', 'ABCD', string)) # troca as ocorrencias de teste pra ABCD

regex = re.compile(r'teste') # compila a expressão e reutiliza ela
print(regex.search(string))
print(regex.findall(string))
print(regex.sub('EFGH', string))