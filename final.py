graph=[]
n=int(raw_input("Enter no. of nodes : "))
parent = [-1]*n
for i in range(n):
	u=int(raw_input("\nEnter node : "))
	k=int(raw_input("Enter no. of nodes it is connected to : "))
	for j in range(k):
		v=int(raw_input("Enter connected node : "))
		w=int(raw_input("Enter edge weight : "))
		graph.append([u,v,w])
print "\n\nGiven Graph:"
for i in range(len(graph)):
	print str(graph[i][0])+"-->"+str(graph[i][1])+" | "+str(graph[i][2])
graph.sort(key=lambda x : x[2])
print "\n\nSorted Graph:"
for i in range(len(graph)):
	print str(graph[i][0])+"-->"+str(graph[i][1])+" | "+str(graph[i][2])
def find(i):
	if parent[i-1]==-1:
		return i
	else:
		return find(parent[i-1])
def union(i,j):
	i_s=find(i)
	j_s=find(j)
	parent[i_s-1]=j_s
def Kruskals():
	result = []
	for k in range(0,len(graph)-1):
		u=graph[k][0]
		v=graph[k][1]
		u_s=find(u)
		v_s=find(v)
		if u_s != v_s:
			result.append([u,v,graph[k][2]])
			union(u,v)
	return result
result=Kruskals()
print "\n\nSpanning Tree Fomat:\nNode --> Node | Edge Weight"
for i in range(len(result)):
	print str(result[i][0])+"-->"+str(result[i][1])+" | "+str(result[i][2])
