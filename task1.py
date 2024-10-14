import os
import shutil
from argparse import ArgumentParser

def recursive_copy(source_dir, dest_dir):
    try:
        os.makedirs(dest_dir, exist_ok=True)

        for entry in os.listdir(source_dir):
            entry_path = os.path.join(source_dir, entry)

            if os.path.isdir(entry_path):
                recursive_copy(entry_path, dest_dir)
            else:
                ext = os.path.splitext(entry)[1][1:].lower()
                if ext == '':
                    ext = 'no_extension'

                ext_dir = os.path.join(dest_dir, ext)
                os.makedirs(ext_dir, exist_ok=True)

                shutil.copy(entry_path, ext_dir)
                print(f"Файл {entry} скопійовано до {ext_dir}")

    except Exception as e:
        print(f"Помилка при обробці {source_dir}: {e}")

def parse_arguments():
    parser = ArgumentParser(description="Рекурсивне копіювання і сортування файлів за розширенням.")
    parser.add_argument("source", help="Шлях до вихідної директорії")
    parser.add_argument("destination", nargs="?", default="dist", help="Шлях до директорії призначення (за замовчуванням 'dist')")
    return parser.parse_args()

def main():
    args = parse_arguments()

    if not os.path.isdir(args.source):
        print(f"Директорія {args.source} не існує або не є директорією.")
        return

    recursive_copy(args.source, args.destination)

if __name__ == "__main__":
    main()
