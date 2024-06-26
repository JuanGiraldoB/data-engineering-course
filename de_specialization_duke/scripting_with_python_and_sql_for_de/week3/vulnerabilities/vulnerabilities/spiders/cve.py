import scrapy
import os
import sqlite3

from os.path import dirname

current_dir = os.path.dirname(__file__)
url = os.path.join(current_dir, 'source_cve.html')


class CveSpider(scrapy.Spider):
    name = "cve"
    allowed_domains = ["cve.mitre.org"]
    start_urls = [
        "https://cve.mitre.org/data/refs/refmap/source-EXPLOIT-DB.html"]

    # start_urls = [f'file://{url}']

    def parse(self, response):
        connection = sqlite3.connect('vuln.db')
        table = 'CREATE TABLE vulns (exploit TEXT, cve TEXT)'
        cursor = connection.cursor()
        cursor.execute(table)
        connection.commit()
        for child in response.xpath('//table'):
            if len(child.xpath('tr')) > 100:
                table = child
                break

        count = 0
        for row in table.xpath('//tr'):
            if count > 100:
                break

            try:
                exploit_id = row.xpath('td//text()')[0].extract()
                cve_id = row.xpath('td//text()')[2].extract()

                cursor.execute(
                    "INSERT INTO vulns(exploit, cve) VALUES(?, ?)", (exploit_id, cve_id))
                connection.commit()

                count += 1
            except IndexError:
                pass
