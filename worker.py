from xmlrpc.server import SimpleXMLRPCServer
import sys
import json

# Storage of data
data_table = {}


def load_data(group):
    global data_table
    # load data based which portion it handles (am or nz) (loaded as dictionary)
    if group == 'am':
        data_table=json.load(open('data-am.json'))
    elif group == 'nz':
        data_table=json.load(open('data-nz.json'))


def getbyname(name):
    # if name is found, return the person's record in list
    results = []
    for person in data_table:
        if data_table[person]['name'] == name:
            # returns the dictionary of the whole matching record except for record_id
            results.append({k: v for k, v in data_table[person].items() if k != "record_id"})
    # if name is not found, return error message and assign error to True, otherwise return the list of results
    return {
        'error': False if results else True,
        'result': results if results else ['name not found']
        }
    

def getbylocation(location):
    # if location is found, return the person's record in list
    results = []
    for person in data_table:
        if data_table[person]['location'] == location:
            # returns the dictionary of the whole matching record except for record_id
            results.append({k: v for k, v in data_table[person].items() if k != "record_id"})
    # if name is not found, return error message and assign error to True, otherwise return the list of results
    return {
        'error': False if results else True,
        'result': results if results else ['location not found']
    }

def getbyyear(location, year):
    # if location and year is found, return the person's record in list
    results = []
    for person in data_table:
        if data_table[person]['location'] == location and data_table[person]['year'] == year:
            # returns the dictionary of the whole matching record except for record_id
            results.append({k: v for k, v in data_table[person].items() if k != "record_id"})
    # if location and year is not found, return error message and assign error to True, otherwise return the list of results
    return {
        'error': False if results else True,
        'result': results if results else ['year with associated location not found']
    }

def main():
    if len(sys.argv) < 3:
        print('Usage: worker.py <port> <group: am or nz>')
        sys.exit(0)

    # 23001 or 23002 port used
    port = int(sys.argv[1])
    # am or nz
    group = sys.argv[2]
    server = SimpleXMLRPCServer(("localhost", port))
    print(f"Listening on port {port}...")
    load_data(group)
    # register RPC functions
    server.register_function(getbyname, 'getbyname')
    server.register_function(getbylocation, 'getbylocation')
    server.register_function(getbyyear, 'getbyyear')
    #start server
    server.serve_forever()

if __name__ == '__main__':
    main()