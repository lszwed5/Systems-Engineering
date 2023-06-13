from Lista12zad01 import CustomGraph


if __name__ == '__main__':
    graph = CustomGraph(directed=True)
    graph.load_from_json("directed_conf.json")
    graph.topological_sort()
