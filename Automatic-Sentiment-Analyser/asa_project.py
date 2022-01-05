def prcyan(skk): print("\033[96m {}\033[00m".format(skk))


def pryellow(skk): print("\033[93m {}\033[00m".format(skk))


def prlightpurple(skk): print("\033[94m {}\033[00m".format(skk))


def prred(skk): print("\033[91m {}\033[00m".format(skk))


def title_screen():
    prcyan("""                        _____                      
                  /\    / ____|  /\                 
                 /  \  | (___   /  \                
                / /\ \  \___ \ / /\ \               
               / ____ \ ____) / ____ \              
              /_/    \_\_____/_/    \_\ """)
    prred("""    /\        | |                      | | (_)     
    /  \  _   _| |_ ___  _ __ ___   __ _| |_ _  ___ 
   / /\ \| | | | __/ _ \| '_ ` _ \ / _` | __| |/ __|
  / ____ \ |_| | || (_) | | | | | | (_| | |_| | (__ 
 /_/____\_\__,_|\__\___/|_| |_| |_|\__,_|\__|_|\___|""")
    prlightpurple(""" / ____|          | | (_)                    | |   
 | (___   ___ _ __ | |_ _ _ __ ___   ___ _ __ | |_  
  \___ \ / _ \ '_ \| __| | '_ ` _ \ / _ \ '_ \| __| 
  ____) |  __/ | | | |_| | | | | | |  __/ | | | |_  
 |_____/ \___|_| |_|\__|_|_| |_| |_|\___|_| |_|\__| """)
    pryellow("""    /\               | |                           
    /  \   _ __   __ _| |_   _ ___  ___ _ __        
   / /\ \ | '_ \ / _` | | | | / __|/ _ \ '__|       
  / ____ \| | | | (_| | | |_| \__ \  __/ |          
 /_/    \_\_| |_|\__,_|_|\__, |___/\___|_|          
                          __/ |                     
                         |___/            """)


def data_from_json():
    import json
    with open('data_words.json') as json_file:
        data = json.load(json_file)
        positive = data['positive']
        negative = data['negative']
        stopwords = data['stopwords']
        reverse = data['reverse']
    return positive, negative, stopwords, reverse


def plot_create(positive, negative, positive_words, negative_words):
    num_positive_words = len(positive_words)
    num_negative_words = len(negative_words)
    if num_positive_words > 0 and num_negative_words > 0:
        import matplotlib.pyplot as plt
        left = [2, 20]
        heights = [int(num_positive_words), int(num_negative_words)]
        plt.subplot(121)
        bar_width = 10
        plt.bar(left, heights, bar_width, color=('g', 'r'))
        plt.title('Word Frequencies')
        plt.xticks([2, 20], ['Positive', 'Negative'])
        plt.minorticks_on()
        plt.grid()

        data = [positive, negative]
        plt.subplot(122)
        slice_labels = ['Positive', 'Negative']
        plt.pie(data, shadow=True,
                autopct='%1.1f%%', labels=slice_labels, colors=('g', 'r'))
        plt.title("Sentiment Values")
        plt.savefig('plot.png')
        plt.show()


def analysis(file_name_input, keyword_q, stopwords_q):
    positive, negative, stopwords, reverse = data_from_json()
    file_name = str(file_name_input) + '.txt'
    try:
        keyword = ""
        data = []
        if keyword_q:
            keyword = input("Please write your keyword: ")
            data_start = keyword_data(file_name_input, keyword)
        else:
            file = open(file_name, 'r')
            text = file.read()
            text = text.lower()
            data_start = text.split()
            data_core = [word.strip('.,!;()?:[]\"') for word in data_start]
            file.close()
            data_start = data_core

        if stopwords_q:
            data = data_start
        else:
            for word in data_start:
                if word not in stopwords:
                    data.append(word)
        val_sentiment = 0
        val_positive = 0
        val_negative = 0
        positive_words = []
        negative_words = []
        index = 0
        while index < len(data):
            if str(data[index]).lower() in positive:
                if data[index - 1] in reverse:
                    val_sentiment -= 1
                    val_negative += 1
                    index += 1
                elif data[index - 1] == 'very':
                    val_sentiment += 2
                    val_positive += 2
                    positive_words.append(data[index])
                    index += 1
                else:
                    val_sentiment += 1
                    val_positive += 1
                    positive_words.append(data[index])
                    index += 1
            elif str(data[index]).lower() in negative:
                if data[index - 1] in reverse:
                    val_sentiment += 1
                    val_positive += 1
                    index += 1
                elif data[index - 1] == 'very':
                    val_sentiment -= 2
                    val_positive -= 2
                    positive_words.append(data[index])
                    index += 1
                else:
                    val_sentiment -= 1
                    val_negative += 1
                    negative_words.append(data[index])
                    index += 1
            else:
                index += 1
        print(verdict(val_sentiment, data))
        words_frequencies(positive_words, negative_words)
        plot_create(val_positive, val_negative, positive_words, negative_words)
        save_analysis(file_name_input, verdict(val_sentiment, data), val_positive, val_negative, val_sentiment, keyword_q, keyword)
    except IOError:
        print("Error while trying to open", file_name)


