import argparse

from src.chatbot.engine import Chatbot

ASCII_USER_PROMPT = '⛇ '
ASCII_CHATBOT_PROMPT = '☣ '

def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def main():
    global args
    chatbot = Chatbot(args.reset) #the saves a state to resume from
    starter_prompt = chatbot.launch()
    print(ASCII_CHATBOT_PROMPT + starter_prompt)
    while (user_prompt := input(ASCII_USER_PROMPT)) != 'exit':
        response = chatbot.query(user_prompt)
        print(ASCII_CHATBOT_PROMPT + response )
    chatbot.exit_routine()
    return 

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Chatbot entrypoint")
    parser.add_argument('--reset', type=str2bool, nargs='?', const=True, default=False, help='Default=False. If flag is given, resets the chatbot agent to its initial state. Else it continues from where it was left off.')
    args = parser.parse_args()
    main()
