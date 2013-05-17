/***
* bracket racket
***/
#include <iostream>
#include <stack>

using namespace std;

int main(int argc, char* argv[])
{
	stack<char> stack;
	char* cstr = argv[1];
	cout << cstr <<endl;
	for(int i = 0 ; i < std::strlen(cstr); i++){
		char curr = cstr[i];
		if(curr == '(' || curr == '{' || curr == '<' || curr == '[')
			stack.push(curr);
		else if(curr == ')'){
			if(stack.empty() || stack.top() != '(') {
				cerr << "false" << endl;
				return -1;
			}
			else {
				stack.pop();
			}
		} else if(curr == ']'){
			if(stack.empty() || stack.top() != '[') {
				cerr << "false" << endl;
				return -1;
			}
			else {
				stack.pop();
			}
		} else if(curr == '}'){
			if(stack.empty() || stack.top() != '{') {
				cerr << "false" << endl;
				return -1;
			}
			else {
				stack.pop();
			}
		} else if(curr == '>'){
			if(stack.empty() || stack.top() != '<') {
				cerr << "false" << endl;
				return -1;
			}
			else {
				stack.pop();
			}
		}
		
	}
	cout << (stack.empty() ? "true" : "false") << endl;
	return 0;
}
