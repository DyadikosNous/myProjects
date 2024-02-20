from instadm import InstaDM

if __name__ == '__main__':
    # Auto login
    insta = InstaDM(username='my_instagram_username', password='my_instagram_password', headless=False)

    # Send message
    insta.sendMessage(user='user1', message='Hey !')

    # Send message
    #insta.sendGroupMessage(users=['user1', 'user2'], message='Hey !')