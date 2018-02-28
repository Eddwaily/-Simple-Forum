class member:
    member_count = 0
    def __init__( self, name, age):
        self.name = name
        self.age = age
        member.member_count += 1
    def __str__(self):
        print "="*3 + "Member - Profile" + "="*3
        print "Name: " + str(self.name)
        print "Age: " + str(self.age)
        print "="*10

class post:
    posts_count = 0
    def __init__( self, title, content):
        self.title = title
        self.content = content
        post.posts_count += 1
    def __str__(self):
        print "="*10
        print "*"*4 + self.title + "*"*4
        print self.content
        print "="*10
