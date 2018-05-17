from ncclient import manager
import sys
import xml.dom.minidom
HOST='10.0.131.205'
PORT=830
USER='cisco'
PASS='cisco'
FILE='get_interface_gigabit3.xml'
def get_configured_interfaces(xml_filter):
    with manager.connect(host=HOST, port=PORT, username=USER,
                password=PASS, hostkey_verify=False,
                device_params={'name':'default'},
                allow_agent=False, look_for_keys=False) as m:
         with open(xml_filter) as f:
              return(m.get_config('running',f.read()))

def main():
    interfaces= get_configured_interfaces(FILE)
    interfaces= xml.dom.minidom.parseString(interfaces.xml)
    interfaces= interfaces.getElementsByTagName("interfaces")
    print(interfaces[0].toprettyxml())

if __name__=='__main__':
  sys.exit(main())
