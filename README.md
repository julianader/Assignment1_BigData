## Assignment1_BigData


# Commands for docker 

1. docker build -t julianaguib/bd-a1-image .
2. docker run -it --name finalContainer julianaguib/bd-a1-image
3. touch load.py eda.py dper.py model.py vis.py
4. python3 load.py train.csv


# Commands for shell file run on Windows
1. Get-ExecutionPolicy
2. Set-ExecutionPolicy RemoteSigned
3. Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
4. choco install dos2unix
5. dos2unix final.sh
6. wsl ./final.sh