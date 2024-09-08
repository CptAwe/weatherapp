from objects import User

admin = User(username="test")
admin.fetch()
print(admin)

test = User(username="test")
test.fetch()
print(test)
