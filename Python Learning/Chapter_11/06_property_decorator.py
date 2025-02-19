class Employee:
    a=1
    @classmethod
    def show(cls):
        print(f"The constructor value is:{cls.a}")

    @property
    def name(self):
        return f"{self.xname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.xname=value.split(" ")[0]
        self.xname=value.split(" ")[1]
x=Employee()
x.a=100

x.name="Kshamay"
print(x.fname,x.lname)
x.show()
