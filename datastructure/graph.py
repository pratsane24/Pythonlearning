# class Graph:
#     def __init__(self,edges):
#         self.edges = edges
#         self.graph_dict = {}
#         for start, end in self.edges:
#             if start in self.graph_dict:
#                 self.graph_dict[start].append(end)
#             else:
#                 self.graph_dict[start] = [end]
#         print("Graph dict:",self.graph_dict)

#     def get_paths(self,start,end,path=[]):
#         # While using recursive fun u have think about the simplest case first.
         
#         path = path + [start]
        
#         if start == end:
#             return [path]

#         # This is for toronto and Mumbai path
#         if start not in self.graph_dict:
#             return []

#         # This is for our regular recursive routes case.
#         paths = []
#         for node in self.graph_dict[start]:
#             if node not in path:
#                 new_paths=  self.get_paths(node,end,path)
#                 for p in new_paths:
#                     paths.append(p)

#             return paths 
                
     
# if __name__ == '__main__':
#     routes = [
#         ("Mumbai", "Paris"),
#         ("Mumbai", "Dubai"),
#         ("Paris","Dubai"),
#         ("Paris","New York"),
#         ("Dubai", "New York"),
#         ("New York", "Toronto"),
#     ]

#     routes_graph = Graph(routes)


#     # d = {
#     #     "Mumbai": ["Paris","Dubai"]
#     # }

#     # start = "Mumbai"
#     # end = "Mumbai"
#     # print(f"Paths between {start} and {end}: ",routes_graph.get_paths(start,end))

#     # Lets do it for another path
#     # start = "Toronto"
#     # end = "Mumbai"
#     # print(f"Paths between {start} and {end}: ",routes_graph.get_paths(start,end))


#     # Lets do it for recursive case
#     start = "Mumbai"
#     end = "New York"
#     print(f"Paths between {start} and {end}: ",routes_graph.get_paths(start,end))

#     # print(f"Paths between {start} and {end}:")
#     # for i, p in enumerate(routes_graph.get_paths(start, end), start=1):
#     #     print(f"Path {i}: {' -> '.join(p)}")


# Alternate Method:

class Graph:
    def __init__(self, routes):
        self.graph_dict = {}
        for start, end in routes:
            if start not in self.graph_dict:
                self.graph_dict[start] = []
            self.graph_dict[start].append(end)

    def get_paths(self, start, end, path=None):
        if path is None:
            path = []
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths
    
    def get_shortest_path(self,start,end,path=[]):
        path = path + [start]

        if start == end:
            return path
        
        if start not in self.graph_dict:
            return None

        shorest_path = None

        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node , end, path)
                if sp:
                    if shorest_path is None or len(sp) < len(shorest_path):
                        shorest_path = sp
        return shorest_path


if __name__ == '__main__':
    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    routes_graph = Graph(routes)

    start = "Mumbai"
    end = "New York"
    print(f"Paths between {start} and {end}:")
    for i, path in enumerate(routes_graph.get_paths(start, end), start=1):
        print(f"Path {i}: {' -> '.join(path)}")


# We want to shortest path based on minimum no of stops.
    start = "Mumbai"
    end = "New York"
    print(f"Shortest Paths between {start} and {end}: ",routes_graph.get_shortest_path(start,end))