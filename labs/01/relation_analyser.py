from collections import defaultdict
import graphviz


def analyze(R):
    # Se define helper function para obtener el conjunto A
    def getA(R):
        A = set()
        for pair in R:
            A.add(pair[0])
            A.add(pair[1])
        return A

    A = getA(R)

    def checkTransitive(R):
        if len(R) == 0:
            return True

        tup = defaultdict(set)

        for pair in R:
            tup[pair[0]].add(pair[1])

        for a in tup.keys():
            relationsA = tup.get(a)
            if relationsA is not None:
                for rel in list(relationsA):
                    relationsB = tup.get(rel)
                    if relationsB is not None:
                        for b in list(relationsB):
                            if b not in relationsA:
                                return False

        return True

    def checkSymmetric(R):
        if len(R) == 0:
            return True

        for pair in R:
            if (pair[1], pair[0]) not in R:
                return False
        return True

    def checkReflexive(A, R):
        if len(A) == 0:
            return True

        for a in A:
            if (a, a) not in R:
                return False
        return True

    Reflexive = checkReflexive(A, R)
    Symmetric = checkSymmetric(R)
    Transitive = checkTransitive(R)

    return Reflexive, Symmetric, Transitive


def plot(R):
    g = graphviz.Digraph("G", filename="relation_graph.gv")
    for pair in R:
        g.edge(str(pair[0]), str(pair[1]))
    g.view()


def main():
    print("Analyzing!")
    # Aqui se le dejo el set de ejemplo, pero se podria pasar un set por input
    # val = input("Enter the set: ")
    val = {(0, 0), (0, 1), (0, 3), (1, 0), (1, 1), (2, 2), (3, 0), (3, 3)}
    print(val)
    Reflexive, Symmetric, Transitive = analyze(val)
    print(
        f"\
        1. Reflexive: {Reflexive} \
        2. Symmetric: {Symmetric} \
        3. Transitive: {Transitive}"
    )
    plot(val)


if __name__ == "__main__":
    main()
