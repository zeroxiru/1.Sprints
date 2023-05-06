def count_domains(log_file, min_hits=0):
    domains = {}
    for line in log_file.strip().split('\n'):
        parts = line.strip().split()
        if len(parts) != 2:
            continue
        domain, count = parts
        count = int(count)
        subdomains = domain.split('.')
        if subdomains[0].isdigit() or subdomains[0] == 'www':
            subdomains.pop(0)
        if subdomains[-2] == 'co' or subdomains[-2] == 'com':
            main_domain = '.'.join(subdomains[-3:])
        else:
            main_domain = '.'.join(subdomains[-2:])
        domains[main_domain] = domains.get(main_domain, 0) + count
    result = []
    for domain, count in domains.items():
        if count >= min_hits:
            result.append((domain, count))
    result.sort(key=lambda x: (-x[1], x[0]))
    return '\n'.join(['{} ({})'.format(domain, count) for domain, count in result])


def main():
    log_file = """
    *.amazon.co.uk    89
    *.doubleclick.net    139
    *.fbcdn.net    212
    *.in-addr.arpa    384
    *.l.google.com    317
    1.client-channel.google.com    110
    6.client-channel.google.com    45
    a.root-servers.net    1059
    apis.google.com    43
    clients4.google.com    71
    clients6.google.com    81
    connect.facebook.net    68
    edge-mqtt.facebook.com    56
    graph.facebook.com    150
    mail.google.com    128
    mqtt-mini.facebook.com    47
    ssl.google-analytics.com    398
    star-mini.c10r.facebook.com    46
    staticxx.facebook.com    48
    www.facebook.com    178
    www.google.com    162
    www.google-analytics.com    127
    www.googleapis.com    87
    """
    print(count_domains(log_file))


if __name__ == "__main__":
    main()