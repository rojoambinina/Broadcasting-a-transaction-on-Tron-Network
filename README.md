# Broadcasting a transaction on Tron Network

For several months, I have seen people posting their passphrases or private keys of their TRX addresses with balances of several thousand USDT on social networks to trick people and harvest TRX. They pretend to have no money left, and encourage you to send some TRX.

![Kaita Ma](https://user-images.githubusercontent.com/89576432/186005976-2b784944-b04d-46e9-bc4b-2a0dc355f991.png)

And many people have been deceived by these scammers from what I have seen in the TRX trap address transaction because if you send TRX to the published address (e.g. TGEbBaHpoVXbLzbo1heSENn2GjThAFgT2n), the balance will be immediately transferred to another TRX address. And you will never have enough TRX fees to transfer those thousands of USDT already promised. At the same time, the address is protected in Multisig, a second TRX address is needed to approve a transfer or withdrawal.

To put into practice everything I said above, I coded a small script that instantly broadcasts transactions on Trons networks. 
I leave the private key "**8386338e8b18c8f2ec2089fcc8991b396afa9f0ad668555461d8736bd4d23c08**" and the TRX address "**TGEbBaHpoVXbLzbo1heSENn2GjThAFgT2n**" within the code, so that you can test on Tron Mainnet or Tron Nile networks.

# Usage
Open you terminal and type the command below to install Tronpy and Colorama modules.

## pip install tronpy

You go to the folder where the python file is, and type the command below to launch the script.

## py broadcast-transaction.py
