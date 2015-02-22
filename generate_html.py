
import re

color="""
color-theme-aalto-dark 	color-theme-aalto-light
color-theme-aliceblue
color-theme-andreas 	color-theme-arjen
color-theme-bharadwaj 	color-theme-bharadwaj-slate
color-theme-billw 	color-theme-black-on-gray
color-theme-blippblopp 	color-theme-blue-eshell
color-theme-blue-gnus 	color-theme-blue-mood
color-theme-blue-sea 	color-theme-calm-forest
color-theme-charcoal-black 	color-theme-clarity
color-theme-classic 	color-theme-comidia
color-theme-dark-blue
color-theme-dark-blue2 	color-theme-dark-erc
color-theme-dark-font-lock 	color-theme-dark-gnus
color-theme-dark-green 	color-theme-dark-info
color-theme-dark-laptop 	color-theme-deep-blue
color-theme-digital-ofs1
color-theme-emacs-21 	color-theme-emacs-nw
color-theme-euphoria 	color-theme-example
color-theme-feng-shui 	color-theme-fischmeister
color-theme-gnome 	color-theme-gnome2
color-theme-goldenrod 	color-theme-gray1
color-theme-gray30 	color-theme-greiner
color-theme-gtk-ide 	color-theme-high-contrast
color-theme-hober 	color-theme-infodoc
color-theme-jb-simple 	color-theme-jedit-grey
color-theme-jonadabian 	color-theme-jonadabian-slate
color-theme-jsc-dark 	color-theme-jsc-light
color-theme-jsc-light2 	color-theme-katester
color-theme-kingsajz 	color-theme-late-night
color-theme-lawrence 	color-theme-ld-dark
color-theme-lethe 	color-theme-marine
color-theme-marquardt 	color-theme-matrix
color-theme-midnight 	color-theme-mistyday
color-theme-montz 	color-theme-oswald
color-theme-parus 	color-theme-pierson
color-theme-pok-wob 	color-theme-pok-wog
color-theme-ramangalahy
color-theme-raspopovic 	color-theme-renegade
color-theme-resolve 	color-theme-retro-green
color-theme-retro-orange 	color-theme-robin-hood
color-theme-rotor 	color-theme-ryerson
color-theme-salmon-font-lock 	color-theme-scintilla
color-theme-shaman
color-theme-simple-1 	color-theme-sitaramv-nt
color-theme-sitaramv-solaris 	color-theme-snow
color-theme-snowish 	color-theme-standard
color-theme-subtle-blue
color-theme-subtle-hacker 	color-theme-taming-mr-arneson
color-theme-taylor 	color-theme-tty-dark
color-theme-vim-colors 	color-theme-whateveryouwant
color-theme-wheat 	color-theme-word-perfect
color-theme-xemacs 	color-theme-xp
"""



def strip(s):
    if s == None:
        return ""
    else:
        s = s.strip()
        return s


def stringp(s):
    if len(s) > 0:
        return True
    else:
        return False


def make_theme_list():
    lines = filter(stringp,
                   map(strip,
                       re.split(r"\n|(\s{2,})", color)))
    return lines


def generate_html():
    print "<table border=\"1\">"
    for theme in make_theme_list():
        print "<tr>"
        print "<td><img src=\"" + theme + ".png\" width=\"300\" /> " + theme + ".png </td>"
        print "<td><img src=\"" + theme + "_terminal.png\" width=\"300\" /> " + theme + "_terminal.png </td>"
        print "</tr>"
    print "</table>"


def main():
    generate_html()

if __name__=="__main__":
    main()
