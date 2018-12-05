import requests


class User:
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f'https://vk.com/id{self.id}'

    def __and__(self, other):
        return self.friends_get_mutual(other)

    def friends_get_mutual(self, other):
        token = 'e992755a101098afbb73d51a9dc8f340ebf84658ed6e400649bef00004e0459682fb556ea9a1a3c0b8085'
        url_get_mutual = 'https://api.vk.com/method/friends.getMutual?'
        params = {
            'access_token': token,
            'source_uid': self.id,
            'target_uid': other.id,
            'v': '5.92'
        }
        response = requests.get(url_get_mutual, params)
        friends_list = [User(friend) for friend in response.json()['response']]
        return friends_list


user1 = User(30791772)
user2 = User(171691064)
for item in user1 & user2:
    print(item)

