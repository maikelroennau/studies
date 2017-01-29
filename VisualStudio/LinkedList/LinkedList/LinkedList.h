#pragma once

#ifndef LINKEDLIST_H
#define LINKEDLIST_H

#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;

class LinkedList
{
private:
	typedef struct node
	{
		int data;
		node* next;
	} * nodePtr;

	nodePtr head;
	nodePtr curr;

public:
	
	LinkedList()
	{
		head = NULL;
		curr = NULL;
	}

	void appendNode(int data)
	{
		nodePtr newNode = new node;
		newNode->data = data;
		newNode->next = NULL;

		if (head != NULL)
		{
			curr = head;
			while (curr->next != NULL)
			{
				curr = curr->next;
			}

			curr->next = newNode;
		}
		else
		{
			head = newNode;
		}
	}

	void deleteNode(int value)
	{
		nodePtr delection = NULL;
		nodePtr temp = new node;

		curr = head;
		
		while (curr != NULL && curr->data != value)
		{
			temp = curr;
			curr = curr->next;
		}

		if (curr == NULL)
		{
			cout << "Value " << value << " not found in the list." << endl;
		}
		else
		{
			delection = curr;
			curr = curr->next;
			temp->next = curr;

			if (delection == head)
				head = head->next;

			delete delection;
		}
	}

	void searchNode(int search)
	{
		curr = head;

		while (curr != NULL && curr->data != search)
		{
			curr = curr->next;
		}

		if (curr == NULL)
			cout << "Value not found!" << endl;
		else
			cout << "Value found!" << endl;
	}

	void showContent()
	{
		curr = head;

		while (curr != NULL)
		{
			cout << curr->data << endl;
			curr = curr->next;
		}
	}
};

#endif	