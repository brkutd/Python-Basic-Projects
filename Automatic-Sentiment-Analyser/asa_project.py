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
    import matplotlib.pyplot as plt
    left = [2, 20]
    heights = [num_positive_words, num_negative_words]
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

    plt.show()


def analysis_no_stopwords(file_name_input):
    positive, negative, stopwords, reverse = data_from_json()
    file_name = str(file_name_input) + '.txt'
    try:
        file = open(file_name, 'r')
        text = file.read()
        text = text.lower()
        data = text.split()
        data = [word.strip('.,!;()?:[]\"') for word in data]
        file.close()
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
                else:
                    val_sentiment -= 1
                    val_negative += 1
                    negative_words.append(data[index])
                    index += 1
            else:
                index += 1
        print(len(data))
        print("The sentiment value of the text is", val_sentiment, '\n')
        plot_create(val_positive, val_negative, positive_words, negative_words)
    except IOError:
        print("Error while trying to open", file_name)


def analysis_with_stopwords(file_name_input):
    positive, negative, stopwords, reverse = data_from_json()
    file_name = str(file_name_input) + '.txt'
    try:
        file = open(file_name, 'r')
        text = file.read()
        text = text.lower()
        data = text.split()
        data = [word.strip('.,!;()?:[]\"') for word in data]
        file.close()
        val_sentiment = 0
        val_positive = 0
        val_negative = 0
        positive_words = []
        negative_words = []
        index = 0
        while index < len(data):
            if data[index] in positive:
                if data[index - 1] in reverse:
                    val_sentiment -= 1
                    val_negative += 1
                    index += 1
                else:
                    val_sentiment += 1
                    val_positive += 1
                    positive_words.append(data[index])
                    index += 1
            elif data[index] in negative:
                if data[index - 1] in reverse:
                    val_sentiment += 1
                    val_positive += 1
                    index += 1
                else:
                    val_sentiment -= 1
                    val_negative += 1
                    negative_words.append(data[index])
                    index += 1
            else:
                index += 1
        print(len(data))
        print("The sentiment value of the text is", val_sentiment, '\n')
        plot_create(val_positive, val_negative, positive_words, negative_words)
    except IOError:
        print("Error while trying to open", file_name)


#def verdict(val_sentiment, data):
#    data_length = len(data)


def another_text():
    question = input("Do you want to analyse another text? (y/n)\n").lower()
    if question == 'y' or question == 'yes' or question == 'yup':
        main_continue()
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


def main_start():
    title_screen()
    file_name_input = input("Please input the name of your txt file here (omit the .txt extension): ")
    if stopwords_question():
        analysis_with_stopwords(file_name_input)
    else:
        analysis_no_stopwords(file_name_input)
    another_text()


def main_continue():
    file_name_input = input("Please input the name of your txt file here (omit the .txt extension): ")
    if stopwords_question():
        analysis_with_stopwords(file_name_input)
    else:
        analysis_no_stopwords(file_name_input)
    another_text()

main_start()
