import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(probabilities):
    """
    Builds the Huffman tree from a dictionary of symbol -> probability.
    """
    heap = []
    for char, freq in probabilities.items():
        heapq.heappush(heap, HuffmanNode(char, freq))

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        merged = HuffmanNode(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2

        heapq.heappush(heap, merged)

    return heap[0] if heap else None

def generate_huffman_codes(node, current_code="", codes=None):
    """
    Traverses the Huffman tree to generate codes.
    """
    if codes is None:
        codes = {}

    if node is None:
        return

    if node.char is not None:
        codes[node.char] = current_code
        return codes

    generate_huffman_codes(node.left, current_code + "0", codes)
    generate_huffman_codes(node.right, current_code + "1", codes)
    
    return codes

def print_huffman_table(probabilities, codes):
    print(f"{'Symbol':<10} | {'Probability':<12} | {'Huffman Code':<15}")
    print("-" * 45)
    # Sort by probability descending for display, matching the typical table style
    sorted_symbols = sorted(probabilities.items(), key=lambda item: item[1], reverse=True)
    
    for symbol, prob in sorted_symbols:
        code = codes.get(symbol, "")
        print(f"{symbol:<10} | {prob:<12.2f} | {code:<15}")
