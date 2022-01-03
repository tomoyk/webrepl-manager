import webrepl

config = [
    {
        'host': '192.168.0.7',
        'port': 8266,
        'password': 'pass'
    }
]


def main():
    repl = webrepl.Webrepl(
        **(config[0]))
    resp = repl.sendcmd(
        "import network; sta_if = network.WLAN(network.STA_IF); sta_if.ifconfig();")
    print(resp.decode("ascii"))


if __name__ == "__main__":
    main()
