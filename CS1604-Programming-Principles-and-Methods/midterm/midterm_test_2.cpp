#include <iostream>
#include <stack>

using namespace std;

long long Ackermann(int m, int n) {
	if (m == 0) { return n + 1; }
	else if (n == 0) { return Ackermann(m - 1, 1); }
	else {
		long long new_n = Ackermann(m, n - 1);
		return Ackermann(m - 1, new_n);
	}
}

long long Ackermann_iter(int m, int n)
{
	stack<long long> s;
	s.push(m);
	s.push(n);
	while (s.size() > 1) {
		long long a = s.top(); s.pop();
		long long b = s.top(); s.pop();
		if (b == 0) {
			s.push(a + 1);
		}
		else if (a == 0) {
			s.push(b - 1);
			s.push(1);
		}
		else {
			s.push(b - 1);
			s.push(b);
			s.push(a - 1);
		}
	}
	return s.top();
}

int main() {
	int m = 1, n = 1;
	cout << Ackermann(m, n) << " " << Ackermann_iter(m, n) << endl;
	return 0;
}