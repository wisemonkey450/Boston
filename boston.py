#! /usr/bin/env python3

consonants =['b', 'c','d', 'f', 'g', 'h', 'j', 'k', 'l', 'm' ,'n' ,'p', 'q', 'r', 's', 't','v', 'w', 'x', 'z']
wicked_awesome_words = ["awesome", "good", "great", "fantastic", "weird", "strange", "patriots", "fenway", "red sox", "celtics", "bruins", "leominster", "peabody", "worcester", "boston", "dorchester", "Cape Cod"]

def main():
    while True:
        wicked = False
        word = input("Give me a word!!")
        if "Cape" in word or "Cod" in word or "cape" in word or "cod" in word:
            print("The Cape")
            continue

        if "Patriots" in word or "patriots" in word:
            print("The Pats")
            continue

        if word in wicked_awesome_words:
            wicked = True

        word.replace("re", "ah").replace("er","ah").replace("ing", "in")

        wordlist = list(word)
        for index,letter in enumerate(wordlist):
            if letter == 'o' or letter == letter == 'O':
                if index == 0:
                    continue
                #if wordlist[index - 1] in consonants:
                #    wordlist[index - 1] = 'a'
                #    wordlist[index] = 'w'
                #    break
                if index == len(word):
                    break
                if wordlist[index+1] in consonants:
                    wordlist.insert(index, 'a')
                    wordlist.insert(index+1, 'w')
                    break

        word = "".join(wordlist)

        #Just get rid of the ahs
        if 'r' in word:
            word.replace('r','')

        if wicked:
            print("Wicked {}".format(word))

        else:
            print(word)


if __name__ == "__main__":
    main()
