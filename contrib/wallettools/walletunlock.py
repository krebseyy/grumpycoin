from jsonrpc import ServiceProxy
access = ServiceProxy("http://127.0.0.1:3432")
pwd = raw_input("Enter wallet passphrase: ")
access.walletpassphrase(pwd, 60)
