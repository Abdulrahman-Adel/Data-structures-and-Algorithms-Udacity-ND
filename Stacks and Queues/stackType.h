#pragma once
template<class Type>
class stackType
{
public:
	void initializeStack(); // Method to initialize the stack to an empty state
	//Postcondition: Returns true if the stack is empty, otherwise returns false.
	bool isEmptyStack() const; //Function to determine whether the stack is empty.
	//Postcondition: Returns true if the stack is empty, otherwise returns false.
	bool isFullStack() const; //Function to determine whether the stack is full.
	//Postcondition: Returns true if the stack is full, otherwise returns false.
	void push(const Type& newItem); //Function to add newItemto the stack.
	//Precondition: The stack exists and is not full.
	//Postcondition: The stack is changed and newItemis added to the top of the stack.
	Type top() const; //Function to return the top element of the stack.
	//Precondition: The stack exists and is not empty.
	//Postcondition: If the stack is empty, the program terminates; otherwise,
	//the top element of the stack is returned.
	void pop(); //Function to remove the top element of the stack.
	//Precondition: The stack exists and is not empty.
	//Postcondition: The stack is changed and the top element is removed from the stack.
	stackType(int stackSize = 100);
	//Constructor
	//Create an array of the size stackSizeto hold the stack elements. The default stack size is 100.
	//Postcondition: The variable list contains the base address of the array, stackTop= 0, and
	// maxStackSize= stackSize
private:
	int maxStackSize; //variable to store the maximum stack size
	int stackTop; //variable to point to the top of the stack
	Type* list; //pointer to the array that holds the stack elements
};

template <class Type>
void stackType<Type>::initializeStack()
{
	stackTop = 0;
} //end initializeStack

template <class Type>
bool stackType<Type>::isEmptyStack() const
{
	return (stackTop == 0);
} //end isEmptyStack

template <class Type>
bool stackType<Type>::isFullStack() const
{
	return (stackTop == maxStackSize);
} //end isFullStack

template <class Type>
void stackType<Type>::push(const Type& newItem)
{
	if (!isFullStack())
	{
		list[stackTop] = newItem; //add newItemat the top
		stackTop++;//increment stackTop
	}
	else
		cout << "Cannot add to a full stack." << endl;
}//end push

template <class Type>
Type stackType<Type>::top() const
{
	assert(stackTop != 0); //if stack is empty, terminate the program

	return list[stackTop - 1]; //return the element of the stack indicated by stackTop–1
}//end top

template <class Type>
void stackType<Type>::pop()
{
	if (!isEmptyStack())
		stackTop--; //decrement stackTop
	else
		cout << "Cannot remove from an empty stack." << endl;
} //end pop

template <class Type>
stackType<Type>::stackType(int stackSize)
{
	if (stackSize <= 0) {
		cout << "Size of the array to hold the stack must"
			<< "be positive." << endl;
		cout << "Creating an array of size 100." << endi;

		maxStackSize = 100;
	}
	else
		maxStackSize = stackSize;	//set the stack size to
									//the value specified by
									//the parameter stackSize 

	stackTop = 0;
	list = new Type[maxStackSize]; //set stackTop to 0
								   //create the array to
								   //hold the stack elements 
}//end constructor 
