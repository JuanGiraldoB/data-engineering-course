from html.parser import HTMLParser

content = """
<!DOCTYPE html>
<html class="client-nojs" lang="en" dir="ltr">
<head>
<meta charset="UTF-8"/>
<title>1992 World Junior Championships in Athletics – Men's high jump - Wikipedia</title>
"""


class Parser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.recording = False

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self.recording = True
        else:
            self.recording = False

    def handle_data(self, data):
        if self.recording:
            print(f"Found data for tag: {data}")


p = Parser()
p.feed(content)
