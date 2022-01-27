# Hashing is an improvement over direct access table. The idea is to use
# Hash Function: that converts a given key to a smaller number and uses the smaller number as index in hash table.
# A good hash function is efficiently computable and should uniformly distribute keys
# Hash Table: An array that stores pointers to records corresponding to given data
# Collision: It is possible that two key results same value. That's called collision.
# Collision Handling: Chaining, Open Addressing


# Program for index matching with negatives allowed


def search(x):
    if x >= 0:
        return has[x][0] == 1

    x = abs(x)
    return has[x][1] == 1

def insert(a,n):
    for i in range(0,n):
        if a[i] >= 0:
            has[a[i]][0] = 1
        else:
            has[abs(a[i])][1] = 1

if __name__ == "__main__":
    a = [-1,9,-5,-8,-5,-2]
    n = len(a)

    MAX = 1000

    has = [[0 for i in range(2)]
                for j in range(MAX+1)]
    insert(a,n)

    x = -5
    if search(x) == True:
        print("present")
    else:
        print("Not present")