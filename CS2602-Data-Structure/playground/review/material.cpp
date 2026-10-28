#include <iostream>
#include <stdexcept>

template<class T>
class SeqList {
private:
    T* data;
    int length;
    int capacity;

    void grow() {
        int newCapacity = capacity * 2;
        T* newData = new T[newCapacity];

        try {
            for (int i = 0; i < length; ++i) {
                newData[i] = data[i];
            }
        } catch (...) {
            delete[] newData;
            throw;
        }

        delete[] data;
        data = newData;
        capacity = newCapacity;
    }

    void checkIndex(int index) const {
        if (index < 0 || index >= length) {
            throw std::out_of_range("SeqList: invalid index");
        }
    }

public:
    explicit SeqList(int initialCapacity = 10)
        : data(nullptr), length(0), capacity(initialCapacity) {
        if (initialCapacity <= 0) {
            throw std::invalid_argument("SeqList: invalid capacity");
        }

        data = new T[capacity];
    }

    ~SeqList() {
        delete[] data;
    }

    SeqList(const SeqList&) = delete;
    SeqList& operator=(const SeqList&) = delete;

    int size() const {
        return length;
    }

    int getCapacity() const {
        return capacity;
    }

    bool empty() const {
        return length == 0;
    }

    T& at(int index) {
        checkIndex(index);
        return data[index];
    }

    const T& at(int index) const {
        checkIndex(index);
        return data[index];
    }

    int search(const T& value) const {
        for (int i = 0; i < length; ++i) {
            if (data[i] == value) {
                return i;
            }
        }

        return -1;
    }

    void insert(int index, T value) {
        if (index < 0 || index > length) {
            throw std::out_of_range("SeqList: invalid insert index");
        }

        if (length == capacity) {
            grow();
        }

        for (int i = length; i > index; --i) {
            data[i] = data[i - 1];
        }

        data[index] = value;
        ++length;
    }

    void pushBack(T value) {
        insert(length, value);
    }

    void remove(int index) {
        checkIndex(index);

        for (int i = index; i < length - 1; ++i) {
            data[i] = data[i + 1];
        }

        --length;
    }

    void clear() {
        length = 0;
    }

    void print() const {
        for (int i = 0; i < length; ++i) {
            if (i != 0) {
                std::cout << ' ';
            }

            std::cout << data[i];
        }

        std::cout << '\n';
    }
};


template<class T>
class LinkedList {
private:
    struct Node {
        T value;
        Node* next;

        Node()
            : value(), next(nullptr) {
        }

        Node(const T& x, Node* nextNode = nullptr)
            : value(x), next(nextNode) {
        }
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

    void checkIndex(int index) const {
        if (index < 0 || index >= length) {
            throw std::out_of_range("LinkedList: invalid index");
        }
    }

public:
    LinkedList()
        : head(new Node()), length(0) {
    }

    ~LinkedList() {
        clear();
        delete head;
    }

    LinkedList(const LinkedList&) = delete;
    LinkedList& operator=(const LinkedList&) = delete;

    int size() const {
        return length;
    }

    bool empty() const {
        return length == 0;
    }

    T& at(int index) {
        checkIndex(index);
        return predecessor(index)->next->value;
    }

    const T& at(int index) const {
        checkIndex(index);
        return predecessor(index)->next->value;
    }

    int search(const T& value) const {
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

    void insert(int index, const T& value) {
        if (index < 0 || index > length) {
            throw std::out_of_range("LinkedList: invalid insert index");
        }

        Node* prev = predecessor(index);
        Node* p = new Node(value, prev->next);

        prev->next = p;
        ++length;
    }

    void pushFront(const T& value) {
        insert(0, value);
    }

    void pushBack(const T& value) {
        insert(length, value);
    }

    void remove(int index) {
        checkIndex(index);

        Node* prev = predecessor(index);
        Node* victim = prev->next;

        prev->next = victim->next;
        delete victim;
        --length;
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
        bool first = true;

        while (p != nullptr) {
            if (!first) {
                std::cout << ' ';
            }

            std::cout << p->value;
            first = false;
            p = p->next;
        }

        std::cout << '\n';
    }
};


template<class T>
class Stack {
private:
    T* data;
    int length;
    int capacity;

