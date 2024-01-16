import socket

def get_google_maps_info():
    host = 'maps.google.com'
    services = ['https']

    for service in services:
        try:

            port = socket.getservbyname(service)


            print(f'Service: {service.upper()}, Port: {port}')


            result = socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM)


            for res in result:
                family, socktype, proto, canonname, sockaddr = res
                ip_address, _ = sockaddr[:2]
                print(f'  IP Address: {ip_address}')

        except (socket.gaierror, socket.error) as e:
            print(f'Error: {e}')

if __name__ == "__main__":
    get_google_maps_info()
