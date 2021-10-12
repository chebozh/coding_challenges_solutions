"""Remove the Computer Virus

Your computer might have been infected by a virus! Create a function that finds the viruses in files and removes them from your computer.
Examples

remove_virus("PC Files: spotifysetup.exe, virus.exe, dog.jpg") ➞ "PC Files: spotifysetup.exe, dog.jpg"

remove_virus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe ") ➞ "PC Files: antivirus.exe, cat.pdf"

remove_virus("PC Files: notvirus.exe, funnycat.gif") ➞ "PC Files: notvirus.exe, funnycat.gif")

Notes

    Bad files will contain "virus" or "malware", but "antivirus" and "notvirus" will not be viruses.
    Return "PC Files: Empty" if there are no files left on the computer.
"""
def remove_virus(files):
    pc_files = files.split('PC Files: ')[1].split(', ')
    res = []
    for file in pc_files:
        if any(substr in file for substr in ('antivirus', 'notvirus')):
            res.append(file)
        elif any(substr in file for substr in ('virus', 'malware')):
            continue
        else:
            res.append(file)
    del pc_files # have to remove the virus after all
    return 'PC Files: {}'.format(', '.join(f for f in res) if res else 'Empty')


if __name__ == '__main__':
    assert remove_virus("PC Files: virus.exe, bestmalware.exe, memzvirus.exe") == "PC Files: Empty"

    assert remove_virus("PC Files: spotifysetup.exe, virus.exe, dog.jpg") == "PC Files: spotifysetup.exe, dog.jpg"

    assert remove_virus(
        "PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe ") == "PC Files: antivirus.exe, cat.pdf"

    assert remove_virus("PC Files: notvirus.exe, funnycat.gif") == "PC Files: notvirus.exe, funnycat.gif"
