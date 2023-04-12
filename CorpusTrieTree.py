class TrieNode:
    def __init__(self):
        self.children = {}
        self.endValue = False

class Trie:
    def __init__(self):
        self.markers = {' ', ',', '?', '!'}
        self.root = TrieNode()
    
    def insert(self, abbreviation: str, full: str):
        curr = self.root
        for char in abbreviation:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endValue = full

    def search(self, abbreviation: str):
        curr = self.root
        for char in abbreviation:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.endValue

def buildTrie(abbreviations):
    trie = Trie()
    for word in abbreviations:
        trie.insert(word, abbreviations.get(word))

    return trie

def analyze(trie, punctuations, text):
    arr = []
    words = text.split()
    for word in words:
        loweredWord = word.lower()
        start = 0
        end = len(word) - 1
        while word[start] in punctuations and start < end:
            start += 1
        while word[end] in punctuations and start < end:
            end -= 1
        end += 1
        strippedWord = loweredWord[start:end]
        correspondingValue = trie.search(strippedWord)
        if correspondingValue:
            arr.append("".join([word[0:start], correspondingValue, word[end:len(word)]]))
        else:
            arr.append(word)
    return " ".join(arr)


# Sample Abbreviations, Punctuations, and Inputs
abbreviations = {
  "gpt": "generative pre-trained transformer",
  "ai": "artificial intelligence",
  "ml": "machine learning",
  "dl": "deep learning",
  "asap": "as soon as possible"
}

punctuations = "#,?!"

inputs = [
  "Just read an interesting article on AI and its potential impact on the job market #AI #FutureofWork",
  "ML algorithms are getting better every day. Can't wait to see what kind of advancements will come next #ML #Tech",
  "Happy Friday! Time to relax and unplug from the digital world ASAP #TGIF #DigitalDetox",
  "DL models have been making waves in computer vision and natural language processing #DL #NLP",
  "Just finished a great book on the history of computing. If you're into GPT then read it ASAP #IT #TechHistory",
  "Excited to dive into a new online course on GPT-3 and its implications for language processing #GPT3 #LanguageTech"
]

outputs = [
  "Just read an interesting article on artificial intelligence and its potential impact on the job market #artificial intelligence #FutureofWork",
  "machine learning algorithms are getting better every day. Can't wait to see what kind of advancements will come next #machine learning #Tech",
  "Happy Friday! Time to relax and unplug from the digital world as soon as possible #TGIF #DigitalDetox",
  "deep learning models have been making waves in computer vision and natural language processing #deep learning #NLP",
  "Just finished a great book on the history of computing. If you're into generative pre-trained transformer then read it as soon as possible #IT #TechHistory",
  "Excited to dive into a new online course on GPT-3 and its implications for language processing #GPT3 #LanguageTech"
]

trie = buildTrie(abbreviations)

for i in range(len(inputs)):
    assert analyze(trie, punctuations, inputs[i]) == outputs[i], f"Test {i}: Failed"
