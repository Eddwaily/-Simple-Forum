class member:
    member_count = 0
    def __init__( self, name, age):
        self.name = name
        self.age = age
        member.member_count += 1
    def __str__(self):
        str = "="*3 + "Member - Profile" + "="*3 + "\n"
        str += "Name: " + str(self.name) + "\n"
        str += "Age: " + str(self.age) + "\n"
        str += "="*10
		return str

class post:
    posts_count = 0
    def __init__( self, title, content):
        self.title = title
        self.content = content
        post.posts_count += 1
    def __str__(self):
        str = "="*10
        str += "*"*4 + self.title + "*"*4
        str += self.content
        str += "="*10
		return str
