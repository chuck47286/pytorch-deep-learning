# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exporters import JsonItemExporter


class ArticlespiderPipeline:
    def process_item(self, item, spider):
        return item

# 自定义的导出json文件
class JsonWithEncodingPipeline(object):
    # 自定义json文件的导出

    # 打开文件
    def __init__(self):
        # w 模式 会重写
        # a 模式 会追加
        self.file = codecs.open("article.json", "a", encoding="utf-8")

    # 写文件
    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(lines)
        return item

    # 关闭文件
    def spider_closed(self, spider):
        self.file.closed()


# scrapy提供的导出json文件
class JsonExporterPipeline(object):
    # 打开文件
    def __init__(self):
        self.file = open('articleExport.json', 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    # 写文件
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    # 关闭文件
    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.file.closed()


class ArticleImagesPipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        if "front_image_url" in item:
            image_file_path = None
            for ok, value in results:
                image_file_path = value["path"]
            item["front_image_url"] = image_file_path
        return item