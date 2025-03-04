from abc import ABC,abstractmethod
class BankApp(ABC):
    def userdata(self):
        print("username and Account no.")
    def login(self):
        print("user login")
    @abstractmethod
    def database(self):
        pass
class WebApp(BankApp):
    def new(self):
        print("database")
    def database(self):
        return "database connected" 


obj=WebApp()
print(obj.database())
obj.login()
