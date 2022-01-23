import pickle

text = input("Fill in the information about the news you'd want to corroborate: ")
print("You formulated the following inclusion: " + str(text))


def detecting_fake_news(text):    
    load_model = pickle.load(open('final_model.sav', 'rb'))
    prediction = load_model.predict([text])
    probability = load_model.predict_proba([text])
    return (print("The hereunder is the supplied statement: ", prediction[0]), print("The truth probability score is: ", probability[0][1]))

detecting_fake_news(text)