def send_group_message(self, content, chat_id):
    url = f"https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/send?access_token={self.access_token}"
    data = {
        "chat_id": chat_id,
        "msgtype": "text",
        "text": {"content": content}
    }
    response = requests.post(url, json=data)
    return response.json()