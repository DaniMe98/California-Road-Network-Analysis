# California-Road-Network-Analysis
A What-if Analysis conducted on the **California Road Network** for the Social Network Analysis project work

The aim of this project is to investigate the response of a real network to **link/node removal (LNR)**:

	1. assess network robustness, a measure that indicates the capacity of the system to maintain its functions after LNR, and 
	2. identify the LNRs that trigger the greatest amount of damage in the systems, thus revealing the links/nodes that act as key players in network functioning. 

## Dataset

I am considering the data coming from “California road network”, which consists of a directed graph, with labelled nodes and edges that connect them, saved in a .txt file in a structure like: ”FromNodeId    ToNodeId”. 

The dataset is available at http://snap.stanford.edu/data/roadNet-CA.html  

In ***Figure 1*** you can see an image from [1] where they juxtaposed the network created with these data and the map with the main roads of California.
<p align="center">
<img src="https://github.com/DaniMe98/California-Road-Network-Analysis/blob/main/22-scaled.webp" width="65%" height="65%" text-align="center" />
</p>
## Strategy

The **“removal strategy”** chosen for this experiment is based on the betweenness centrality, the goal is to disrupt and stress the network as much as possible, so, I came up with 2 different removal strategies: 

***1. First strategy:***

	a. Sort the nodes according to BC in descending order, 
	b. Remove the node with top BC, 
	c. Return to Point A and re-calculate BC for each point. 
***2. Second strategy:*** 

	a. Sort the nodes according to BC in descending order, 
	b. Write down the top n nodes with higher BC, 
	c. Remove them one by one. 
In each strategy with the same number of BC, the node with the ***highest degree*** is chosen. 

## Tests
To evaluate the network changes, we use an **efficiency measure** that is based on the shortest paths (also called geodesic path) between two nodes, i.e., the minimum number of links used to travel from one node to another. 

The network efficiency is defined as [2]: 

$$ 	Eff = \bigg(~ {1 \over N \cdot (N-1)} \cdot {\sum_{i \neq j \in G} {1 \over d(i,j)}}  ~ \bigg) $$

where **N** is the total number of nodes of network G, and **d(i,j)** is the shortest path between nodes i and j. 
Eff decreases with an increase in the nodes' shortest paths, thus defining as a more efficient networks the one with closer nodes.
## References 
[1] California road network, Elena Korshakova 
https://studentwork.prattsi.org/infovis/labs/california-road-network/ 

[2] Latora V, Marchiori M. Efficient behavior of small-world networks. Phys Rev Lett. 
(2001) 87:198701. doi: 10.1103/PhysRevLett.87.198701 
