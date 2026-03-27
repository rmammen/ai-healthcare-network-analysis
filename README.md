# AI Healthcare Network Analysis

This project analyzes the structure of a web-based network of AI-powered healthcare tools and patient support platforms.

## Objective
The goal of this analysis is to identify which healthcare platforms are most central within the digital healthcare ecosystem and understand how they connect to each other.

## Dataset
The dataset is structured as an edge list representing relationships between major healthcare platforms:

- ChatGPT  
- Ada Health  
- Buoy Health  
- WebMD  
- Mayo Clinic  
- MedlinePlus  
- NHS 111  

Connections between platforms are based on shared functionality, such as:
- Symptom checking  
- Patient education  
- Care navigation  

## Methods
The network was built and analyzed using Python. The following tools were used:

- Pandas (data handling)  
- NetworkX (network analysis)  
- Matplotlib (visualization)  

Two centrality measures were used to define importance:
- **Degree Centrality**: number of connections a node has  
- **Betweenness Centrality**: how often a node connects different parts of the network  

## Results
The analysis shows that **Ada Health** and **Mayo Clinic** are the most central nodes in the network. This means they are the most connected platforms and play a key role in linking different parts of the healthcare ecosystem.

Platforms like **MedlinePlus**, **WebMD**, and **Buoy Health** are also well connected, while **ChatGPT** and **NHS 111** appear more specialized in their roles.

## Network Visualization

![Image 3-26-26 at 9 32 PM](https://github.com/user-attachments/assets/37e1758e-e266-4a6b-a8c4-5248c50c5bc6)


## Files Included

- `health_network_edges.csv` – edge list dataset  
- `centrality_results.csv` – calculated centrality metrics  
- `network_analysis.py` – Python code used for analysis  
- `network_graph.png` – visualization of the network  

## Key Takeaway
A small number of platforms dominate the AI healthcare ecosystem and act as central hubs, connecting multiple types of patient support tools and resources.

## Tools Used
- Python  
- Pandas  
- NetworkX  
- Matplotlib  
