from flask import Flask, request, redirect
app = Flask(__name__)

entities = {"ORDINAL", "LOC", "DATE", "LANGUAGE", "NORP","PRODUCT", "GPE"}
from gensim.models import KeyedVectors
import spacy
import random
import requests
        
nlp = spacy.load('en_core_web_sm')    
gmodel=KeyedVectors.load_word2vec_format("GoogleNews-vectors-negative300.bin", binary=True)



def changeQuerry(query):
    doc = nlp(query)
    queryOptions = []

    entitiesToReplace = []
    
    for ent in doc.ents:
        entitiesToReplace.append(ent.text)
        
    for ent in doc:
        # print(ent.pos_)
        if ent.text in entitiesToReplace:
            temp = [ent.text]
            sim = gmodel.most_similar(ent.text)
            for i in sim:
                temp.append(i[0])
            queryOptions.append(temp)
        else:
            queryOptions.append([ent.text])
       

    # print (queryOptions)
    # print (entitiesToReplace)
    
    queries = []
    for i in range(5):
        temp = ""
        for j in queryOptions:
            if len(j) == 1:
                temp += str(j[0]) + " "
            else:
                index =  random.randint(1, len(j)-1)
                temp += str(j[index]) + " "
                
        temp = temp.strip()
        queries.append(temp)
    
    return queries
    


@app.route('/search' , methods=['POST', 'GET'])
def search():
    query  = request.values.get('id').strip()
    backgroundQueries = [ "https://www.google.com/search?q=" + "+".join(i.strip().split(" ")) for i in changeQuerry(query)]
    print ("Making call to related random queries")
    for i in backgroundQueries:
        print(i)
        r = requests.get(i)
    return "https://www.google.com/search?q=" + "+".join(query.split(" "))
    
@app.route('/' , methods=['POST', 'GET'])
def test():
    return "Server is alive"

if __name__ == '__main__':
    app.run(debug=True)



        
    
   