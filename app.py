import requests

class InstagramProfile:
    def __init__(self, username):
        self.username = username
        self.base_url = f'https://www.instagram.com/{username}/?__a=1'

    def fetch_profile_info(self):
        response = requests.get(self.base_url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Failed to fetch profile: {response.status_code}')

if __name__ == '__main__':
    username = 'instagram_username'  # Change to the desired username
    profile = InstagramProfile(username)
    try:
        info = profile.fetch_profile_info()
        print(info)
    except Exception as e:
        print(e)