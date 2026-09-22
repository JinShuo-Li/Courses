# 线性表

处理线性结构的数据结构称为线性表。线性表是n（n≥0）个数据元素的有限序列。线性表中的数据元素具有相同的类型，并且在逻辑上是有序的。线性表中每个数据元素最多只有一个直接前驱和一个直接后继。

## 线性表的实现

- 线性表的顺序存储结构
- 线性表的链式存储结构

### 线性表的顺序存储结构

- 线性表中结点存储在存储器上一块连续的空间中 (物理位置上相邻)
- 线性表的元素个数是动态的, 所以需要采用动态数组
- 线性表要支持插入和删除操作, 所以需要预留一定的空间
- 保存一个动态数组需要: 数组的首地址、数组的最大容量、数组的当前长度

以下是一个实现示例:

```C++
class OutOfBound{};
class IllegalSize{};
template <class elemType>
class seqList: public list<elemType> {
private:
    elemType *data;
    int currentLength;
    int maxSize;
    void doubleSpace();
public:
    seqList(int initSize = 10);
    ~seqList() {delete [] data;}
    int length() const {return currentLength;}
    int search(const elemType &x) const;
    elemType visit(int i) const;
    void insert(int i, const elemType &x);
    void remove(int i);
    void traverse() const;
};
```

- Insert: 在第i个位置插入元素x, 其余元素后移

对于一个有$n$个元素的线性表，我们可以在$n+1$个位置插入一个新元素, 位置编号为$0, 1, 2, \ldots, n$。在第$i$个位置插入元素$x$的操作步骤如下:

```C++
template <class elemType>
void seqList<elemType>::insert(int i, const elemType &x) {
    if (i < 0 || i > currentLength) throw OutOfBound();
    if (currentLength == maxSize) doubleSpace();
    for (int j = currentLength; j > i; --j) data[j] = data[j - 1];
    data[i] = x;
    ++currentLength;
}
```

Insert操作的时间复杂度为$O(n)$, 因为在最坏情况下, 需要移动$n$个元素。

- DoubleSpace: 当线性表的长度达到最大容量时, 需要将线性表的容量加倍

```C++
template <class elemType>
void seqList<elemType>::doubleSpace() {
    elemType *tmp = data;
    maxSize *= 2;
    data = new elemType[maxSize];
    for (int i = 0; i < currentLength; ++i) data[i] = tmp[i];
    delete [] tmp;
}
```