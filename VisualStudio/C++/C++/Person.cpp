#include <iostream>
#include <string>

using namespace std;

class Person
{
	private:
		string name;
		int age;

	public:
		// Constructor
		Person()
		{
			name = "Not setted";
			age = 0;
		}

		void setName(string person_name)
		{
			name = person_name;
		}

		string getName()
		{
			return name;
		}

		int getAge()
		{
			return age;
		}

		void setAge(int person_age)
		{
			age = person_age;
		}

		void toString()
		{
			cout << "Name: " + getName() << endl;
			cout << "Age:  " << getAge() << endl;
		}
};