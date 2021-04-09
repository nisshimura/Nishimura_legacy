class Person:
    name = ''
    age = ''
    
    def setName(self, inputname):
        self.name = inputname
    def getName(self):
        return self.name

    def setAge(self, inputage):
        self.age = inputage
    def getAge(self):
        return self.age

def main():
    instanceA = Person()
    instanceA.setName('nishimura')
    instanceA.setAge('18')

    instanceB = Person()
    instanceB.setName('sakoda')
    instanceB.setAge('41')

    print(instanceA.getName())
    print(instanceA.getAge())

    print(instanceB.getName())
    print(instanceB.getAge())

if __name__ == '__main__':
    main()