    void grow() {
        int newCapacity = capacity * 2;
        T* newData = new T[newCapacity];

        try {
            for (int i = 0; i < length; ++i) {
                newData[i] = data[i];
            }
        } catch (...) {
            delete[] newData;
            throw;
        }

        delete[] data;
        data = newData;
        capacity = newCapacity;
    }

    void checkNotEmpty() const {
        if (empty()) {
            throw std::out_of_range("Stack: empty stack");
        }
    }

public:
    explicit Stack(int initialCapacity = 10)
        : data(nullptr), length(0), capacity(initialCapacity) {
        if (initialCapacity <= 0) {
            throw std::invalid_argument("Stack: invalid capacity");
        }

        data = new T[capacity];
    }

    ~Stack() {
        delete[] data;
    }

    Stack(const Stack&) = delete;
    Stack& operator=(const Stack&) = delete;

    int size() const {
        return length;
    }

    bool empty() const {
        return length == 0;
    }

    void push(T value) {
        if (length == capacity) {
            grow();
        }

        data[length] = value;
        ++length;
    }

    T pop() {
        checkNotEmpty();

        T value = data[length - 1];
        --length;

        return value;
    }

    T& top() {
        checkNotEmpty();
        return data[length - 1];
    }

    const T& top() const {
        checkNotEmpty();
        return data[length - 1];
    }

    void clear() {
        length = 0;
    }
};


template<class T>
class Queue {
private:
    T* data;
    int maxSize;
    int frontIndex;
    int rearIndex;

    void grow() {
        int count = size();
        int newSize = maxSize * 2;
        T* newData = new T[newSize];

        try {
            for (int i = 0; i < count; ++i) {
                newData[i + 1] =
                    data[(frontIndex + 1 + i) % maxSize];
            }
        } catch (...) {
            delete[] newData;
            throw;
        }

        delete[] data;
        data = newData;
        maxSize = newSize;
        frontIndex = 0;
        rearIndex = count;
    }

    void checkNotEmpty() const {
        if (empty()) {
            throw std::out_of_range("Queue: empty queue");
        }
    }

public:
    explicit Queue(int initialCapacity = 10)
        : data(nullptr),
          maxSize(0),
          frontIndex(0),
          rearIndex(0) {
        if (initialCapacity <= 0) {
            throw std::invalid_argument("Queue: invalid capacity");
        }

        maxSize = initialCapacity + 1;
        data = new T[maxSize];
    }

    ~Queue() {
        delete[] data;
    }

    Queue(const Queue&) = delete;
    Queue& operator=(const Queue&) = delete;

    int size() const {
        return (rearIndex - frontIndex + maxSize) % maxSize;
    }

    bool empty() const {
        return frontIndex == rearIndex;
    }

    void enQueue(T value) {
        if ((rearIndex + 1) % maxSize == frontIndex) {
            grow();
        }

        int nextRear = (rearIndex + 1) % maxSize;
        data[nextRear] = value;
        rearIndex = nextRear;
    }

    T deQueue() {
        checkNotEmpty();

        int nextFront = (frontIndex + 1) % maxSize;
        T value = data[nextFront];
        frontIndex = nextFront;

        return value;
    }

    T& getHead() {
        checkNotEmpty();
        return data[(frontIndex + 1) % maxSize];
    }

    const T& getHead() const {
        checkNotEmpty();
        return data[(frontIndex + 1) % maxSize];
    }

    T& getTail() {
        checkNotEmpty();
        return data[rearIndex];
    }

    const T& getTail() const {
        checkNotEmpty();
        return data[rearIndex];
    }

    void clear() {
        frontIndex = 0;
        rearIndex = 0;
    }

    void print() const {
        int count = size();

        for (int i = 0; i < count; ++i) {
            if (i != 0) {
                std::cout << ' ';
            }

            std::cout << data[(frontIndex + 1 + i) % maxSize];
        }

        std::cout << '\n';
    }
};