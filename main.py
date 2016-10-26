from math import *;

# Args: letras - tuple of 25 characters
# Return: 1 tuple with 5 character tuples
#TODO: Refactor(horrible code)
def gera_chave1(letras):
    result=();
    aux=();
    count=0;
    for character in letras:
        count+=1;
        aux+=(character,);
        if(count>=5):
            count=0;
            result+=(aux,);
            aux=();
    return result;
# Args: cat - character to search , chave - tuple
# Return: encryption of cat
def obtem_codigo1(cat,chave):
    for i in range(len(chave)):
        for j in range(len(chave[i])):
            if(chave[i][j]==cat):
                return str(i)+str(j);
# Args: cadeia - string to encrypt, chave - tuple of encryption
# Return: encryption of cadeia
def codifica1(cadeia,chave):
    result="";
    for i in cadeia:
        result+=obtem_codigo1(i,chave);
    return result;


# Args: cod - 2 digits for decryption, chave - decryption key
# Return: character decrypted
def obtem_car1(cod,chave):
    return chave[int(list(cod)[0])][int(list(cod)[1])];

# Args: cad_codificada - string to decode, chave - decryption key
# Return: string cad_codificada decrypted
def descodifica1(cad_codificada,chave):
    result="";
    for i in range(0,len(list(cad_codificada)),2):
        result+=obtem_car1(list(cad_codificada)[i]+list(cad_codificada)[i+1],chave);
    return result;

# Args: letras - tuple
# Return: decryption of letras
def gera_chave2(letras):
    result=();
    aux=();
    count=0;
    maxSize=calculateSize(len(letras));
    for character in letras:
        count+=1;
        aux+=(character,);
        if(count>=maxSize):
            count=0;
            result+=(aux,);
            aux=();
    if(len(aux)>0):
	       result+=(aux,);
    return result;
# Args: cat - character to search , chave - tuple
# Return: encryption of cat
def obtem_codigo2(cat,chave):
    for i in range(len(chave)):
        for j in range(len(chave[i])):
            if(chave[i][j]==cat):
                return str(i)+str(j);
    return 'XX';
# Args: cadeia - string to encrypt, chave - tuple of encryption
# Return: encryption of cadeia
def codifica2(cadeia,chave):
    result="";
    for i in cadeia:
        result+=obtem_codigo2(i,chave);
    return result;
# Args: cod - 2 digits for decryption, chave - decryption key
# Return: character decrypted
def obtem_car2(cod,chave):
    return chave[int(list(cod)[0])][int(list(cod)[1])] if cod!="XX" else '?';
# Args: cad_codificada - string to decode, chave - decryption key
# Return: string cad_codificada decrypted
def descodifica2(cad_codificada,chave):
    result="";
    for i in range(0,len(list(cad_codificada)),2):
        result+=obtem_car2(list(cad_codificada)[i]+list(cad_codificada)[i+1],chave);
    return result;
#Auxiliary functions

def calculateSize(length):
    root=sqrt(length);
    return floor(root) if( root-floor(root)<0.5) else ceil(root);
