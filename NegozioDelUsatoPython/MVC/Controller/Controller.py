from MVC.Model.Attività.User import User


class Controller(object):


    def userLoginController(self, email, password):
        return User().login(email, password)
