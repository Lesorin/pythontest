import threading
import time

people = [
    {"first_name": "John", "last_name": "Black", "age": 30},
    {"first_name": "Michael", "last_name": "Johnsson", "age": 13},
    {"first_name": "Mery", "last_name": "Hunter", "age": 60},
    {"first_name": "Chris", "last_name": "Williams", "age": 45},
]

class Person:
    people_count = 0

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        # there was two "=", removed the extra.
        self.age = age
        self.id = self.increase_count()

    # This method should not be modified.
    def introduce(self):
        time.sleep(1)
        print(f"Hello, my first name is {self.first_name} and I am {self.age} years old.")

    def increase_count():
        Person.people_count += 1
        return Person.people_count

def main():
    threads = []
    for p in people:
        #fixed ordering to match script
        x = Person(p["first_name"], p["last_name"], p["age"])
        threads.append(threading.Thread(target=x.introduce))
        
    for thread in threads:
        thread.start()

     for thread in threads:
    
    print(f"Number of people created: {Person.people_count}")
    return
#i compared some scripts i knew of and main seemed to be wrong
if __name__ == "__main__":
    main()
