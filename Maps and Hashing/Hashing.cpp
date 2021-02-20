#include<iostream>

using namespace std;

int hashFunction(char* insertKey, int keyLength, int HTSize)
{
	int sum = 0;
	for (int j = 0; j < keyLength; j++)
		sum = sum + static_cast<int>(insertKey[j]);
	return (sum % HTSize);
}

int hashFunc(string name, int HTSize)
{
	/*Determine hash address of an item */
	int i, sum;
	int len;

	i = 0;
	sum = 0;

	len = name.length();

	for (int k = 0; k < 15 - len; k++)
	{
		name = name + ' '; //increase the length of the name
						  //to 15 characters
	}

	for (int k = 0; k < 5; k++)
	{
		sum = sum + static_cast<int> (name[1]) * 128 * 128
			+ static_cast<int>(name[i + 1]) * 128
			+ static_cast<int> (name[i + 2]);
		i = i + 3;
	}
	return (sum % HTSize);
}

void LinearProbing(char* insertKey,int keyLength, int HT[], int HTSize, int newItem)
{
	int hIndex = hashFunction(insertKey, keyLength, HTSize);
	bool found = false;
	while (HT[hIndex] != NULL && !found)
		if (HT[hIndex].key == key)
			found = true;
		else
			hIndex = (hIndex + 1) % HTSize;
	if (found)
		cout << "Duplicate items are not allowed." << endl;
	else
		HT[hIndex] = newItem;
}

void QuadraticProbing(int hashIndex, const int rec)
{
	int pCount;
	int inc;

	pCount = 0;
	inc = 1;

	while (indexStatueList[hashIndex] == 1
		&& HTable[hashIndex] != rec
		&& pCount < HTSize / 2)
	{
		pCount++;
		hashIndex = (hashIndex + inc) % HTSize;
		inc = inc + 2;
	}

	if (indexStatusList[hashIndex] != 1)
	{
		HTable[hashIndex] = rec;
		indexStatusList[hashIndex] = 1;
		length++;
	}
	else if (HTable[hashIndex] == rec)
		cout << "Error: No duplicates are allowed." << endl;
	else
		cout << "Error : The table is full." << "Unable to resolve the collision." << endl;
}