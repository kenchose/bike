class Bike(object):
    def __init__(self, price, max_speed): 
        self.price = price                  
        self.max_speed = max_speed
        self.miles = 0
   
    def display_info(self):
        print 'Price: $' + str(self.price)
        print 'Max speed is ' + str(self.max_speed) + 'mph'
        print 'Your bike has ' + str(self.miles) + ' miles'
        return self

    def ride(self):
        print "Riding "
        self.miles += 10
        return self

    def reverse(self):
        if self.miles >= 5:
           print "Reversing"
           self.miles -= 5
        else:
            print "You can't"
        return self

bike_one = Bike(200, 25)
bike_one.ride()
bike_one.ride()
bike_one.ride()
bike_one.reverse()
bike_one.display_info()

bike_two = Bike(100, 50)
bike_two.ride()
bike_two.ride()
bike_two.reverse()
bike_two.reverse()
bike_two.display_info()

bike_three = Bike(50, 100)
bike_three.reverse()
bike_three.reverse()
bike_three.reverse()
bike_three.display_info()



