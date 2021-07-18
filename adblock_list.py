import requests

def fetch_and_format(url: str) -> list:
    data = requests.get(url).text
    formatted_data = []
    if data:
        rows = [r.strip() for r in data.split('\n')]
        for line in rows:
            if line:
                if not line.startswith('#'):
                    line = line.replace('0.0.0.0', '')
                    line = line.replace('127.0.0.1', '')
                    formatted_data.append('0.0.0.0 ' + line.split(' ')[-1])
                    '''
                    if line.startswith('127.0.0.1'):
                        line = line.replace('127.0.0.1', '0.0.0.0')
                    if not line.startswith('0.0.0.0 '):
                        line = '0.0.0.0 ' + line
                    elif line.startswith('0.0.0.0'):
                        line = line.replace('0.0.0.0', '0.0.0.0 ')
                    elif line.startswith('0.0.0.0\t'):
                        line = line.replace('0.0.0.0\t', '0.0.0.0 ')                        
                    formatted_data.append(line)
                    '''
    return formatted_data

def write_consolidated(file_name: str, consolidated: list):
    lines = set([row + '\n' for rowset in consolidated for row in rowset])
    for line in lines:
        if not line.startswith('0.0.0.0 '):
            line = line.replace('0.0.0.0', '0.0.0.0 ')
        
    with open(file_name, 'w') as of:
        of.writelines(lines)


def main():
    consolidated = []
    with open('adblock-sources.txt') as af:
        for line in af:
            print(line.strip())
            rows = fetch_and_format(line.strip())
            print(len(rows))
            consolidated.append(rows)
    write_consolidated('consolidated_adlist.txt', consolidated)
if __name__ == '__main__':
    main()