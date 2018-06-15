#include <stdio.h>
#include <stdlib.h>
int graph[100][3];
int visited[20];
int parent[20];
int result[20][20];
int u,v,w;
int i,j,n,cn;
int count=0;
void input()
{
	printf("\nEnter the no. of nodes : ");
	scanf("%d",&n);
	for(i=0;i<n;i++)
		parent[i]=-1;visited[i]=0;
	for(i=0;i<n;i++)
	{
		printf("\nEnter node : ");
		scanf("%d",&u);
		printf("Enter no. of nodes it is connected to : ");
		scanf("%d",&cn);
		for(j=0;j<cn;j++)
		{
			printf("Enter the connected node : ");
			scanf("%d",&v);
			printf("Enter edge weight : ");
			scanf("%d",&w);
			graph[count][0]=u;
			graph[count][1]=v;
			graph[count][2]=w;
			count++;
	 	}
	}
	printf("\nEntered Graph : \n");
	for(i=0;i<count;i++)
			printf("\n%d --> %d | %d",graph[i][0],graph[i][1],graph[i][2]);
	printf("\nTotal number of elements in the graph : %d",count);
}
void sort()
{
	int i,j,temp;
	for(i=0;i<count;i++)
	{
		for(j=0;j<count-i-1;j++)
		{
			if(graph[j][2]>graph[j+1][2])
			{
				temp=graph[j][2];
				graph[j][2]=graph[j+1][2];
				graph[j+1][2]=temp;
			}
		}
	}
	printf("\n Sorted Edges : \n");
	for(i=0;i<count;i++)
		printf("%d ",graph[i][2]);
	printf("\nSorted Graph : ");
	for(i=0;i<count;i++)
		printf("\n%d --> %d | %d",graph[i][0],graph[i][1],graph[i][2]);
}
int find(int i)
{
	if(parent[i]==-1)
		return i;
	else
		return find(parent[i]);
}
void uni(int i, int j)
{
	int i_s=find(i);
	int j_s=find(j);
	parent[i_s]=j_s;
}
int main()
{
	input();
	sort();
	int u,v,k,l;
	int c=0,totalcost=0;
	int u_s,v_s;
	for(k=0;k<count;k++)
	{
		u=graph[k][0]; v=graph[k][1];
		u_s=find(u);v_s=find(v);
		if(u_s != v_s)
		{
			result[c][0]=u;
			result[c][1]=v;
			result[c][2]=graph[k][2];
			c++;
			uni(u,v);
		}
	}
	printf("\nSpanning Tree : ");
	for(k=0;k<c;k++)
	{
		printf("\n%d --> %d | %d",graph[k][0],graph[k][1],graph[k][2]);
		totalcost+=graph[k][2];
	}
	printf("\nTotal cost of the MST : %d\n",totalcost);
}