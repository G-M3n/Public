import os.path, os, config
from ftplib import FTP_TLS, error_perm
directorypath = config.path
log=""
try:
    ftp = FTP_TLS(config.url)
    ftp.login(config.user, config.password)
    ftp.prot_p()
except error_perm as error:
    print(error)
def SaveFiles(ftp, path):
    for (file) in os.listdir(path):
        fullpath = os.path.join(path, file)
        if os.path.isdir(fullpath):
            try:
                ftp.mkd(file)
            except error_perm as error:
                if not error.args[0].startswith('550'): 
                    raise
            ftp.cwd(file)
            SaveFiles(ftp, fullpath)
            ftp.cwd("..")
        elif os.path.isfile(fullpath):
            ftp.storbinary('STOR '+file, open(fullpath, 'rb'))
SaveFiles(ftp, directorypath)
ftp.dir(log)
print(log)
ftp.quit()

# TimeoutError: [WinError 10060] Ein Verbindungsversuch ist fehlgeschlagen,
# da die Gegenstelle nach einer bestimmten Zeitspanne nicht richtig reagiert hat, 
# oder die hergestellte Verbindung war fehlerhaft, da der verbundene Host nicht reagiert hat
