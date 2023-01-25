# Anton and Polyhedron
# https://codeforces.com/problemset/problem/785/A

def main():
    number = int(input())
    faces = 0
    polyhedron_faces = {"Tetrahedron": 4, "Cube": 6, "Octahedron": 8, "Dodecahedron": 12, "Icosahedron": 20}
    for i in range(number):
        faces += polyhedron_faces[input()]
    print(faces)


if __name__ == "__main__":
    main()
