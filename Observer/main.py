from Observer.Channel.Channel import Channel
from Observer.Subscriber.Subscriber import Subscriber

def main():
    channel = Channel('pepe420',[])

    subscriber1 = Subscriber('Petar')
    subscriber2 = Subscriber('Ivan')
    subscriber3 = Subscriber('Georgi')

    channel.subscribe(subscriber1)
    channel.subscribe(subscriber2)
    channel.subscribe(subscriber3)

    channel.addVideo("prank gone wrong 420 69")


if __name__ == '__main__':
    main()