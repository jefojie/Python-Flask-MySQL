

class User:

    def __init__(self, first_name, last_name, email, age):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0




    def display_info(self):

        # Have this method print all of the users' details on separate lines.

        print("=================================")
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        print("=================================")


    def enroll(self):

# Add logic in the enroll method to check if they are a member already,
#  and if they are, print "User already a member." 
#  and return False, otherwise return True.

        if self.is_rewards_member:
            print("User already is a member")
            return False


# Have this method change the user's member status to
#  True and set their gold card points to 200.
        self.is_rewards_member = True
        self.gold_card_points = 200


def spend_points(self,amount):

# Add logic in the spend points method to be sure 
# they have enough points to spend that 
# amount and handle appropriately.

        if self.gold_card_points < amount:
            print("You DO NOT have enough points")
            return 


# have this method decrease the user's points by the amount specified.
    self.gold_card_points = self.gold_card_points - amount



my_user = User("Joshua","Efojie","justlikenike06@gmail.com", 104)
my_user.display_info()
my_user.enroll()
my_user.display_info()
my_user.spend_points(99)
my_user.display_info( )

