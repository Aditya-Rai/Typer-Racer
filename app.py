import csv
import numpy as np
import pandas as pd
from flask import Flask, request, render_template
from  essential_generators import DocumentGenerator


app = Flask(__name__)
para = ""

def generate_para():
    para = ""
    for i in range(2):
        main = DocumentGenerator()
        current_sentence = main.sentence()
        para = para + current_sentence + " "
    return para


def start_game(generated_para,user):
    para_len = len(generated_para) - 1
    list_para = para.split()
    list_user = user.split()
    matched_written_chars = 0
    if list_user == list_para:
        correct_words = len(list_para)
        matched_written_chars = para_len
    else:
        matched_words = set(list_para) & set(list_user)
        matched_written_chars = len(" ".join(matched_words))
        correct_words = len(matched_words)
        print(" ".join(matched_words))
    print(correct_words, generated_para)
    return correct_words,matched_written_chars

@app.route('/')
def index():
    global para

    para = generate_para()
    return render_template("index.html", para = para, typing_speed = "0 WPM" ,accuracy = "0%")


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        
        name = request.form['name']
        email = request.form['email']
        user_input = request.form['user_input']
        typing_time = 60 - int(request.form['countdown'])
        total_chars_written = int(request.form['total_count'])

        if len(name) == 0:
            name = "Na"
        if len(email) == 0:
            email = "NA"

        correct_words, total_matched_chars = start_game(para, user_input.strip())
        
        typing_speed = int((correct_words / typing_time) * 60)
        accuracy = int((total_matched_chars / total_chars_written) * 100)


        # print(correct_words)
        with open('data.csv', mode='a') as file:
            writer = csv.writer(file)
            writer.writerow([name, email,int(typing_speed) ,int(accuracy)])

        df = pd.read_csv("data.csv", names = ["Name", "Email", "WPM", "Accuracy"])

        sorted_df = df.sort_values(by=['WPM'], ascending=False)
        sorted_df = sorted_df.reset_index()
        sorted_df = sorted_df.drop(["index"], axis = 1)
        try:
            current_player_position = sorted_df[sorted_df["Email"] == email].index[0] + 1
        except:
            current_player_position = "NA"
            
        sorted_df.index = np.arange(1, len(sorted_df) + 1)
        sorted_df.head(10).to_csv("static/top_players.csv")
        
        return render_template("submit.html", typing_speed = str(typing_speed) + " WPM", accuracy = str(accuracy) + "%", position = current_player_position)


if __name__ == '__main__':
    app.run(debug=True)
