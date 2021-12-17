# -*- coding:utf-8 -*-
from search_engine.a01_search_engine_base import SearchEngineBase, main


class SimpleEngine(SearchEngineBase):
    def __init__(self, file_path=None):
        self.__id_to_texts = {}
        super(SimpleEngine, self).__init__(file_path)

    def process_corpus(self, id, text):
        self.__id_to_texts[id.split("/")[-1]] = text

    def search(self, query):
        results = []
        for id, text in self.__id_to_texts.items():
            if query in text:
                results.append(id)
        return results


if __name__ == '__main__':
    search_engine = SimpleEngine()
    main(search_engine)
