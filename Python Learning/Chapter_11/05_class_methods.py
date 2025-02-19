class Employee:
    a=1
    @classmethod
    def show(cls):
        print(f"The constructor value is:{cls.a}")

x=Employee()
x.a=100

x.show()



