#include "SortingAlgs.h"
#include<iostream>

using namespace std;

int main() {
	SortingAlgs srt;
	int arr[10] = { 3,77,12,4,8,23,9,34,5,788 };
	int size = sizeof(arr) / sizeof(arr[0]);
	int choice;
	const char* const Q =
		R"(`Chose the number of sorting algorithm:
1) insertion sort
2) bubble sort
3) selection sort
4) quick sort
5) heap sort
6) merge sort
)";
	cout << Q << endl;
	cin >> choice;

	switch (choice) {
	case 1:
		cout << "The Sorted Array (Insertion sort):" << endl;
		srt.insertionSort(arr, size);
		break;
	case 2:
		cout << "The Sorted Array (Bubble sort):" << endl;
		srt.bubble_sort(arr, size);
		break;

	case 3:
		cout << "The Sorted Array (Selection Sort):" << endl;
		srt.selection_sort(arr, size);
		break;

	case 4:
		cout << "The Sorted Array (Quick Sort):" << endl;
		srt.quickSort(arr, 0, size - 1);
		break;

	case 5:
		cout << "The Sorted Array (Heap Sort):" << endl;
		srt.heapSort(arr, size);
		break;

	case 6:
		cout << "The Sorted Array (Merge Sort):" << endl;
		srt.mergeSort(arr, 0, size - 1);
		break;

	default:
		cout << "Invalid Input! Please Enter a number from 1 to 6." << endl;
		cout << "The Unsorted array is:" << endl;
		break;
	}
	srt.print_arr(arr, size);
	return 0;
	}