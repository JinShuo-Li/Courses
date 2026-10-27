#include <iostream>

using namespace std;

class IntLinkedList {
private:
    struct Node {
        int value;
        Node* next;
    };

    Node* head;
    int length;

    Node* predecessor(int index) const {
        Node* p = head;

        for (int i = 0; i < index; ++i) {
            p = p->next;
        }

        return p;
    }

public:
    IntLinkedList() {
        head = new Node{0, nullptr};
        length = 0;
    }

    ~IntLinkedList() {
        clear();
        delete head;
    }

    IntLinkedList(const IntLinkedList&) = delete;
    IntLinkedList& operator=(const IntLinkedList&) = delete;

    int size() const {
        return length;
    }

    bool empty() const {
        return length == 0;
    }

    int& at(int index) {
        return predecessor(index)->next->value;
    }

    int search(int value) const {
        Node* p = head->next;
        int index = 0;

        while (p != nullptr) {
            if (p->value == value) {
                return index;
            }

            p = p->next;
            ++index;
        }

        return -1;
    }

    bool insert(int index, int value) {
        if (index < 0 || index > length) {
            return false;
        }

        Node* prev = predecessor(index);
        Node* p = new Node{value, prev->next};

        prev->next = p;
        ++length;

        return true;
    }

    bool remove(int index) {
        if (index < 0 || index >= length) {
            return false;
        }

        Node* prev = predecessor(index);
        Node* victim = prev->next;

        prev->next = victim->next;
        delete victim;
        --length;

        return true;
    }

    void pushFront(int value) {
        insert(0, value);
    }

    void pushBack(int value) {
        insert(length, value);
    }

    void clear() {
        Node* p = head->next;

        while (p != nullptr) {
            Node* nextNode = p->next;
            delete p;
            p = nextNode;
        }

        head->next = nullptr;
        length = 0;
    }

    void print() const {
        Node* p = head->next;

        while (p != nullptr) {
            std::cout << p->value << ' ';
            p = p->next;
        }

        std::cout << '\n';
    }
};

int main() {
    IntLinkedList list;

    std::cout << list.size() << ' ' << list.empty() << '\n';

    list.pushBack(10);
    list.pushBack(20);
    list.pushFront(5);
    list.print();

    std::cout << list.insert(2, 99) << '\n';
    list.print();

    list.at(1) = 88;
    list.print();

    std::cout << list.search(99) << ' '
              << list.search(100) << '\n';

    list.remove(0);
    list.remove(list.size() - 1);
    list.print();

    std::cout << list.insert(-1, 7) << ' '
              << list.remove(list.size()) << '\n';

    list.clear();

    std::cout << list.size() << ' ' << list.empty() << '\n';

    list.pushBack(42);
    list.print();

    list.remove(0);

    std::cout << list.size() << ' ' << list.empty() << '\n';
}