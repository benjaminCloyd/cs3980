class Animal:
    def speak(self):
        return "Animal makes a sound."


class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

    def __init__(self, name):
        self.name = name


class Cat(Animal):
    def speak(self):
        # Calls the parent's speak method
        base_sound = super().speak()
        return f"{self.name} meows. {base_sound}"


dog = Dog("Rocky")
cat = Cat("Tom")

print(dog.speak())
print(cat.speak())
