def lyrics_to_map (lyrics): 
    new_lyrics = lyrics.split()
    hashmap = {}
    print ("\nYou entered these lyrics: ") 
    print (new_lyrics)
    

    for i in new_lyrics: 
        if i in hashmap: 
            hashmap[i] += 1
        else: 
            hashmap[i] = 1
    print("\nBefore: ") 
    print(hashmap)
    
    for i in hashmap: 
        hashmap[i] -= 1
    print("\nAfter: ")
    print(hashmap)


lyrics = input("Please put in the lyrics that you would like to use: \n")
song = lyrics_to_map(lyrics)
print(song)
