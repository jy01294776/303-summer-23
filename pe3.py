
def encode(input_text,shift):
    alpha = list('abcdefghijklmnopqrstuvwxyz') 
    enco_text = ''

    for char in input_text:
        if char.isalpha():
            index1 = (alpha.index(char.lower()) + shift) % 26 
            enco_text += alpha[index1]
        else:
            enco_text += char
    return (alpha,enco_text)


encode("a", 3) #should return (["a", "b", ... "z"], "d")
encode("xyz", 3) #should return (["a", "b", ... "z"], "abc")
encode("abc", 4) #should return (["a", "b", ... "z"], "efg") encode("xyz", 3) #should return (["a", "b", ... "z"], "abc")
encode("j!K,2?", 3) #should return (["a", "b", ... "z"], "m!n,2?")


def decode(input_text, shift):
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    deco_text = ''

    for char in input_text:
        if char.isalpha():
            index1 = (alpha.index(char.lower()) - shift) % len(alpha)
            deco_text += alpha[index1]
        else:
            deco_text += char
    return deco_text

decode("d", 3) #should return "a" 
decode("efg", 4) #should return "abc"
decode("abc", 3) #should return "xyz" 
decode("m!n,2?", 3) #should return "j!K,2?"


# ------------- Bank Account 

from datetime import date, timedelta

class BankAccount():
    def __init__( self, name = 'Billy', ID = 450204, creation_date = date.today(), balance =0 ):
        self.name  = name
        self.ID = ID
        if creation_date > date.today():
            raise Exception('Please choose a valid date')
        self.creation_date = creation_date
        self.balance = balance 
    
    def deposit( self , amount  ):
        if amount >= 0:
            self.balance += amount

    def withdraw( self, amount ):
        self.balance -= amount
        if amount < 0:
            raise Exception('No Overdraft')
        
    def view_balance(self):
        return self.balance

class SavingsAccount( BankAccount ):

    def withdraw( self, amount ):
        six_mon_creation_date = self.creation_date + timedelta(days = 6 * 30 )
        if date.today() <= six_mon_creation_date:
            raise Exception(' Sorry, the money can only be withdrawn after 6 months of your account creation' )
        if amount > self.balance:
            raise Exception('Insufficient balance')
        self.balance -= amount
    


class CheckingAccount( BankAccount ):

    def withdraw( self, amount ):
        if amount > self.balance:
            self.balance -= amount + 30
        self.balance -= amount






