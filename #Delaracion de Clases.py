#Delaracion de Clases
import string
class Operacion:

    def sumar(self,a,b): #la palabra self  debe ponerse en todo #1 método.
        c=a+b;
        return c;

    def restar(self,a,b):
        c=a-b;
        return c;

    def multiplicar(self,a,b):
        c=a*b;
        return c;

    def dividir(self,a,b):
        c=float(a)/float(b);
        return c;

#Programa Principal
print ("Programa que hace operaciones con dos numeros");
op=Operacion
a=10;
b=4;
print ("Suma: "+str(a)+"+"+str(b)+"="+str(op.sumar(a,b)));
# print ("Resta: "+str(a)+"-"+str(b)+"="+str(op.restar(a,b)));
# print ("Multiplicación: "+str(a)+"*"+str(b)+"="+str(op.multiplicar(a,b)));
# print ("División: "+str(a)+"/"+str(b)+"="+str(op.dividir(a,b)));