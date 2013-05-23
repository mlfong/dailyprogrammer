#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <stdlib.h>
#include <time.h>

using namespace std;

struct instr_t {
	string opcode;
	int num_regs;
	int regs[2];
	instr_t(string _opcode, int _num, int* _regs) {
		opcode = _opcode;
		num_regs = _num;
		regs[0] = _regs[0], regs[1] = _regs[1];
	}
	friend std::ostream& operator<<(std::ostream& os, const instr_t& obj) {
		os << obj.opcode << " " ;
		for(int i = 0; i < obj.num_regs; ++i)
			os << obj.regs[i] << " ";
		return os;
	}
};

int main(int argc, char* argv[]) {
	if(argc != 2) {
		cerr << "Usage: ./a.out INFILE" << endl;
		return -1;
	}
	int regs[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
				  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	string line, part;
	ifstream infile(argv[1]);
	vector<instr_t> instructions;
	while(infile.good()) {
		getline(infile, line);
		int numInstr = atoi(line.c_str());
		for(int i = 0 ; i < numInstr; i++) {
			getline(infile, line);
			stringstream stream(line);
			vector<string> split;
			while(getline(stream, part, ' '))
				split.push_back(part);
			string temp_opcode = split.at(0);
			int temp_regs[2];
			for(int j = 1; j < split.size(); ++j){
				temp_regs[j-1] = atoi(split.at(j).c_str());
			}
			int temp_num_regs = split.size()-1;
			instr_t instr(temp_opcode, temp_num_regs, temp_regs);
			instructions.push_back(instr);
		}
	}
	srand(time(0));
	int numInstr = 0, x = 0;
	for(; numInstr < 100000; ++numInstr){
		instr_t& curr = instructions[x];
		if(curr.opcode == "AND"){
			regs[curr.regs[0]] = regs[curr.regs[0]] & regs[curr.regs[1]];
		} else if(curr.opcode == "OR"){
			regs[curr.regs[0]] = regs[curr.regs[0]] | regs[curr.regs[1]];
		} else if(curr.opcode == "XOR"){
			regs[curr.regs[0]] = regs[curr.regs[0]] ^ regs[curr.regs[1]];
		} else if(curr.opcode == "NOT"){
			regs[curr.regs[0]] = ~regs[curr.regs[0]];
		} else if(curr.opcode == "OR"){
			regs[curr.regs[0]] = regs[curr.regs[0]] | regs[curr.regs[1]];
		} else if(curr.opcode == "MOV"){
			regs[curr.regs[0]] = regs[curr.regs[1]];
		} else if(curr.opcode == "SET"){
			regs[curr.regs[0]] = curr.regs[1];
		} else if(curr.opcode == "RANDOM"){
			regs[curr.regs[0]] = rand() % 2;
		} else if(curr.opcode == "JMP"){
			x = curr.regs[0];
			continue;
		} else if(curr.opcode == "JZ"){
			if(regs[curr.regs[1]] == 0){
				x = curr.regs[0];
				continue;
			}
		} else if(curr.opcode == "HALT"){
			cout << "Program halts! " << numInstr << " instructions executed." << endl;
			return 1;
		}
		++x;
	}
	cout << "Program might not halt, limit of 100000 reached." << endl;
	return 1;
}




