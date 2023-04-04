import sys


def txt_importer(path_file):
    if '.txt' not in path_file:
        print('Formato inválido', file=sys.stderr)
        return
    try:
        with open(path_file, 'r') as f:
            return f.read().split('\n')
    except FileNotFoundError:
        print(f'Arquivo {path_file} não encontrado', file=sys.stderr)
