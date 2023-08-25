
def computeFrequency(Text, k):
    frequencyArray = [0 for i in range(4**k - 1)]
    
    for i in range(len(Text) - k):
        pattern = Text[i:i+k]
        
    