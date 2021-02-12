from matplotlib import collections  as mc
import pylab as pl

def afficher( liste ) :
  mu , h , lines = sum(liste) / len(liste) , 0 , []
  for élément in  liste :
    lines.append( [ ( mu , h )  ,  ( élément , h ) ])
    h += 1
  muLine = mc.LineCollection([ [ ( mu , 0 )  , ( mu , len( liste )-1 )  ] ] , color = "red",  linewidths=2)
  lc = mc.LineCollection(lines, color = "green",  linewidths=1)
  fig, ax = pl.subplots()
  ax.add_collection(lc)
  ax.add_collection(muLine)
  #ax.autoscale()
  pl.xlim([25, 50])
  ax.margins(0.1)
