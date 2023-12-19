path = '/Users/paulvincent/Library/CloudStorage/OneDrive-InterWorks,Inc/Python/adventofcode_23/04/'
#input_file = 'part 1 sample.csv'
input_file = 'part 1 input.csv'

class Scratchcard():
    '''A single scratchcard'''
    
    def __init__(self, card : str):
        '''Initiate new scratchcard'''
        self.card = card
        self.card_no = self.card.split(':')[0]

    def get_points(self):
        '''Get the number of points on the card'''
        winners, numbers = self.card.split(' | ')
        winstr = winners.split(': ')[1]
        wins = [int(x) for x in winstr.split(' ') if x != '']
        nums = [int(x) for x in numbers.split(' ') if x != '']
        matches = len([x for x in nums if x in wins])
        if matches > 0:
            return 2 ** (matches -1)
        else:
            return 0

    def get_wins(self):
        '''Returns the number of winning numbers'''
        winners, numbers = self.card.split(' | ')
        winstr = winners.split(': ')[1]
        wins = [int(x) for x in winstr.split(' ') if x != '']
        nums = [int(x) for x in numbers.split(' ') if x != '']
        return len([x for x in nums if x in wins])

    def get_card_number(self) -> int:
        '''Get the card number'''
        return int(self.card_no.strip('Card '))
    
    def __str__(self):
        '''Show scratchcard'''
        return f'{self.card_no}'
    

class Deck():
    ''' A deck of scratchcards'''

    def __init__(self, cards) -> None:
        '''Setup a new deck'''
        #self.cards = cards
        self.deck = {}                                  # Setup an empty deck as a dictionary
        for card in cards:                              # Add cards as Scratchcard objects to the deck
            name = card.split(': ')[0]
            content = Scratchcard(card)
            self.deck[int(name.strip('Card '))] = content
        return None

    def have_card(self, number : int) -> bool:
        '''Test if cards is available in deck'''
        return number in range(1,len(self.deck)+1)
    
    def get_number_of_cards(self) -> int:
        return len(self.deck)
    
    def get_card(self, number :int) -> Scratchcard:
        '''Get the card with specified number from the deck'''
        if self.have_card(number):
            return self.deck[number]
        else:
            return ''

    def __str__(self):
        return f'Deck of {len(self.deck)} cards.'
    

# Create a new deck
with open(path + input_file) as f:
    cards = [x.strip() for x in f.readlines()]

deck = Deck(cards)

stack = []
stack_pointer = 0

# Place the original cards on the stack
for n in range(deck.get_number_of_cards()):
    stack.append(deck.get_card(n + 1))

# Step through the stack and add copies as merited by the wins on the cards
#for stack_pointer in range(100):
while stack_pointer < len(stack):

    num = stack[stack_pointer].get_card_number()
    wins = stack[stack_pointer].get_wins()
    for n in range(num + 1, num + wins + 1):
        stack.append(deck.get_card(n))
    #print(stack_pointer, stack[stack_pointer], wins, len(stack))
    stack_pointer += 1

print(f'There are {len(stack)} cards in the stack.')