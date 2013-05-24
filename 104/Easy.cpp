#include <iostream>

using namespace std;

int main(int argc, char* argv[]) {
	if(argc != 2) {
		cerr << "Usage: ./a.out NUM" << endl;
		return -1;
	}
	int n = atoi(argv[1]);
	int valid = n - ( n/3 + n/14 + n/100) + (n/42 + n/300 + n/700) - (n/2100);
	cout << "valid: " << valid << endl;
	return 1;
}