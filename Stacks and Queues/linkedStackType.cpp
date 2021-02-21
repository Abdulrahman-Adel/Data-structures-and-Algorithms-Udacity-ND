#include<iostream>

using namespace std;

template <class Type>
struct nodeType
{
	Type info;
	nodeType<Type>* link;
};

template <class Type>
class linkedStackType
{
public:
	bool isEmptyStack() const;
	bool isFullStack() const;
	void initializeStack();
	void push(const Type& newItem);
	Type top() const;
	void pop();
	linkedStackType();	//Default constructor
						//Postcondition: stackTop= NULL;
private:
	nodeType<Type>* stackTop; //pointer to the stack
};

template <class Type>
linkedStackType<Type>::linkedStackType()
{
	stackTop = NULL;
}

template <class Type>
bool linkedStackType<Type>::isEmptyStack() const
{
	return(stackTop == NULL);
}//end isEmptyStack

template <class Type>
bool linkedStackType<Type>::isFullStack() const
{
	return false;
} //end isFullStack

template <class Type>
void linkedStackType<Type>::initializeStack()
{
	nodeType<Type>* temp; //pointer to delete the node
	while (stackTop != NULL) //while there are elements in the stack
	{
		temp = stackTop; //set temp to point to the current node
		stackTop = stackTop->link; //advance stackTopto the next node
		delete temp; //deallocate memory occupied by temp
	}
}//end initializeStack

template <class Type>
void linkedStackType<Type>::push(const Type& newElement)
{
	nodeType<Type>* newNode;	//pointer to create the new node

	newNode = new nodeType<Type>; //create the node 

	newNode->info = newElement; //store newElement in the node
	newNode->link = stackTop; //insert newNode before stackTop
	stackTop = newNode; //set stackTop to point to the
						//top node 
}//end push 

template <class Type>
Type linkedStackType<Type>::top() const
{
	assert(stackTop != NULL); //if stack is empty,
							  //terminate the program
	return stackTop->info; //return the top element 
}//end top

template <class Type>
void linkedStackType<Type>::pop()
{
	nodeType<Type>* temp; //pointer to deallocate memory

	if (stackTop !- NULL)
	{
		temp = stackTop; //set temp to point to the top node

		stackTop = stackTop->link //advance stackTop to the
								  //next node 
		delete temp; //delete the top node
	}
	
	else
		cout << "Cannot remove from an empty stack." << endl;
}//end pop 


