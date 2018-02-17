class member:
    member_count = 0

    def __init__( self, name, age):
        self.name = name
        self.age = age
        member.member_count += 1


class post:
    post_count = 0

    def __init__( self, title, content):
        self.title = title
        self.content = content
        post.post_count += 1
