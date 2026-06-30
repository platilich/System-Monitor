import subprocess



def main():
    subprocess.run(['python3', '-m', 'venv', 'venv'], check=True)


    subprocess.run(['venv/bin/pip', 'install', '-r', 'requirements.txt'], check=True)




if __name__ == '__main__':
    accept = input('введите -y, чтобы подтвердить установку виртуального окружения и зависимостей: ')

    if accept != 'y':
        print('-- отмена --')


    main()