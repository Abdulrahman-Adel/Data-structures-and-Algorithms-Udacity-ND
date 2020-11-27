#pragma once
#include<iostream>
using namespace std;

class SortingAlgs
{
private:
	/*Helper Functions*/
	void swap(int* xp, int* yp) {
		int temp = *xp;
		*xp = *yp;
		*yp = temp;
	}

	//low-- > Starting index,
	//high-- > Ending index
	int partition(int arr[], int low, int high) {
		int pivot = arr[high]; // pivot  
		int i = (low - 1); // Index of smaller element  

		for (int j = low; j <= high - 1; j++)
		{
			// If current element is smaller than the pivot  
			if (arr[j] < pivot)
			{
				i++; // increment index of smaller element  
				swap(&arr[i], &arr[j]);
			}
		}
		swap(&arr[i + 1], &arr[high]);
		return (i + 1); // return pivot index
	}

	// Merges two subarrays of arr[].
	// First subarray is arr[l..m]
	// Second subarray is arr[m+1..r]
	void merge(int arr[], int l, int m, int r)
	{
		int n1 = m - l + 1;
		int n2 = r - m;

		// Create temp arrays
		int* L = new int[n1];
		int* R = new int[n2];

		// Copy data to temp arrays L[] and R[]
		for (int i = 0; i < n1; i++)
			L[i] = arr[l + i];
		for (int j = 0; j < n2; j++)
			R[j] = arr[m + 1 + j];

		// Merge the temp arrays back into arr[l..r]

		// Initial index of first subarray
		int i = 0;

		// Initial index of second subarray
		int j = 0;

		// Initial index of merged subarray
		int k = l;

		while (i < n1 && j < n2) {
			if (L[i] <= R[j]) {
				arr[k] = L[i];
				i++;
			}
			else {
				arr[k] = R[j];
				j++;
			}
			k++;
		}

		// Copy the remaining elements of
		// L[], if there are any
		while (i < n1) {
			arr[k] = L[i];
			i++;
			k++;
		}

		// Copy the remaining elements of
		// R[], if there are any
		while (j < n2) {
			arr[k] = R[j];
			j++;
			k++;
		}
	}

	// To heapify a subtree rooted with node i which is
	// an index in arr[]. n is size of heap
	void heapify(int arr[], int n, int i)
	{
		int largest = i; // Initialize largest as root
		int l = 2 * i + 1; // left = 2*i + 1
		int r = 2 * i + 2; // right = 2*i + 2

		// If left child is larger than root
		if (l < n && arr[l] > arr[largest])
			largest = l;

		// If right child is larger than largest so far
		if (r < n && arr[r] > arr[largest])
			largest = r;

		// If largest is not root
		if (largest != i) {
			swap(&arr[i], &arr[largest]);

			// Recursively heapify the affected sub-tree
			heapify(arr, n, largest);
		}
	}

public:
	//Note: n is the length of the array
	void selection_sort(int arr[], int n) {
		int min_idx;

		for (int i = 0; i < n - 1; i++) {
			min_idx = i;

			for (int j = i + 1; j < n; j++) {
				if (arr[j] < arr[min_idx]) {
					min_idx = j;
				}
			}
			swap(&arr[min_idx], &arr[i]);
		}
	}

	void bubble_sort(int arr[], int n) {
		bool swapped;
		for (int i = 0; i < n - 1; i++) {
			swapped = false;
			for (int j = 0; j < n - i - 1; j++) {
				if (arr[j] > arr[j + 1]) {
					swap(&arr[j + 1], &arr[j]);
					swapped = true;
				}
			}

			// IF no two elements were swapped by inner loop, then break 
			if (swapped == false)
				break;
		}
	}

	void insertionSort(int arr[], int n) {
		int key, j;

		for (int i = 1; i < n; i++) {
			key = arr[i];
			j = i - 1;

			while (j >= 0 && arr[j] > key) {
				arr[j + 1] = arr[j];
				j = j - 1;
			}
			arr[j + 1] = key;
		}
	}

	void quickSort(int arr[], int low, int high)
	{
		if (low < high)
		{
			/* pi is partitioning index, arr[p] is now
			at right place */
			int pi = partition(arr, low, high);

			// Separately sort elements before  
			// partition and after partition  
			quickSort(arr, low, pi - 1);
			quickSort(arr, pi + 1, high);
		}
	}

	// l is for left index and r is
	// right index of the sub-array
	// of arr to be sorted */
	void mergeSort(int arr[], int l, int r) {
		if (l >= r) {
			return;//returns recursively
		}
		int m = (l + r - 1) / 2;
		mergeSort(arr, l, m);
		mergeSort(arr, m + 1, r);
		merge(arr, l, m, r);
	}

	void heapSort(int arr[], int n)
	{
		// Build heap (rearrange array)
		for (int i = n / 2 - 1; i >= 0; i--)
			heapify(arr, n, i);

		// One by one extract an element from heap
		for (int i = n - 1; i > 0; i--) {
			// Move current root to end
			swap(&arr[0], &arr[i]);

			// call max heapify on the reduced heap
			heapify(arr, i, 0);
		}
	}

	void print_arr(int arr[], int size) {
		int i;
		for (i = 0; i < size; i++)
			cout << arr[i] << " ";
		cout << endl;
	}
};

