def exists_word(word, instance):
    search = {
        "palavra": word,
        "arquivo": "",
        "ocorrencias": []
    }

    all_word_searched = []

    # O(n²)
    for index in range(0, len(instance)):
        file = instance.search(index)
        search["arquivo"] = file["nome_do_arquivo"]

        for idx, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                search["ocorrencias"].append({"linha": idx + 1})

        if len(search["ocorrencias"]) > 0:
            all_word_searched.append(search)

    return all_word_searched


def search_by_word(word, instance):
    """Aqui irá sua implementação."""
