from enum import Enum
from typing import Optional, NoReturn, IO


class NodeType(Enum):
    START, MIDDLE, END = "START", "MIDDLE", "END"


class Node:

    """
    Class that represents each individual Node of the Graph
    """

    def __init__(self, key: int = -1, height: Optional[int] = None, node_type: Optional[NodeType] = None,
                 parent_nodes: Optional[list["Node"]] = None, child_nodes: Optional[dict] = None) -> NoReturn:
        self.id: Optional[int] = key
        self.height: Optional[int] = height
        self.node_type: Optional[int] = node_type
        self.parent_nodes: Optional[list[int]] = parent_nodes if parent_nodes else list()  # --------- TERNARY OPERATOR
        self.child_nodes: Optional[dict[int, int]] = child_nodes if child_nodes else dict()
        return

    def __str__(self) -> str: return "Node object\tkey: " + str(self.id)  # TODO --------------------------------------

    def add_child(self, child: "Node", value: int) -> NoReturn:
        child.parent_nodes.append(self.id)
        self.child_nodes[child.id] = value
        return


class Graph:

    """
    Container class that represents a graph consisting of Node objects.

    If you wish to add Node objects in a Graph, you should use the add() method.
    """

    def __init__(self) -> NoReturn:
        self.__nodes: list[Node] = []
        return

    def __str__(self) -> str:
        out: str = "Graph object with " + str(len(self)) + " nodes:\n"
        return out + "\n".join([str(node) for node in self.__nodes])  # ---------- USAGE OF str.join(__iterable) METHOD

    def __len__(self) -> int: return len(self.__nodes)

    def add(self, node: Optional[Node] = None, nodes: Optional[list[Node]] = None) -> NoReturn:  # ---------- RECURSIVE
        if node is not None:
            if node.id < 0: node.id = len(self)
            self.__nodes.append(node)
        if nodes is not None:
            if not len(nodes): return
            self.add(node=nodes[0])
            self.add(nodes=nodes[1:])
        return

    def get(self, key: int) -> Optional[Node]:
        for node in self.__nodes:
            if node.id == key: return node
        return None

    @staticmethod
    def sample() -> "Graph": return Graph()  # --------------------- RETURNS EMPTY GRAPH OBJECT USING FORWARD REFERENCE

    @property
    def final_nodes(self) -> list[Node]:
        out: list[Node] = []
        for node in self.__nodes:
            if node.node_type == NodeType.END: out.append(node)
        return out

    @property
    def height(self) -> int: return -1  # ------------------------------------------------------------------------ TODO

    def route(self) -> list[Node]: ...  # ------------------------------------------------------------------------ TODO

    def connect_parents(self) -> NoReturn:
        for node in self.__nodes:
            for child in node.child_nodes:
                child.parent_nodes.append(node.id)
        return

    @staticmethod
    def parser(path: str) -> "Graph":
        graph_obj: Graph = Graph()
        file: IO = open(path, "r")
        for height, line in enumerate(file.readlines()):
            print("nodes with height:", height)
            for segment in line.replace(" ", "").strip("\n").split(sep="|"):
                print(segment)
                info: list[str] = segment.split(sep=":")
                node: Node = Node(key=int(info[0]), height=height)
                numbers: list[int] = [int(element) for element in info[1].split(",")]
                for index in range(0, len(numbers), 2): node.child_nodes[numbers[index]] = numbers[index + 1]
                graph_obj.add(node)
        file.close()
        graph_obj.connect_parents()
        return graph_obj


if __name__ == "__main__":
    graph = Graph.parser("data.txt")
    print(graph)
    print(len(graph))
    print(graph.final_nodes)
