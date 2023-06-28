'''Exercício Python 18: Faça um programa que leia um ângulo qualquer
e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'''

'''import math
ang = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O ângulo de {} tem o SENO de: {:.2f}'.format(ang, seno))
print('O ângulo de {} tem o COSSENO de: {:.2f}'.format(ang, cos))
print('O ângulo de {} tem a TANGENTE de: {:.2f}'.format(ang, tan))'''

from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('O ângulo de {} tem o SENO de: {:.2f}'.format(ang, seno))
print('O ângulo de {} tem o COSSENO de: {:.2f}'.format(ang, cos))
print('O ângulo de {} tem a TANGENTE de: {:.2f}'.format(ang, tan))