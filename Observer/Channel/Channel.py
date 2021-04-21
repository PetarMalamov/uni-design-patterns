from Observer.Observable.Observable import Observable


class Channel(Observable):
    name=""
    subscribers = []
    latestVideoTitle = ""

    def __init__(self,name,subscribers):
        self.name = name
        self.subscribers = subscribers

    def subscribe(self, observer):
        self.subscribers.append(observer)
        observer.setSubscription(self)

    def unsubscribe(self, observer):
        self.subscribers.remove(observer)

    def notifyObservers(self):
        for subscriber in self.subscribers:
            subscriber.update()

    def addVideo(self, title):
        self.latestVideoTitle = title
        self.notifyObservers()

    def getUpdate(self):
        return self.latestVideoTitle

    def getName(self):
        return self.name