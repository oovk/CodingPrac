class employee:

    def __init__(self, firstname, lastname, salary) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.email = self.firstname + "." + self.lastname + "@kite.com"

    def giveRaise(self,salary):
        self.salary = salary


class developer(employee):

    def __init__(self, firstname, lastname, salary, programming_lang) -> None:
        super().__init__(firstname, lastname, salary)
        self.prog_lang = programming_lang

    def addLang(self,lang):
        self.prog_lang += [lang]

employee1 = employee("john","k",1000)
print(employee1.salary)
employee1.giveRaise(10000)
print(employee1.salary)
dev1 = developer("joe", "p", 2999, ["java", "python"])
print(dev1.salary)
dev1.giveRaise(3555)
print(dev1.salary)
dev1.addLang("c++")
print(dev1.prog_lang)

