# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os
from urllib.parse import urlparse

from scrapy.pipelines.files import FilesPipeline


class DwnldmpPipeline:
    def file_path(self, request, response=None, info=None, *, item=None):
        print(os.path.basename(urlparse(request.url).path))
        return 'files/' + os.path.basename(urlparse(request.url).path)
