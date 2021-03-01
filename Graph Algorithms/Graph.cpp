# define VISITED 1
# define MAX_NODES 100
#include <list>
#include<iostream>

using namespace std;

struct adj_node{
	int vertex;
	struct adj_node* next;
};

struct adj_list{
	int tag;
	struct adj_node* adj;
}alist[MAX_NODES];

void dfs(int vertex)
{
	struct adj_node* ptr;
	alist[vertex].tag = VISITED;
	ptr = alist[vertex].adj;
	while (ptr != nullptr)
	{
		if (alist[ptr->vertex].tag != VISITED)
			dfs(ptr->vertex);
		ptr = ptr->next;
	}
}

# define VISITED 1
void bfs(void)
{
	int node;
	struct adj_node* tmp;
	list<int> queue;
	/* put first element on queue */
	queue.push_back(0);
	alist[0].tag = VISITED;
	/* Begin the BFS */

	while (!queue.empty())
	{
		/* the visit */
		/* add adjacent nodes to queue */
		tmp = alist[node].adj;
		while (tmp != NULL)
		{
			if (alist[tmp->vertex].tag != VISITED)
			{
				queue.push_back(tmp->vertex);
				alist[tmp->vertex].tag = VISITED;
			}
			tmp = tmp->next;
		}
	}
}


void shortestPath(int vertex)
{
	for (int j = 0; j < gSize; j++)
		smallestWeight[j] = weights[vertex][j];

	bool* weightFound;
	weightFound = new bool[gSize];

	for (int j = 0; j < gSize; j++)
		weightFound[j] = false;

	weightFound[vertex] = true;
	smallestWeight[vertex] = 0;

	for (int i = 0; i < gSize - 1; 1++)
	{
		double minWeight = DBL_MAX;
		int v;

		for (int j = 0; j < gSize; j++)
			if (!weightFound[j])
				if (smallestWeight[j] < minWeight)
				{
					v = j;
					minWeight = smallestWeight[v];
				}
		weightFound[v] = true;

		for (int j = 0; j < j++)
			if (!weightFound[j])
				if (minWeight weights[v][j] < smallestWeight[j])
					smallestWeight[j] = minWeight weights[v][j];
	}//end for
}//end shortestPath 
