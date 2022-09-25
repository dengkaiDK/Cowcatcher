# Code solution for ByteDance


class Tree:
    def __init__(self, member):
        self.member = member
        self.children = []
        self.parent = None

    def add_child(self, child):
        if child not in self.children:
            self.children.append(child)
            child.parent = self


class Solution:
    def __init__(self):
        self.name = 'ByteDance'
        self.n = int(input())
        self.family_list = []
        for _ in range(self.n):
            family = input().split()
            self.family_list.append(family)
        self.family_era = int(input())
        self.family_number = 0
        self.family_dict = {}

    def build_family_tree(self):
        for family in self.family_list:
            parent = family[0]
            i = 1
            if parent not in self.family_dict:
                self.family_dict[parent] = Tree(parent)

            while i < len(family):
                child = family[i]
                if child not in self.family_dict:
                    self.family_dict[child] = Tree(child)
                self.family_dict[parent].add_child(self.family_dict[child])
                parent = child
                i += 1

    def run(self):
        self.build_family_tree()
        candidate = self.family_list[0][0]
        node = self.family_dict[candidate]
        while node.parent:
            node = node.parent
        print(node.member)
        i = 0
        queue =[(i, node)]
        while len(queue) > 0:
            i, current = queue.pop(0)
            if i == self.family_era:
                break
            if i == self.family_era - 1:
                self.family_number += 1
            for child in current.children:
                queue.append((i+1, child))

        print(self.family_number)


if __name__ == '__main__':
    s = Solution()
    s.run()
