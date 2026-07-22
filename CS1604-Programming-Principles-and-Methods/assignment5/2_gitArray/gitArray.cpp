#include "gitArray.h"

#include <iostream>
#include <sstream>

GitArray::GitArray(int array_length) : arrayLength(array_length), currentBranch("main") {
    BranchData mainBranch;
    mainBranch.versions.push_back(std::vector<int>(arrayLength, 0));
    mainBranch.current = 0;
    branches[currentBranch] = mainBranch;
}

std::string GitArray::toString() const {
    const BranchData& branchData = branches.at(currentBranch);
    const std::vector<int>& currentArray = branchData.versions[branchData.current];

    std::ostringstream oss;
    oss << '(';
    for (int i = 0; i < arrayLength; ++i) {
        if (i > 0) {
            oss << ',';
        }
        oss << currentArray[i];
    }
    oss << ')';
    return oss.str();
}

void GitArray::set(int index, int value) {
    BranchData& branchData = branches[currentBranch];

    if (branchData.current + 1 < static_cast<int>(branchData.versions.size())) {
        branchData.versions.erase(branchData.versions.begin() + branchData.current + 1,
                                  branchData.versions.end());
    }

    std::vector<int> nextArray = branchData.versions[branchData.current];
    nextArray[index] = value;
    branchData.versions.push_back(nextArray);
    branchData.current = static_cast<int>(branchData.versions.size()) - 1;
}

int GitArray::get(int index, int version) const {
    const BranchData& branchData = branches.at(currentBranch);
    int targetVersion = branchData.current + version;
    return branchData.versions[targetVersion][index];
}

void GitArray::undo() {
    BranchData& branchData = branches[currentBranch];
    if (branchData.current == 0) {
        std::cout << "No Previous Version to Undo" << std::endl;
        return;
    }
    --branchData.current;
}

void GitArray::redo() {
    BranchData& branchData = branches[currentBranch];
    if (branchData.current + 1 >= static_cast<int>(branchData.versions.size())) {
        std::cout << "No Next Version to Redo" << std::endl;
        return;
    }
    ++branchData.current;
}

void GitArray::branch(const std::string& branch_name) {
    const BranchData& sourceBranch = branches[currentBranch];

    BranchData newBranch;
    newBranch.versions.assign(sourceBranch.versions.begin(),
                              sourceBranch.versions.begin() + sourceBranch.current + 1);
    newBranch.current = static_cast<int>(newBranch.versions.size()) - 1;
    branches[branch_name] = newBranch;
}

void GitArray::checkout(const std::string& branch_name) {
    std::map<std::string, BranchData>::iterator it = branches.find(branch_name);
    if (it == branches.end()) {
        std::cout << "Branch not found" << std::endl;
        return;
    }

    currentBranch = branch_name;
    BranchData& branchData = branches[currentBranch];
    branchData.current = static_cast<int>(branchData.versions.size()) - 1;
}
