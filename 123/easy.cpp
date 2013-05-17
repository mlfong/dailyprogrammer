#include <iostream>

using namespace std;

int main(int argc, char* argv[])
{
	if(argc != 2) {
		cerr << "usage: ./a.out NUM" << endl;
		return -1;
	}
	int num = std::atoi(argv[1]);
	if(num < 0) {
		cerr << "number must be positive" << endl;
		return -1;
	}
	while(num > 9)
		num = num%10 + num/10;
	cout << num << endl;
	
	return 1;
}