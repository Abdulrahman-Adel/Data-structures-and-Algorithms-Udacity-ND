#include<iostream>

using namespace std;

template<typename T>
struct nodeType {
	T info;
	nodeType* link;
};

template<class Type>
class LinkedListType 
{
public:
	void initialize();
	bool isEmpty() const;
	void print() const;
	int length() const;
	void destroyList();
	Type front();
	Type back();
	bool search(const Type& searchItem) const;
	void insertFirst(const Type& newItem);
	void insertFirst(const Type& newItem);
	void deleteNode(const Type& deleteItem);
	LinkedListType();
	~ LinkedListType();
protected:
	int count;
	nodeType<Type>* first;
	nodeType<Type>* last;
};

template<class Type>
bool LinkedListType<Type>::isEmpty() const{
	return (first == NULL)
}
template<class Type>
LinkedListType<Type>::LinkedListType() {
	first = NULL;
	last = NULL;
	count = 0;
}
template<class Type>
LinkedListType<Type>::~LinkedListType()
{
}
template<class Type>
void LinkedListType<Type>::destroyList() {
	nodeType<Type>* temp;
	while (first != NULL) {
		temp = first;
		first = first->link;
		delete temp;
	}
	last = NULL;
	count = 0;
}
template<class Type>
void LinkedListType<Type>::initialize() {
	destroyList();
}
template<class Type>
void LinkedListType<Type>::print() const{
	nodeType<Type>* current;
	current = first;

	while (current != NULL) {
		cout << current->info << " ";
		current = current->link
	}
}
template<class Type>
int LinkedListType<Type>::length() const{
	return count;
}
template<class Type>
Type LinkedListType<Type>::front() {
	assert(first != NULL);
	return first->info;
}
template<class Type>
Type LinkedListType<Type>::back() {
	assert(last != NULL);
	return last->info;
}
template<class Type>
LinkedListType<Type>::~LinkedListType(){
	destroyList();
}

//***********************************************************
// This class specifies the members to implement the basic properties of an unordered linked list.
// This class is derived from the class linkedListType.
//***********************************************************
template <class Type>
class unorderedLinkedList : public linkedListType<Type>
{
public:
	bool search(const Type& searchItem) const;
	void insertFirst(const Type& newItem);
	void insertLast(const Type& newItem);
	void deleteNode(const Type& deleteItem);
};

template<class Type>
bool unorderedLinkedList<Type>::search(const Type& searchItem) const {
	nodeType<Type>* current;
	current = first;

	while (current != NULL) {
		if (current->info == searchItem){
			return true;
		}
		current = current->link;
	}
	return false;
}
template<class Type>
void unorderedLinkedList<Type>::insertFirst(const Type& newItem) {
	nodeType<Type>* newNode;
	newNode = new nodeType<Type>;
	newNode->info = newItem;
	newNode->link = first;
	first = newNode;
	count += 1;
	if (last == NULL) {
		last = newNode;
	}
}
template<class Type>
void unorderedLinkedList<Type>::insertLast(const Type& newItem) {
	nodeType<Type>* newNode;
	newNode = new nodeType<Type>;
	newNode->info = newItem;
	newNode->link = NULL;
	if (first == NULL) {
		first = newNode;
		last = newNode;
		count += 1;
	}
	else {
		last->link = newNode;
		last = newNode;
		count += 1;
	}
}
template<class Type>
void unorderedLinkedList<Type>::deleteNode(const Type& deleteItem) {
	nodeType<Type>* current; //pointer to traverse the list
	nodeType<Type>* trailCurrent; //pointer just before current
	bool found;
	if (first == NULL) //Case 1; the list is empty.
		cout << "Cannot delete from an empty list." << endl;
	else
	{
		if (first->info == deleteItem) //Case 2
		{
			current = first;
			first = first->link;
			count--;
			if (first == NULL) //the list has only one node
				last = NULL;
			delete current;
		}
		else //search the list for the node with the given info
		{
			found = false;
			trailCurrent = first; //set trailCurrentto point to the first node
			current = first->link; //set current to point to the second node
			while (current != NULL && !found)
			{
				if (current->info != deleteItem)
				{
					trailCurrent = current;
					current = current->link;
				}
				else
					found = true;
			}//end while
			if (found) //Case 3; if found, delete the node
			{
				trailCurrent->link = current->link;
				count--;
				if (last == current) //node to be deleted was the last node
					last = trailCurrent; //update the value of last
				delete current; //delete the node from the list
			}
			else
				cout << "The item to be deleted is not in the list." << endl;
		}//end else
	}//end else
}//end deleteNode
	








