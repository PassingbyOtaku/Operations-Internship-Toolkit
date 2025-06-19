if __name__ == "__main__":
    wechat_app = WeChatApp(CORPID, CORPSECRET, AGENTID)
    groups = wechat_app.get_group_chats()
    for group in groups:
        wechat_app.send_group_message("外部群定时通知内容", group["chat_id"])