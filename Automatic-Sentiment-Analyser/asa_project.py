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


def clearing_no_stopwords(data_core):
    positive, negative, stopwords, reverse = data_from_json()
    data_with_stopwords = []
    for word in data_core:
        data_with_stopwords.append(
            word.replace(',', '').replace('!', '').replace('.', '')
                .replace(';', '').replace(':', '').replace('?', '')
        )
    data = []
    for word in data_with_stopwords:
        if word not in stopwords:
            data.append(word)
    return data


def clearing_with_stopwords(data_core):
    data_with_stopwords = []
    for word in data_core:
        data_with_stopwords.append(
            word.replace(',', '').replace('!', '').replace('.', '')
                .replace(';', '').replace(':', '').replace('?', '')
        )
    return data_with_stopwords


def plot_create(positive, negative):
    import matplotlib.pyplot as plt
    data = [positive, negative]
    slice_labels = ['Positive', 'Negative']
    plt.pie(data, shadow=True,
            autopct='%1.1f%%', labels=slice_labels)

    plt.title("Sentiment Values")

    plt.show()


def analysis_no_stopwords(data_core):
    positive, negative, stopwords, reverse = data_from_json()
    data = clearing_no_stopwords(data_core)
    val_sentiment = 0
    val_positive = 0
    val_negative = 0
    val_neutral = 0
    index = 0
    while index < len(data):
        if str(data[index]).lower() in positive:
            if data[index - 1] in reverse:
                val_sentiment -= 1
                val_negative += 1
                index += 1
            else:
                val_sentiment += 1
                val_positive += 1
                index += 1
        elif str(data[index]).lower() in negative:
            if data[index - 1] in reverse:
                val_sentiment += 1
                val_positive += 1
                index += 1
            else:
                val_sentiment -= 1
                val_negative += 1
                index += 1
        else:
            val_neutral += 1
            index += 1
        index += 1
    print("The sentiment value of the text is", val_sentiment, '\n')
    plot_create(val_positive, val_negative)
    return val_sentiment


def analysis_with_stopwords(data_core):
    positive, negative, stopwords, reverse = data_from_json()
    data = clearing_with_stopwords(data_core)
    val_sentiment = 0
    val_positive = 0
    val_negative = 0
    val_neutral = 0
    index = 0
    while index < len(data):
        if str(data[index]).lower() in positive:
            if data[index - 1] in reverse:
                val_sentiment -= 1
                val_negative += 1
                index += 1
            else:
                val_sentiment += 1
                val_positive += 1
                index += 1
        elif str(data[index]).lower() in negative:
            if data[index - 1] in reverse:
                val_sentiment += 1
                val_positive += 1
                index += 1
            else:
                val_sentiment -= 1
                val_negative += 1
                index += 1
        else:
            val_neutral += 1
            index += 1
        index += 1
    print("The sentiment value of the text is", val_sentiment, '\n')
    plot_create(val_positive, val_negative)
    return val_sentiment


def another_text(data_core):
    question = input("Do you want to analyse another text? (y/n)\n").lower()
    if question == 'y' or question == 'yes' or question == 'yup':
        main_continue()
    elif question == 'n' or question == 'no' or question == 'nope':
        print("\nThank you!")
        print("Exiting...")
        exit()
    else:
        print("I don't understand.\n")
        another_text(data_core)


def stopwords_question():
    question = input("Do you want to include stopwords? (y/n)\n")
    if question == 'y' or question == 'yes' or question == 'yup':
        return True
    elif question == 'n' or question == 'no' or question == 'nope':
        return False
    else:
        print("I don't understand.\n")
        stopwords_question()


def main_start():
    title_screen()
    data_core = input("Please input the text here: ").split()
    if stopwords_question():
        analysis_with_stopwords(data_core)
    else:
        analysis_no_stopwords(data_core)
    another_text(data_core)


def main_continue():
    data_core = input("Please input the text here: ").split()
    if stopwords_question():
        analysis_with_stopwords(data_core)
    else:
        analysis_no_stopwords(data_core)
    another_text(data_core)

main_start()