def verdict(val_sentiment, data):
    data_length = len(data)
    if data_length > 1000:
        if 20 > val_sentiment > 0:
            return "\nThe sentiment value of the text is slightly positive. (" + str(val_sentiment) + ")"
        elif -20 < val_sentiment < 0:
            return "\nThe sentiment value of the text is slightly negative. (" + str(val_sentiment) + ")"
        elif 20 < val_sentiment <= 70:
            return "\nThe sentiment value of the text is positive. (" + str(val_sentiment) + ")"
        elif -20 > val_sentiment >= -70:
            return "\nThe sentiment value of the text is negative. (" + str(val_sentiment) + ")"
        elif val_sentiment > 70:
            return "\nThe sentiment value of the text is highly positive. (" + str(val_sentiment) + ")"
        elif val_sentiment < -70:
            return "\nThe sentiment value of the text is highly negative. (" + str(val_sentiment) + ")"
    if data_length < 1000:
        if 5 > val_sentiment > 0:
            return "\nThe sentiment value of the text is slightly positive. (" + str(val_sentiment) + ")"
        elif -5 < val_sentiment < 0:
            return "\nThe sentiment value of the text is slightly negative. (" + str(val_sentiment) + ")"
        elif 5 < val_sentiment <= 10:
            return "\nThe sentiment value of the text is positive. (" + str(val_sentiment) + ")"
        elif -5 > val_sentiment >= -10:
            return "\nThe sentiment value of the text is negative. (" + str(val_sentiment) + ")"
        elif val_sentiment > 10:
            return "\nThe sentiment value of the text is highly positive. (" + str(val_sentiment) + ")"
        elif val_sentiment < -10:
            return "\nThe sentiment value of the text is highly negative. (" + str(val_sentiment) + ")"


def create_sentences(file_name_input):
    file_name = str(file_name_input) + '.txt'
    try:
        import re
        file = open(file_name, 'r')
        text = file.read()
        sent = text.replace('\n', ' ')
        sent = sent.strip(';():[]\"')
        sentences = re.split('[.?!]', sent)
        file.close()
        return sentences
    except IOError:
        print("Error while trying to open", file_name)


def search_keyword(sentences, keyword):
    sentences_with_keyword = []
    for sent in sentences:
        if sent.find(str(keyword)) != -1:
            sentences_with_keyword.append(sent)
    if not sentences_with_keyword:
        print("Your keyword is not present in the text!")
    return sentences_with_keyword


def sentences_into_words(sentences_and_keyword):
    sentences = sentences_and_keyword
    word_list = [word for line in sentences for word in line.split()]
    return word_list


def words_frequencies(positive_words, negative_words):
    from collections import Counter
    occurrence_count_positive = Counter(positive_words)
    occurrence_count_negative = Counter(negative_words)
    if occurrence_count_positive:
        most_frequent_positive = occurrence_count_positive.most_common(1)[0][0]
        print("The most frequent positive word:", most_frequent_positive)
    if occurrence_count_negative:
        most_frequent_negative = occurrence_count_negative.most_common(1)[0][0]
        print("The most frequent negative word:", most_frequent_negative, '\n')


def keyword_data(file_name_input, keyword):
    sent = create_sentences(file_name_input)
    sent_with_keyword = search_keyword(sent, keyword)
    keyword_list = sentences_into_words(sent_with_keyword)
    return keyword_list


def another_text():
    question = input("Do you want to analyse another text? (y/n)\n").lower()
    if question == 'y' or question == 'yes' or question == 'yup':
        program()
    elif question == 'n' or question == 'no' or question == 'nope':
        print("\nThank you!")
        print("Exiting...")
        exit()
    else:
        print("I don't understand.\n")
        another_text()


def stopwords_question():
    question = input("Do you want to include stopwords? (y/n)\n")
    if question == 'y' or question == 'yes' or question == 'yup':
        return True
    elif question == 'n' or question == 'no' or question == 'nope':
        return False
    else:
        print("I don't understand.\n")
        stopwords_question()


def keyword_question():
    question = input("Do you want to use a keyword? (y/n)\n")
    if question == 'y' or question == 'yes' or question == 'yup':
        return True
    elif question == 'n' or question == 'no' or question == 'nope':
        return False
    else:
        print("I don't understand.\n")
        keyword_question()


def save_analysis(file_name, verdict_output, val_positive, val_negative, val_sentiment, keyword_q, keyword):
    file_name_output = str(file_name) + '.txt'
    try:
        file = open("analysis.txt", 'w')
        file.write("File name: " + str(file_name_output) + '\n'
                   + str(verdict_output) + '\n' +
                   "Positive value: " + str(val_positive) + '\n' +
                   "Negative value: " + str(val_negative) + '\n' +
                   "Sentiment value: " + str(val_sentiment))
        file.close()
        if keyword_q:
            file = open("analysis.txt", 'a')
            file.write('\nKeyword: ' + str(keyword))
            file.close()
    except IOError:
        print("Error while trying to open", file_name_output)


def program():
    file_name_input = input("\nPlease input the name of your txt file here (omit the .txt extension): ")
    keyword_q = keyword_question()
    stopwords_q = stopwords_question()
    analysis(file_name_input, keyword_q, stopwords_q)
    another_text()


def main():
    title_screen()
    program()


if __name__ == '__main__':
    main()
