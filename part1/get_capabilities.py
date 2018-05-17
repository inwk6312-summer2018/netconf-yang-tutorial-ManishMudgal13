from ncclient import manager
import sys
HOST='10.0.131.202'
PORT=830
USER='cisco1'
PASS='cisco1'
def main():
    with manager.connect(host=HOST,port=PORT,username=USER,
                password=PASS,hostkey_verify=False,
                device_params={'name':'default'},
                look_for_keys=False, allow_agent=False) as m:
    print(***Here are the Remote Devices Capabilities***)
    for capability in m.server_Capabilities:
        print(capability.split('?')[0])

if __name__='__main__':
   sys.exit(main())
