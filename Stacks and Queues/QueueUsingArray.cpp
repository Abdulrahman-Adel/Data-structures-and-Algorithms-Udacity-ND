#include<iostream>

using namespace std;

template <class Type>
class queueType
{
public:
	bool isEmptyQueue();
	//Function to determine whether the queue is empty.
	//Postcondition: Returns true if the queue is empty, otherwise returns false.
	bool isFullQueue();
	//Function to determine whether the queue is full.
	//Postcondition: Returns true if the queue is full, otherwise returns false.
	void initializeQueue();
	//Function to initialize the queue to an empty state.
	//Postcondition: The queue is empty.
	Type front();
	//Function to return the first element of the queue.
	//Precondition: The queue exists and is not empty.
	//Postcondition: If the queue is empty, the program terminates; otherwise, the first
	// element of the queue is returned.
	Type back();
	//Function to return the last element of the queue.
	//Precondition: The queue exists and is not empty.
	//Postcondition: If the queue is empty, the program terminates; otherwise, the
	//last element of the queue is returned.
	void addQueue(const Type& queueElement);
	//Function to add queueElementto the queue.
	//Precondition: The queue exists and is not full.
	//Postcondition: The queue is changed and queueElementis added to the queue.
	void deleteQueue();
	//Function to remove the first element of the queue.
	//Precondition: The queue exists and is not empty.
	//Postcondition: The queue is changed and the first element is removed from the queue.
	queueType(int queueSize = 100); //Constructor
private:
	int maxQueueSize; //variable to store the maximum queue size
	int count; //variable to store the number of elements in the queue
	int queueFront; //variable to point to the first element of the queue
	int queueRear; //variable to point to the last element of the queue
	Type* list; //pointer to the array that holds the queue elements
};

template<class Type>
bool queueType<Type>::isEmptyQueue()
{
	return(count == 0);
}//end isEmptyQueue

template<class Type>
bool queueType<Type>::isFullQueue()
{
	return(count == maxQueueSize);
}//end isFullQueue

template <class Type>
void queueType<Type>::initializeQueue()
{
	queueFront = 0;
	queueRear = maxQueueSize - 1;
	count = 0;
} //end initializeQueue

template <class Type>
Type queueType<Type>::front()
{
	assert(!isEmptyQueue());
	return list[queueFront];
} //end front

template <class Type>
Type queueType<Type>::back()
{
	assert(!isEmptyQueue());
	return list[queueRear];
} //end back

template <class Type>
void queueType<Type>::addQueue(const Type& newElement)
{
	if (!isFullQueue())
	{
		queueRear = (queueRear + 1) % maxQueueSize;
		//use the mod operator to advance queueRear because the array is circular
		count++;
		list[queueRear] = newElement;
	}
	else cout << "Cannot add to a full queue." << endl;
} //end addQueue

template<class Type>
void queueType<Type>::deleteQueue()
{
	if (!isEmptyQueue())
	{
		count--;
		queueFront = (queueFront + 1) % maxQueueSize;
		//use the mod operator to advance queueFront because the array is circular
	}
	else
		cout << "Cannot remove from an empty queue" << endl;
}//end deleteQueue

template<class Type>
queueType<Type>::queueType(int queueSize)
{
	if (queueSize <= 0)
	{
		cout << "Size of the array to hold the queue must"<<"be positive."<<endl;
			cout << "Creating an array of size 100." << endl;
		maxQueueSize = 100;
	}
	else
		maxQueueSize = queueSize;//set maxQueueSize to queueSize

	queueFront = 0;//initialize queueFront
	queueRear = maxQueueSize - 1;//initialize queueRear
	count = 0;
	list = new Type[maxQueueSize];//create the array to hold the queueElements
}//endconstructor
