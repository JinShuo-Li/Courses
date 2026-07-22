#include <iostream>
#include <vector>
#include <string>
#include <stack>

using namespace std;

int find_var_index(const vector<string>& state_names, const string& var_name) {
    // 修复 Warning：将 int i 改为 size_t i
    for (size_t i = 0; i < state_names.size(); i++) {
        if (state_names[i] == var_name) {
            return (int)i; 
        }
    }
    return -1;
}

bool op_add(stack<int>& eval_stack, int& pc) {
    if (eval_stack.size() < 2) return false;
    int first_popped = eval_stack.top(); eval_stack.pop();
    int second_popped = eval_stack.top(); eval_stack.pop();
    eval_stack.push(second_popped + first_popped);
    pc++;
    return true;
}

bool op_sub(stack<int>& eval_stack, int& pc) {
    if (eval_stack.size() < 2) return false;
    int first_popped = eval_stack.top(); eval_stack.pop(); 
    int second_popped = eval_stack.top(); eval_stack.pop(); 
    eval_stack.push(second_popped - first_popped); 
    pc++;
    return true;
}

bool op_mul(stack<int>& eval_stack, int& pc) {
    if (eval_stack.size() < 2) return false;
    int first_popped = eval_stack.top(); eval_stack.pop();
    int second_popped = eval_stack.top(); eval_stack.pop();
    eval_stack.push(second_popped * first_popped);
    pc++;
    return true;
}

bool op_div(stack<int>& eval_stack, int& pc) {
    if (eval_stack.size() < 2) return false;
    int first_popped = eval_stack.top(); eval_stack.pop();
    int second_popped = eval_stack.top(); eval_stack.pop();
    if (first_popped == 0) return false; 
    eval_stack.push(second_popped / first_popped); 
    pc++;
    return true;
}

bool op_assign(stack<int>& eval_stack, vector<string>& state_names, vector<int>& state_values, int& pc, const string& var_name) {
    if (eval_stack.empty()) return false;
    int val = eval_stack.top();
    eval_stack.pop();

    int idx = find_var_index(state_names, var_name);
    if (idx != -1) {
        state_values[idx] = val;
    } else {
        state_names.push_back(var_name);
        state_values.push_back(val);
    }
    pc++;
    return true;
}

bool op_var(stack<int>& eval_stack, const vector<string>& state_names, const vector<int>& state_values, int& pc, const string& var_name) {
    int idx = find_var_index(state_names, var_name);
    if (idx == -1) return false; 
    eval_stack.push(state_values[idx]);
    pc++;
    return true;
}

bool op_const(stack<int>& eval_stack, int& pc, int val) {
    eval_stack.push(val);
    pc++;
    return true;
}

bool op_jmp(int& pc, int target_pc) {
    pc = target_pc; 
    return true;
}

bool op_jmpeq(stack<int>& eval_stack, int& pc, int target_pc) {
    if (eval_stack.size() < 2) return false;
    int first_popped = eval_stack.top(); eval_stack.pop();
    int second_popped = eval_stack.top(); eval_stack.pop();
    if (second_popped == first_popped) {
        pc = target_pc;
    } else {
        pc++;
    }
    return true;
}

bool op_jmpgt(stack<int>& eval_stack, int& pc, int target_pc) {
    if (eval_stack.size() < 2) return false;
    int first_popped = eval_stack.top(); eval_stack.pop();
    int second_popped = eval_stack.top(); eval_stack.pop();
    if (second_popped > first_popped) {
        pc = target_pc;
    } else {
        pc++;
    }
    return true;
}

bool op_jmplt(stack<int>& eval_stack, int& pc, int target_pc) {
    if (eval_stack.size() < 2) return false;
    int first_popped = eval_stack.top(); eval_stack.pop();
    int second_popped = eval_stack.top(); eval_stack.pop();
    if (second_popped < first_popped) {
        pc = target_pc;
    } else {
        pc++;
    }
    return true;
}

bool op_input(stack<int>& eval_stack, int& pc) {
    int val;
    if (!(cin >> val)) return false; 
    eval_stack.push(val);
    pc++;
    return true;
}

bool op_print(const vector<string>& state_names, const vector<int>& state_values, int& pc, const string& var_name) {
    int idx = find_var_index(state_names, var_name);
    if (idx == -1) return false;
    cout << state_values[idx] << endl;
    pc++;
    return true;
}

int main() {
    int n;
    if (!(cin >> n)) return 0;
    cin.ignore();

    vector<string> instructions(n);
    for (int i = 0; i < n; ++i) {
        getline(cin, instructions[i]);
    }

    stack<int> eval_stack;
    vector<string> state_names;
    vector<int> state_values;
    int pc = 0;

    while (true) {
        if (pc < 0 || pc >= n) {
            cout << "Error" << endl;
            break;
        }

        string current_cmd = instructions[pc];

        if (!current_cmd.empty() && current_cmd.back() == '\r') {
            current_cmd.pop_back();
        }

        string op_code = "";
        string arg_str = "";

        size_t space_pos = current_cmd.find(' ');
        if (space_pos != string::npos) {
            op_code = current_cmd.substr(0, space_pos);
            arg_str = current_cmd.substr(space_pos + 1);
        } else {
            op_code = current_cmd;
        }

        bool success = true;

        if (op_code == "Add") {
            success = op_add(eval_stack, pc);
        } else if (op_code == "Sub") {
            success = op_sub(eval_stack, pc);
        } else if (op_code == "Mul") {
            success = op_mul(eval_stack, pc);
        } else if (op_code == "Div") {
            success = op_div(eval_stack, pc);
        } else if (op_code == "Assign") {
            success = op_assign(eval_stack, state_names, state_values, pc, arg_str);
        } else if (op_code == "Var") {
            success = op_var(eval_stack, state_names, state_values, pc, arg_str);
        } else if (op_code == "Const") {
            int val = stoi(arg_str); 
            success = op_const(eval_stack, pc, val);
        } else if (op_code == "Jmp") {
            int target = stoi(arg_str);
            success = op_jmp(pc, target);
        } else if (op_code == "JmpEq") {
            int target = stoi(arg_str);
            success = op_jmpeq(eval_stack, pc, target);
        } else if (op_code == "JmpGt") {
            int target = stoi(arg_str);
            success = op_jmpgt(eval_stack, pc, target);
        } else if (op_code == "JmpLt") {
            int target = stoi(arg_str);
            success = op_jmplt(eval_stack, pc, target);
        } else if (op_code == "Input") {
            success = op_input(eval_stack, pc);
        } else if (op_code == "Print") {
            success = op_print(state_names, state_values, pc, arg_str);
        } else if (op_code == "Halt") {
            break;
        } else {
            success = false;
        }

        if (!success) {
            cout << "Error" << endl;
            break;
        }
    }

    return 0;
}