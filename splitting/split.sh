#!/bin/bash

# Fungsi untuk splitting dataset
split_dataset() {
        label="$1"
        input_file="$2"
        output_train_file="$3"
        output_valid_file="$4"

        # Splitting untuk dataset train
        grep "__label__$label" "$input_file" | head -n 200 >> "$output_train_file"

        # Splitting untuk dataset valid
        grep "__label__$label" "$input_file" | tail -n 50 >> "$output_valid_file"
}

split() {
        category=("fraud" "sexual" "harsh" "none")
        for c in "${category[@]}"
        do
                split_dataset "$c" "dataset_1000.txt" "dataset.train.unshuffled" "dataset.valid.unshuffled"
        done
}

get_seeded_random() {
        seed="$1"
        openssl enc -aes-256-ctr -pass pass:"$seed" -nosalt \
                < /dev/zero 2> /dev/null
}

shuffle() {
        shuf dataset.train.unshuffled --random-source=<(get_seeded_random 27) > dataset.train
        shuf dataset.valid.unshuffled --random-source=<(get_seeded_random 27) > dataset.valid
}

clean() {
        rm dataset.train.unshuffled
        rm dataset.valid.unshuffled
}

display_total_row() {
        wc -l dataset.train
        wc -l dataset.valid
}

split
shuffle
clean
display_total_row
