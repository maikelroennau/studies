#include <iostream>
#include <string>

#include "LinkedList.h"

using namespace std;

int main()
{
	LinkedList list;

	list.appendNode(1);
	list.appendNode(2);
	list.appendNode(3);

	list.showContent();

	cin.ignore();

	return 0;
}