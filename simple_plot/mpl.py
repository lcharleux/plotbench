import numpy as np
import matplotlib.pyplot as plt


#-------------------------------------------------------------------------------
# FIGURE SIZING
# https://www.elsevier.com/authors/author-schemas/artwork-and-media-instructions/artwork-sizing
#fig_width = 190. * 0.0393701 # Double column 190mm
#fig_width = 140. * 0.0393701 # One and half column 190mm
fig_width = 90.  * 0.0393701 # Single column 90mm
fig_heigth = fig_width /1.4    # Feel free to modify fig heigth
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# LATEX CONFIGURATION
import matplotlib
params = {'text.usetex'      : True,
          'axes.labelsize'   : 12,
          'axes.linewidth'   : 1.5,
          'lines.markersize' : 8,
          'font.size'        : 11,
          'font.family'      : 'serif',         # Options: serif, sans-serif, cursive, monospace
          'font.serif'       : 'Computer Modern Roman',         # Options: Times, Palatino, New Century Schoolbook, Bookman, Computer Modern Roman
          'font.sans-serif'  : 'Helvetica',     # Options: Hevetica, Avant Garde, Computer Modern Sans serif
          'font.cursive'     : 'Zapf Chancery', # Options: Zapf Chancery
          'font.monospace'   : 'Courier',       # Options: Courier, Computer Modern Typewriter
          'legend.fontsize'  : 12,
          'legend.numpoints' : 1,
          'xtick.labelsize'  : 11,
          'ytick.labelsize'  : 11,
         }
matplotlib.rcParams.update(params)
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# FIGURE 
data = np.loadtxt("data.csv").transpose()
x  = data[0]
y1 = data[1]
y2 = data[2]

fig = plt.figure()
fig.set_size_inches(fig_width, fig_heigth)
plt.title("A rather simple plot")
plt.plot(x, y1, label = "Great data")
plt.plot(x, y2, label = "Awesome data")
plt.xlabel("Inputs,  $x$")
plt.ylabel("Outputs, $y$")
plt.grid()
plt.tight_layout()
plt.savefig("mpl.pdf")
plt.savefig("mpl.pgf")
#-------------------------------------------------------------------------------

