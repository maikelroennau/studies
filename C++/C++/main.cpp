#include <iostream>
#include <string>

#include "Person.cpp"
#include "Car.h"
#include "Sum.h"

using namespace std;

int main()
{
	cout << "Hello, World!" << endl;

	/*Person person;

	cout << "Before setting the data: " << endl;
	person.toString();

	person.setName("Maikel");
	person.setAge(21);

	cout << "After setting the data: " << endl;
	person.toString();*/

	//Car car;

	cout << sum(4.5, 1) << endl;

	int i;
	cin >> i;
	return 0;
}

Car::Car()
{
	plate = "Not setted";
	cout << "Constructor" << endl;
};

Car::~Car()
{
	plate = "";
	cout << "Destructor" << endl;
};