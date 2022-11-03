def parse(file):
    with open(file) as f:
        all_lines = [line.strip() for line in f.readlines()]
        all_lines.pop(0)
        all_lines = sorted(all_lines, key=lambda elem: len(elem), reverse=True)
        return all_lines


def compare_words(w1, w2):
    return len([i for i in list(w1) if i not in list(w2)]) == 1 and len(w1) - len(w2) == 1


def find_levels(graph):
    current_chain_len = 1  # Current max length of chain
    already_seen_children = []  # children that has been seen before
    while graph:
        current_vertex = graph.pop(0)  # Current vertex for visiting
        children = [
            vertex for vertex in graph if compare_words(current_vertex, vertex) and vertex not in already_seen_children
                    ]
        if children:
            current_chain_len += 1
            already_seen_children = already_seen_children + children
    return current_chain_len


def find_max_chain(file):
    graph = parse(file)
    max_chain_len = str(find_levels(graph))
    with open('wchain.out', 'w') as f:
        f.write(max_chain_len)


if __name__ == '__main__':
    find_max_chain('wchain.in')
