from turtle import title
from pyvis.network import Network
from provaVisual import arrayNoDup,numberOfInstances
import numpy as np
from tqdm import tqdm


from IPython.core.display import display, HTML
CaliforniaRoadNetwork = Network()  #instantiate the network

#load nodes and degree
Nodes,Degree = np.loadtxt('C:/path/to/RoadNoDupCount.txt', 
                dtype= int, unpack= True, delimiter='\t')      

vet=[]
deg=[]

#Next, add nodes to the network, The ID parameter must be unique
#Instead of single nodes at a time, we can add list of nodes.

for node in Nodes.tolist():
    print(node)
    vet.append(str(node))
    #deg.append()
    
print(vet)

CaliforniaRoadNetwork.add_nodes(Nodes, label=vet, size=Degree.tolist())
CaliforniaRoadNetwork.show('CaliforniaRoadNetwork.html')  #save the network.

display(HTML("CaliforniaRoadNetwork.html"))

'''
ToDo: connect these nodes using edges. 


'''