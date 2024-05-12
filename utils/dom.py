import yaml


class UserCard(object):
    def __init__(self, username, uid, badge=None, sign=None) -> None:
        self.username = username
        self.uid = uid
        self.badge = badge
        self.sign = sign

    def __repr__(self) -> str:
        return f"UserCard(username={self.username}, uid={self.uid}, badge={self.badge}, sign={self.sign})"
    
    def dump(self):
        header = "```component UserCard\n"
        meta = {
            'username': self.username,
            'uid': self.uid
        }
        if self.badge:
            meta['badge'] = self.badge
        if self.sign:
            meta['sign'] = self.sign
        footer = "\n```\n"

        return header + yaml.dump(meta) + footer


if __name__ == "__main__":
    user_card = UserCard("username", 123456789, sign="sign")
    print(user_card.dump())

