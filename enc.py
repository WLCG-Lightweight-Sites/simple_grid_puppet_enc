#!/usr/bin/env python
import socket
import sys
import yaml



if __name__ == "__main__":
    print "---"
    print "classes:"
    hostname = sys.argv[1]
    master_hostname = socket.gethostname()
    if hostname == master_hostname:
        print "    role::master"
    else:
        print "    role::lightweight_component:"
        print "        id: "
        data_source = yaml.load(open('/etc/simple_grid/XXXX/XXXX.yaml', 'r'))
        component_ids = []
        for component in data_source['lightweight_components']:
            if component['deploy']['node'] == hostname:
                print "            - " + str(component['id'])
