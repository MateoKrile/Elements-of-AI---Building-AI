portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
 

def permutations(route, ports):
    if len(ports)==0:
        print(' '.join([portnames[i] for i in route]))  
    else:
        for i, port in enumerate(ports):
            route.append(port)
            remaining_ports = [x for x in ports if x!=port]
            permutations(route, remaining_ports)
            route.remove(port)    
        

permutations([0], list(range(1, len(portnames))))

'''
Their solution

def permutations(route, ports):
    if len(ports) < 1:
        print(' '.join([portnames[i] for i in route]))
    else:
        for i in range(len(ports)):
            permutations(route+[ports[i]], ports[:i]+ports[i+1:])
 
permutations([0], list(range(1, len(portnames))))

'''