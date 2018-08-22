#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
  @author: Vinícius Veríssimo
  @email: vinicius.matheus@lavid.ufpb.br
'''

import sys
from os import listdir
from os.path import isfile, join
from filterfile import FilterFile
from filterapplier import FilterApplier

if __name__ == "__main__":
    file_src = sys.argv[1]
    filters_dir = sys.argv[2]
    filtered_file_name = sys.argv[3]
    filters_files = []
    filters_list = []
    filter_applier = None
    filtered_sentences = []

    # procurar todos os arquivos no diretório
    filters_files = [join(filters_dir, f) for f in listdir(
        filters_dir) if isfile(join(filters_dir, f))]

    # criar a lista de objetos de filtro
    for f in filters_files:
        filter_file = FilterFile(f)
        filter_file.load()
        filters_list.append(filter_file)

    filter_applier = FilterApplier(filters_list)
    filtered_sentences = filter_applier.filter(file_src)

    with open(filtered_file_name, 'w', encoding='utf-8') as out_file:

        for sentence in filtered_sentences:
            out_file.write(sentence + '\n')
