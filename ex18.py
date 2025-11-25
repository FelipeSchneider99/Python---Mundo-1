from math import radians, sin, cos, tan
ang = float(input('Digite angulo: '))
angrad = radians(ang)
print('Seno é: {:.2f}'
      '\nCosseno é: {:.2f}'
      '\nTangente é: {:.2f}'.format(sin(angrad), cos(angrad), tan(angrad)))