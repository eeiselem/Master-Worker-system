import xmlrpc.client
import sys

# 23000 port used
master_port = int(sys.argv[1])
with xmlrpc.client.ServerProxy(f"http://localhost:{master_port}/") as proxy:
    name = 'xander'
    print(f'Client => Asking for person with {name}')
    # RPC call
    result = proxy.getbyname(name)
    print(result)
    print()

    location = 'Kansas City'
    print(f'Client => Asking for person lived at {location}')
    # RPC call
    result = proxy.getbylocation(location)
    print(result)
    print()

    location = 'New York City'
    year = 2002
    print(f'Client => Asking for person lived in {location} in {year}')
    # RPC call
    result = proxy.getbyyear(location, year)  
    print(result)
    print()

    location = 'New York City'
    print(f'Client => Asking for person lived in {location}')
    # RPC call
    result = proxy.getbylocation(location)  
    print(result)
    print()


    # below are additional test cases
    # Test non-existing user
    print(f'Client => Asking for person with Elliott')
    result = proxy.getbyname("Elliott")
    print(result)
    print()

    # Test non-existing location
    print(f'Client => Asking for person lived at Tokyo')
    result = proxy.getbylocation("Tokyo")
    print(result)
    print()

    # Test existing year, non-existing location
    print(f'Client => Asking for person lived in Tokyo in 2002')
    result = proxy.getbyyear("Tokyo",2002) 
    print(result)
    print()

    # Test non-existing year, non-existing location
    print(f'Client => Asking for person lived in Tokyo in 69420')
    result = proxy.getbyyear("Tokyo",6245)
    print(result)
    print()

    # Test non-existing year, existing location
    print(f'Client => Asking for person lived in Kansas City in 42069')
    result = proxy.getbyyear("Kansas City", 45034)
    print(result)  
    print()