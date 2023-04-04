from .file_management import txt_importer


def process(path_file, instance):
    importer = txt_importer(path_file)
    process = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(importer),
        "linhas_do_arquivo": importer
    }

    for i in range(0, len(instance)):
        if instance.search(i)["nome_do_arquivo"] == process["nome_do_arquivo"]:
            return
    
    instance.enqueue(process)
    print(process)


def remove(instance):
    file = instance.dequeue()
    if file is None:
        print('Não há elementos')
    else:
        print(f'Arquivo {file["nome_do_arquivo"]} removido com sucesso')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
