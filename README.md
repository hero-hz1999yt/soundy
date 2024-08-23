
# SOUNDY
**ES UN SENSUAL SCRIPT QUE CORRE AL ARRANCAR EL SISTEMA PARA ESTAR A LA ESCUCHA DE CUANDO CONECTES UN DISPOSITIVO A LOS PUERTOS USB Y REPRODUCIR UN SONIDO QUE TU CONFIGURES.**


## AUTOR
- [hero-hz1999yt(GITHUB)](https://www.github.com/hero-hz1999yt)
- [hero-hz1999yt(YOUTUBE)](https://www.youtube.com/@HERO_LINUX1999)
- [hero-hz1999yt(FACEBOOK)](https://www.facebook.com/hero.hz1999yt/)
- [hero-hz1999yt(TWITTER)](https://twitter.com/ErikAlbertoRod3)


## INSTALACION
### ===================>> DEPENDENCIAS <<======================
**_--ARCH LINUX Y DERIVADAS--_**
```bash
sudo pacman -S git mpg123 python-pyudev
```
**_--UBUNTU Y DERIVADAS--_**
```bash
sudo apt install git mpg123 python3-pyudev
```
**_--FEDORA Y DERIVADOS--_**
```bash
sudo dnf install git mpg123 python3-pyudev
```
### ==========>> DESCARGA Y INSTALACION DE SOUNDY <<==========
```bash
# para la descarga y instalacion copea y pega los siguientes comandos
# en tu terminal.
cd && git clone https://github.com/hero-hz1999yt/soundy.git
mv soundy/ .soundy/
mv .soundy/soundy.desktop /home/$USER/.config/autostart
echo "Exec=python3 /home/$USER/.soundy/soundy.py" >> /home/$USER/.config/autostart/soundy.desktop
```


## DESINSTALACION
### ==========>> DESINSTALACION DE DEPENDENCIAS <<=============
**_--ARCH LINUX Y DERIVADAS--_**
```bash
sudo pacman -Rsn git mpg123 python-pyudev
sudo pacman -Rsn $(pacman -Qdtq)
```
**_--UBUNTU Y DERIVADAS--_**
```bash
sudo apt remove git mpg123 python3-pyudev
sudo apt autoremove
```
**_--FEDORA Y DERIVADOS--_**
```bash
sudo dnf remove git mpg123 python3-pyudev
sudo dnf autoremove
```
### ==============>> DESINSTALACION DE SOUNDY <<==============
```bash
rm -r ~/.soundy ~/.config/autostart/soundy.desktop
```


## COMENTARIOS SOBRE LA INSTALACION
### ====================>> MUY IMPORTANTE <<===================
* **CONFIGURAR EL VOLUMEN**
PARA CONFIGURAR EL VOLUMENT DEBES DE CONFIGURAR EL ARCHIVO QUE SE ENCUENTRA EN LA RUTA _/home/user/.soundy/config.azc_, DENTRO ABRA UN PARAMETRO:
```bash
VOLUMEN=100;
```
SOLO TIENES QUE MODIFICAR EL PORCENTAJE, EJEMPLO SI QUIERES QUE SUENE AL 75 PORCIENTO:
```bash
VOLUMEN=75;
```
SI LLEGAS A ELIMINAR EL PARAMETRO O NO LO CONFIGURAS BIEN SOUNDY PONDRA EL VALOR POR DEFECTO, AL IGUAL SI ELIMINAS EL ARCHIVO SOUNDY LO VOLVERA A CREAR.

* **CONFIGURAR LOS SONIDOS**
PARA CONFIGURAR LOS SONIDOS DEBES DE IR A LA SIGUIENTE RUTA _/home/user/.soundy/sonidos/_, DENTRO ABRAN 2 ARCHIVOS MP3, SOLO REMPLAZALOS POR EL QUE GUSTES MANTENIENDO EL MISMO NOMBRE CLARO.
```bash
#sonido al conectar el USB
/home/user/.soundy/sonidos/usb-conectado.mp3

#sonido al desconectar el USB
/home/user/.soundy/sonidos/usb-desconectado.mp3
```


## DISTRIBUCIONES DONDE SE TESTEO
SON POCAS IGUAL SE IRA TESTEANDO EN MAS DISTRIBUCIONES PARA VALIDAR QUE FUNCIONE Y SE IRAN AGREGANDO AQUI.
| Distribucion | Version | Escritorio | Resultado del testeo |
| :---         | :---    | :---       | :---                 |
| KDE Neon     | 5.27    | KDE Plasma | **OK**               |
| Arch linux   | RL      | KDE Plasma | **OK**               |
| SteamOS      | 3.5.7   | KDE Plasma | **OK**               |


## LICENCIA
[GNU General Public License v3.0](https://choosealicense.com/licenses/gpl-3.0/)
