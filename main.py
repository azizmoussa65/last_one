import sys
from file_utils import count_words_in_file

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <chemin_du_fichier>")
        return

    file_path = sys.argv[1]
    count_words_in_file(file_path)

if __name__ == "__main__":
    main()
