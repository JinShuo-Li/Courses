#ifndef GITARRAY_H
#define GITARRAY_H

#include <map>
#include <string>
#include <vector>

class GitArray {
private:
    struct BranchData {
        std::vector<std::vector<int> > versions;
        int current;
    };

    int arrayLength;
    std::string currentBranch;
    std::map<std::string, BranchData> branches;

public:
    explicit GitArray(int array_length);

    std::string toString() const;
    void set(int index, int value);
    int get(int index, int version) const;
    void undo();
    void redo();
    void branch(const std::string& branch_name);
    void checkout(const std::string& branch_name);
};

#endif
