def main():
    print(f"Opening dataset_accumulated.txt...")
    with open('dataset_accumulated.txt', 'r') as f:
        text = f.readlines()
    text = [t.strip() for t in text]

    label_fraud = "__label__fraud"
    label_sexual = "__label__sexual"
    label_harsh = "__label__harsh"
    label_none = "__label__none"

    counter_fraud = 0
    counter_sexual = 0
    counter_harsh = 0
    counter_none = 0
    for t in text:
        if label_fraud in t:
            counter_fraud += 1
        if label_sexual in t:
            counter_sexual += 1
        if label_harsh in t:
            counter_harsh += 1
        if label_none in t:
            counter_none += 1
    print(f"Summary:")
    print(f"total fraud: {counter_fraud}")
    print(f"total sexual: {counter_sexual}")
    print(f"total harsh: {counter_harsh}")
    print(f"total none: {counter_none}")
    print(f"total: {len(text)}")

if __name__ == '__main__':
    main()
