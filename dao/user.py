from dao.model.user import User


class UserDao:

    def __init__(self, session):
        self.session = session
    
    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_all(self):
        return self.session.query(User).all()

    def create(self, user_data):
        pass
        # ent = User(**user_data)
        # self.session.add(ent)
        # self.session.commit()
        # return ent

    def delete(self, uid):
        pass
        # User = self.get_one(rid)
        # self.session.delete(User)
        # self.session.commit()

    def update(self, user_data):
        pass
        # User = self.get_one(user_data.get("id"))
        # User.name = user_data.get("name")
        #
        # self.session.add(User)
        # self.session.commit()
