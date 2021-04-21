from Observer.Observer.ObserverMain import Observer


class Subscriber(Observer):
    name = ""
    subscribedTo = None # TODO: change to array

    def __init__(self, name):
        self.name = name

    def update(self):
        if self.subscribedTo == None:
            print(self.getName() + " has no subscriptions")
            return

        newVideoTitle = self.subscribedTo.getUpdate()
        channalName = self.subscribedTo.getName()
        print(f'{channalName} uploaded a new video titled "{newVideoTitle}"')

    def setSubscription(self, channel):
        self.subscribedTo = channel

    def getName(self):
        return self.name