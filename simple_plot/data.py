import numpy as np

def func(x, a = 1., mu = .1, f = 10.):
  return a * np.exp(-x * mu) * np.sin(2. * np.pi * f * x)

x = np.linspace(0., 10., 100)
y1 = func(x)
y2 = func(x*2.)/2.

data = np.array([x, y1, y2]).transpose()
np.savetxt("data.csv", data)
