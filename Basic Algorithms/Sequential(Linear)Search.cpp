#include<iostream>
#include<string>

using namespace std;

template<class elemType>
int seqSearch(elemType items[],int length, elemType target) {

	int loc, index = 0;
	bool found = false;

	for(loc = 0; loc < length; loc++) {
		if (items[loc] == target) {
			found = true;
			index = loc;
			break;
		}
	}
	if (found == true) return index;
	else return -1;
}

int main() {
	int arr[5] = { 1,2,3,4,5 };
	int target = 9;
	int length = sizeof(arr) / sizeof(arr[0]);
	int index = seqSearch<int>(arr, length, target);
	cout << "The index of the target value (if found) --> " << index << endl;

	return 0;
}