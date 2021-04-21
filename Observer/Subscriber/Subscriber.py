from Observer.Observer.ObserverMain import Observer


class Subscriber(Observer):
    name = ""

    def __init__(self, name):
        self.name = name

    def update(self,channel):
        newVideoTitle = channel.getUpdate()
        channalName = channel.getName()
        print(f'{channalName} uploaded a new video titled "{newVideoTitle}"')

    def getName(self):
        return self.name