from root.entities import *

import sqlalchemy as db
from sqlalchemy.orm import Session


class Database():

    engine = db.create_engine('postgresql://postgres:edcpolo@localhost/Messengers')


    def __init__(self):
        self.connection = self.engine.connect()
        print('DB Instance created')


    def fetchByQyery(self, query):
        fetchQyery = self.connection.execute(f"SELECT * FROM {query}")
        return fetchQyery

#-----------------------------------Users-------------------------------------


    def fetchAllUsers(self):
        self.session = Session(bind=self.connection)
        users = self.session.query(Users).all()
        return users

    def createUser(self, user):
        session = Session(bind=self.connection)
        session.add(user)
        session.commit()
        print("User created successfully!")


    def fetchUser(self, username):
        self.session = Session(bind=self.connection)
        user = self.session.query(Users).filter(Users.username == username).first()
        return user


    def  updateUserName(self, username, first_name, second_name):
        session = Session(bind=self.connection)
        dataToUpdate = {Users.first_name: first_name, Users.second_name: second_name}
        customerData = session.query(Users).filter(Users.username == username)
        customerData.update(dataToUpdate)
        session.commit()
        print('User updated successfully!')

    def deleteUser(self, username):
        session = Session(bind=self.connection)
        userData = session.query(Users).filter(Users.username == username).first()
        session.delete(userData)
        session.commit()
        print("User deleted successfully!")




#M------------------Messege---------------------------------------


    def fetchAllMesseges(self):
        self.session = Session(bind=self.connection)
        messeges = self.session.query(Message).all()
        return messeges


    def create_messege(self, new_message):
        session = Session(bind=self.connection)
        session.add(new_message)
        session.commit()
        print('Messege created successfully!')


    def fetchMessage(self, messege_id):
        self.session = Session(bind=self.connection)
        message = self.session.query(Message).filter(Message.messege_id == messege_id).first()
        return message

    def updateCatagoryMessage(self, messege_id, catagory):
        session = Session(bind=self.connection)
        dataToUpdate = {Message.catagory: catagory}
        messageData = session.query(Message).filter(Message.messege_id == messege_id)
        messageData.update(dataToUpdate)
        session.commit()
        print('Message catagory updated successfully!')


    def deleteMessage(self, messege_id):
        session = Session(bind=self.connection)
        messageData = session.query(Message).filter(Message.messege_id == messege_id).first()
        session.delete(messageData)
        session.commit()
        print("Message deleted successfully!")



#---------------------Catagory
    def createCatagory(self, catagory):
        session = Session(bind=self.connection)
        session.add(catagory)
        session.commit()
        print('Catagory created successfully!')

    def fetchCatagory(self, catagory_name):
        self.session = Session(bind=self.connection)
        catagory = self.session.query(Catagory).filter(Catagory.catagory_name == catagory_name).first()
        return catagory

    def updateCatagoryPopulation(self, catagory_name, population):
        session = Session(bind=self.connection)
        dataToUpdate = {Catagory.population: population}
        catagoryData = session.query(Catagory).filter(Catagory.catagory_name == catagory_name)
        catagoryData.update(dataToUpdate)
        session.commit()
        print('population catagory updated successfully!')

    def deleteCatagory(self, catagory_name):
        session = Session(bind=self.connection)
        Data = session.query(Catagory).filter(Catagory.catagory_name == catagory_name).first()
        session.delete(Data)
        session.commit()
        print("Message deleted successfully!")


base = Database()


# user = Users(username = 'Foo', password = 'password', first_name = 'имя', second_name = 'фамилия')
# base.saveUser(user)
# base.updateUserName('Foo', 'Оля', 'Яблунева')
for row in (base.fetchAllMesseges()):
    print (row)

#
# base.deleteUser('Foo')
#
# new_mes = Message(recipient='puy-puy', sender='user1', messenger='1',content='сообщение jffh')
# base.create_messege(new_mes)



# base.updateCatagoryMessage(9, 'sport')
# base.fetchByQyery('message')
# base.deleteMessage(9)
