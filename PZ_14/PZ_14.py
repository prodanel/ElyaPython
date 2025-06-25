#Из исходного текстового файла (ip_address.txt) из раздела «Зарезервированные
#адреса» перенести в первый файл строки с ненулевыми первым и вторым октетами,
#а во второй – все остальные. Посчитать количество полученных строк в каждом
#файле.
def process_ip_addresses(input_file, output_file_nonzero, output_file_zero):

    nonzero_count = 0
    zero_count = 0

    with open(input_file, 'r') as infile, \
            open(output_file_nonzero, 'w') as outfile_nonzero, \
            open(output_file_zero, 'w') as outfile_zero:

        for line in infile:
            line = line.strip()
            if not line:
                continue

            if any(char.isdigit() or char == '.' for char in line):
                try:
                    ip_address = line.split('/')[0]
                    octets = ip_address.split('.')
                    if len(octets) == 4:
                        first_octet = int(octets[0])
                        second_octet = int(octets[1])

                        if first_octet != 0 and second_octet != 0:
                            outfile_nonzero.write(line + '\n')
                            nonzero_count += 1
                        else:
                            outfile_zero.write(line + '\n')
                            zero_count += 1
                except ValueError:
                    continue

    return nonzero_count, zero_count

input_file = 'ip_address.txt'
output_file_nonzero = 'nonzero_ip.txt'
output_file_zero = 'zero_ip.txt'

nonzero_count, zero_count = process_ip_addresses(input_file, output_file_nonzero, output_file_zero)

print(f"Количество строк в {output_file_nonzero}: {nonzero_count}")
print(f"Количество строк в {output_file_zero}: {zero_count}")
