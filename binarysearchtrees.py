# Definisi kelas untuk simpul pada Binary Search Tree
class Node:
    def __init__(self, tingkatan):
        self.tingkatan = tingkatan
        self.left = None
        self.right = None

# Definisi kelas untuk Binary Search Tree
class BST:
    def __init__(self):
        self.root = None
    
    def tambah_hewan(self, tingkatan):
        self.root = self._tambah_hewan_recursive(self.root, tingkatan)
    
    def _tambah_hewan_recursive(self, node, tingkatan):
        if node is None:
            return Node(tingkatan)
        
        if tingkatan < node.tingkatan:
            node.left = self._tambah_hewan_recursive(node.left, tingkatan)
        elif tingkatan > node.tingkatan:
            node.right = self._tambah_hewan_recursive(node.right, tingkatan)
        
        return node
    
    def hapus_hewan(self, tingkatan):
        self.root = self._hapus_hewan_recursive(self.root, tingkatan)
    
    def _hapus_hewan_recursive(self, node, tingkatan):
        if node is None:
            return node
        
        if tingkatan < node.tingkatan:
            node.left = self._hapus_hewan_recursive(node.left, tingkatan)
        elif tingkatan > node.tingkatan:
            node.right = self._hapus_hewan_recursive(node.right, tingkatan)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            min_node = self._find_min(node.right)
            node.tingkatan = min_node.tingkatan
            node.right = self._hapus_hewan_recursive(node.right, min_node.tingkatan)
        
        return node
    
    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node
    
    def tingkatan_tertinggi(self):
        if self.root is None:
            return None
        
        node = self.root
        while node.right is not None:
            node = node.right
        
        return node.tingkatan
    
    def tingkatan_terendah(self):
        if self.root is None:
            return None
        
        node = self.root
        while node.left is not None:
            node = node.left
        
        return node.tingkatan

# Contoh penggunaan BST untuk memecahkan permasalahan cerita
kelompok_hewan = BST()

kelompok_hewan.tambah_hewan(5)
kelompok_hewan.tambah_hewan(2)
kelompok_hewan.tambah_hewan(5)
kelompok_hewan.tambah_hewan(6)
kelompok_hewan.tambah_hewan(4)
kelompok_hewan.tambah_hewan(6)
kelompok_hewan.tambah_hewan(8)

print("Tingkatan hewan tertinggi:", kelompok_hewan.tingkatan_tertinggi())
print("Tingkatan hewan terendah:", kelompok_hewan.tingkatan_terendah())

kelompok_hewan.hapus_hewan(3)
kelompok_hewan.hapus_hewan(8)

print("Tingkatan hewan tertinggi setelah penghapusan:", kelompok_hewan.tingkatan_tertinggi())
print("Tingkatan hewan terendah setelah penghapusan:", kelompok_hewan.tingkatan_terendah())
