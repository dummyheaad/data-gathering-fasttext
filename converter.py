import sys
from os import system

text  = []
fasttext_dataset = []

counter_fraud = 0
counter_sexual = 0
counter_harsh = 0
counter_none = 0

def readInput():
    global text
    print('reading input from samples.txt.....')
    with open('samples.txt', 'r') as f:
        text = f.readlines()
    text = [t.strip() for t in text]

def manualLabelling():
    global text
    global fasttext_dataset

    global counter_fraud
    global counter_sexual
    global counter_harsh
    global counter_none

    label_fraud = "__label__fraud "
    label_sexual = "__label__sexual "
    label_harsh = "__label__harsh "
    label_none = "__label__none "

    system('cls')
    print("===MANUAL LABELLING===\n")
    for t in text:
        while True:
            print(f"Text: \"{t}\"")
            print("Choose a label:")
            print("1.) FRAUD")
            print("2.) SEXUAL")
            print("3.) HARSH")
            print("4.) NONE OF THEM")
            answer = int(input())
            if (answer == 1):
                t = label_fraud + t
                print(f"Chosen label: {label_fraud}")
                counter_fraud += 1
                break
            elif (answer == 2):
                t = label_sexual + t
                print(f"Chosen label: {label_sexual}")
                counter_sexual += 1
                break
            elif (answer == 3):
                t = label_harsh + t
                print(f"Chosen label: {label_harsh}")
                counter_harsh += 1
                break
            elif (answer == 4):
                t = label_none + t
                print(f"Chosen label: {label_none}")
                counter_none += 1
                break
            else:
                print("\n")
                print("invalid option...")
                print("\n")
        print("\n")
        fasttext_dataset.append(t)

def writeOutput():
    global fasttext_dataset

    global counter_fraud
    global counter_sexual
    global counter_harsh
    global counter_none

    print("===FINAL RESULT===")
    for t in fasttext_dataset:
        print(t)
    print("==================")
    print(f"Total Fraud: {counter_fraud}")
    print(f"Total Sexual: {counter_sexual}")
    print(f"Total Harsh: {counter_harsh}")
    print(f"Total None: {counter_none}")
    print("==================")
    print("Continue ? (y/n)")
    answer = input()
    if (answer == 'y'):
        with open('dataset.txt', 'w') as output:
            for t in fasttext_dataset:
                output.write(t + '\n')
        print('output saved as dataset.txt')
    elif (answer == 'n'):
        print('operation cancelled...')

def main():
    readInput()
    manualLabelling()
    writeOutput()
    

if __name__ == '__main__':
    main()