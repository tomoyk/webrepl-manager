import webrepl


def exec(**args):
    print(args)
    repl = webrepl.Webrepl(**args)
    resp = repl.sendcmd(
        "import network; sta_if = network.WLAN(network.STA_IF); sta_if.ifconfig();")
    print(resp.decode("ascii"))


def main():
    configs = [
        {
            'host': '192.168.0.17',
            'port': 8266,
            'password': 'pass'
        },
        {
            'host': '192.168.0.18',
            'port': 8266,
            'password': 'pass'
        }
    ]
    for conf in configs:
        exec(**conf)


if __name__ == "__main__":
    main()
