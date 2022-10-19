from ctypes import sizeof
from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
from tqdm import tqdm
from numba import jit, cuda
import pandas as pd

'''The data has been divided into 4 sub-dataset due to computational'''

X,Y = np.loadtxt('C:/path/to/first/subset/0.txt', 
                dtype= int,skiprows=(4), unpack= True, delimiter='\t')    
                
Z,S = np.loadtxt('C:/path/to/second/subset/1.txt', 
                dtype= int, unpack= True, delimiter='\t')  
             
A,B = np.loadtxt('C:/path/to/third/subset/2.txt', 
                dtype= int, unpack= True, delimiter='\t')    
                
C,D = np.loadtxt('C:/path/to/fourth/subset/3.txt', 
                dtype= int, unpack= True, delimiter='\t')  


#use cuda for better performance when possible
@jit(target_backend='cuda')	
def numberOfInstances(v, X):
    i=0
    for z in X:
        if(v==z): i= i+1
        
    return i

@jit(target_backend='cuda')	
def arrayNoDup(X):
    result = []
    
    print("Creazione array senza doppioni")

    for v in tqdm(X):
        if v not in result:
            result.append(v)
    
    print("Array senza doppioni creato")

    return result


def visualize(X,Y):
    plt.plot(X,Y)

    plt.title('Prova Visual')
    plt.ylabel('Y Riceventi')
    plt.xlabel('X Mandanti')

    plt.show()

def createHistogram(X):
    #X_No_Dup= arrayNoDup(X) 
   
    '''for v in X_No_Dup:
        X_num.append(numberOfInstances(v,X))
        i=i+1'''

    plt.hist(X, density=False, bins = 400)  # density=False would make counts    

    plt.ylabel('Degree')
    plt.xlabel('Node')
    plt.show()
   


def saveArrayNoDup(X,name):
    X_num = []
    X_No_Dup= arrayNoDup(X) 
    i = 0
    for v in X_No_Dup:
        X_num.append(numberOfInstances(v,X))
        i=i+1

    i = 0
    
    with open(name+'RoadNoDupCount.txt', 'w') as f:
        for y in X_No_Dup:
            line = [str(X_No_Dup[i]),str(X_num[i])]
            tab = '\t' 
            lines = tab.join(line)
            f.write(lines + '\n')
            i = i+1
    f.close


''' 
visualize(X_No_Dup,X_num)   
print(X[0],Y[0])            
'''
#createHistogram(X)

'''caricare un .txt direttamente in un dizionario con chiave il nodo e valore il numIstanze ''' 
def createDict(d,txt,i):

    print("Creazione dizionario "+i)

    with open(txt) as f:
       for line in f:
        (key, val) = line.split()
        d[int(key)] = val
        
    print("Dizionario "+i+" creato \n")
    
    return d

#@jit(target_backend='cuda',nopython=True)	
def mergeDict(dx,dy,n,m):
    
    Degree = []
    Nodes = []

    print("Merging dizionari "+n+" e "+m+" \n")
    for j in tqdm(dx.keys()):
    #for j in dx.keys():    
        if j in dy.keys(): 
            Nodes.append(j) 
            val = int(dx[int(j)])
            val2 = int(dy[int(j)])
            
            Degree.append(val+val2)
            
        else:
            Nodes.append(j)
            Degree.append(int(dx[int(j)]))

        

    for k in tqdm(dy.keys()):
        if k not in Nodes:
            Nodes.append(k)
            Degree.append(int(dy[int(k)]))    
           

    print("Merging dizionari completo \n Salvataggio...")
    return Nodes,Degree



def mergeAndSave():
    
    Degree = []
    Nodes = []
    Degree1 = []
    Nodes1 = []
    Degree2 = []
    Nodes2 = []
    
    saveArrayNoDup(A,'0')
    saveArrayNoDup(C,'1')
    saveArrayNoDup(A,'2')
    saveArrayNoDup(C,'3')

    d0 = {}

    d0 = createDict(d0,"C:/path/to/0RoadNoDupCount.txt",'0')
    
    d1 = {}

    d1 = createDict(d1,"C:/path/to/1RoadNoDupCount.txt",'1')

    d2 = {}
        
    d2 = createDict(d2,"C:/path/to/2RoadNoDupCount.txt",'2')

    d3 = {}

    d3 = createDict(d3,"C:/path/to/3RoadNoDupCount.txt",'3')
    
    
    Nodes,Degree = mergeDict(d0,d1,'0','1')		#merge first two subset and save the result
    
    i = 0
    with open('1provaRoadNoDupCount.txt', 'w') as f:
        for y in tqdm(Nodes):
            line = [str(Nodes[i]),str(Degree[i])]
            tab = '\t' 
            lines = tab.join(line)
            f.write(lines + '\n')
            i = i+1
    print("Salvataggio dizionario completo")

    
    Nodes1,Degree1 = mergeDict(d2,d3,'2','3') 	#merge last two subset and save the result

    i = 0
    with open('2HalfRoadNoDupCount.txt', 'w') as f:
        for y in tqdm(Nodes1):
            line = [str(Nodes1[i]),str(Degree1[i])]
            tab = '\t' 
            lines = tab.join(line)
            f.write(lines + '\n')
            i = i+1
    print("Salvataggio dizionario completo")

    

    dh1 = {}

    dh1 = createDict(dh1,"C:/Users/danil/Downloads/magistrale/Social Network Analysis/Project/1HalfRoadNoDupCount.txt",'H-1')

    dh2 = {}
    
    dh2 = createDict(dh2,"C:/Users/danil/Downloads/magistrale/Social Network Analysis/Project/2HalfRoadNoDupCount.txt",'H-2')

    Nodes2,Degree2 = mergeDict(dh1,dh2,'H-1','H-2')	#merge intermediate subset and save the result

    i = 0
    with open('FullRoadNoDupCount.txt', 'w') as f:
        for y in tqdm(Nodes2):
            line = [str(Nodes2[i]),str(Degree2[i])]
            tab = '\t' 
            lines = tab.join(line)
            f.write(lines + '\n')
            i = i+1
    print("Salvataggio dizionario totale completo")
    
    
mergeAndSave()    