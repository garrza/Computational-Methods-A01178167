from collections import defaultdict
import graphviz  # https://graphviz.readthedocs.io/en/stable/index.html


def analyze(R):
    # Here goes your code to do the analysis
    # 1. Reflexive: aRa for all a in X,
    # 2. Symmetric: aRb implies bRa for all a,b in X
    # 3. Transitive: aRb and bRc imply aRc for all a,b,c in X,
    def getA(R):
        A = []
        for i in R:
            if i[0] not in A:
                A.append(i[0])
        return A

    A = getA(R)

    def checkTransitive(R):
        if len(R) == 0:
            return True

        tup = defaultdict(set)

        for i in R:
            tup[i[0]].add(i[1])

        for a in tup.keys():
            all_b_in_aRb = tup.get(a)
            if all_b_in_aRb is not None:
                for b in all_b_in_aRb:
                    all_c_in_bRc = tup.get(b)
                    if a != b and all_c_in_bRc is not None:
                        if not all_c_in_bRc.issubset(all_b_in_aRb):
                            return False

        return True

    def checkSymmetric(R):
        if len(R) == 0:
            return True

        for i in R:
            if (i[1], i[0]) not in R:
                return False
        return True

    def checkReflexive(A, R):
        if len(A) > 0 and len(R) == 0:
            return False

        elif len(A) == 0:
            return True

        for i in A:
            if (i, i) not in R:
                return False

        return True

    Reflexive = checkReflexive(A, R)
    Symmetric = checkSymmetric(R)
    Transitive = checkTransitive(R)

    return Reflexive, Symmetric, Transitive


def plot():
    """
    Here goes your code to do the plot of the set
    """
    g = graphviz.Digraph("G", filename="hello.gv")
    g.edge("Hello", "World")
    g.view()


def main():
    print("Hello World analyzing input!")
    val = input("Enter your set: ")
    print(val)
    Reflexive, Symmetric, Transitive = analyze(val)
    print(
        f"\
    1. Reflexive: {Reflexive} \
    2. Symmetric: {Symmetric} \
    3. Transitive: {Transitive}"
    )
    plot()


if __name__ == "__main__":
    main()
