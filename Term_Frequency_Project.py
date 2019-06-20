stop = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', 'should', 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', 'couldn', 'didn', 'doesn', 'hadn', 'hasn', 'haven', 'isn', 'ma', 'mightn', 'mustn', 'needn', 'shan', 'shouldn', 'wasn', 'weren', 'won', 'wouldn']

files = [
    open("cv000_tok-9611.txt"),
    open("cv000_tok-11609.txt"),
    open("cv001_tok-10180.txt"),
    open("cv001_tok-19324.txt"),
    open("cv002_tok-3321.txt"),
    open("cv002_tok-12931.txt"),
    open("cv003_tok-8338.txt"),
    open("cv003_tok-13044.txt"),
    open("cv004_tok-25944.txt"),
    open("cv004_tok-29856.txt"),
    open("cv005_tok-24602.txt"),
    open("cv005_tok-26110.txt"),
    open("cv006_tok-29539.txt"),
    open("cv007_tok-11669.txt"),
]

tokens = [
    files[0].readlines(),
    files[1].readlines(),
    files[2].readlines(),
    files[3].readlines(),
    files[4].readlines(),
    files[5].readlines(),
    files[6].readlines(),
    files[7].readlines(),
    files[8].readlines(),
    files[9].readlines(),
    files[10].readlines(),
    files[11].readlines(),
    files[12].readlines(),
    files[13].readlines(),
]

raw = []

for line in tokens[0]:
    split = line.split()
    if split[1] != ' ' :
        word = [w for w in split if not w in stop]
        raw.append(word)

Dictionary = []
Documents = []
Complete = []

for document in raw:
    Documents.append(document[0])
    documentWordCount = {}
    for word in document[1: ]
        Dictionary.append(word)
        if word not in documentWordCount
            documentWordCount[word] = 1
        else
            documentWordCount[word] += 1
    Complete.append({document[0]: documentWordCount})

Unique = list(set(Dictionary))
Unique = [x for x in Unique if not any(c.isdigit() for c in x)]

row = {}
for word in Unique:
    for document in Dictionary:
        x = document.values()
        if word not in row:
            row[word] = []
        if word in x[0].keys():
            row[word].append(x[0][word])
        else:
            row[word].append(0)

