
# Given: A string s of length at most 10000 letters.

# Return: How many times any word occurred in string. Each letter case (upper or lower) in word matters. Lines in output can be in any order.


str = raw_input("Enter your string:") #"When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"

def list(x):
    list_words = []
    for word in x.split(' '):
        list_words.append(word)
    return list_words
    
def create_dict(z):
    dict = {}
    for item in z:
        dict[item] = z.count(item)
    return dict
        
        
dictionary = create_dict(list(str))

def print_dict(x):
    for i, j in x.iteritems():
        print i, j
        
print_dict(dictionary)