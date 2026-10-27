#include <iostream>

using namespace std;

// data structure class

class IntVector {
    private:
        int* data;
        int length;
        int capacity;

        void grow() {
            capacity *= 2;
            int* newData = new int[capacity];
            int index = 0;
            while (index < length) {
                newData[index] = data[index];
                index++;
            };
            delete[] data;
            data = newData;
        };

    public:
        IntVector(int initialCapacity = 4) {
            capacity = initialCapacity;
            data = new int[capacity];
            length = 0;
        };

        ~IntVector() {
            delete[] data;
        };

        IntVector(const IntVector&) = delete;
        IntVector& operator=(const IntVector&) = delete;

        int size() const {
            return length;
        };

        int getCapacity() const {
            return capacity;
        };

        bool empty() const{
            return length == 0;
        };

        int& at(int index) {
            return data[index];
        };

        int search(int value) const {
            int i = 0;
            while (i < length){
                if (data[i] == value) return i;
                i++;
            }
            return -1;
        };

        void pushBack(int value) {
            if (length >= capacity) {
                grow();
            };

            data[length] = value;
            length++;
        };

        bool insert(int index, int value) {
            if (index < 0 or index > length) return false;

            if (length + 1 > capacity) {
                grow();
            };

            int i = length - 1;
            while (i >= index) {
                data[i+1] = data[i];
                i--;
            };

            data[index] = value;
            length++;

            return true;
        };

        bool remove(int index) {
            if (index < 0 or index >= length) return false;

            int i = index;
            while (i < length - 1) {
                data[i] = data[i+1];
                i++;
            };

            length--;
            return true;
        };

        void clear() {
            length = 0;
        };

        void print() const {
            int index = 0;
            while (index < length) {
                cout << data[index] << " ";
                index++;
            };
            cout << endl;
        };
};

// main function

int main() {
    IntVector v(3);

    cout << v.size() << ' '
         << v.getCapacity() << ' '
         << v.empty() << '\n';

    v.pushBack(10);
    v.pushBack(20);
    v.pushBack(30);

    v.print();

    cout << v.insert(1, 99) << '\n';

    v.print();

    cout << v.size() << ' '
         << v.getCapacity() << '\n';

    v.remove(2);
    v.at(1) = 88;

    v.print();

    cout << v.search(88) << ' '
         << v.search(100) << '\n';

    cout << v.insert(-1, 7) << ' '
         << v.insert(v.size() + 1, 7) << ' '
         << v.remove(v.size()) << '\n';

    v.print();

    v.clear();

    cout << v.size() << ' '
         << v.getCapacity() << ' '
         << v.empty() << '\n';

    v.pushBack(7);
    v.print();
}