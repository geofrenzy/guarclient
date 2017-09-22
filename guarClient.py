import base64
import json
from string import Template

import dns.resolver


def lookupuas(droneid):
    dronehost = droneid + '.uas.directory'
    txtanswers = dns.resolver.query(dronehost, 'TXT')
    rdapanswers = dns.resolver.query('_rdap._tcp.' + dronehost, 'URI')
    placeanswers = dns.resolver.query('_http._tcp.' + dronehost, 'URI')
    for rdata in txtanswers:
        for string in rdata.strings:
            decoded_string = base64.b64decode(string)
            dronedict = json.loads(decoded_string)
    for rdata in rdapanswers:
        rdapstring = rdata.target.decode()
        dronedict["rdapstring"] = rdapstring
    for rdata in placeanswers:
        placestring = rdata.target.decode()
        dronedict["placestring"] = placestring
    dronedict["fullid"] = droneid

    outstringtemplate = """
    Rdap referal = $rdapstring
    .place fence referal = $placestring
    Drone $fullid is owned by $droneowner for $dronepurpose purposes
    Drone $fullid has a $dronetype configuration
    """
    outstring = Template(outstringtemplate)
    resultstring = outstring.safe_substitute(dronedict)
    return resultstring


if __name__ == "__main__":
    # execute only if run as a script
    droneid = input("Drone ID: ")
    result = lookupuas(droneid)
    print(result)
