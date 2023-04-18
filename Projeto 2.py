#MARCELO JUNIO AVELINO MOREIRA
#TURMA 8
#INTRODUÇÃO A PROGRAMAÇÃO

#Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do 
# hotel é supersticioso e optou por não ter um 13ro andar.
#Escreva um código que imprima todos os números exceto o número 13.
#Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando
# os outros dois tipos de laços de repetição aprendidos.
#Como desafio, imprima eles em ordem decrescente (20, 19, 18...)   
print("")
print("Ordem crescente dos andares sem o 13 andar no laço FOR")
print("")
for i in range(20):
    i=i+1
    if (i==13):
     continue
    print(i, end=",") 
    
    
print("")   
print("") 
print("Ordem decrescente dos andares sem o 13 andar FOR")
print("")
    
for i in range(20,0,-1):
    
    if (i==13):
     continue
    print(i,end=",")
    
print("")
print("")

print("")
print("Ordem crescente dos andares sem o 13 andar no laço WHILE")
print("")

j = 0
while (j<20):
     j=j+1
     if (j==13):
        continue
     print(j,end=",")
     
print("")   
print("")
print("Ordem decrescente dos andares sem o 13 andar no laço WHILE")
print("")
  

k = 21
while (k>1):
     k=k-1   
     if (k==13):
        continue
     print(k,end=",")
     
     
print("")  
print("")
