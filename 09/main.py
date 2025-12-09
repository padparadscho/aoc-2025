with open('09/input.txt', 'r') as f:
    lines = f.read().splitlines()

def solve_part_1(lines):
    pts = [tuple(map(int, l.split(','))) for l in lines if l.strip()]
    n = len(pts)
    max_area = 0

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = pts[i]
            x2, y2 = pts[j]
            
            # Calculate area of rectangle defined by opposite corners
            # Include boundary tiles
            width = abs(x2 - x1) + 1
            height = abs(y2 - y1) + 1
            max_area = max(max_area, width * height)

    print(f"Part 1 Solution: {max_area}")

def solve_part_2(lines):
    pts = [tuple(map(int, l.split(','))) for l in lines if l.strip()]
    n = len(pts)
    edges = [(pts[i], pts[(i+1)%n]) for i in range(n)]
    
    # Vertical edges for ray casting (x, ymin, ymax)
    v_edges = [(p1[0], min(p1[1], p2[1]), max(p1[1], p2[1])) 
               for p1, p2 in edges if p1[0] == p2[0]]

    def is_inside(x, y):
        hits = 0
        for vx, vymin, vymax in v_edges:
            if vx > x and vymin <= y < vymax:
                hits += 1
        return hits % 2 == 1

    max_area = 0
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = pts[i]
            x2, y2 = pts[j]
            
            rx1, rx2 = min(x1, x2), max(x1, x2)
            ry1, ry2 = min(y1, y2), max(y1, y2)
            
            area = (rx2 - rx1 + 1) * (ry2 - ry1 + 1)
            if area <= max_area: continue

            # Check intersections with edges
            valid = True
            for (ex1, ey1), (ex2, ey2) in edges:
                if ex1 == ex2: # Vertical
                    if rx1 < ex1 < rx2 and max(ry1, min(ey1, ey2)) < min(ry2, max(ey1, ey2)):
                        valid = False; break
                else: # Horizontal
                    if ry1 < ey1 < ry2 and max(rx1, min(ex1, ex2)) < min(rx2, max(ex1, ex2)):
                        valid = False; break
            
            if valid and is_inside((rx1 + rx2) / 2, (ry1 + ry2) / 2):
                max_area = area

    print(f"Part 2 Solution: {max_area}")

if __name__ == "__main__":
    solve_part_1(lines)
    solve_part_2(lines)