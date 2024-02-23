import random as r
import time
import heapq


#Helper function to generate a graph
def generate_graph(v,e):
    vertices = [i for i in range(v)]
    edges = []
    while len(edges)<e:
        b = r.randint(0,v-1)
        c = r.randint(0,v-1)
        if b!=c and [b,c] not in edges:
            edges.append([b, r.randint(300,2000), c])        #Adjacent list format [node1, weight, node2]

    #edges.sort(key = lambda edges:edges[0])        #Uncomment for debugging purpose
    #print(edges)
    #print("No of edges: ",len(edges))
    adjlis = [[] for i in range(v)]     #making the adjacency list
    for i in edges:
        adjlis[i[0]].append((i[1],i[2]))
    adjlis_dic = []
    G = {i:adjlis[i] for i in range(v)}
    #print(G)
    return G        #returns the graph in the form of adjacency list using dictonary data structure.

def dijkstra_sp(G,s,t):     #Dijkstra's Algorithm
    Q = [(0, s, ())]
    S = set()
    dist={s: 0.0}
    while Q:
        node_cost, v, path = heapq.heappop(Q)       #Min heapifying the Graph based on node cost
        if v not in S:                              #Relaxation starts here
            S.add(v)
            path += (v,)
            if v == t:
                return (node_cost, path)        #Returns shortest path
            
            for node_cost2, v2 in G.get(v, ()):
                if v2 in S:
                    continue
                if node_cost + node_cost2 < dist.get(v2, float('inf')):
                    dist[v2] = node_cost + node_cost2
                    heapq.heappush(Q, (node_cost + node_cost2, v2, path)) 
    return float('inf'), ()     #Returns infinite path when no path found

if __name__=='__main__':
    nodes_and_edges = [[25,50],[50,200],[100,800],[200,3200]]       #list of nodes and edges in the format [No_of_nodes,No_of_edges]
    #nodes_and_edges = [[25,50]]      #list of nodes and edges in the format [No_of_nodes,No_of_edges]
    timelis = []
    for i in nodes_and_edges:
        v,e = i[0],i[1]
        G = generate_graph(v,e)
        #print(G)       #Uncomment to verify the output
        s,t = 0,0
        while(s==t):
            s=r.randint(0,v-1)
            t=r.randint(0,v-1)
        print('{} -> {}:'.format(s, t),end=" ")
        start_time=time.perf_counter_ns()
        w,sp=dijkstra_sp(G,s,t)  # Calling Dijkstra Algorithm
        end_time=time.perf_counter_ns()
        if sp:
            print(sp)
        else:
            print("None")
        print(end_time - start_time)   # we will get the execution time of the program here in seconds and converts it to microseconds)