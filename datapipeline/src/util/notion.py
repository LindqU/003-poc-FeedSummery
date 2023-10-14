import requests
import datetime


today = datetime.datetime.now()
date = format(today, "%Y-%m-%d")

headers = {
    "Accept": "application/json",
    "Notion-Version": "2022-06-28",
    "Authorization": "Bearer " + NOTION_API_KEY,
}

url = "https://api.notion.com/v1/pages"

# データ追加
data = {
    "parent": {
        "database_id": "df23edee0bcd48c6bf8537bdf6b2c950"
    },
    "properties": {
        "Name": {
            "title": [{"text": {"content": date}}],
        },
        "Date": {"date": {"start": date}},
    },
}
response = requests.post(url, headers=headers, json=data)
print(response.json())

# class Notion:
#     def __init__(self, notion_api_key):
#         self.api_key = notion_api_key
#         self.__header = self._gen_header(notion_api_key)
#         self.url = "https://api.notion.com/v1/"

#     def get(self, url):
#         requests.get(url, headers=self.header)

#     def post(self, data):
#         requests.post(self.url, data=data, headers=self.header)

#     @property
#     def header(self):
#         return self.__header

#     def _gen_header(self, notion_api_key) -> dict:
#         return {
#             "Accept": "application/json",
#             "Notion-Version": "2022-06-28",
#             "Authorization": "Bearer " + notion_api_key,
#         }


# class NotionDatabase:
#     def __init__(self, notion: Notion, database_id: str):
#         self.notion = notion
#         self.database_id = database_id
#         self.url = notion.url + "databases/" + database_id

#     def query(self, filter=None, sorts=None, start_cursor=None, page_size=None):
#         pass

#     def create(self, data):
#         pass

#     def insert(self, data):
#         self.notion.post(data)

#     def update(self, data):
#         pass

#     def delete(self):
#         pass


# @dataclass
# class NotionData:
#     parent: Parent


# @dataclass
# class Parent:
#     database_id: str


# @dataclass
# class proparties:
#     name: Name
