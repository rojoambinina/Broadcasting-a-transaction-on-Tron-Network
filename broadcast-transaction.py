from tronpy import Tron
from tronpy.providers import HTTPProvider
from tronpy.keys import PrivateKey
import time
from colorama import Back, Fore, Style, deinit, init
from termcolor import colored

# connect to the Tron blockchain
#client = Tron(network='nile')
#client = Tron(HTTPProvider(api_key=" YOUR API HERE "))  #Use mainnet(trongrid) with a single api_key
client = Tron()

while True:
    init()
    sending = 0
    tron_address = "TGEbBaHpoVXbLzbo1heSENn2GjThAFgT2n"
    balance = client.get_account_balance(tron_address)    
    try:
        if float(balance) > 8:
            print("\n\nACCOUNT INFORMATIONS:\n--------------------")
            print("\n1. Your TRX Address: \t" + tron_address + "\n\n2. Balance :\t\t" + str(balance) + "\n")          
            priv_key = PrivateKey(bytes.fromhex("8386338e8b18c8f2ec2089fcc8991b396afa9f0ad668555461d8736bd4d23c08"))
            txn = (
                client.trx.transfer("TGEbBaHpoVXbLzbo1heSENn2GjThAFgT2n", "TVymPuBKEnfmkz86c32pvrs9zFRkHGTMYA", 20_000000)
                .memo("test memo")
                .build()
                .sign(priv_key)
            )
            print("\n\nTRANSACTIONS DETAILS:\n--------------------\n\n" + txn.txid)
            print(txn.broadcast().wait()) 
            print(colored("\n\t\t TRX HAS BEEN SENT ..."),"yellow")
            balance_finale = client.get_account_balance(tron_address)
            print("\n3. New Finale Balance:\t" + str(balance_finale))
            time.sleep(5)
            sending = sending + 1
        else:
            print("\n\t\t" + tron_address)
            balance_finale = client.get_account_balance(tron_address)
            print(colored("\t\tInsufficient TRX Balance:   " + str(float(balance_finale)),'yellow'))
            time.sleep(5) 
            deinit()
            sending = sending + 1

    except:
        print("\n\t An error occurred, please wait...\n")
        time.sleep(1)
        sending = sending + 1