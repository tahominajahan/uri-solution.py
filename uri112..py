area=input().split(" ")
A,B,C=area
A=float(A)
B=float(B)
C=float(C)
TRIANGULO=((1/2)*A*C)
CIRCULO=(3.14159*C**2)
T=(A+B)/2*C
Q=B**2
R=A*B
print("TRIANGULO: %.3f"%TRIANGULO)
print("CIRCULO: %.3f"%CIRCULO)
print("TRAPEZIO: %.3f"%T)
print("QUADRADO: %.3f"%Q)
print("RETANGULO: %.3f"%R)