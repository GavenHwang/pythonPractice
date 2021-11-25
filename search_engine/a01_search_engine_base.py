# -*- coding:utf-8 -*-
import os


class SearchEngineBase(object):
    """
    一个搜索引擎由搜索器、索引器、检索器和用户接口四个部分组成。
    搜索器，通俗来讲就是我们常提到的爬虫（scrawler），它能在互联网上大量爬取各类网站的内容，送给索引器。
    索引器拿到网页和内容后，会对内容进行处理，形成索引（index），存储于内部的数据库等待检索。
    用户接口很好理解，是指网页和 App 前端界面，例如百度和谷歌的搜索页面。
    用户通过用户接口，向搜索引擎发出询问（query），询问解析后送达检索器；检索器高效检索后，再将结果返回给用户。
    """
    def __init__(self, file_path=None):
        file_path = file_path or os.path.abspath("files")
        for file in os.listdir(file_path):
            self.add_corpus(os.path.join(file_path, file))

    def add_corpus(self, file_path):
        """搜索器：负责搜索内容"""
        with open(file_path, 'r') as fin:
            text = fin.read()
        self.process_corpus(file_path, text)

    def process_corpus(self, id, text):
        """索引器：负责对内容进行处理，形成索引"""
        raise Exception('process_corpus not implemented.')

    def search(self, query):
        """检索器"""
        raise Exception('search not implemented.')


def main(search_engine):
    """用户接口"""
    while True:
        query = input()
        results = search_engine.search(query)
        print('found {} result(s):'.format(len(results)))
        for result in results:
            print(result)
