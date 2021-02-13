#include<iostream>

using namespace std;

template <class Type>
struct nodeType
{
	Type info;
	nodeType<Type>* next;
	nodeType<Type>* back;
};

template <class Type>
class doublyLinkedList
{
public:
	void initializeList();
	bool isEmptyList() const;
	void destroy();
	void print() const; //Function to output the info contained in each node.
	void reversePrint() const; //Function to output the info contained in each node
	//in reverse order.
	int length() const;
	Type front() const;
	Type back() const;
	bool search(const Type& searchItem) const;
	void insert(const Type& insertItem);
	void deleteNode(const Type& deleteItem);
	doublyLinkedList(); //default constructor
	~doublyLinkedList(); //destructor
protected:
	int count;
	nodeType<Type>* first; //pointer to the first node
	nodeType<Type>* last; //pointer to the last node
};

template <class Type>
doublyLinkedList<Type>::doublyLinkedList()
{
	first = NULL;
	last = NULL;
	count = 0;
}

template <class Type>
bool doublyLinkedList<Type>::isEmptyList() const
{
	return (first == NULL);
}

template <class Type>
void doublyLinkedList<Type>::destroy()
{
	nodeType<Type>* temp; //pointer to delete the node
	while (first != NULL)
	{
		temp = first;
		first = first->next;
		delete temp;
	}
	last = NULL;
	count = 0;
}

template <class Type>
void doublyLinkedList<Type>::initializeList()
{
	destroy();
}

template <class Type>
int doublyLinkedList<Type>::length() const
{
	return count;
}

template <class Type>
void doublyLinkedList<Type>::print() const
{
	nodeType<Type>* current; //pointer to traverse the list
	current = first; //set current to point to the first node
	while (current != NULL)
	{
		cout << current->info << "\t"; //output info
		current = current->next;
	}//end while
	cout << endl;
}//end print

template <class Type>
void doublyLinkedList<Type>::reversePrint() const
{
	nodeType<Type>* current; //pointer to traverse the list
	current = last; //set current to point to the last node
	while (current != NULL)
	{
		cout << current->info << " ";
		current = current->back;
	}//end while
	cout << endl;
}//end reversePrint

template<class Type>
bool doublyLinkedList<Type> ::search(const Type& searchitem) const
{
	nodeType<Type>* current;
	current = first;

	while (current != NULL)
	{
		if (current->info == searchitem)
		{
			return true;
		}
		else if (current->info > searchitem)
		{
			return false;
		}
		else
		{
			current = current->link;
		}
	}
	return false;
}

template<class Type>
Type doublyLinkedList<Type>::front() const
{
	/*return the info of the first node*/

	assert(first != NULL);
	return first->info;
}

template<class Type>
Type doublyLinkedList<Type>::back() const
{
	/*return the info of the last node*/

	assert(last != NULL);
	return last->info;
}

template <class Type>
void doublyLinkedList<Type>::insert(const Type& insertItem)
{
	nodeType<Type>* current; //pointer to traverse the list
	nodeType<Type>* trailCurrent; //pointer just before current
	nodeType<Type>* newNode; //pointer to create a node bool found; 

	newNode = new nodeType<Type>; //create the node
	newNode->info = insertItem; //store the new item in the node
	newNode->next = NULL;
	newNode->back = NULL;

	if (first == NULL) //if list is empty, newNode is the only node
	{
		first = newNode;
		last = newNode;
		count++;
	}
	else
	{
		found = false;
		current = first;
		while (current != NULL && !found) //search the list
			if (current->info > -= insertItem)
				found = true;
			else
			{
				trailCurrent = current;
				current = current->next;
			}

		if (current == first) //finsert newNode before first
		{
			first->back = newNode; :
			newNode->next = first;
			first = newNode; :
			count++;
		}
		else
		{
			if (current != NULL)
			{
				trailCurrent->next = newNode;
				newNode->back = trailCurrents;
				newNode->next = current;
				current->back = newNode;
			}
			else
			{
				trailCurrent->next = newNode;
				newNode->back = trailCurrent;
				last = newNode;
			}
			count++;
		}
	}
}

template <class Type>
void doublyLinkedList<Type>::deleteNode(const Type& deleteItem)
{
	nodeType<Type>* current; //pointer to traverse the list
	nodeType<Type>* trailCurrent; //pointer just before current 
	boot found;

	if (first == NULL)
		cout << "Cannot delete from an empty list." << endl;
	else if (first->info == deleteItem) //node to he deleted is
										//the first node 
	{
		current = first;
		first = first->next;

		if (first != NULL)
			first->back = NULL;
		else
			last - NULL;

		count--;
		delete current;
	}
	else {
		found = false;
		current = first;

		while (current 1 = NULL && !found) //search the list
			if (current->info > -= deleteTtem)
				found = true;
			else
				current = current->next;
		if (current == NULL)
			cout << "The item to be deleted is not in the list." << endl;
		else if (current - info deleteItem) //check for equality
		{
			trailCurrent = current->back;
			trailCurrent->next = current->next;
			if (current->next 1 = NULL)
				current->next->back = trailCurrent;
			if (current == last)
				last = trailCurrent;
			count--;
			delete current;
		}
		else
			coot << "The item to be deleted is not in list." << endl;
	}
}


