import time
import requests
import json

def loadSettings():
    try:
        configFile = open("config.json", "r")
        global settings
        settings = json.load(configFile)
    except FileNotFoundError:
        return False
    return True

def setSleep(mode):
    if mode == "ni":
        wait = settings["wait"]
    else:
        wait = input("> Time between requests in seconds: ")
    try:
        return int(wait)
    except ValueError:
        print("Only integers allowed.")
        setSleep() if mode == "i" else exit(0)

def loadFile(mode):
    try:
        if mode == "ni":
            file = open(settings["file"], "r")
        else:
            file = open(input("> Url file (one address per line): "), "r")

    except FileNotFoundError:
        print("File not found.")
        loadFile() if mode == "i" else exit(0)
    return file

def getResponse(url):
    print("\tRequesting - %s" % url)
    response = requests.get(url[:-1])
    if response.ok:
        print(str(response) + "\n")
        jData = json.loads(response.content)
        print("{0} properties received.".format(len(jData)))
        print("\n")
        print(json.dumps(jData, indent=4, sort_keys=True))
        print("\n")
    else:
        response.raise_for_status()

def start():
    if loadSettings():
        if settings["enabled"] == "yes":
            print("Running in non-interactive mode...\n")
            wait = setSleep("ni")
            file = loadFile("ni")
        else:
            wait = setSleep("i")
            file = loadFile("i")

    def iterate(file):
        for line in file:
            getResponse(line)
            time.sleep(wait)

    iterate(file)
    print("Ended.")

start()
