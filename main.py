import discord, itertools, httpx, random, string, time, json
from datetime import datetime
client = discord.Client()

def rc(x):
    return "".join(random.choice(string.digits) for i in range(x))

def nonce():
        date = datetime.now()
        unixts = time.mktime(date.timetuple())
        return str((int(unixts)*1000-1420070400000)*4194304)


class Listener():
    def __init__(self) -> None:
        print("Tool made by cChimney\nListening for reactions...")
        client.run(listener)
        
    @client.event
    async def on_raw_reaction_add(reaction):
        try:
            channels = open('./data/reactionChannels.txt').read().splitlines()
            if f"{reaction.channel_id}:{reaction.message_id}" in channels:
                
                completed = open('./data/completed.txt').read().splitlines()
                failed =  open('./data/failed.txt').read().splitlines()
                done = failed+completed
                if str(reaction.user_id) in done:
                    print(f"New reaction in {reaction.channel_id}, user is already DMed")
                    pass
                else:
                    print(f"New reaction in {reaction.channel_id}, DMing user.")
                    sendMsg(user_id=reaction.user_id)
            else:
                print(reaction.channel_id)
        except Exception as err:
            print(err)

class sendMsg():
    def __init__(self, user_id):
        self.openChannel(user_id)
        
    
    def openChannel(self, user_id):
        
        for i in range(3): #THREE RETRIES
            self.token = next(tokens)
            with httpx.Client(cookies={"locale": "en-US"}, headers={"Accept": "*/*", "Accept-Language": "en-US", "Connection": "keep-alive", "Content-Type": "application/json", "DNT": "1", "Host": "discord.com", "Referer": "https://discord.com/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "TE": "trailers", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0", "X-Track": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2Ojk0LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTQuMCIsImJyb3dzZXJfdmVyc2lvbiI6Ijk0LjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTk5OSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="}, proxies=None, timeout=30) as client:
                client.headers["X-Super-Properties"] = "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2Ojk0LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTQuMCIsImJyb3dzZXJfdmVyc2lvbiI6Ijk0LjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTA2OTA1LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="
                client.headers["Authorization"] = self.token
                client.headers["cookie"] = f'__dcfduid={rc(43)}; __sdcfduid={rc(96)}; __stripe_mid={rc(18)}-{rc(4)}-{rc(4)}-{rc(4)}-{rc(18)}; locale=en-GB; __cfruid={rc(40)}-{rc(10)}'
                
                openChannel = client.post('https://discord.com/api/v10/users/@me/channels', json={"recipient_id": user_id})
                id = openChannel.json().get('id')
                if id != None:
                    username = openChannel.get('recipients')[0].get('username')
                    x = self.sendMsg(id, user_id, client, username)
                    if x == True:
                        with open('./data/completed.txt', 'a') as f:
                            f.write(f"{user_id}\n")
                        break
                    elif x == False:
                        pass
                    elif x == "dms_disabled":
                        with open('./data/failed.txt', 'a') as f:
                            f.write(f"{user_id}\n")
                        break
                    elif x == "Ratelimited":
                        for i in range(5):
                            time.sleep(120)
                            x = self.sendMsg(id, user_id, client)
                            if x == True:
                                with open('./data/completed.txt', 'a') as f:
                                    f.write(f"{user_id}\n")
                            elif x == False: break
                                
                            elif x == "dms_disabled":
                                with open('./data/failed.txt', 'a') as f:
                                    f.write(f"{user_id}\n")
                                break
                            else: pass
                        if x == True:
                            break
                        if x == "dms_disabled":
                            break
                else:
                    print(f'locked TOKEN > {self.token}')
                    print(openChannel.json())
                    pass
    
    def sendMsg(self, id, user_id, client, username):
        message = msg.format(user=f"<@{user_id}>")
        sendMsg = client.post(f'https://discord.com/api/v10/channels/{id}/messages', json={"content": message, "nonce": nonce(), "tts":False})
        if sendMsg.status_code == 200:
            
            print(f"Successfully sent message to {username} {user_id}")
            return True
        elif sendMsg.status_code == 401:
            print("Invalid account")
            return False
        elif sendMsg.status_code == 403 and sendMsg.json()["code"] == 40003:
            print("Ratelimited")
            return "Ratelimited"
        elif sendMsg.status_code == 403 and sendMsg.json()["code"] == 50007:
            print("User has direct messages disabled")
            return "dms_disabled"
        elif sendMsg.status_code == 403 and sendMsg.json()["code"] == 40002:
            print("Locked")
            return False
        elif sendMsg.status_code == 429:
            print("Ratelimited, waiting")
            return "Ratelimited"
        else:
            print(sendMsg.json())
            return False

try:
    tokens = itertools.cycle(open('./data/tokens.txt').read().splitlines())
    with open('config.json', encoding='utf-8') as config:
        config = json.load(config)
        msg = config['message']
        listener = config['listener_token']
    Listener()
except Exception as err:
    print(err)
