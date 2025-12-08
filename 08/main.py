with open('08/input.txt', 'r') as f:
    lines = f.read().splitlines()


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_components = n

    def find(self, x):
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Returns True if components were merged
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        # Union by size
        if self.size[root_x] < self.size[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        else:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        self.num_components -= 1
        return True


def solve_part_1(lines):
    junction_boxes = []
    for line in lines:
        if line.strip():
            x, y, z = map(int, line.split(','))
            junction_boxes.append((x, y, z))

    n = len(junction_boxes)
    distances = []
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1, z1 = junction_boxes[i]
            x2, y2, z2 = junction_boxes[j]
            dist = ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)**0.5
            distances.append((dist, i, j))
    distances.sort()

    uf = UnionFind(n)
    
    # Connect the 1000 closest pairs
    limit = min(1000, len(distances))
    for idx in range(limit):
        _, i, j = distances[idx]
        uf.union(i, j)
        
    # Get sizes of all circuits
    unique_roots = set(uf.find(i) for i in range(n))
    sizes = sorted([uf.size[root] for root in unique_roots], reverse=True)
    
    result = sizes[0] * sizes[1] * sizes[2]
    print(f"Part 1 Solution: {result}")


def solve_part_2(lines):
    junction_boxes = []
    for line in lines:
        if line.strip():
            x, y, z = map(int, line.split(','))
            junction_boxes.append((x, y, z))

    n = len(junction_boxes)
    distances = []
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1, z1 = junction_boxes[i]
            x2, y2, z2 = junction_boxes[j]
            dist = ((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)**0.5
            distances.append((dist, i, j))
    distances.sort()

    uf = UnionFind(n)
    
    # Kruskal's algorithm to find the MST
    for _, i, j in distances:
        if uf.union(i, j):
            if uf.num_components == 1:
                # This is the last connection needed
                x1 = junction_boxes[i][0]
                x2 = junction_boxes[j][0]
                print(f"Part 2 Solution: {x1 * x2}")
                return


if __name__ == "__main__":
    solve_part_1(lines)
    solve_part_2(lines)
