n = int(input("Enter number of characters: "))

characters = []
frequencies = []

for i in range(n):
    ch = input("Enter character: ")
    freq = int(input("Enter frequency: "))

    characters.append(ch)
    frequencies.append(freq)

def huffman(characters, frequencies):

    nodes = []

    for i in range(len(characters)):
        nodes.append([frequencies[i], characters[i]])

    while len(nodes) > 1:
        nodes.sort(key=lambda x: x[0])

        f1, left = nodes.pop(0)
        f2, right = nodes.pop(0)

        nodes.append([f1 + f2, [left, right]])

    def print_codes(node, code=""):
        if isinstance(node, str):
            print(node, ":", code)
        else:
            print_codes(node[0], code + "0")
            print_codes(node[1], code + "1")

    print("\nHuffman Codes:")
    print_codes(nodes[0][1])

characters = ['A', 'B', 'C', 'D', 'E', 'F']
frequencies = [5, 9, 12, 13, 16, 45]
huffman(characters, frequencies)



nodes = [
    [
        100,
        [
            'F',
            [
                ['C', 'D'],
                [
                    ['A', 'B'],
                    'E'
                ]
            ]
        ]
    ]
]