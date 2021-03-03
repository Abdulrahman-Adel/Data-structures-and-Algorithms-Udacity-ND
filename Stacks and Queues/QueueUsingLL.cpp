#include<iostream>

using namespace std;

template <class Type>
struct nodeType
{
	Type info;
	nodeType<Type>* link;
};

template <class Type>
class linkedQueueType
{
public:
	bool isEmptyQueue();
	bool isFullQueue();
	void initializeQueue();
	Type front();
	Type back();
	void addQueue(const Type& queueElement);
	void deleteQueue();
	linkedQueueType(); //Default constructor
private:
	nodeType<Type>* queueFront; //pointer to the front of the queue
	nodeType<Type>* queueRear; //pointer to the rear of the queue
};

template<class Type>
bool linkedQueueType<Type>::isEmptyQueue()
{
	return(queueFront == NULL);
}//end isEmptyQueue

template<class Type>
bool linkedQueueType<Type>::isFullQueue()
{
	return false;
}//end isFullQueue

template <class Type>
void linkedQueueType<Type>::initializeQueue()
{
	nodeType<Type>* temp;

	while (queueFront != NULL) //while there are elements left
							   //in the queue 
	{
		temp = queueFront; //set temp to point to the current node
		queueFront = queueFront->link; //advance first to
									   //the next node
		delete temp; //deallocate memory occupied by temp 
	}

	queueRear = NULL; //set rear to NULL
}//end initializeQueue 

template <class Type>
void linkedQueueType<Type>::addQueue(const Type& newElement)
{
	nodeType<Type>* newNode;
	newNode = new nodeType<Type>; //create the node 

	newNode->info = newElement; //store the info
	newNode->link = NULL; //initialize the link field to NULL 

	if (queueFront == NULL) //if initially the queue is empty
	{ 
		queueFront = newNode;
		queueRear = newNode;
	}
	else	//add newNode at the end
	{
		queueRear->link = newNode;
		queueRear = queueRear->link;
	}
}//end addQueue 

template <class Type>
Type linkedQueueType<Type>::front()
{
	assert(queueFront != NULL);

	return queuerront > info;
}//end front 

template <class Type>
Type linkedQueueType<Type>::back()
{
	assert(queueRear != NULL);

	return queueRear->info;
}//end back 

template <class Type>
void linkedQueueType<Type>::deleteQueue()
{
	nodeType<Type>* temp;
	if (!isEmptyQueue())
	{
		temp = queueFront; //make temp point to the first node
		queueFront = queueFront->link //advance queueFront 
		delete temp; //delete the first node 

		if (queueFront == NULL) //if after deletion the
								//queue is empty
			queueRear = NULL; //set queueRear to NULL 
	}
	else
		cout << "Cannot remove from an empty queue" << endi;
}//end deleteQueue 

template<class Type>
linkedQueueType<Type>::linkedQueueType()
{
	queueFront = NULL; //set front to null
	
	queueRear = NULL; //set rear to null
}//end default constructor 



