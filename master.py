from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.client import ServerProxy
import sys


workers = {
    'worker-1': ServerProxy("http://localhost:23001/"),
    'worker-2': ServerProxy("http://localhost:23002/")
}

 
def getbylocation(location):
    results = []
    # iterate through workers
    for worker in workers:
        # use try so that if one worker fails, the other worker can still be used
        try:
            # call getbylocation function from worker
            result = workers[worker].getbylocation(location)
            # if no error, add result to results
            if not result["error"]:
                results.extend(result["result"])
        # if worker fails, add error message to results
        except Exception as e:
            results.append({
                'error': True,
                'result': str(e)
                }  )
    # if location is not found, return error message and assign error to True, otherwise return the list of results
    return {
        'error': False if results else True,
        'result': results if results else ['location not found']
    }

def getbyname(name):
    results = []
    # if first letter of name is between a-m, use worker-1 
    if name[0].lower() <= 'm':
        # use try so that if one worker fails, the other worker can still be used
        try:
            # call getbyname function from worker-1
            result = workers['worker-1'].getbyname(name)
            # if no error, add result to results
            if not result["error"]:
               results.extend(result["result"])
        # if worker fails, add error message to results
        except Exception as e:
            results.append({
                'error': True,
                'result': str(e)
                })
    # if first letter of name is between n-z, use worker-2
    elif 'z' >= name[0].lower() > 'm':
        try:
            # call getbyname function from worker-1
            result = workers['worker-2'].getbyname(name)
            # if no error, add result to results
            if not result["error"]:
                results.extend(result["result"])
        except Exception as e:
            results.append({
                'error': True,
                'result': str(e)
            })
    # if name is not valid, return error message
    else:
        return {
            'error': True,
            'result': ['not a valid name']}
    # if name is not found, return error message and assign error to True, otherwise return the list of results
    return {
        'error': False if results else True,
        'result': results if results else ['name not found']
        }

def getbyyear(location, year):
    results = []
    for worker in workers:
        try:
            result = workers[worker].getbyyear(location,year)
            if not result["error"]:
                results.extend(result["result"])
        except Exception as e:
            results.append({
                'error': True,
                'result': str(e)
            })
    return {
        'error': False if results else True,
        'result': results if results else ['year with associated location not found']
    }

def main():
    #23000
    port = int(sys.argv[1])
    server = SimpleXMLRPCServer(("localhost", port))
    print(f"Listening on port {port}...")

    # register RPC functions
    server.register_function(getbyname, 'getbyname')
    server.register_function(getbylocation, 'getbylocation')
    server.register_function(getbyyear, 'getbyyear')
    server.serve_forever()


if __name__ == '__main__':
    main()