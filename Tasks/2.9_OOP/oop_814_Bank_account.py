class Bank:
    '''Banking operations'''
    def __init__(self, account_balance):
        self.balance = account_balance
        print('I open a bank account')

    def deposit(self):
        '''Deposit money into a bank account'''
        add_dep= int(input('I deposit to your account: '))
        self.balance += add_dep
        print('On the account: ', self.balance)

    def withdraw (self):
        '''Withdraw money from a bank account'''
        take_dep = int(input('I withdraw from your bank account: '))
        if take_dep <= self.balance:
            self.balance -= take_dep
            print('On the account:', self.balance)
        else:
            print ('Error: not enough money')
            print('On the account:', self.balance)



raboshuk = Bank(1000)
raboshuk.deposit()
raboshuk.withdraw()



