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
from twisted.enterprise import adbapi
import MySQLdb


class ArticlespiderPipeline:
    def process_item(self, item, spider):
        return item


# 写入Mysql数据库（同步实现，不推荐）
class MysqlPipeLine(object):
    # 打开文件
    def __init__(self):
        self.conn = MySQLdb.connect("120.26.12.74", "root", "123456", "article_spider",
                                    charset='utf8', use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = """
            INSERT INTO `article_spider`.`jobbole_article` (`title`, `url`, `url_object_id`, `front_image_path`, 
            `front_image_url`, `praise_nums`, `comment_nums`, `fav_nums`, `tags`, `content`, `create_date`) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE praise_nums=VALUES(praise_nums);
        """
        params = list()
        params.append(item.get('title', ''))
        params.append(item.get('url', ''))
        params.append(item.get('url_object_id', ''))
        params.append(item.get('front_image_path', ''))
        params.append(item.get('front_image_url', ''))
        params.append(item.get('praise_nums', 0))
        params.append(item.get('comment_nums', 0))
        params.append(item.get('fav_nums', 0))
        params.append(item.get('tags', ''))
        params.append(item.get('content', ''))
        params.append(item.get('create_date', '1970-07-01'))
        self.cursor.execute(insert_sql, tuple(params))  # 执行SQL
        self.conn.commit()  # 入库
        return item


# 异步写入Mysql数据库
class MysqlTwistedPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        from MySQLdb.cursors import DictCursor
        dbparams = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWORD'],
            charset='utf8',
            cursorclass=DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool("MySQLdb", **dbparams)
        return cls(dbpool)

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error, item, spider)

    def handle_error(self, failure, item, spider):
        print(failure)

    def do_insert(self, cursor, item):
        insert_sql = """
                    INSERT INTO `article_spider`.`jobbole_article` (`title`, `url`, `url_object_id`, `front_image_path`, 
                    `front_image_url`, `praise_nums`, `comment_nums`, `fav_nums`, `tags`, `content`, `create_date`) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE praise_nums=VALUES(praise_nums)
                """
        params = list()
        params.append(item.get('title', ''))
        params.append(item.get('url', ''))
        params.append(item.get('url_object_id', ''))
        params.append(item.get('front_image_path', ''))
        params.append(item.get("front_image_url", ''))
        params.append(item.get('praise_nums', 0))
        params.append(item.get('comment_nums', 0))
        params.append(item.get('fav_nums', 0))
        params.append(item.get('tags', ''))
        params.append(item.get('content', ''))
        params.append(item.get('create_date', '1970-07-01'))

        cursor.execute(insert_sql, tuple(params))  # 执行SQL


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
