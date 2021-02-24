#include<iostream>

using namespace std;

template<class elemType>
struct binaryTreeNode
{
	elemType info;
	binaryTreeNode<elemType>* llink;
	binaryTreeNode<elemType>* rlink;
};

template<class elemType>
class binaryTreeType
{
public:
	void inorder(binaryTreeNode<elemType>* p);
	void postorder(binaryTreeNode<elemType>* p);
	int height(binaryTreeNode<elemType>* p) const;
	void insert(const elemType& insertItem);
	void destroyTree();
	bool search(const elemType& searchItem) const;
	void deleteFromTree(binaryTreeNode<elemType>*& p);
private:
	binaryTreeNode<elemType> root;
	int max(int x, int y) const;
	void destroy(binaryTreeNode<elemType>*& p);
};

template <class elemType>
void binaryTreeType<elemType>::inorder(binaryTreeNode<elemType>* p)
{
	if (p != NULL)
	{
		inorder(p->llink);
		cout << p->info << " ";
		inorder(p->rlink);
	}
}

template <class elemType>
void binaryTreeType<elemType>::postorder(binaryTreeNode<elemType>* p)
{
	if (p != NULL)
	{
		postorder(p->llink);
		postorder(p->rlink);
		cout << p->info << " ";
	}
}

template <class elemType>
int binaryTreeType<elemType>::height(binaryTreeNode<elemType>* p) const
{
	if (p == NULL)
		return 0;
	else
		return 1 + max(height(p->llink), height(p->rlink));
}
template <class elemType>
int binaryTreeType<elemType>::max(int x, int y) const
{
	if (x >= y)
		return x;
	else
		return y;
}

template <class elemType>
void binaryTreeType<elemType>::insert(const elemType& insertItem)
{
	binaryTreeNode<elemType>* current; //pointer to traverse the tree
	binaryTreeNode<elemType>* trailCurrent; //pointer behind current
	binaryTreeNode<elemType>* newNode; //pointer to create the node
	newNode = new binaryTreeNode < elemType›;

	assert(newNode != NULL);
	newNode->info = insertItem;
	newNode->llink = NULL;
	newNode->rlink = NULL;

	if (root == NULL)
		root = newNode;
	else
	{
		current = root;
		while (current != NULL)
		{
			trailCurrent = current;
			if (current->Info == insertItem)
			{
				cout << "The insert item is already in the list-";
				cout << "duplicates are not allowed."
					<< insertItem << endl;
				return;
			}
			else if (current->info > insertItem)
				current = current->llink;
			else
				current = current->rlink;
		}//end while 
		if (trailCurrent->info > insertItem)
			trailCurrent->llink = newNode;
		else
			trailCurrent->rlink = newNode;
	}
}//end insert 

template <class elemType>
void binaryTreeType<elemType>::destroy(binaryTreeNode<elemType>*& p)
{
	if (p != NULL) {
		destroy(p->llink);
		destroy(p->rlink);
		delete p;
		p = NULL;
	}
}

template <class elemType>
void binaryTreeType<elemType>::destroyTree()
{
	destroy(root);
}

template <class elemType>
bool binaryTreeType<elemType>::search(const elemType& searchItem) const
{
	binaryTreeNode<elemType>* current;
	bool found = false;

	if (root == NULL)
		cout << "Cannot search the empty tree." << endl;
	else
	{
		current = root;
		while (current != NULL && !found)
		{
			if (current->info == searchItem)
				found = true;
			else if (current->info > searchltem)
				current = current->llink;
			else
				current = current->rlink;
		}//end while
	}//end else 

	return found;
}//end search 

template <class elemType>
void binaryTreeType<elemType>::deleteFromTree(binaryTreeNode<elemType>*& p)
{
	binaryTreeNode<elemType>* current;  //pointer to traverse the tree
	binaryTreeNode<elemType> *trailCurrent; //pointer behind current
	binariTreeNode<elemType> *temp; //pointer to delete the node 

	if (p == NULL)
		cout << "Error: The node to be deleted is NULL" << endl;
	else if (p->llink == NULL && p->rlink == NULL)
	{
		temp = p;
		p = NULL;
		delete temp;
	}
	else if (p->llink == NULL)
	{
		temp p;
		p = temp->rlink;
		delete temp;
	}
	else if (p->rlink == NULL)
	{
		temp = p;
		p = temp->llink;
		delete temp
	}
	else
	{
		current = p->llink;
		trailCurrent = NULL;

		while (current->rlink != NULL)
		{
			trailCurrent = current;
			current = current->rlink;
		}//end while

		p->info = current->info;

		if (trailCurrent == NULL) //current did not move;
								  //current == p->llink; adjust p
			p->llink = current->llink;
		else
			trailCurrent->rlink = current->llink;

		delete current;
	}//end else
}//end deleteFromTree 
