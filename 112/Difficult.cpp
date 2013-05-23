#include <iostream>
#include <algorithm>

using namespace std;

void brainfuck(char* input){
	char tape[30000];
	for(int i = 0; i < 30000; i++) tape[i] = 0;
	char *ptr = tape;
	char *read = input;
	while(*read){
		switch(*read){
			case '>': ++ptr;
				break;
			case '<': --ptr;
				break;
			case '+': ++*ptr;
				break;
			case '-': --*ptr;
				break;
			case '.': putchar(*ptr);
				break;
			case ',': *ptr=getchar();
				break;
			case '[': while (*ptr) {
				break;
			case ']': }
				break;
			default:
				return;
		}
		cout << *read << endl;
		*read++;
		
	}
}

int main(int argc, char* argv[]){
	if(argc != 2) {
		cerr << "Usage: ./a.out brainfuck-string" << endl;
		return -1;
	}
	int c_lparen = 0, c_rparen = 0;
	char* input = argv[1];
	for(int i = 0 ; i < std::strlen(input); i++){
		if(input[i]=='[') ++c_lparen;
		else if(input[i]==']') ++c_rparen;
	}
	if(c_lparen != c_rparen){
		cerr << "square brackets not properly closed" << endl;
		return -1;
	}
		
	brainfuck(input);
	return 1;
}

