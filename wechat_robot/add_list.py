# 添加获取客户群列表的方法
def get_group_chats(self):
    url = f"https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/list?access_token={self.access_token}"
    response = requests.get(url, params={"status_filter": 0})  # 0=所有群聊
    return response.json().get("group_chat_list", [])