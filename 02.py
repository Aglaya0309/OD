# Стек
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Стек пуст! Нельзя выполнить pop().")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Стек пуст! Нельзя выполнить peek().")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Верхний элемент (peek):", stack.peek())
print("Размер стека:", stack.size())
print("Удалённый элемент (pop):", stack.pop())
print("Теперь верхний элемент:", stack.peek())
print("Стек пуст?", stack.is_empty())

# Очередь

class Queue:
   def __init__(self):
       self.items = []

   def is_empty(self):
       return self.items == []

   def enqueue(self, item):
       self.items.insert(0, item)

   def dequeue(self):
       return self.items.pop()

   def size(self):
       return len(self.items)

queue = Queue()
print(queue.is_empty())
queue.enqueue("первый")
queue.enqueue("второй")
queue.enqueue("третий")
queue.enqueue("четвертый")
print(queue.is_empty())
print(queue.size())
print(queue.dequeue())
print(queue.size())

#Дерево

class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

    def insert(root, key):
        if root is None:
            return Node(key)
        else:
            if root.val < key:
                root.right = Node.insert(root.right, key)
            else:
                root.left = Node.insert(root.left, key)
        return root

    def search(root, key):
        if root is None:
            return False
        if root.val == key:
            return True
        elif root.val < key:
            return Node.search(root.right, key)
        else:
            return Node.search(root.left, key)

    def print_tree(root):
        if root:
            Node.print_tree(root.left)
            print(root.val, end=" ")
            Node.print_tree(root.right)

root = Node(50)

root = Node.insert(root, 30)
root = Node.insert(root, 20)
root = Node.insert(root, 40)
root = Node.insert(root, 70)
root = Node.insert(root, 60)
root = Node.insert(root, 80)

print("Есть ли 40 в дереве?", Node.search(root, 40))  # True
print("Есть ли 90 в дереве?", Node.search(root, 90))  # False

print("Дерево (in-order):", end=" ")
Node.print_tree(root)  # 20 30 40 50 60 70 80

#Граф
class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):

        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 in self.graph[vertex1]:
                self.graph[vertex1].remove(vertex2)
            if vertex1 in self.graph[vertex2]:
                self.graph[vertex2].remove(vertex1)

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            for neighbor in self.graph[vertex]:
                self.graph[neighbor].remove(vertex)
            del self.graph[vertex]

    def get_neighbors(self, vertex):
        return self.graph.get(vertex, [])

    def __str__(self):
        return "\n".join(f"{v}: {neighbors}" for v, neighbors in self.graph.items())


g = Graph()

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "D")

print("Исходный граф:")
print(g)

g.remove_edge("A", "B")
print("\nПосле удаления ребра A-B:")
print(g)

g.remove_vertex("C")
print("\nПосле удаления вершины C:")
print(g)

print("\nСоседи D:", g.get_neighbors("D"))