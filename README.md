# Python dla średniozaawansowanych

Ćwiczenia z [kursu Udemy](https://www.udemy.com/course/python-dla-srednio-zaawansowanych/learn/)

## Strony

* https://realpython.com/
*

## YT

* [@mCoding](https://www.youtube.com/@mCoding) ciekawy kanał o Pythonie (ale nie tylko)
* [25 nooby Python habits you need to ditch](https://www.youtube.com/watch?v=qUeud6DvOWI)
*

## Windows WSL

Przy pracy w WSL Ubuntu-20, irytujące jest że do `PATH` dodawane są ścieżki z Windows,
przez co np. wywołując `python`, Bash próbuje uruchomić `python.exe`.

Aby to rozwiązać, można sie posłużyć rozwiązaniem stąd: https://stackoverflow.com/questions/51336147/how-to-remove-the-win10s-path-from-wsl

```sh
sudo nano /etc/wsl.conf
```

wkleić

```ini
[interop]
appendWindowsPath = false
```

i wyjść `^X`

Na koniec w PowerShell zrestartować Ubuntu

```bat
wslconfig /t Ubuntu-20.04
```

Od teraz, zmienna PATH powinna pokazywać tylko ścieżli z Linuxa

```sh
echo $PATH
```
