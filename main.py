# Timothy Gorst 3/12/2021
# drawing stuff
from guizero import App, Drawing

w = 500
h = 500
pan = 250
scale = 3
app = App(width=w, height=h)
drawing = Drawing(app, width=w, height=h)

def transform(coord):
    return coord * scale + pan
# end of drawing stuff

def eisensteinPrimes():
  for a in range(-100,100):
    for b in range(-100,100):
      try:
        if 12**(a**2-a*b+b**2-1)%(a**2-a*b+b**2) == 1:
          point = a + b*((-1+1j*3**(1/2))/2)
          print(a-b-a*b)
          drawing.rectangle(transform(point.real),transform(point.imag),transform(point.real)+2,transform(point.imag)+2,color = 'green')
      except:
        continue

def eisenstein():
  for a in range(-10,10):
    for b in range(-10,10):
      point = a + b*((-1+1j*3**(1/2))/2)
      drawing.rectangle(transform(point.real),transform(point.imag),transform(point.real)+2,transform(point.imag)+2,color = 'black')
  drawing.rectangle(transform(0),transform(0),transform(0)+2,transform(0)+2,color = 'red')
#eisenstein()
eisensteinPrimes()
