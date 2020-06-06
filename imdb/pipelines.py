import pymongo


class MongodbPipeline:
    collection_name = 'best_movies'

    def open_spider(self, spider):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.db = self.client['IMDB']

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(item)
        return item
