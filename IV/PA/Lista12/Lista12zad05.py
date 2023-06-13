from Lista12zad01 import CustomGraph

if __name__ == '__main__':
    graph = CustomGraph(directed=True)
    graph.load_from_json("weighted_directed_conf.json")
    print(graph.edmunds_karp("A", "F"))
