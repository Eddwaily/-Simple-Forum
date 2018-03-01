class member:
    member_count = 0
    def __init__( self, name, age):
        self.name = name
        self.age = age
        member.member_count += 1
    def __str__(self):
        mystr = "="*3 + "Member - Profile" + "="*3 + "\n"
        mystr += "Name: " + str(self.name) + "\n"
        mystr += "Age: " + str(self.age) + "\n"
        mystr += "="*10
        return mystr

class post:
    posts_count = 0
    def __init__( self, title, content):
        self.title = title
        self.content = content
        post.posts_count += 1
    def __str__(self):
        mystr = "="*10
        mystr += "*"*4 + self.title + "*"*4
        mystr += self.content
        mystr += "="*10
        return mystr
