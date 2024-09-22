from ipaddress import ip_network


# Вариант от Л. Шастина и Д. Бахтиева(1)
net = ip_network('228.172.236.0/255.255.240.0', 0)
counter = 0
for ip in net:
    binary_ip = format(ip, 'b')
    if binary_ip.count('1') % 5 != 0:
        counter += 1
print(counter)


# Вариант Бахтиева(2024 - 2025) -> № 2
net = ip_network('123.222.111.192/255.255.255.248', 0)
counter = 0
for ip in net:
    ip = str(ip).split('.')
    b_4 = bin(int(ip[-1]))[2::]
    if (b_4).count('0') % 3 != 0:
        counter += 1
print(counter)