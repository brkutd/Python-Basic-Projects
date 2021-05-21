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
    return positive, negative, stopwords


def clearing(data_core):
    data = []
    for word in data_core:
        data.append(
            word.replace(',', '').replace('!', '').replace('.', '')
                .replace(';', '').replace(':', '').replace('?', '')
        )
    return data


def analysis(data_core):
    positive, negative, stopwords = data_from_json()
    data = clearing(data_core)
    val_sentiment = 0
    val_neutral = 0
    index = 0
    while index < len(data):
        if str(data[index]).lower() in positive:
            if data[index - 1] == "not" or data[index - 1] == "don't" or data[index - 1] == "doesn't" or data[index - 1] == "dont" or data[index - 1] == "doesnt":
                val_sentiment -= 1
                index += 1
            else:
                val_sentiment += 1
                index += 1
        elif str(data[index]).lower() in negative:
            if data[index - 1] == "not" or data[index - 1] == "don't" or data[index - 1] == "doesn't" or data[index - 1] == "dont" or data[index - 1] == "doesnt":
                val_sentiment += 1
                index += 1
            else:
                val_sentiment -= 1
                index += 1
        else:
            val_neutral += 1
            index += 1
    print("The sentiment value of the text is", val_sentiment, '\n')


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
