# Data Gathering for Fasttext Model
## Tahapan
- Clone Repository  
```
git clone https://github.com/dummyheaad/data-gathering-fasttext.git
```
- Fetch & Pull
```
git fetch origin
git pull origin master
```
- Labelling
```
python converter.py
```
- Copas hasil labelling dari dataset.txt ke dataset\_accumulated.txt
- Fetch & Pull
```
git fetch origin
git pull origin master
```
- Add ke Staging
```
git add .
atau
git add dataset_accumulated.txt
```
- Commit ke Repo Lokal
```
git commit -m "add dataset"
```
- Push
```
git push origin master
```

