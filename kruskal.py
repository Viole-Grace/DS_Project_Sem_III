import time
graph=[]
n=int(raw_input("Enter no. of nodes : "))
for i in range(n):
	node1=int(raw_input("\nEnter node : "))
	k=int(raw_input("Enter no. of nodes it is connected to : "))
	for j in range(k):
		node2=int(raw_input("Enter connected node : "))
		edge=int(raw_input("Enter edge weight : "))
		nodelist=[]
		nodelist.append(node1)
		nodelist.append(node2)
		nodelist.append(edge)
		graph.append(nodelist)
#print "Given Graph :\n",graph
graph.sort(key=lambda x : x[2])
parent = [-1]*len(graph)
def find(i):
	if parent[i]==-1:
		return i
	else:
		return find(parent[i])
def union(i,j):
	i_s=find(i)
	j_s=find(j)
	parent[i_s]=j_s
start=time.clock()
result = []
for k in range(0,len(graph)-1):
	u=graph[k][0]
	print u
	v=graph[k][1]
	print v
	u_s=find(u)
	v_s=find(v)
	if u_s != v_s:
		result.append([u,v,graph[k][2]])
		union(u,v)
end=time.clock()
print "Spanning Tree Fomat : \nNode --> Node | Edge Weight \n",result,"\nTime taken to apply Kruskal's algorithm - ",end-start," seconds"