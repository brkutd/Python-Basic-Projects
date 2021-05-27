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


def clearing(data_core):
    data = []
    for word in data_core:
        data.append(
            word.replace(',', '').replace('!', '').replace('.', '')
                .replace(';', '').replace(':', '').replace('?', '')
        )
    return data


def plot_create(positive, negative):
    import matplotlib.pyplot as plt
    data = [positive, negative]
    slice_labels = ['Positive', 'Negative']
    plt.pie(data, shadow=True,
            autopct='%1.1f%%', labels=slice_labels)

    plt.title("Sentiment Values")

    plt.show()


def analysis(data_core):
    positive, negative, stopwords, reverse = data_from_json()
    data = clearing(data_core)
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
    print("The sentiment value of the text is", val_sentiment, '\n')
    plot_create(val_positive, val_negative)
    return val_sentiment


def another_text(data_core):
    question = input("Do you want to analyse another text? (y/n)\n").lower()
    if question == 'y' or question == 'yes' or question == 'yup':
        data_core = input("Please input the text here: ").split()
        analysis(data_core)
        another_text(data_core)
    elif question == 'n' or question == 'no' or question == 'nope':
        print("\nThank you!")
        print("Exiting...")
        exit()
    else:
        print("I don't understand.\n")
        another_text(data_core)


def main():
    title_screen()
    data_core = input("Please input the text here: ").split()
    analysis(data_core)
    another_text(data_core)


main()
