
# TODO:
# - separate XFS to be standalone - is it possible without duplicated files?

#
# Conditional build:
# _without_tdfx		- disables tdfx drivers building
#

%define		_sver	%(echo %{version} | tr -d .)

Summary:	XFree86 Window System servers and basic programs
Summary(de):	Xfree86 Window-System-Server und grundlegende Programme
Summary(es):	Programas b�sicos y servidores para el sistema de ventanas XFree86
Summary(fr):	Serveurs du syst�me XFree86 et programmes de base
Summary(ja):	XFree86 window system �Υ����Фȴ���Ū�ʥץ������
Summary(ko):	X�� �ʿ��� �⺻���� �۲ð� ���α׷��� ������
Summary(pl):	XFree86 Window System wraz z podstawowymi programami
Summary(tr):	XFree86 Pencereleme Sistemi sunucular� ve temel programlar
Summary(pt_BR):	Programas b�sicos e servidores para o sistema de janelas XFree86
Summary(ru):	������� ������, ��������� � ������������ ��� ������� ������� ��� X
Summary(uk):	����צ ������, �������� �� ���������æ� ��� �����ϧ ����æ� Ц� X
Summary(zh_CN):	XFree86 ����ϵͳ�������ͻ�������
Name:		XFree86
Version:	4.3.99.5
Release:	0.1
License:	MIT
Group:		X11/XFree86
Source0:	ftp://ftp.xfree86.org/pub/XFree86/develsnaps/%{name}-%{version}.tar.bz2
# Source0-md5:	d01d01a7abd4f0764e20ef493f76a3b2
#Source1:	ftp://ftp.xfree86.org/pub/XFree86/4.3.0/source/X430src-2.tgz
#Source2:	ftp://ftp.xfree86.org/pub/XFree86/4.3.0/source/X430src-3.tgz
Source3:	ftp://ftp.pld-linux.org/software/xinit/xdm-xinitrc-0.2.tar.bz2
# Source3-md5:	0a15b1c374256b5cad7961807baa3896
Source4:	xdm.pamd
Source5:	xserver.pamd
Source6:	xdm.init
Source7:	xfs.init
Source8:	xfs.config
Source9:	XTerm.ad-pl
Source10:	xdm.sysconfig
Source11:	xfs.sysconfig
Source20:	twm.desktop
Source21:	xeyes.desktop
Source22:	xedit.desktop
Source23:	xterm.desktop
Source24:	xclipboard.desktop
Source25:	xclock.desktop
Source26:	oclock.desktop
Source27:	xconsole.desktop
Source30:	xlogo64.png
Source31:	xeyes.png
Source32:	xedit.png
Source33:	xterm.png
# Source33-md5:	a9e182f1f2ce977c51cdfd28dae53fdb
Source34:	xclipboard.png
# Source34-md5:	a2eb1994b5b6871124178d0ce518f157
Source35:	xclock.png
# Source35-md5:	b7a0e68f24dc55bfed08220bfdc7e538
Source36:	oclock.png
# Source36-md5:	1bd2b33adc6ff3e7607a164d9fd16e8a
Source37:	xconsole.png
# Source37-md5:	7da3e9920e4b03dd643425f426c52adc
Source38:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-Xman-pages.tar.bz2
# Source38-md5: a184106bb83cb27c6963944d9243ac3f
Source39:	cvs://anonymous@cvs.gatos.sourceforge.net/cvsroot/gatos/ati.2-20021001.tar.bz2
# Source39-md5: 8d43c01d364576c195a5294279f92566
Patch0:		%{name}-PLD.patch
Patch1:		%{name}-HasZlib.patch
Patch2:		%{name}-DisableDebug.patch
Patch3:		%{name}-Xwrapper.patch
Patch4:		%{name}-xfs.patch
Patch5:		%{name}-xfs-fix.patch
Patch6:		%{name}-xfs-logger.patch
Patch7:		%{name}-xterm-utempter.patch
Patch8:		%{name}-app_defaults_dir.patch
Patch9:		%{name}-v4l.patch
Patch10:	%{name}-broken-includes.patch
Patch11:	%{name}-alpha-pcibus-lemming.patch
Patch12:	%{name}-fhs.patch
Patch13:	%{name}-xdmsecurity.patch
Patch14:	%{name}-xman.patch
Patch15:	%{name}-HasXdmAuth.patch
Patch16:	%{name}-xdm-fixes.patch
Patch17:	%{name}-imake-kernel-version.patch
Patch18:	%{name}-no-kernel-modules.patch
Patch19:	%{name}-parallelmake.patch
Patch20:	%{name}-pic.patch
Patch21:	%{name}-r128-busmstr2.patch
Patch22:	%{name}-neomagic_swcursor.patch
Patch23:	%{name}-mga-busmstr.patch
Patch24:	%{name}-agpgart-load.patch
Patch25:	%{name}-mkfontdir-chmod_644.patch
Patch26:	%{name}-HasFreetype2.patch
Patch27:	%{name}-config-s3.patch
Patch28:	%{name}-sparc_pci_domains.patch
Patch29:	%{name}-XTerm.ad.patch
Patch30:	%{name}-alpha_GLX_align_fix.patch
Patch32:	%{name}-xman-manpaths.patch
Patch33:	%{name}-clearrts.patch
Patch34:	%{name}-fix-07-s3trio64v2gx+netfinity.patch
Patch35:	%{name}-i740-driver-update-cvs-20020617.patch
Patch36:	%{name}-tdfx-disable-dri-on-16Mb-cards-in-hires.patch
Patch37:	%{name}-tdfx-interlace.patch
Patch38:	%{name}-tdfx-fix-compiler-warnings.patch
Patch39:	%{name}-tdfx-fix-vtswitch-font-corruption.patch
Patch40:	%{name}-Xfont-Type1-large-DoS.patch
# "strip -g libGLcore.a" leaves empty objects m_debug_*.o, which cause
# warnings during GLcore loading ("m_debug_*.o: no symbols") - shut up them
Patch41:	%{name}-GLcore-strip-a-workaround.patch
Patch42:	%{name}-disable_glide.patch
Patch43:	%{name}-expat.patch
Patch44:	%{name}-pkgconfig.patch
Patch45:	%{name}-VidMode-nocrashafterfailure.patch
# spencode.o in libspeedo.a is empty - patch like for libGLcore.a
Patch46:	%{name}-spencode-nowarning.patch
# Small (maybe buggy) patch to resolve problems with totem 0.97.0
Patch47:	%{name}-lock.patch
Patch48:	%{name}-savage-20030505.patch
URL:		http://www.xfree86.org/
BuildRequires:	bison
BuildRequires:	expat-devel
BuildRequires:	flex
BuildRequires:	freetype-devel >= 2.0.0
BuildRequires:	gcc-c++
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRequires:	pam-devel
BuildRequires:	%{_bindir}/perl
BuildRequires:	tcl-devel
BuildRequires:	utempter-devel
BuildRequires:	zlib-devel
BuildRequires:	ed
%ifarch %{ix86} alpha
%{!?_without_tdfx:BuildRequires:	Glide3-DRI-devel}
%endif
# Required by xc/programs/Xserver/hw/xfree86/drivers/glide/glide_driver.c
%ifarch %{ix86}
%{!?_without_tdfx:BuildRequires:	Glide2x_SDK}
%endif
Requires:	xauth
Requires:	%{name}-libs = %{version}
ExclusiveArch:	%{ix86} alpha sparc m68k armv4l noarch ppc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	xpm-progs
Obsoletes:	xterm

%ifarch sparc sparc64
Obsoletes:	X11R6.1
%endif

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_icondir	/usr/share/icons
%define		_pixmapsdir	/usr/share/pixmaps
%define		_soundsdir	/usr/share/sounds
%define		_themesdir	/usr/share/themes
%define		_wmpropsdir	/usr/share/wm-properties

# avoid Mesa dependency in XFree86-OpenGL-libs
# Glide3 (libglide3.so.3) can be provided by Glide_V3-DRI or Glide_V5-DRI
%define		_noautoreqdep	libGL.so.1 libGLU.so.1 libOSMesa.so.3.3 libglide3.so.3

%description
The X Window System provides the base technology for developing
graphical user interfaces. Simply stated, X draws the elements of the
GUI on the user's screen and builds methods for sending user
interactions back to the application. X also supports remote
application deployment--running an application on another computer
while viewing the input/output on your machine. X is a powerful
environment which supports many different applications, such as games,
programming tools, graphics programs, text editors, etc. XFree86 is
the version of X which runs on Linux, as well as other platforms.

This package contains the basic fonts, programs and documentation for
an X workstation. However, this package doesn't provide the program
which you will need to drive your video hardware. To control your
video card, you'll need the particular X server package which
corresponds to your computer's video card.

%description -l de
X-Window ist eine voll funktionsf�hige grafische Benutzeroberfl�che
mit mehreren Fenstern, mehreren Clients und verschiedenen Arten von
Fenstern. Es kommt auf den meisten Unix-Plattformen zum Einsatz. Die
Clients lassen sich auch mit Hilfe anderer Fenstersysteme anzeigen.
Das X-Protokoll gestattet die Ausf�hrung der Applikationen direkt auf
lokalen Rechnern oder �ber ein Netz und bietet gro�e Flexibilit�t bei
Client-Server-Implementierungen.

%description -l es
X Window es una interface gr�fica completa con m�ltiples ventanas,
m�ltiples clientes y diferentes estilos de ventanas. Se usa en la
mayor�a de las plataformas Unix, y los clientes tambi�n pueden
ejecutar en otros sistemas de ventanas populares. El protocolo X
permite que las aplicaciones puedan ejecutarse tanto en la m�quina
local como a trav�s de la red, y proveer flexibilidad en
implementaciones cliente/servidor. Este paquete contiene las fuentes
b�sicas, programas y documentaci�n para una estaci�n de trabajo X. No
ofrece un servidor X que acceda tu hardware de v�deo -- estos son
puestos a disposici�n en otro paquete.

%description -l pl
X Window System jest graficznym interfejsem u�ytkownika; cechuje si�
mo�liwo�ci� pracy w wielu oknach, z wieloma klientami i do tego w
r�nych wystrojach okien. :) Jest u�ywany na wi�kszo�ci platform
sytem�w Unix, a klienci mog� by� uruchamiani tak�e pod innymi
popularnymi systemami okienkowymi. Protok� X pozwala na uruchamianie
aplikacji zar�wno z lokalnej maszyny jak i poprzez sie� - daj�c przez
to elastyczn� implementacj� architektury klient/serwer.

Pakiet ten nie zawiera X serwera kt�ry jest po�rednikiem z Twoj� kart�
graficzn� (jest on w innym pakiecie).

%description -l tr
X Window sistemi, �oklu pencere, �oklu istemci ve �e�itli pencere
stilleriyle geni� �zelliklere sahip bir Grafik Kullan�c� Arabirimidir.
�o�u UNIX sisteminde �al��t��� gibi istemcileri de bir�ok pencereleme
sistemiyle �al��abilir. X protokolu kullanan uygulamalar�n yerel
makina veya bilgisayar a�� �zerinden �al��t�r�labilmesi esnek bir
istemci/sunucu ortam� sa�lar. Bu paket bir X istasyonu i�in gerekli
olan temel yaz�tiplerini, programlar� ve belgeleri sunar. Ekran
kart�n�z� s�rmek i�in gerekli olan X sunucusu bu pakete dahil
de�ildir.

%description -l pt_BR
X Window � uma interface gr�fica completa com m�ltiplas janelas,
m�ltiplos clientes e diferentes estilos de janelas. � usado na maioria
das plataformas Unix, e clientes tamb�m podem rodar em outros sistemas
de janelas populares. O protocolo X permite que aplica��es possam
rodar tanto na m�quina local como atrav�s da rede, provendo
flexibilidade em implementa��es cliente/servidor.

Este pacote cont�m as fontes b�sicas, programas e documenta��o para
uma esta��o de trabalho X. Ele n�o fornece um servidor X que acessa
seu hardware de v�deo -- estes s�o disponibilizados em outro pacote.

%description -l ru
X Window System ������������� ���� ��� ���������� �����������
����������� ������������. �������� ������, X ������ �������� GUI ��
������ ������������ � ����� ������ ��� �������� �������� ������������
���������� ����������. X ����� ������������ ������������� ���������� -
������ �������� �� ��������� ���������� � ������/������� ��
���������������� ������. X - ��� ������ �����, ��������������
��������� ����������, ����� ��� ����, ����������� ��� ������������,
����������� ���������, ��������� ��������� � �.�. XFree86 - ��� ������
X, ���������� �� Linux � ������ ��������.

���� ����� �������� ������� ������, ��������� � ������������ ���
������� ������� X.

������������� ���������� ���������� ������ Xconfigurator, ����������
xfs � ���������� XFree86-libs. �������� �������� ���������� ����� ����
��� ����� ������� ������� XFree86.

�� �, �������, ���� �� ����������� ������������� ����������,
���������� ��� X-�������, ��� ����� ���� ����� ����������
XFree86-devel.

%description -l uk
X Window System ����� ���� ��� �������� ���Ʀ���� ��������Ӧ�
�����������. ����Ԧ�� ������, X ����� �������� GUI �� ����Φ
����������� �� ���դ ������ ��� ������ަ Ħ� ����������� ����������
���������. X ����� Ц�����դ �����Ħ� ���������� ������� - ������
������� �� צ��������� ����'���Ҧ � ������/������� �� ������
�����������. X - �� ������� ����������, ��� Ц�����դ ������ ˦��˦���
Ҧ���� �������, ����� �� ����, ����������� ��� ������ͦ���, ���Ʀ�Φ
��������, ������צ ��������� � �.�. XFree86 - �� ���Ӧ� X, ��� ������
�� Linux �� ����� ��������.

��� ����� ͦ����� ����צ ������, �������� �� ���������æ� ��� �����ϧ
����æ� X.

��������� ����Ȧ��� ���������� ������ Xconfigurator, ���������� xfs ��
¦�̦����� XFree86-libs. ������� ����� ���������� ���������� ���� ���
��˦���� ����Ԧ� ����Ԧ� XFree86.

�� �, �����Ԧ, ���� �� ���������� ���������� �������Φ ��������, ��
�������� �� X-�̦����, ��� ����� ����� ���� ���������� XFree86-devel.

%package common
Summary:	XFree86 files required both on server and client side
Summary(pl):	Pliki XFree86 wymagane zar�wno po stronie serwera jak i klienta
Group:		X11/XFree86

%description common
XFree86 files required both on server and client side.

%description common -l pl
Pliki XFree86 wymagane zar�wno po stronie serwera jak i klienta.

%package DPS
Summary:	Display PostScript
Summary(pl):	Display PostScript
Group:		X11/XFree86
Provides:	DPS
Obsoletes:	dgs

%description DPS
X-Window Display PostScript is device-independent imaging model for
displaying information on a screen.

%description DPS -l pl
X-Window Display PostScript to niezale�ny od urz�dzenia model
wy�wietlania informacji na ekranie.

%package DPS-devel
Summary:	Display PostScript
Summary(pl):	Display PostScript
Group:		X11/XFree86
Requires:	%{name}-DPS = %{version}
Obsoletes:	dgs-devel

%description DPS-devel
Header files for develop X-Window Display Postscript.

%description DPS-devel -l pl
Pliki nag��wkowe biblioteki X-Window Display PostScript.

%package DPS-static
Summary:	Display PostScript
Summary(pl):	Display PostScript
Group:		X11/XFree86
Requires:	%{name}-DPS-devel = %{version}
Obsoletes:	dgs-static

%description DPS-static
X-Window Display PostScript static libraries.

%description DPS-static -l pl
Statyczne biblioteki X-Window Display PostScript.

%package xft1
Summary:	Old version of font rendering library
Summary(pl):	Stara wersja biblioteki wy�wietlaj�cej fonty
Group:		X11/XFree86
Requires:	%{name}-libs = %{version}
Obsoletes:	XFree86-xft < 4.2.99

%description xft1
Old version of font rendering library.

%description xft1 -l pl
Stara wersja biblioteki wy�wietlaj�cej fonty.

%package xft
Summary:	X Font rendering library
Summary(pl):	Biblioteka do renderowania font�w
Group:		X11/XFree86
Requires:	%{name}-libs = %{version}
Requires:	%{name}-fontconfig = %{version}
Provides:	Xft = 2.1-2
Obsoletes:	XFree86-xft2
Obsoletes:	Xft

%description xft
Xft is a font rendering library for X.

%description xft -l pl
Xft jest bibliotek� s�u��c� do renderowania font�w dla X Window.

%package xft-devel
Summary:	X Font Rendering library
Summary(pl):	Biblioteka do renderowania font�w
Group:		X11/Development/Libraries
Requires:	%{name}-xft = %{version}
Requires:	%{name}-fontconfig-devel
Provides:	Xft-devel = 2.1-2
Obsoletes:	XFree86-xft2-devel
Obsoletes:	Xft-devel

%description xft-devel
Xft is a font rendering library for X.

This package contains the header files needed to develop programs that
use these Xft.

%description xft-devel -l pl
Xft jest bibliotek� s�u��c� do renderowania font�w dla X Window.

Ten pakiet zawiera pliki nag��wkowe potrzebne do kompilowania
program�w korzystaj�cych z biblioteki Xft.

%package xft-static
Summary:	X Font Rendering library
Summary(pl):	Biblioteka do renderowania font�w
Group:		X11/Development/Libraries
Requires:	%{name}-xft-devel = %{version}
Provides:	Xft-static = 2.1-2
Obsoletes:	XFree86-xft2-static
Obsoletes:	Xft-static

%description xft-static
Xft is a font rendering library for X.

This package contains static libraries.

%description xft-static -l pl
Xft jest bibliotek� s�u��c� do renderowania font�w dla X Window.

Ten pakiet zawiera biblioteki statyczne.

%package fontconfig
Summary:	Font configuration and customization library
Summary(pl):	Biblioteka do konfigurowania font�w
Requires:	%{name}-libs = %{version}
Group:		Libraries
Requires(post):	/sbin/ldconfig
Provides:	fontconfig = 1.0.1
Provides:	%{name}-fontconfig-realpkg = %{version}
Obsoletes:	fontconfig

%description fontconfig
Fontconfig is designed to locate fonts within the system and select
them according to requirements specified by applications.

%description fontconfig -l pl
Fontconfig jest biblioteka przeznaczon� do lokalizowania font�w w
systemie i wybierania ich w zale�no�ci od potrzeb aplikacji.

%package fontconfig-devel
Summary:	Font configuration and customization library
Summary(pl):	Biblioteka do konfigurowania font�w
Group:		Development/Libraries
Requires:	%{name}-fontconfig-realpkg = %{version}
Requires:	freetype-devel
Provides:	fontconfig-devel = 1.0.1
Provides:	%{name}-fontconfig-devel-realpkg = %{version}
Obsoletes:	fontconfig-devel

%description fontconfig-devel
Fontconfig is designed to locate fonts within the system and select
them according to requirements specified by applications.

This package contains the header files needed to develop programs that
use these fontconfig.

%description fontconfig-devel -l pl
Fontconfig jest biblioteka przeznaczon� do lokalizowania font�w w
systemie i wybierania ich w zale�no�ci od potrzeb aplikacji.

Ten pakiet zawiera pliki nag��wkowe potrzebne do kompilowania
program�w korzystaj�cych z biblioteki fontconfig.

%package fontconfig-static
Summary:	Font configuration and customization library
Summary(pl):	Biblioteka do konfigurowania font�w
Group:		Development/Libraries
Requires:	%{name}-fontconfig-devel-realpkg = %{version}
Provides:	fontconfig-static = 1.0.1
Obsoletes:	fontconfig-static

%description fontconfig-static
Fontconfig is designed to locate fonts within the system and select
them according to requirements specified by applications.

This package contains static libraries.

%description fontconfig-static -l pl
Fontconfig jest biblioteka przeznaczon� do lokalizowania font�w w
systemie i wybierania ich w zale�no�ci od potrzeb aplikacji.

Ten pakiet zawiera biblioteki statyczne.

%package render
Summary:	X Render Extension
Summary(pl):	Rozszerzenie X Render
Group:          X11/Development/Libraries
Requires:       XFree86-devel

%description render
This package contains header files and documentation for the X render
extension.  Library and server implementations are separate.

%description render -l pl
Pakiet zawiera pliki nag��wkowe i dokumenetacj� dla rozszerzenia
X render. Biblioteka i implementacja serwera znajduj� si� w osobnym
pakiecie.

%package xrender
Summary:        X Render Extension
Summary(pl):    Rozszerzenie X Render
Group:          X11/Libraries
Requires:	%{name}-libs = %{version}

%description xrender
X render library.

%description xrender -l pl
Biblioteka X render.

%package xrender-devel
Summary:        X Render Extension headers
Summary(pl):    Pliki nag��wkowe rozszerzenia X Render
Group:          X11/Libraries
Requires:	%{name}-devel = %{version}
Requires:	%{name}-render = %{version}
Requires:	%{name}-xrender = %{version}

%description xrender-devel
X render library headers.

%description xrender-devel -l pl
Pliki nag��wkowe biblioteki X render.

%package xrender-static
Summary:        X Render static library
Summary(pl):    Biblioteka statyczna X render
Group:          X11/Libraries/Development
Requires:	%{name}-xrender-devel = %{version}

%description xrender-static
X render static library.

%description xrender-static -l pl
Biblioteka statyczna X render.

%package xcursor
Summary:        X cursor library
Summary(pl):    Biblioteka X cursor
Group:          X11/Libraries
Requires:	%{name}-libs = %{version}

%description xcursor
X cursor library.

%description xcursor -l pl
Biblioteka X cursor.

%package xcursor-devel
Summary:        X cursor library headers
Summary(pl):    Pliki nag��wkowe biblioteki X cursor
Group:          X11/Libraries/Development
Requires:	%{name}-devel = %{version}
Requires:	%{name}-xcursor = %{version}

%description xcursor-devel
X cursor library headers.

%description xcursor-devel -l pl
Pliki nag��wkowe biblioteki X cursor.

%package xcursor-static
Summary:        X cursor static library
Summary(pl):    Biblioteka statyczna X cursor
Group:          X11/Libraries/Development
Requires:	%{name}-xcursor-devel = %{version}

%description xcursor-static
X cursor static library.

%description xcursor-static -l pl
Biblioteka statyczna X cursor.

%package OpenGL-core
Summary:	OpenGL support for X11R6
Summary(pl):	Wsparcie OpenGL dla systemu X11R6
Group:		X11/Libraries
Requires:	%{name}-libs = %{version}
Obsoletes:	XFree86-driver-nvidia

%description OpenGL-core
OpenGL support for X11R6 system.

%description OpenGL-core -l pl
Wsparcie OpenGL dla systemu X11R6.

%package OpenGL-devel
Summary:	OpenGL for X11R6 development
Summary(pl):	Pliki nag��wkowe OpenGL dla systemu X11R6
Group:		X11/Development/Libraries
Requires:	%{name}-OpenGL-libs = %{version}
Requires:	%{name}-devel
Requires:	OpenGL-devel-base
Provides:	OpenGL-devel
Obsoletes:	Mesa-devel
Obsoletes:	glxMesa-devel
Obsoletes:	XFree86-OpenGL-doc

%description OpenGL-devel
Headers and man pages for OpenGL for X11R6.

%description OpenGL-devel -l pl
Pliki nag��wkowe i manuale do OpenGL dla systemu X11R6.

%package OpenGL-devel-base
Summary:	OpenGL for X11R6 development (only gl?.h)
Summary(pl):	Pliki nag��wkowe OpenGL dla systemu X11R6 (tylko gl?.h)
Group:		X11/Development/Libraries
Requires:	%{name}-OpenGL-libs = %{version}
Requires:	%{name}-devel
Provides:	OpenGL-devel-base
Requires:	OpenGL-devel

%description OpenGL-devel-base
Base headers (only gl?.h) for OpenGL for X11R6.

%description OpenGL-devel-base -l pl
Podstawowe pliki nag��wkowe (tylko gl?.h) OpenGL dla systemu X11R6.

%package OpenGL-libs
Summary:	OpenGL libraries for X11R6
Summary(pl):	Biblioteki OpenGL dla systemu X11R6
Group:		X11/Libraries
Requires:	%{name}-libs = %{version}
Requires:	%{name}-OpenGL-core
Provides:	OpenGL
Obsoletes:	%{name}-OpenGL
Obsoletes:	Mesa

%description OpenGL-libs
OpenGL libraries for X11R6 system.

%description OpenGL-libs -l pl
Biblioteki OpenGL dla systemu X11R6.

%package OpenGL-static
Summary:	X11R6 static libraries with OpenGL
Summary(pl):	Biblioteki statyczne do X11R6 ze wsparciem dla OpenGL
Group:		X11/Development/Libraries
Requires:	%{name}-OpenGL-devel = %{version}
Provides:	OpenGL-static
Obsoletes:	Mesa-static

%description OpenGL-static
X11R6 static libraries with OpenGL.

%description OpenGL-static -l pl
Biblioteki statyczne zawieraj�ce wsparcie dla OpenGL do X11R6.

%package Xnest
Summary:	XFree86 Xnest server
Summary(pl):	Serwer XFree86 Xnest
Summary(ru):	"���������" ������ XFree86
Summary(uk):	"���������" ������ XFree86
Group:		X11/XFree86/Servers
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-common /usr/X11R6/lib/X11/rgb.txt
Requires:	XFree86-fonts-base

%description Xnest
Xnest is an X Window System server which runs in an X window. Xnest is
a 'nested' window server, actually a client of the real X server,
which manages windows and graphics requests for Xnest, while Xnest
manages the windows and graphics requests for its own clients.

You will need to install Xnest if you require an X server which will
run as a client of your real X server (perhaps for testing purposes).

%description Xnest -l pl
Xnest jest X serwerem uruchamianym w okienku innego X serwera. Xnest
zachowuje si� jak X klient w stosunku do prawdziwego X serwera, a jak
X serwer dla w�asnych klient�w.

%description Xnest -l ru
Xnest - ��� ������ X Window System, ������� �������� � ���� X. ��
����� ���� ��� ������ ��������� X-�������, ������� ��������� ������ �
������������ ��������� ��� Xnest � �� �����, ��� Xnest ���������
������ � ������������ ��������� ��� ����� ����������� ��������.

��� ���� ���������� Xnest ���� ��� ����� X-������, ������� ��������
��� ������ ������ ��������� X-������� (������ �����, � ��������
�����).

%description Xnest -l uk
Xnest - �� ������ X Window System, ���� ������ � צ�Φ X. �������� ��
�̦��� ��������� X-�������, ���� ���դ צ����� �� ���Ʀ����� ��������
��� Xnest � ��� ���, �� Xnest ���դ צ����� �� ���Ʀ����� �������� ���
��ϧ� ������� �̦��Ԧ�.

��� ����� ���������� Xnest ���� ��� ���Ҧ��� X-������, ���� ������ ��
�̦��� ������ ��������� X-������� (������ ������, � �������� æ���).

%package Xprt
Summary:	X print server
Summary(pl):	X serwer z rozszerzeniem Xprint
Group:		X11/XFree86/Servers
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-common /usr/X11R6/lib/X11/rgb.txt
Requires:	XFree86-fonts-base
PreReq:		xprint-initrc

%description Xprt
Xprt provides an X server with the print extension and special DDX
implementation.

%description Xprt -l pl
Xprt jest X serwerem z rozszerzeniem Xprint.

%package Xserver
Summary:	XFree86 X display server
Summary(de):	XFree86 Server
Summary(fr):	Serveur XFree86
Summary(pl):	Serwer XFree86
Summary(tr):	XFree86 sunucusu
Group:		X11/XFree86/Servers
Requires:	pam
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-common /usr/X11R6/lib/X11/rgb.txt
Requires:	XFree86-fonts-base
Obsoletes:	XFree86-VGA16 XFree86-SVGA XFree86-Mono
# obsoleted by many drivers: suncg3,suncg6,suncg14,sunffb,sunleo,suntcx
Obsoletes:	XFree86-Sun XFree86-Sun24
# still not supported in 4.2.0:
#Obsoletes:	XFree86-Mach8 XFree86-8514 XFree86-AGX XFree86-P9000
# (and many drivers from XF86_SVGA server... and some from others)
Obsoletes:	XFree86-XF86Setup Xconfigurator

%description Xserver
Generally used X server which uses display hardware. It requires
proper driver for your display hardware - package itself contains only
drivers for VGA and VESA-compliant cards (without acceleration). Other
drivers can be found in XFree86-driver-* packages.

%description Xserver -l de
X-Server f�r die elementarsten Framebuffer-SVGA-Ger�te, einschlie�lich
Karten, die aus ET4000-Chips, Cirrus Logic-Chips, Chips and
Technologies Laptop-Chips sowie Trident 8900 und 9000 Chips gebaut
sind. Funktioniert mit Diamond Speedstar, Orchid Kelvins, STB Nitros
und Horizons, Genoa 8500VL, den meisten Actix-Karten sowie Spider VLB
Plus und au�erdem mit vielen anderen Chips und Karten. Es lohnt sich,
diesen Server auszuprobieren, wenn Sie Probleme haben.

%description Xserver -l fr
Serveur X pour les circuits SVGA les plus simples, dont les cartes
construites avec les circuits ET4000, Cirrus Logic, Chips and
Technologies laptop, Trident 8900 et 9000. Fonctionne pour les cartes
Diamond Speedstar, Orchid Kelvins, STB Nitros et Horizons, Genoa
8500VL, la plupart des Actix et la Spider VLB Plus. Fonctionne aussi
pour de nombreux autres circuits et cartes. Essayez ce serveur si vous
avez des probl�mes.

%description Xserver -l pl
Jest to podstawowy Xserwer wy�wietlaj�cy obraz na karcie graficznej.
Do dzia�ania wymaga odpowiedniego sterownika - sam pakiet zawiera
tylko odpowiedni dla kart VGA oraz SVGA zgodnych z VESA (bez
akceleracji). Inne sterowniki mo�na znale�� w pakietach
XFree86-driver-*.

%description Xserver -l tr
ET4000, Cirrus Logic, Chips and Technologies diz�st�, Trident 8900 ve
9000 gibi basit 'framebuffer' SVGA kullananan kartlar i�in X sunucusu.
Ayn� zamanda Diamond Speedstar, Orchid Kelvins, STB Nitros / Horizons,
Genoa 8500VL, �o�u Actix kartlar�, Spider VLB Plus gibi kartlar ve
bir�ok di�er kart ile de �al���r. Herhangi bir sorun ya�arsan�z bu
sunucuyu deneyin.

%package Xvfb
Summary:	XFree86 Xvfb server
Summary(pl):	Serwer XFree86 Xvfb
Summary(ru):	������ XFree86 ��� ������������ �����������
Summary(uk):	������ XFree86 ��� צ���������� �����������
Group:		X11/XFree86/Servers
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-common /usr/X11R6/lib/X11/rgb.txt
Requires:	XFree86-fonts-base

%description Xvfb
Xvfb (X Virtual Frame Buffer) is an X Window System server that is
capable of running on machines with no display hardware and no
physical input devices. Xvfb emulates a dumb framebuffer using virtual
memory. Xvfb doesn't open any devices, but behaves otherwise as an X
display. Xvfb is normally used for testing servers. Using Xvfb, the
mfb or cfb code for any depth can be exercised without using real
hardware that supports the desired depths. Xvfb has also been used to
test X clients against unusual depths and screen configurations, to do
batch processing with Xvfb as a background rendering engine, to do
load testing, to help with porting an X server to a new platform, and
to provide an unobtrusive way of running applications which really
don't need an X server but insist on having one.

If you need to test your X server or your X clients, you may want to
install Xvfb for that purpose.

%description Xvfb -l pl
Xvfb (X Virtual Frame Buffer) jest X serwerem, kt�ry mo�na uruchamia�
na maszynach bez urz�dze� wy�wietlaj�cych ani fizycznych urz�dze�
wej�ciowych. Xvfb emuluje prosty framebuffer w pami�ci. Zwykle jest
u�ywany do testowania X serwer�w, mo�e te� by� u�ywany do testowania X
klient�w w rzadko u�ywanych konfiguracjach ekranu. Mo�na te� u�y� Xvfb
do uruchomienia aplikacji, kt�re w rzeczywisto�ci nie wymagaj� X
serwera, ale odmawiaj� uruchomienia bez niego.

%description Xvfb -l ru
Xvfb (X Virtual Frame Buffer) - ��� X-������, ������� ��������
�������� �� ������� ��� ���������� ���������� � ���������� ���������
�����. Xvfb ��������� ���������� ���������� ��������� �����������
������. Xvfb �� ��������� ������� ���������, ���� ���� ��� ����������
X-������ �� ���� ���������. ������ �� ������������ ��� ��������
��������. ��������� Xvfb, ����� ����������� ��� mfb ��� cfb ��� �����
������� ����� ��� ������������� �������� ����������, ��������������
����� �������. Xvfb ����� ����� ������������ ��� �������� X-�������� �
���������� ��������� ����� � �������������� ������, �����������
�������� ��������� � Xvfb � �������� �������� ���������, ���������
����������� �����, ��� ������ � ������������ X-������� �� �����
��������� � ��� ����������� ������� ����������, ������� ������� ��
����� X-������, �� ������� ���������� �� ���, ���� �� ��� ��������.

���� ��� ���� ����������� ���� X-������� ��� X-�������, �� ������
���������� ��� ���� ���� Xvfb.

%description Xvfb -l uk
Xvfb (X Virtual Frame Buffer) - �� X-������, ������� ��������� ��
������� ��� ��������ϧ ��������� �� צ������ ������ϧ� �����. Xvfb
������ �������Ԧ��� ���������� �������������� צ�������� ���'���. Xvfb
�� צ������� Φ���� ������ϧ�, ������ ���� �� ���������� X-������ �
���Ԧ צ�������. �������� ���� �������������� ��� ����צ��� �����Ҧ�.
�������������� Xvfb, ����� ��������� ��� mfb ��� cfb ��� ����-��ϧ
������� ������� �� ���Ʀ����æ� ������ ��� ������������ ������ϧ
���������, ��� Ц�����դ ��˦ ������. ����� Xvfb ����� ����������� ���
����צ��� X-�̦��Ԧ� � ���������� ��������� ������� �� ���Ʀ����æ���
������, ��������� ������� ������� � Xvfb � ����Ԧ �������� ���������,
��������� ��������Φ �����, ��� �������� � ��������Φ X-������� ��
���� ��������� �� ������� �������, ���� ������� �� ���Ҧ��� X-������,
��� �˦ ����������� �� ����, ��� צ� ��� ���������.

���� ��� ���Ҧ��� ��������� ��ۦ X-������� ��� X-�̦����, �� ������
���������� ��� æ�� æ̦ Xvfb.

%package devel
Summary:	X11R6 headers and programming man pages
Summary(de):	X11R6 Headers und man pages f�r Programmierer
Summary(fr):	Pages man de programmation
Summary(pl):	Pliki nag��wkowe X11R6
Summary(ru):	���������� ������������, ������ � ������������ �� ���������������� X11R6
Summary(tr):	X11R6 ile geli�tirme i�in gerekli dosyalar
Summary(uk):	��̦����� ������ͦ���, ������ �� ���������æ� �� ������������� X11R6
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}
Requires:	imake = %{version}
Obsoletes:	xpm-devel
Provides:	xpm-devel
%ifarch sparc sparc64
Obsoletes:	X11R6.1-devel
%endif

%description devel
Libraries, header files, and documentation for developing programs
that run as X clients. It includes the base Xlib library as well as
the Xt and Xaw widget sets. For information on programming with these
libraries, PLD recommends the series of books on X Programming
produced by O'Reilly and Associates.

%description devel -l de
Libraries, Header-Dateien und Dokumentation zum Entwickeln von
Programmen, die als X-Clients laufen. Enth�lt die Xlib-Library und die
Widget-S�tze Xt und Xaw. Information zum Programmieren mit diesen
Libraries finden Sie in der Buchreihe zur X-Programmierung von
O'Reilly and Associates.

%description devel -l fr
Biblioth�ques, fichiers d'en-t�te, et documentation pour d�velopper
des programmes s'ex�cutant en clients X. Cela comprend la Biblioth�que
Xlib de base aussi bien que les ensembles de widgets Xt et Xaw. Pour
des informations sur la programmation avec ces Biblioth�ques, Red Hat
recommande la s�rie d'ouvrages sur la programmation X edit�e par
O'Reilly and Associates.

%description devel -l pl
Pliki nag��wkowe, dokumentcja dla programist�w rozwijaj�cych aplikacje
klienckie pod X Window. Zawiera podstawow� bibliotek� Xlib a tak�e Xt
i Xaw. Wi�cej informacji nt. pisania program�w przy u�yciu tych
bibliotek mo�esz znale�� w ksi��kach wydawnictwa O'Reilly and
Associates (X Programming) polecanych przez Red Hata.

%description devel -l ru
XFree86-devel �������� ����������, ������ � ������������, �����������
��� ���������� ��������, ���������� ��� X-�������. XFree86-devel
�������� ������� ���������� Xlib � ������ ���������� Xt � Xaw.

���������� XFree86-devel ���� �� ����������� ������������� ���������,
������� ����� �������� ��� X-�������.

%description devel -l tr
X istemcisi olarak �al��acak programlar geli�tirmek i�in gereken
statik kitapl�klar, ba�l�k dosyalar� ve belgeler. Xlib kitapl���n�n
yan�s�ra Xt ve Xaw aray�z kitapl�klar�n� da i�erir.

%description devel -l uk
XFree86-devel ͦ����� ¦�̦�����, ������ �� ���������æ�, ����Ȧ�Φ
��� �������� �������, �˦ �������� �� X-�̦����. XFree86-devel ͦ�����
������ ¦�̦����� Xlib �� ������ ���ͦ��צ� Xt �� Xaw.

������צ�� XFree86-devel ���� �� ���������� ���������� ��������, �˦
������ ��������� �� X-�̦����.

%package driver-apm
Summary:	Alliance Promotion video driver
Summary(pl):	Sterownik do kart Alliance Promotion
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-Alliance

%description driver-apm
Alliance Promotion driver.

%description driver-apm -l pl
Sterownik do kart Alliance Promotion.

%package driver-ark
Summary:	Ark Logic video driver
Summary(pl):	Sterownik do kart Ark Logic
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-ark
Ark Logic driver.

%description driver-ark -l pl
Sterownik do kart Ark Logic.

%package driver-ati
Summary:	ATI video driver
Summary(pl):	Sterownik do kart ATI
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-ATI XFree86-Mach32 XFree86-Mach64

%description driver-ati
ATI video driver.

%description driver-ati -l pl
Sterownik do kart ATI.

%package driver-r128
Summary:	ATI Rage 128 video driver
Summary(pl):	Sterownik do kart ATI Rage 128
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Requires:	OpenGL
Conflicts:	XFree86-driver-nvidia
Obsoletes:	XFree86-Rage128

%description driver-r128
ATI Rage 128 video driver.

%description driver-r128 -l pl
Sterownik do kart ATI Rage 128.

%package driver-radeon
Summary:	ATI Radeon video driver
Summary(pl):	Sterownik do kart ATI Radeon
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Requires:	XFree86-driver-ati
Requires:	OpenGL
Conflicts:	XFree86-driver-nvidia

%description driver-radeon
ATI Radeon video driver.

%description driver-radeon -l pl
Sterownik do kart ATI Radeon.

%package driver-ati.2
Summary:	ATI video driver (ATI.2)
Summary(pl):	Sterownik do kart ATI (ATI.2)
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-ATI XFree86-Mach32 XFree86-Mach64

%description driver-ati.2
ATI video driver (ATI.2) from gatos (http://gatos.sourceforge.net/).

%description driver-ati.2 -l pl
Sterownik do kart ATI (ATI.2) projektu gatos
(http://gatos.sourceforge.net/).

%package driver-r128.2
Summary:	ATI Rage 128 video driver (ATI.2)
Summary(pl):	Sterownik do kart ATI Rage 128 (ATI.2)
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Requires:	OpenGL
Requires:	XFree86-driver-ati.2
Conflicts:	XFree86-driver-nvidia
Obsoletes:	XFree86-Rage128

%description driver-r128.2
ATI Rage 128 video driver (ATI.2) from gatos
(http://gatos.sourceforge.net/).

%description driver-r128.2 -l pl
Sterownik do kart ATI Rage 128 (ATI.2) projektu gatos
(http://gatos.sourceforge.net/).

%package driver-radeon.2
Summary:	ATI Radeon video driver (ATI.2)
Summary(pl):	Sterownik do kart ATI Radeon (ATI.2)
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Requires:	XFree86-driver-ati.2
Requires:	OpenGL
Conflicts:	XFree86-driver-nvidia

%description driver-radeon.2
ATI Radeon video driver (ATI.2) from gatos
(http://gatos.sourceforge.net/).

%description driver-radeon.2 -l pl
Sterownik do kart ATI Radeon (ATI.2) projektu gatos
(http://gatos.sourceforge.net/).

%package driver-chips
Summary:	Chips and Technologies video driver
Summary(pl):	Sterownik do kart na uk�adach Chips and Technologies
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-ChipsTechnologies

%description driver-chips
Chips and Technologies video driver.

%description driver-chips -l pl
Sterownik do kart na uk�adach Chips and Technologies.

%package driver-cirrus
Summary:	Cirrus Logic video driver
Summary(pl):	Sterownik do kart Cirrus Logic
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-Cirrus

%description driver-cirrus
Cirrus Logic video driver.

%description driver-cirrus -l pl
Sterownik do kart Cirrus Logic.

%package driver-cyrix
Summary:	Cyrix video driver
Summary(pl):	Sterownik do grafiki na uk�adzie Cyrix MediaGX
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-Cyrix

%description driver-cyrix
Cyrix video driver.

%description driver-cyrix -l pl
Sterownik do grafiki na uk�adzie Cyrix MediaGX.

%package driver-fbdev
Summary:	Video driver for framebuffer device
Summary(pl):	Sterownik korzystaj�cy z framebuffera
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-FBDev

%description driver-fbdev
Non-accelerated video driver for framebuffer device.

%description driver-fbdev -l pl
Nieakcelerowany sterownik korzystaj�cy z framebuffera.

%package driver-ffb
Summary:	Video driver for DRI sparc framebuffer device
Summary(pl):	Sterownik do framebuffera DRI na sparc
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-ffb
Video driver for DRI sparc framebuffer device.

%description driver-ffb -l pl
Sterownik do framebuffera DRI na sparc.

%package driver-glide
Summary:	3Dfx Voodoo1 and Voodoo2 video driver
Summary(pl):	Sterownik do kart 3Dfx Voodoo1 i Voodoo2
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-glide
Voodoo1 and Voodoo2 video driver.

%description driver-glide -l pl
Sterownik do kart Voodoo1 i Voodoo2 firmy 3Dfx.

%package driver-glint
Summary:	GLINT/Permedia video driver
Summary(pl):	Sterownik do kart GLINT i Permedia
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Requires:	OpenGL
Conflicts:	XFree86-driver-nvidia
Obsoletes:	XFree86-3DLabs

%description driver-glint
GLINT/Permedia video driver.

%description driver-glint -l pl
Sterownik do kart GLINT i Permedia.

%package driver-i128
Summary:	Number 9 I128 video driver
Summary(pl):	Sterownik do kart Number 9 I128
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-I128

%description driver-i128
Number 9 I128 video driver.

%description driver-i128 -l pl
Sterownik do kart Number 9 I128.

%package driver-i740
Summary:	Intel i740 video driver
Summary(pl):	Sterownik do kart na uk�adzie Intel i740
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-i740

%description driver-i740
Intel i740 video driver.

%description driver-i740 -l pl
Sterownik do kart na uk�adzie Intel i740.

%package driver-i810
Summary:	Intel i810/i815/i830 video driver
Summary(pl):	Sterownik do grafiki na uk�adach Intel i810/i815/i830
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Requires:	OpenGL
Conflicts:	XFree86-driver-nvidia
Obsoletes:	XFree86-i810

%description driver-i810
Intel i810/i815/i830 video driver.

%description driver-i810 -l pl
Sterownik do grafiki na uk�adach Intel i810/i815/i830.

%package driver-imstt
Summary:	Integrated Micro Solutions Twin Turbo 128 driver
Summary(pl):	Sterownik do kart Integrated Micro Solutions Twin Turbo 128
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-imstt
Integrated Micro Solutions Twin Turbo 128 driver.

%description driver-imstt -l pl
Sterownik do kart Integrated Micro Solutions Twin Turbo 128.

%package driver-mga
Summary:	Matrox video driver
Summary(pl):	Sterownik do kart Matrox
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Requires:	OpenGL
Conflicts:	XFree86-driver-nvidia
Obsoletes:	XFree86-mga

%description driver-mga
Matrox video driver.

%description driver-mga -l pl
Sterownik do kart Matrox.

%package driver-neomagic
Summary:	NeoMagic video driver
Summary(pl):	Sterownik do kart NeoMagic
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-NeoMagic

%description driver-neomagic
NeoMagic video driver.

%description driver-neomagic -l pl
Sterownik do kart NeoMagic.

%package driver-newport
Summary:	Newport (XL) adapters video driver
Summary(pl):	Sterownik do kart Newport (XL)
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-newport
Newport (XL) adapters video driver (found primarily in SGI Indy and
Indigo2 machines).

%description driver-newport -l pl
Sterownik do kart Newport (XL) (wyst�puj�cych g��wnie w komputerach
SGI Indy i Indigo).

%package driver-nsc
Summary:	National Semiconductors GEODE family video driver
Summary(pl):	Sterownik dla kart na uk�adach z rodziny GEODE firmy National Semiconductors
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-nsc
National Semiconductors GEODE family video driver. Supports GXLV (5530
companion chip), SC1200, SC1400 and GX2 (5535 companion chip).

%description driver-nsc -l pl
Sterownik dla kart na uk�adach z rodziny GEODE firmy National
Semiconductors. Obs�uguje GXLV (uk�ad towarzysz�cy 5530), SC1200,
SC1400 oraz GX2 (uk�ad towarzysz�cy 5535).

%package driver-nv
Summary:	nVidia video driver
Summary(pl):	Sterownik do kart na uk�adach firmy nVidia
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-NVidia

%description driver-nv
nVidia video driver. Supports Riva128, RivaTNT, GeForce.

%description driver-nv -l pl
Sterownik do kart na uk�adach firmy nVidia: Riva128, RivaTNT, GeForce.

%package driver-rendition
Summary:	Rendition video driver
Summary(pl):	Sterownik do kart Rendition
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-Rendition

%description driver-rendition
Rendition/Micron video driver.

%description driver-rendition -l pl
Sterownik do kart Verite firmowanych przez Rendition/Micron.

%package driver-s3virge
Summary:	S3 ViRGE/Trio3D video driver
Summary(pl):	Sterownik do kart na uk�adach S3 ViRGE i Trio3D
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-S3V

%description driver-s3virge
S3 ViRGE/Trio3D video driver.

%description driver-s3virge -l pl
Sterownik do kart na uk�adach S3 ViRGE i Trio3D.

%package driver-s3
Summary:	S3 Trio video driver
Summary(pl):	Sterownik do kart na uk�adach S3 Trio
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-S3

%description driver-s3
S3 Trio video driver.

%description driver-s3 -l pl
Sterownik do kart na uk�adach S3 Trio.

%package driver-savage
Summary:	S3 Savage video driver
Summary(pl):	Sterownik do kart na uk�adach S3 Savage
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-savage
S3 Savage video driver.

%description driver-savage -l pl
Sterownik do kart na uk�adach S3 Savage.

%package driver-siliconmotion
Summary:	Silicon Motion video driver
Summary(pl):	Sterownik do kart na uk�adach Silicon Motion
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-siliconmotion
Silicon Motion video driver.

%description driver-siliconmotion -l pl
Sterownik do kart na uk�adach Lynx firmy Silicon Motion.

%package driver-sis
Summary:	SiS video driver
Summary(pl):	Sterownik do kart na uk�adach SiS
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-SiS

%description driver-sis
SiS video driver.

%description driver-sis -l pl
Sterownik do kart na uk�adach SiS.

%package driver-sunbw2
Summary:	sunbw2 - Sun BW2 video driver
Summary(pl):	Sterownik do monochromatycznego framebuffera BW2 na Sunie
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-SunMono

%description driver-sunbw2
sunbw2 - Sun BW2 video driver.

%description driver-sunbw2 -l pl
Sterownik do monochromatycznego framebuffera BW2 na Sunie.

%package driver-suncg14
Summary:	suncg14 - Sun CG14 video driver
Summary(pl):	Sterownik do kolorowego framebuffera CG14 na Sunie
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-suncg14
suncg14 - Sun CG14 video driver.

%description driver-suncg14 -l pl
Sterownik do kolorowego framebuffera CG14 na Sunie.

%package driver-suncg3
Summary:	suncg3 - Sun CG3 video cards driver
Summary(pl):	Sterownik do kolorowego framebuffera CG3 na Sunie
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-suncg3
suncg3 - Sun CG3 video cards driver.

%description driver-suncg3 -l pl
Sterownik do kolorowego framebuffera CG3 na Sunie.

%package driver-suncg6
Summary:	suncg6 - Sun GX and Turbo GX video driver
Summary(pl):	Sterownik do grafiki GX i Turbo GX na Sunie
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-suncg6
suncg6 - Sun GX and Turbo GX video driver.

%description driver-suncg6 -l pl
Sterownik do grafiki GX i Turbo GX na Sunie.

%package driver-sunffb
Summary:	sunffb - Sun Creator, Creator 3D and Elite 3D video cards driver
Summary(pl):	Sterownik do kart Sun Creator, Creator 3D, Elite 3D
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-sunffb
sunffb - Sun Creator, Creator 3D and Elite 3D video cards driver.

%description driver-sunffb -l pl
Sterownik do kart Sun Creator, Creator 3D, Elite 3D.

%package driver-sunleo
Summary:	sunleo - Sun Leo (ZX) video cards driver
Summary(pl):	Sterownik do kart Sun Leo (ZX)
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-sunleo
sunleo - Sun Leo (ZX) video cards driver.

%description driver-sunleo -l pl
Sterownik do kart Sun Leo (ZX).

%package driver-suntcx
Summary:	suntcx - Sun TCX video cards driver
Summary(pl):	Sterownik do kart Sun TCX
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-suntcx
suntcx - Sun TCX video cards driver.

%description driver-suntcx -l pl
Sterownik do kart Sun TCX.

%package driver-tdfx
Summary:	3Dfx video driver
Summary(pl):	Sterownik do kart 3Dfx
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Requires:	OpenGL
Requires:	Glide3-DRI
Conflicts:	XFree86-driver-nvidia
Obsoletes:	XFree86-3dfx

%description driver-tdfx
3Dfx video driver. Supports Voodoo Banshee, Voodoo3, Voodoo4, Voodoo5.
For Banshee or Voodoo3, DRI driver requires Glide_V3-DRI package, for
Voodoo4 or Voodoo5 it requires Glide_V5-DRI package.

%description driver-tdfx -l pl
Sterownik do kart 3Dfx: Voodoo Banshee, Voodoo3, Voodoo4, Voodoo5.
Sterownik DRI wymaga pakietu Glide_V3-DRI do kart Banshee lub Voodoo3,
a Glide_V5-DRI do kart Voodoo4 lub Voodoo5.

%package driver-tga
Summary:	TGA video driver
Summary(pl):	Sterownik do kart TGA
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-TGA

%description driver-tga
TGA video driver.

%description driver-tga -l pl
Sterownik do kart TGA.

%package driver-trident
Summary:	Trident video driver
Summary(pl):	Sterownik do kart Trident
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-Trident

%description driver-trident
Trident video driver.

%description driver-trident -l pl
Sterownik do kart Trident.

%package driver-tseng
Summary:	Tseng Labs video driver
Summary(pl):	Sterownik do kart Tseng Labs
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}
Obsoletes:	XFree86-Tseng XFree86-W32

%description driver-tseng
Tseng Labs video driver.

%description driver-tseng -l pl
Sterownik do kart firmy Tseng Labs.

%package driver-via
Summary:	VIA CLE266 driver
Summary(pl):	Sterownik do kart VIA CLE266
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-via
VIA CLE266 driver.

%description driver-via -l pl
Sterownik do kart VIA CLE266.

%package driver-vmware
Summary:	VMWare SVGA emulated video driver
Summary(pl):	Sterownik do emulacji karty SVGA dost�pnej pod VMware
Group:		X11/XFree86
Requires:	%{name}-modules = %{version}-%{release}
Requires:	%{name}-Xserver = %{version}-%{release}

%description driver-vmware
VMware emulated SVGA video driver. Necessary if you run Linux on
VMware virtual machine.

%description driver-vmware -l pl
Sterownik do emulacji karty SVGA dost�pnej pod VMware. Przydatny,
je�li uruchamiasz Linuksa na wirtualnej maszynie VMware.

%package libs
Summary:	X11R6 shared libraries
Summary(de):	X11R6 shared Libraries
Summary(es):	Bibliotecas compartidas X11R6
Summary(fr):	Biblioth�ques partag�es X11R6
Summary(pl):	Biblioteki dzielone dla X11R6
Summary(pt_BR):	Bibliotecas compartilhadas X11R6
Summary(ru):	����������� ���������� ��� X Window System (X11R6.4)
Summary(uk):	��̦����� �Ц������ ������������ ��� X Window System (X11R6.4)
Group:		X11/XFree86
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	grep
Requires(postun):	fileutils
Requires:	%{name}-common = %{version}
Obsoletes:	xpm
Provides:	xpm

%ifarch sparc sparc64
Obsoletes:	X11R6.1-libs
%endif

%description libs
XFree86-libs contains the shared libraries that most X programs need
to run properly. These shared libraries are in a separate package in
order to reduce the disk space needed to run X applications on a
machine without an X server (i.e, over a network).

If you are installing the X Window System on your machine, you will
need to install XFree86-libs. You will also need to install the
XFree86 package, XFree86-Xserver, one of the XFree86-driver-*,
XFree86-fonts, XFree86-fonts-ISO8859-1, optionally some of the other
fonts (choose 75dpi or 100dpi depending upon your monitor's
resolution), the XFree86-setup and the XFree86-tools. And, finally, if
you are going to be developing applications that run as X clients, you
will also need to install XFree86-devel.

%description libs -l de
Dieses Paket enth�lt die zur gemeinsamen Nutzung vorgesehenen
Libraries, die die meisten X-Programme f�r den einwandfreien Betrieb
ben�tigen. Sie wurden in einem separaten Paket untergebracht, um den
Festplattenspeicherplatz auf Computern zu reduzieren, die ohne einen
X- Server (�ber ein Netz) arbeiten.

%description libs -l es
Este paquete contiene bibliotecas compartidas que la mayor�a de los
programas X necesitan para ejecutarse correctamente. Est�n en un
paquete a parte, para reducir el espacio en disco necesario para
ejecutar aplicaciones X en una m�quina sin un servidor X (a trav�s de
la red).

%description libs -l fr
Ce paquetage contient les biblioth�ques partag�es n�cessaires � de
nombreux programmes X. Elles se trouvent dans un paquetage s�par� afin
de r�duire l'espace disque n�cessaire � l'ex�cution des applications X
sur une machine sans serveur X (en r�seau).

%description libs -l pl
Pakiet zawieraj�cy podstawowe biblioteki potrzebne wi�kszo�ci
program�w korzystaj�cych z systemu X Window. Wydzielony w celu
oszcz�dno�ci miejsca potrzebnego do uruchamiania aplikacji X Window na
komputerach bez X serwera (np. przez sie�).

%description libs -l pt_BR
Este pacote cont�m bibliotecas compartilhadas que a maioria dos
programas X precisam para rodar corretamente. Eles est�o em um pacote
separado para reduzir o espa�o em disco necess�rio para rodar
aplica��es X em uma m�quina sem um servidor X (atrav�s da rede).

%description libs -l tr
Bu paket X programlar�n�n d�zg�n �al��abilmeleri i�in gereken
kitapl�klar� i�erir. Bunlar, X programlar�n� (sunucu olsun olmas�n)
�al��t�rmak i�in gerekli disk alan�n� azaltmak i�in ayr� bir paket
olarak sunulmu�tur.

%description libs -l ru
XFree86-libs �������� ����������� ����������, ������� ���������� ���
������ ����������� �������� ��� X. ��� ���������� �������� � ���������
����� ����� ���������� �������� ������������, ����������� ��� �������
���������� X �� ������� ��� X-������� (��������, �� ����).

���� �� �������������� X Window System �� ����� ������, ��� ����������
���������� XFree86-libs. ����� ���������� ���������� ��������� ������:
XFree86, ���� ��� ��������� ������� ������� XFree86, Xconfigurator,
XFree86-xfs.

���� �� ����������� ������������� ���������, ���������� ��� X-�������,
��� ����� ���� ���������� XFree86-devel.

%description libs -l uk
XFree86-libs ͦ����� ¦�̦����� �Ц������ ������������, ���Ҧ
����Ȧ�Φ ��� ������ ¦�����Ԧ ���������� ������� ��� X. � ¦�̦�����
������Φ � ������� ����� ��� �����ͦ� ��������� ��������, ����Ȧ�����
��� ������� ���������� ������� X �� ������� ��� X-������� (���������,
�� ����֦).

���� �� ������������ X Window System �� ��ۦ� ����Φ, ��� ����Ȧ���
���������� XFree86-libs. ����� ����Ȧ��� ���������� ��˦ ������:
XFree86, ���� ��� ��˦���� ����Ԧ� ����Ԧ� XFree86, Xconfigurator,
XFree86-xfs.

���� �� ���������� ���������� ��������, �˦ �������� �� X-�̦����, ���
����� ����Ȧ��� ���������� XFree86-devel.

%package modules
Summary:	Modules with X servers extensions
Summary(pl):	Wsp�lne dla wszystkich X serwer�w modu�y rozszerze�
Group:		X11/XFree86

%description modules
Modules with X servers extensions.

%description modules -l pl
Wsp�lne dla wszystkich X serwer�w modu�y rozszerze�.

%package setup
Summary:	Graphical configuration tool for XFree86
Summary(pl):	Graficzny konfigurator dla XFree86
Summary(ru):	������� ��� ������������ XFree86
Summary(uk):	���̦�� ��� ���Ʀ��������� XFree86
Group:		X11/XFree86
Requires:	%{name}-Xserver = %{version}
Obsoletes:	XFree86-xf86cfg

%description setup
Setup containst a configuration tool for the XFree86 family of
servers. It allows you to configure video settings, keyboard layouts,
mouse type, and other miscellaneous options. It is slow however, and
requires the generic VGA 16 color server be available.

%description setup -l pl
Pakiet setup zawiera narz�dzia do konfiguracji XFree86. Pozwala na
skonfigurowanie ustawie� obrazu, klawiatury, typu myszki i innych
r�nych rzeczy. Jednak�e jest wolny i wymaga dost�pno�ci serwera do
standardowej 16-kolorowej VGA.

%description setup -l ru
������� ��� ������������ XFree86.

%description setup -l uk
���̦�� ��� ���Ʀ��������� XFree86.

%package static
Summary:	X11R6 static libraries
Summary(pl):	Biblioteki statyczne X11R6
Summary(ru):	����������� ���������� X11R6
Summary(uk):	������Φ ¦�̦����� X11R6
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}
%ifarch sparc sparc64
Obsoletes:	X11R6.1-devel
%endif
Obsoletes:	xpm-static
#Obsoletes:	Mesa-static

%description static
X11R6 static libraries.

%description static -l pl
Biblioteki statyczne X11R6.

%description static -l ru
XFree86-static �������� ����������� ����������, ����������� ���
���������� ��������, ���������� ��� X-�������. ��������� ���������,
������� ����� �������� ��� X-�������.

%description static -l uk
XFree86-static ͦ����� ������Φ ¦�̦�����, ����Ȧ�Φ ��� ��������
�������, �˦ �������� �� X-�̦����.

%package tools
Summary:	Various tools for XFree86
Summary(pl):	R�ne narz�dzia dla XFree86
Summary(ru):	������������� ������� ��� XFree86
Summary(uk):	������Φ�Φ ���̦�� ��� XFree86
Group:		X11/XFree86
Requires:	%{name} >= %{version}
Requires:	XFree86-libs = %{version}
Requires:	man-config
Obsoletes:	X11R6-contrib

%description tools
Various tools for X, including listres, xbiff, xedit, xeyes, xcalc,
xload and xman, among others.

If you're using X, you should install XFree86-tools. You will also
need to install the XFree86 package, the XFree86 package which
corresponds to your video card, some of the XFree86 fonts packages,
the XFree86-setup package and the XFree86-libs package.

Finally, if you are going to develop applications that run as X
clients, you will also need to install XFree86-devel.

This package contains all applications that used to be in
X11R6-contrib in older releases.

%description tools -l pl
R�ne narz�dzia dla X, w tym listres, xbiff, xedit, xeyes, xcalc,
xload, xman i inne.

Je�li u�ywasz X�w powiniene� zainstalowa� XFree86-tools. B�dziesz
r�wnie� musia� zainstalowa� pakiet XFree86, pakiet odpowiadaj�cy
Twojej karcie graficznej, jeden z pakiet�w z fontami, pakiet
Xconfigurator oraz XFree86-libs.

Wreszcie, je�li zamierzasz tworzy� aplikacje, kt�re dzia�aj� jako
klienci X, b�dziesz musia� zainstalowa� r�wnie� XFree86-devel.

Ten pakiet zawiera aplikacje, kt�re by�y w X11R6-contrib w starszych
wersjach X.

%description tools -l ru
������������� ������� ��� X, ������� listres, xbiff, xedit, xeyes,
xcalc, xload, xman � ������.

���� �� �������������� X Window System, ��� ���� ����������
XFree86-tools. ����� ��� ����� ���������� ���������� ����� ������:
XFree86, Xconfigurator, XFree86-xfs � XFree86-libs. ��������, ��� ����
���������� � ������ ������ ������� XFree86.

���� �� ����������� ������������� ���������, ���������� ��� X-�������,
��� ����� ���� ���������� XFree86-devel.

���� ����� �������� ��� ���������, ������� ������ ���������� �
X11R6-contrib.

%description tools -l uk
������Φ�Φ ���̦�� ��� X, ��������� listres, xbiff, xedit, xeyes,
xcalc, xload, xman �� ��ۦ.

���� �� ������������ X Window System, ��� ����Ȧ��� ����������
XFree86-tools. ����� ����� ���������� ��˦ ������: XFree86,
Xconfigurator, XFree86-xfs �� XFree86-libs. �������, ��� �����
���������� � ��ۦ ������ ����Ԧ� XFree86.

���� �� ���������� ���������� ��������, �˦ �������� �� X-�̦����, ���
����� ����Ȧ��� ���������� XFree86-devel.

��� ����� ͦ����� �Ӧ ��������, �˦ ��Φ�� ������� �� X11R6-contrib.

%package -n imake
Summary:	C preprocessor interface to the make utility
Summary(pl):	Miedzymordzie do make oparte o preprocesor C
Group:		Development/Building

%description -n imake
Imake is used to generate Makefiles from a template, a set of cpp
macro functions, and a per-directory input file called an Imakefile.
This allows machine dependencies (such as compiler options, alternate
command names, and special make rules) to be kept separate from the
descriptions of the various items to be built.

%description -n imake -l pl
Imake jest u�ywany do generowania plik�w Makefile na bazie szablonu,
zbioru makr preprocesora C oraz (dla ka�dego podkatalogu) pliku
wej�ciowego Imakefile. Pozwala to na oddzielenie informacji zale�nych
od �rodowiska kompilacji (takich jak opcje kompilatora, alternatywne
nazwy komend i regu�y specjalne) od opisu r�nych element�w kt�re maj�
by� kompilowane.

%package -n sessreg
Summary:	sessreg - manage utmp/wtmp entries for non-init clients
Summary(pl):	Program do zarz�dzania wpisami w utmp/wtmp
Group:		X11/XFree86

%description -n sessreg
sessreg is a simple program for managing utmp/wtmp entries for xdm
sessions.

System V has a better interface to /var/run/utmp than BSD; it
dynamically allocates entries in the file, instead of writing them at
fixed positions indexed by position in /etc/ttys.

%description -n sessreg -l pl
sessreg jest prostym programem do zarz�dzania wpisami w utmp/wtmp dla
sesji xdm.

System V ma lepszy ni� BSD interfejs do /var/run/utmp; dynamicznie
alokuje wpisy w pliku, zamiast zapisywania ich na ustalonych pozycjach
indeksowanych po�o�eniem w /etc/ttys.

%package -n twm
Summary:	Tab Window Manager for the X Window System
Summary(pl):	Twm - podstawowy zarz�dca okien dla X Window System
Summary(ru):	������� ������� ��������
Summary(uk):	������� צ������ ��������
Group:		X11/Window Managers
Requires:	XFree86-libs = %{version}

%description -n twm
Twm is a window manager for the X Window System. It provides
titlebars, shaped windows, several forms of icon management,
user-defined macro functions, click-to-type and pointerdriven keyboard
focus, and user-specified key and pointer button bindings.

%description -n twm -l pl
Twm jest zarz�dc� okien dla X Window System. Daje belki tytu�owe,
ramki okien, par� form zarz�dzania ikonami, definiowalne makra,
ustawianie focusu klikni�ciem lub po�o�eniem wska�nika myszy,
definiowalne przypisania klawiszy i przycisk�w myszy.

%description -n twm -l ru
������� ���������� ������� ��������.

%description -n twm -l uk
������� ���������� צ������ ��������.

%package -n xauth
Summary:	xauth - X authority file utility
Summary(pl):	xauth - narz�dzie do plik�w X authority
Group:		X11/XFree86
Requires:	%{name}-libs = %{version}

%description -n xauth
The xauth program is used to edit and display the authorization
information used in connecting to the X server. This program is
usually used to extract authorization records from one machine and
merge them in on another (as is the case when using remote logins or
granting access to other users).

%description -n xauth -l pl
Program xauth s�u�y do edycji i wy�wietlania informacji
autoryzacyjnych u�ywanych przy ��czeniu z Xserwerem. Ten program
przewa�nie jest u�ywany do wyci�gania rekord�w autoryzacji z jednej
maszyny i do��czania ich na innej (w celu umo�liwienia zdalnego
logowania lub udost�pnienia innym u�ytkownikom).

%package -n xdm
Summary:	xdm - X Display Manager with support for XDMCP, host chooser
Summary(pl):	XDM - zarz�dca ekran�w z obs�ug� XDMCP i wybieraniem host�w
Summary(ru):	�������� ������� X
Summary(uk):	�������� ������� X
Group:		X11/XFree86
Requires:	%{name} = %{version}
Requires:	pam >= 0.71
Requires:	%{name}-libs = %{version}
Requires:	sessreg = %{version}
Requires:	/usr/X11R6/bin/sessreg
Provides:	XDM
PreReq:		chkconfig
Obsoletes:	XFree86-xdm
Obsoletes:	gdm
Obsoletes:	kdm

%description -n xdm
Xdm manages a collection of X displays, which may be on the local host
or remote servers. The design of xdm was guided by the needs of X
terminals as well as the X Consortium standard XDMCP, the X Display
Manager Control Protocol.

%description -n xdm -l pl
Xdm zarz�dza zestawem ekran�w X, kt�re mog� by� lokalne lub na
zdalnych serwerach. Zosta� zaprojektowany zgodnie z potrzebami X
terminali oraz standardem X Consortium XDMCP.

%description -n xdm -l ru
�������� ������� X.

%description -n xdm -l uk
�������� ������� X.

%package -n xfs
Summary:	Font server for XFree86
Summary(pl):	Serwer font�w dla XFree86
Summary(ru):	���������� ��� X Window System
Summary(uk):	���������� ��� X Window System
Group:		X11/XFree86
Requires:	%{name}-libs = %{version}
Requires:	XFree86-fonts-base
PreReq:		chkconfig
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/useradd
Requires(pre):	/usr/sbin/groupadd
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Obsoletes:	xfsft XFree86-xfs

%description -n xfs
This is a font server for XFree86. You can serve fonts to other X
servers remotely with this package, and the remote system will be able
to use all fonts installed on the font server, even if they are not
installed on the remote computer.

%description -n xfs -l pl
Pakiet zawiera serwer font�w dla XFree86. Mo�e udost�pnia� fonty dla X
serwer�w lokalnych lub zdalnych.

%description -n xfs -l ru
XFree86-xfs �������� ������ ������� ��� XFree86. Xfs ����� �����
������������� ������ ��������� X-��������. ��������� ������� �����
�������� ������������ ��� ������, ������������� �� ������� �������,
���� ���� ��� �� ����������� �� ��������� ����������.

�� ������ ���������� XFree86-xfs ���� �� �������������� X Window
System. ����� ��� �������� ���������� ��������� ������: XFree86,
�����(�) ������� XFree86, ����������� ��� ����� �������, Xconfigurator
� XFree86-libs.

%description -n xfs -l uk
XFree86-xfs ͦ����� ������ ����Ԧ� ��� XFree86. Xfs ����� ����
�������� ������ צ�������� X-��������. ��������� ������� �����
��������������� �Ӧ ������, �˦ ���������Φ �� �����Ҧ ����Ԧ�, ��צ��
���� ���� �� ���������Φ �� צ��������� ����'���Ҧ.

�� �����Φ ���������� XFree86-xfs ���� �� ������������ X Window
System. ����� ��� ���������� ���������� ������Φ ������: XFree86,
�����(�) ����Ԧ� XFree86, ����Ȧ�Φ ��� ���ϧ �������, Xconfigurator
�� XFree86-libs.

#--- %prep ---------------------------

%prep
%setup -q -c -b3
#-b1 -b2 -a3
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p1
%patch5 -p0
%patch6 -p0
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
#%patch11 -p0	-- obsoleted???
%patch12 -p1
%patch13 -p1
%patch14 -p0
%patch15 -p1
%patch16 -p0
#%patch17 -p1	-- not ready, is it required?
%patch18 -p1
#%patch19 -p1	-- maybe should be updated to allow using make -j
%patch20 -p0
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%ifarch sparc sparc64
#%patch28 -p1	-- needs update
%endif
%patch29 -p0
%patch30 -p1
%patch32 -p1
%patch33 -p1
#%patch34 -p1	-- seems not applied (was partially in rc1??? maybe another fix present?)
#%patch35 -p1	-- obsoleted? (but doesn't look to be applied)
%{!?_without_tdfx:%patch36 -p0}
%{!?_without_tdfx:%patch37 -p1}
#%patch38 -p0	-- causing problems IIRC (but not really needed)
%{!?_without_tdfx:%patch39 -p0}
%patch40 -p1
%{!?debug:%patch41 -p1}
%{?_without_tdfx:%patch42 -p0}
%patch43 -p0
%patch44 -p0
%patch45 -p1
%patch46 -p1
%patch47 -p0
#%patch48 -p1	-- seems applied

rm -f xc/config/cf/host.def

#Remove fonts dir for faster build
# only valid for snapshots
rm -rf xc/fonts

# New ATI drivers
# cd xc/programs/Xserver/hw/xfree86/drivers
#%bzcat %{SOURCE39} | tar x
# ati.2 directory

#--- %build --------------------------

%build
%{__make} -S -C xc World DEFAULT_OS_CPU_FROB=%{_target_cpu} \
	CC="%{__cc}" \
	BOOTSTRAPCFLAGS="%{rpmcflags}" \
	CCOPTIONS="%{rpmcflags}" \
	CXXOPTIONS="%{rpmcflags}" \
	CXXDEBUGFLAGS="" \
	CDEBUGFLAGS="" \
	ICONDIR="%{_icondir}" \
	LINUXDIR="%{_kernelsrcdir}"

%ifnarch alpha
#%%{__make} -C xc/programs/Xserver/hw/xfree86/drivers SUBDIRS="ati.2" Makefiles
#%%{__make} -C xc/programs/Xserver/hw/xfree86/drivers SUBDIRS="ati.2" all \
#	"BOOTSTRAPCFLAGS=%{rpmcflags}" \
#	"CCOPTIONS=%{rpmcflags}" \
#	"CXXOPTIONS=%{rpmcflags}" \
#	"CXXDEBUGFLAGS=" "CDEBUGFLAGS="
%endif

#--- %install ------------------------

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/{X11/fs,pam.d,rc.d/init.d,security/console.apps,sysconfig} \
	$RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/{cs,da,de,es,fr,hu,it,ja,ko,nl,pl,pt,ru,sk,zh_CN.gb2312,zh_TW.big5} \
	$RPM_BUILD_ROOT%{_datadir}/misc \
	$RPM_BUILD_ROOT%{_sbindir} \
	$RPM_BUILD_ROOT/usr/{bin,include,lib} \
	$RPM_BUILD_ROOT/var/{log,lib/xkb} \
	$RPM_BUILD_ROOT%{_applnkdir}/{Amusements,Editors,Utilities,Terminals} \
	$RPM_BUILD_ROOT{%{_pixmapsdir}/mini,%{_wmpropsdir},%{_soundsdir},%{_themesdir}/{Default,ThinIce}}

%{__make} -C xc	install	install.man \
	DESTDIR="$RPM_BUILD_ROOT" \
	DOCDIR="/usr/share/doc/%{name}-%{version}" \
	INSTBINFLAGS="-m 755" \
	INSTPGMFLAGS="-m 755" \
	RAWCPP="/lib/cpp" \
	BOOTSTRAPCFLAGS="%{rpmcflags}" \
	CCOPTIONS="%{rpmcflags}" \
	CXXOPTIONS="%{rpmcflags}" \
	CXXDEBUGFLAGS="" \
	CDEBUGFLAGS="" \
	ICONDIR="%{_icondir}" \
	LINUXDIR="%{_kernelsrcdir}"

%ifnarch alpha
#install -d $RPM_BUILD_ROOT%{_libdir}/modules.gatos/{drivers,dri}
#install xc/programs/Xserver/hw/xfree86/drivers/ati.2/*_drv.o \
#	$RPM_BUILD_ROOT%{_libdir}/modules.gatos/drivers
#install xc/programs/Xserver/hw/xfree86/drivers/ati.2/*_dri.o \
#	$RPM_BUILD_ROOT%{_libdir}/modules.gatos/dri

%endif

# setting default X
rm -f $RPM_BUILD_ROOT%{_bindir}/X
ln -sf XFree86 $RPM_BUILD_ROOT%{_bindir}/X

# setting ghost X in /etc/X11 -- xf86config will fix this ...
ln -sf %{_bindir}/XFree86 $RPM_BUILD_ROOT%{_sysconfdir}/X11/X

# add X11 links in /usr/bin, /usr/lib /usr/include
ln -sf %{_includedir}/X11 $RPM_BUILD_ROOT/usr/include/X11
ln -sf %{_libdir}/X11 $RPM_BUILD_ROOT/usr/lib/X11
ln -sf %{_bindir} $RPM_BUILD_ROOT/usr/bin/X11

# fix libGL*.so links
rm -f $RPM_BUILD_ROOT%{_libdir}/libGL*.so
ln -sf libGL.so.1 $RPM_BUILD_ROOT%{_libdir}/libGL.so
ln -sf libGLU.so.1 $RPM_BUILD_ROOT%{_libdir}/libGLU.so

# set up PLD xdm config
rm -f $RPM_BUILD_ROOT%{_sysconfdir}/X11/xdm/{*Console,Xaccess,Xsession,Xsetup*}
install xdm-xinitrc-*/pixmaps/* $RPM_BUILD_ROOT%{_sysconfdir}/X11/xdm/pixmaps
install xdm-xinitrc-*/{*Console,Xaccess,Xsession,Xsetup*} $RPM_BUILD_ROOT%{_sysconfdir}/X11/xdm

install %{SOURCE4} $RPM_BUILD_ROOT/etc/pam.d/xdm
install %{SOURCE5} $RPM_BUILD_ROOT/etc/pam.d/xserver
install %{SOURCE6} $RPM_BUILD_ROOT/etc/rc.d/init.d/xdm
install %{SOURCE7} $RPM_BUILD_ROOT/etc/rc.d/init.d/xfs
install %{SOURCE8} $RPM_BUILD_ROOT%{_sysconfdir}/X11/fs/config
install %{SOURCE9} $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults/pl/XTerm

install %{SOURCE10} $RPM_BUILD_ROOT/etc/sysconfig/xdm
install %{SOURCE11} $RPM_BUILD_ROOT/etc/sysconfig/xfs

install %{SOURCE20} $RPM_BUILD_ROOT%{_wmpropsdir}/twm.desktop
install %{SOURCE21} $RPM_BUILD_ROOT%{_applnkdir}/Amusements
install %{SOURCE22} $RPM_BUILD_ROOT%{_applnkdir}/Editors
install %{SOURCE23} $RPM_BUILD_ROOT%{_applnkdir}/Terminals
install %{SOURCE24}  %{SOURCE25} %{SOURCE26} %{SOURCE27} \
		$RPM_BUILD_ROOT%{_applnkdir}/Utilities
install %{SOURCE30} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE31} %{SOURCE32} %{SOURCE33} %{SOURCE34} %{SOURCE35} \
	%{SOURCE36} %{SOURCE37} \
	$RPM_BUILD_ROOT%{_pixmapsdir}

bzip2 -dc %{SOURCE38} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

:> $RPM_BUILD_ROOT/etc/security/console.apps/xserver
:> $RPM_BUILD_ROOT/etc/security/blacklist.xserver
:> $RPM_BUILD_ROOT/etc/security/blacklist.xdm

ln -sf %{_fontsdir} $RPM_BUILD_ROOT%{_libdir}/X11/fonts

# do not duplicate xkbcomp program
rm -f $RPM_BUILD_ROOT%{_libdir}/X11/xkb/xkbcomp
ln -sf %{_bindir}/xkbcomp $RPM_BUILD_ROOT%{_sysconfdir}/X11/xkb/xkbcomp

ln -sf /usr/share/doc/%{name}-%{version} $RPM_BUILD_ROOT%{_libdir}/X11/doc

rm -f $RPM_BUILD_ROOT%{_libdir}/X11/config/host.def

:> $RPM_BUILD_ROOT%{_libdir}/X11/config/host.def
:> $RPM_BUILD_ROOT%{_sysconfdir}/X11/XF86Config

rm -rf $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}/html

# resolve conflict with man-pages
mv -f $RPM_BUILD_ROOT%{_mandir}/man4/{mouse.4,mouse-x.4}

# directories for applications locales
echo '%defattr(644,root,root,755)' > XFree86-libs.lang
for lang in af az bg bg_BG.cp1251 br ca cs da de el en_GB eo es et eu fi \
	fr ga gl he hr hu is it ja ko lt mi mk nl nn no pl pt pt_BR ro ru sk \
	sl sr sv ta th tr uk wa zh_CN zh_CN.GB2312 zh_TW.Big5 ; do
	install -d $RPM_BUILD_ROOT%{_datadir}/locale/${lang}/LC_MESSAGES
	echo "%lang(${lang}) %{_datadir}/locale/${lang}" >> XFree86-libs.lang
done

%ifnarch sparc sparc64
gzip -9nf $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}/*

# don't gzip README.* files, they are needed by XF86Setup
gunzip $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{version}/README.*
%endif

%clean
rm -rf $RPM_BUILD_ROOT

#--- %post{un}, %preun, %verifyscript, %trigge ----------

%post	DPS -p /sbin/ldconfig
%postun	DPS -p /sbin/ldconfig

%post	xft1 -p /sbin/ldconfig
%postun	xft1 -p /sbin/ldconfig

%post   xft -p /sbin/ldconfig
%postun xft -p /sbin/ldconfig

%post	fontconfig
/sbin/ldconfig
HOME=/root %{_bindir}/fc-cache -f 2>/dev/null

%postun	fontconfig -p /sbin/ldconfig

%post	OpenGL-core -p /sbin/ldconfig
%postun	OpenGL-core -p /sbin/ldconfig

%post	OpenGL-libs -p /sbin/ldconfig
%postun	OpenGL-libs -p /sbin/ldconfig

%post libs
umask 022
grep -qs "^%{_libdir}$" /etc/ld.so.conf
[ $? -ne 0 ] && echo "%{_libdir}" >> /etc/ld.so.conf
/sbin/ldconfig

%postun libs
if [ "$1" = "0" ]; then
	umask 022
	grep -v "%{_libdir}" /etc/ld.so.conf > /etc/ld.so.conf.new
	mv -f /etc/ld.so.conf.new /etc/ld.so.conf
fi
/sbin/ldconfig

%verifyscript libs
echo -n "Looking for %{_libdir} in /etc/ld.so.conf... "
if ! grep -q "^%{_libdir}$" /etc/ld.so.conf ; then
	echo "missing"
	echo "%{_libdir} missing from /etc/ld.so.conf" >&2
else
	echo "found"
fi

%triggerpostun modules -- XFree86-modules < 4.0.2
if [ -d /usr/X11R6/lib/X11/xkb ]; then
	rm -rf /usr/X11R6/lib/X11/xkb
	ln -sf /etc/X11/xkb /usr/X11R6/lib/X11/xkb
fi

%post -n xdm
/sbin/chkconfig --add xdm
if [ -f /var/lock/subsys/xdm ]; then
	echo "Run \"/etc/rc.d/init.d/xdm restart\" to restart xdm." >&2
	echo "WARNING: it will terminate all sessions opened from xdm!" >&2
else
	echo "Run \"/etc/rc.d/init.d/xdm start\" to start xdm." >&2
fi

%preun -n xdm
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/xdm ]; then
		/etc/rc.d/init.d/xdm stop >&2
	fi
	/sbin/chkconfig --del xdm
fi

%pre -n xfs
if [ -n "`/usr/bin/getgid xfs`" ]; then
	if [ "`/usr/bin/getgid xfs`" != "56" ]; then
		echo "Error: group xfs doesn't have GID=56. Correct this before installing xfs." 1>&2
		exit 1
	fi
else
	/usr/sbin/groupadd -g 56 -r -f xfs
fi
if [ -n "`/bin/id -u xfs 2>/dev/null`" ]; then
	if [ "`/bin/id -u xfs`" != "56" ]; then
		echo "Error: user xfs doesn't have UID=56. Correct this before installing xfs." 1>&2
		exit 1
	fi
else
	/usr/sbin/useradd -u 56 -r -d /etc/X11/fs -s /bin/false -c "X Font Server" -g xfs xfs 1>&2
fi

%post -n xfs
/sbin/chkconfig --add xfs
if [ -f /var/lock/subsys/xfs ]; then
	/etc/rc.d/init.d/xfs restart >&2
else
	echo "Run \"/etc/rc.d/init.d/xfs start\" to start font server." >&2
fi

%preun -n xfs
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/xfs ]; then
		/etc/rc.d/init.d/xfs stop >&2
	fi
	/sbin/chkconfig --del xfs
fi

%postun -n xfs
if [ "$1" = "0" ]; then
	/usr/sbin/userdel xfs 2>/dev/null
	/usr/sbin/groupdel xfs 2>/dev/null
fi


%post xrender -p /sbin/ldconfig
%postun xrender -p /sbin/ldconfig

%post xcursor -p /sbin/ldconfig
%postun xcursor -p /sbin/ldconfig

#--- %files --------------------------

%files
%defattr(644,root,root,755)
%ifnarch sparc sparc64
%doc %{_docdir}/%{name}-%{version}
%doc %{_libdir}/X11/doc
%endif

%{_libdir}/X11/app-defaults/UXTerm
%{_libdir}/X11/app-defaults/XCalc
%{_libdir}/X11/app-defaults/XCalc-color
%{_libdir}/X11/app-defaults/XClipboard
%{_libdir}/X11/app-defaults/XClock
%{_libdir}/X11/app-defaults/XLoad
%{_libdir}/X11/app-defaults/XLogo
%{_libdir}/X11/app-defaults/XLogo-color
%{_libdir}/X11/app-defaults/XSm
%{_libdir}/X11/app-defaults/XTerm
%lang(pl) %{_libdir}/X11/app-defaults/pl/XTerm
%{_libdir}/X11/app-defaults/XTerm-color
%dir %{_icondir}
%{_icondir}/*

%attr(755,root,root) %{_libdir}/X11/lbxproxy
%attr(755,root,root) %{_libdir}/X11/proxymngr
%attr(755,root,root) %{_libdir}/X11/rstart
%attr(755,root,root) %{_libdir}/X11/fonts
%attr(755,root,root) %{_libdir}/X11/xinit
%attr(755,root,root) %{_libdir}/X11/xsm

%dir /etc/X11/xinit
%dir /etc/X11/lbxproxy
/etc/X11/lbxproxy/*
%dir /etc/X11/proxymngr
/etc/X11/proxymngr/*
%dir /etc/X11/rstart
/etc/X11/rstart/config
%attr(755,root,root) /etc/X11/rstart/rstartd.real
%dir /etc/X11/rstart/commands
/etc/X11/rstart/commands/x
/etc/X11/rstart/commands/x11
%attr(755,root,root) /etc/X11/rstart/commands/*List*
%dir /etc/X11/rstart/commands/x11r6
%attr(755,root,root) /etc/X11/rstart/commands/x11r6/*
%dir /etc/X11/rstart/contexts
/etc/X11/rstart/contexts/*
%dir /etc/X11/xsm
/etc/X11/xsm/*

%dir %{_libdir}/X11/x11perfcomp
%attr(755,root,root) %{_libdir}/X11/x11perfcomp/*

%attr(755,root,root) %{_bindir}/Xmark
%attr(755,root,root) %{_bindir}/appres
%attr(755,root,root) %{_bindir}/atobm
%attr(755,root,root) %{_bindir}/bitmap
%attr(755,root,root) %{_bindir}/bmtoa
%attr(755,root,root) %{_bindir}/cxpm
%attr(755,root,root) %{_bindir}/dga
%attr(755,root,root) %{_bindir}/editres
%attr(755,root,root) %{_bindir}/gtf
%attr(755,root,root) %{_bindir}/iceauth
%attr(755,root,root) %{_bindir}/lbxproxy
%attr(755,root,root) %{_bindir}/lndir
%attr(755,root,root) %{_bindir}/luit
%attr(755,root,root) %{_bindir}/makeg
%attr(755,root,root) %{_bindir}/makestrs
%attr(755,root,root) %{_bindir}/mergelib
%attr(755,root,root) %{_bindir}/mkdirhier
%attr(755,root,root) %{_bindir}/mkfontdir
%attr(755,root,root) %{_bindir}/mkfontscale
%attr(755,root,root) %{_bindir}/mkhtmlindex
%attr(755,root,root) %{_bindir}/proxymngr
%attr(755,root,root) %{_bindir}/resize
%attr(755,root,root) %{_bindir}/revpath
%attr(755,root,root) %{_bindir}/rstart
%attr(755,root,root) %{_bindir}/rstartd
%attr(755,root,root) %{_bindir}/setxkbmap
%attr(755,root,root) %{_bindir}/showrgb
%attr(755,root,root) %{_bindir}/smproxy
%attr(755,root,root) %{_bindir}/startx
%attr(755,root,root) %{_bindir}/sxpm
%attr(755,root,root) %{_bindir}/uxterm
%attr(755,root,root) %{_bindir}/xcmsdb
%attr(755,root,root) %{_bindir}/xconsole
%attr(755,root,root) %{_bindir}/xcursorgen
%attr(755,root,root) %{_bindir}/xcutsel
%attr(755,root,root) %{_bindir}/xdpyinfo
%attr(755,root,root) %{_bindir}/xfindproxy
%attr(755,root,root) %{_bindir}/xfwp
%attr(755,root,root) %{_bindir}/xgamma
%attr(755,root,root) %{_bindir}/xhost
%attr(755,root,root) %{_bindir}/xinit
%attr(755,root,root) %{_bindir}/xkbbell
%attr(755,root,root) %{_bindir}/xkbevd
%attr(755,root,root) %{_bindir}/xkbprint
%attr(755,root,root) %{_bindir}/xkbvleds
%attr(755,root,root) %{_bindir}/xkbwatch
%attr(755,root,root) %{_bindir}/xlsatoms
%attr(755,root,root) %{_bindir}/xlsclients
%attr(755,root,root) %{_bindir}/xlsfonts
%attr(755,root,root) %{_bindir}/xmodmap
%attr(755,root,root) %{_bindir}/xon
%attr(755,root,root) %{_bindir}/xprop
%attr(755,root,root) %{_bindir}/xrandr
%attr(755,root,root) %{_bindir}/xrdb
%attr(755,root,root) %{_bindir}/xrefresh
%attr(755,root,root) %{_bindir}/xset
%attr(755,root,root) %{_bindir}/xsetmode
%attr(755,root,root) %{_bindir}/xsetpointer
%attr(755,root,root) %{_bindir}/xsetroot
%attr(755,root,root) %{_bindir}/xsm
%attr(755,root,root) %{_bindir}/xstdcmap
%attr(755,root,root) %{_bindir}/xterm
%attr(755,root,root) %{_bindir}/xvidtune
%attr(755,root,root) %{_bindir}/xvinfo
%attr(755,root,root) %{_bindir}/xwd
%attr(755,root,root) %{_bindir}/xwud

%{_includedir}/X11/bitmaps
%{_includedir}/X11/pixmaps

%{_applnkdir}/Utilities/xconsole.desktop
%{_applnkdir}/Terminals/*
%{_libdir}/X11/app-defaults/Xvidtune
%{_pixmapsdir}/x*

%{_mandir}/man1/Xmark.1*
%{_mandir}/man1/appres.1*
%{_mandir}/man1/atobm.1*
%{_mandir}/man1/bdftopcf.1*
%{_mandir}/man1/bitmap.1*
%{_mandir}/man1/bmtoa.1*
%{_mandir}/man1/cxpm.1*
%{_mandir}/man1/dga.1*
%{_mandir}/man1/editres.1*
%{_mandir}/man1/gtf.1*
%{_mandir}/man1/iceauth.1*
%{_mandir}/man1/lbxproxy.1*
%{_mandir}/man1/libxrx.1*
%{_mandir}/man1/lndir.1*
%{_mandir}/man1/luit.1x*
%{_mandir}/man1/makestrs.1*
%{_mandir}/man1/makeg.1*
%{_mandir}/man1/mergelib.1*
%{_mandir}/man1/mkdirhier.1*
%{_mandir}/man1/mkfontdir.1*
%{_mandir}/man1/mkfontscale.1*
%{_mandir}/man1/mkhtmlindex.1*
%{_mandir}/man1/proxymngr.1*
%{_mandir}/man1/resize.1*
%{_mandir}/man1/revpath.1*
%{_mandir}/man1/rstart.1*
%{_mandir}/man1/rstartd.1*
%{_mandir}/man1/setxkbmap.1*
%{_mandir}/man1/showrgb.1*
%{_mandir}/man1/smproxy.1*
%{_mandir}/man1/startx.1*
%{_mandir}/man1/sxpm.1*
%{_mandir}/man1/xcmsdb.1*
%{_mandir}/man1/xconsole.1*
%{_mandir}/man1/xcursorgen.1*
%{_mandir}/man1/xcutsel.1*
%{_mandir}/man1/xdpyinfo.1*
%{_mandir}/man1/xfindproxy.1*
%{_mandir}/man1/xfwp.1*
%{_mandir}/man1/xgamma.1*
%{_mandir}/man1/xhost.1*
%{_mandir}/man1/xinit.1*
%{_mandir}/man1/xkbevd.1*
%{_mandir}/man1/xkbprint.1*
%{_mandir}/man1/xlsatoms.1*
%{_mandir}/man1/xlsclients.1*
%{_mandir}/man1/xlsfonts.1*
%{_mandir}/man1/xmodmap.1*
%{_mandir}/man1/xprop.1*
%{_mandir}/man1/xrandr.1*
%{_mandir}/man1/xrdb.1*
%{_mandir}/man1/xrefresh.1*
%{_mandir}/man1/xset.1*
%{_mandir}/man1/xsetmode.1*
%{_mandir}/man1/xsetpointer.1*
%{_mandir}/man1/xsetroot.1*
%{_mandir}/man1/xsm.1*
%{_mandir}/man1/xstdcmap.1*
%{_mandir}/man1/xterm.1*
%{_mandir}/man1/xvidtune.1*
%{_mandir}/man1/xvinfo.1*
%{_mandir}/man1/xwd.1*
%{_mandir}/man1/xwud.1*
%{_mandir}/man1/xon.1*
%{_mandir}/man7/*

%lang(it) %{_mandir}/it/man1/startx.1*
%lang(it) %{_mandir}/it/man1/xconsole.1*
%lang(it) %{_mandir}/it/man1/xinit.1*
%lang(it) %{_mandir}/it/man1/xsetpointer.1*

%lang(ko) %{_mandir}/ko/man1/xterm.1*

%lang(pl) %{_mandir}/pl/man1/lbxproxy.1*
%lang(pl) %{_mandir}/pl/man1/startx.1*
%lang(pl) %{_mandir}/pl/man1/xinit.1*
%lang(pl) %{_mandir}/pl/man1/xwd.1*

%files common
%defattr(644,root,root,755)
/usr/bin/X11
/usr/lib/X11
%dir %{_bindir}
%dir %{_libdir}
%dir %{_libdir}/X11
%{_libdir}/X11/rgb.txt

%files DPS
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/makepsres
%attr(755,root,root) %{_bindir}/pswrap
%attr(755,root,root) %{_bindir}/dpsinfo
%attr(755,root,root) %{_bindir}/dpsexec
%attr(755,root,root) %{_libdir}/libdps.so.*.*
%attr(755,root,root) %{_libdir}/libdpstk.so.*.*
%attr(755,root,root) %{_libdir}/libpsres.so.*.*
%{_mandir}/man1/makepsres*
%{_mandir}/man1/pswrap*
%{_mandir}/man1/dpsexec*
%{_mandir}/man1/dpsinfo*

%files DPS-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdps.so
%attr(755,root,root) %{_libdir}/libdpstk.so
%attr(755,root,root) %{_libdir}/libpsres.so
%{_includedir}/DPS

%files DPS-static
%defattr(644,root,root,755)
%{_libdir}/libdps.a
%{_libdir}/libdpstk.a
%{_libdir}/libpsres.a

%files xft1
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXft.so.1.1

%files xft
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXft.so.2.1

%files xft-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xft-config
%{_includedir}/X11/Xft
%{_libdir}/libXft.so
%{_mandir}/man3/Xft.3*
%{_pkgconfigdir}/xft.pc

%files xft-static
%defattr(644,root,root,755)
%{_libdir}/libXft.a

%files fontconfig
%defattr(644,root,root,755)
%dir %{_sysconfdir}/fonts
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/fonts/fonts.conf
%{_sysconfdir}/fonts/fonts.dtd
%attr(755,root,root) %{_bindir}/fc-*
%attr(755,root,root) %{_libdir}/libfontconfig.so.1.0
%{_mandir}/man1/fc-*.1*

%files fontconfig-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fontconfig-config
%{_includedir}/fontconfig
%{_libdir}/libfontconfig.so
%{_pkgconfigdir}/fontconfig.pc
%{_mandir}/man3/fontconfig.3*

%files fontconfig-static
%defattr(644,root,root,755)
%{_libdir}/libfontconfig.a

%files OpenGL-core
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/glxgears
%attr(755,root,root) %{_libdir}/libGL.so.*.*
%attr(755,root,root) %{_libdir}/libGL.so
%attr(755,root,root) %{_libdir}/modules/extensions/libglx.a
%attr(755,root,root) %{_libdir}/modules/extensions/libGLcore.a
%{_mandir}/man1/glxgears.1x*

%files OpenGL-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libGLU.so
%attr(755,root,root) %{_libdir}/libOSMesa*.so
%{_libdir}/libGLw.a
%dir %{_includedir}/GL
%attr(644,root,root) %{_includedir}/GL/*
%exclude %{_includedir}/GL/gl.h
%exclude %{_includedir}/GL/glx.h
%exclude %{_includedir}/GL/glxtokens.h
%{_mandir}/man3/gl[A-Z]*
%{_mandir}/man3/glu*
%{_mandir}/man3/GLw*

%files OpenGL-devel-base
%defattr(644,root,root,755)
%{_includedir}/GL/gl.h
%{_includedir}/GL/glx.h
%{_includedir}/GL/glxtokens.h

%files OpenGL-libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/glxinfo
%attr(755,root,root) %{_libdir}/libGLU.so.*.*
%attr(755,root,root) %{_libdir}/libOSMesa.so.*.*
%{_mandir}/man1/glxinfo.1*

%files OpenGL-static
%defattr(644,root,root,755)
%{_libdir}/libGL.a
%{_libdir}/libGLU.a
%{_libdir}/libOSMesa*.a

%files Xnest
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xnest
%{_mandir}/man1/Xnest.1*

%files Xprt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xprt

%files Xserver
%defattr(644,root,root,755)
%attr(4755,root,root) %{_bindir}/Xwrapper
%attr(755,root,root) %{_bindir}/XFree86
%attr(755,root,root) %{_sysconfdir}/X11/X
%attr(755,root,root) %{_bindir}/X
%{_mandir}/man1/XFree86.1*
%{_mandir}/man1/Xserver.1*
%{_mandir}/man5/XF86Config.5*

%{_libdir}/X11/Cards
%{_libdir}/X11/Options

%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/X11/XF86Config
%attr(640,root,root) %config %verify(not md5 size mtime) /etc/pam.d/xserver
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/security/blacklist.xserver
%config(missingok) /etc/security/console.apps/xserver

%files Xvfb
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/Xvfb
%{_mandir}/man1/Xvfb.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bdftopcf
#%attr(755,root,root) %{_bindir}/xcursor-config
%attr(755,root,root) %{_libdir}/libX[1Ta-eg-t]*.so
%attr(755,root,root) %{_libdir}/libXfont*.so
%attr(755,root,root) %{_libdir}/libI*.so
%attr(755,root,root) %{_libdir}/libS*.so
%attr(755,root,root) %{_libdir}/libx*.so
%attr(755,root,root) %{_libdir}/libXv.so
%{_libdir}/libfntstubs.a
%{_libdir}/libfontenc.a
%{_libdir}/libFS.a
%{_libdir}/libI810XvMC.a
%{_libdir}/liboldX.a
%{_libdir}/libXau.a
%{_libdir}/libXdmcp.a
%{_libdir}/libxf86config.a
%{_libdir}/libXfontcache.a
%{_libdir}/libXinerama.a
%{_libdir}/libxkbfile.a
%{_libdir}/libxkbui.a
%{_libdir}/libXrandr.a
%{_libdir}/libXss.a
%{_libdir}/libXTrap.a
%{_libdir}/libXv.a
%{_libdir}/libXvMC.a
%{_libdir}/libXxf86dga.a
%{_libdir}/libXxf86misc.a
%{_libdir}/libXxf86rush.a
%{_libdir}/libXxf86vm.a
%{_includedir}/X11/*.h
%{_includedir}/X11/ICE
%{_includedir}/X11/PM
%{_includedir}/X11/SM
%{_includedir}/X11/Xaw
%{_includedir}/X11/Xmu
%dir %{_includedir}/X11/extensions
%{_includedir}/X11/extensions/[^X]*.h
%{_includedir}/X11/extensions/X[^I]*.h
%{_includedir}/X11/extensions/XI.h
%{_includedir}/X11/extensions/XI[^E]*.h
%{_includedir}/X11/fonts
%{_includedir}/xf86*.h
%{_libdir}/X11/config

%exclude %{_includedir}/X11/extensions/Xrender.h
%exclude %{_includedir}/X11/extensions/render.h
%exclude %{_includedir}/X11/extensions/renderproto.h
%exclude %{_libdir}/libXrender.so
%exclude %{_libdir}/libXcursor.so

%{_mandir}/man3/[A-EH-Z]*
%exclude %{_mandir}/man3/Xft.3*

# Devel: sparc sparc64
%ifarch %{ix86}
%files driver-apm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/apm_drv.o
%{_mandir}/man4/apm*
%endif

# Devel: sparc sparc64
%ifarch %{ix86}
%files driver-ark
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/ark_drv.o
%endif

# Devel: sparc sparc64
%ifarch %{ix86} mips ppc arm
%files driver-chips
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/chips_drv.o
%{_mandir}/man4/chips*
%endif

# Devel: sparc sparc64
%ifarch %{ix86} alpha
%files driver-cirrus
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/cirrus_*.o
%{_mandir}/man4/cirrus*
%endif

%ifarch %{ix86}
%files driver-cyrix
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/cyrix_drv.o
%{_mandir}/man4/cyrix*
%endif

%ifarch %{ix86} sparc sparc64 mips ppc arm superh
%files driver-fbdev
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/fbdev_drv.o
%{_mandir}/man4/fbdev*
%endif

%ifarch %{ix86}
%{!?_without_tdfx:%files driver-glide}
%{!?_without_tdfx:%defattr(644,root,root,755)}
%{!?_without_tdfx:%attr(755,root,root) %{_libdir}/modules/drivers/glide_drv.o}
%{!?_without_tdfx:%{_mandir}/man4/glide*}
%endif

%files driver-glint
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/glint_drv.o
%ifarch %{ix86} alpha ppc arm
%attr(755,root,root) %{_libdir}/modules/dri/gamma_dri.so
%endif
%{_mandir}/man4/glint*

# Devel: sparc sparc64
%ifarch %{ix86}
%files driver-i128
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/i128_drv.o
%{_mandir}/man4/i128*
%endif

# Devel: sparc sparc64
%ifarch %{ix86}
%files driver-i740
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/i740_drv.o
%{_mandir}/man4/i740*
%endif

# Devel: sparc sparc64
%ifarch %{ix86}
%files driver-i810
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/i810_drv.o
%attr(755,root,root) %{_libdir}/modules/dri/i810_dri.so
%attr(755,root,root) %{_libdir}/modules/dri/i830_dri.so
%{_mandir}/man4/i810*
%endif

# Devel: %{ix86} sparc sparc64 ppc
%if 0
%files driver-imstt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/imstt_drv.o
%{_mandir}/man4/imstt.4*
%endif

%ifarch %{ix86} sparc sparc64 mips alpha ppc arm
%files driver-mga
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/mga_drv.o
%ifarch %{ix86} alpha ppc arm
%attr(755,root,root) %{_libdir}/modules/dri/mga_dri.so
%endif
%{_mandir}/man4/mga*
%endif

# Devel: sparc sparc64
%ifarch %{ix86}
%files driver-neomagic
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/neomagic_drv.o
%{_mandir}/man4/neomagic*
%endif

# Devel: %{ix86} sparc sparc64
%ifarch mips
%files driver-newport
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/newport_drv.o
%{_mandir}/man4/newport.4*
%endif

%ifarch %{ix86}
%files driver-nsc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/nsc_drv.o
%{_mandir}/man4/nsc.4*
%endif

# Devel: sparc sparc64
%ifarch %{ix86} mips alpha arm
%files driver-nv
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/nv_drv.o
%{_mandir}/man4/nv*
%endif

%files driver-ati
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/ati*_drv.o

%files driver-r128
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/r128*_drv.o
%ifarch %{ix86} alpha ppc arm
%attr(755,root,root) %{_libdir}/modules/dri/r128_dri.so
%endif
%{_mandir}/man4/r128*

%files driver-radeon
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/radeon*_drv.o
%ifarch %{ix86} alpha ppc arm
%attr(755,root,root) %{_libdir}/modules/dri/radeon_dri.so
%attr(755,root,root) %{_libdir}/modules/dri/r200_dri.so
%endif
%{_mandir}/man4/radeon*

%ifnarch alpha
#%%files driver-ati.2
#%defattr(644,root,root,755)
#%dir %{_libdir}/modules.gatos/drivers
#%attr(755,root,root) %{_libdir}/modules.gatos/drivers/ati*_drv.o
#%attr(755,root,root) %{_libdir}/modules.gatos/drivers/[bfmt]*_drv.o
%endif

%ifnarch alpha
#%files driver-r128.2
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/modules.gatos/drivers/r128*_drv.o
#%ifnarch sparc sparc64
#%attr(755,root,root) %{_libdir}/modules.gatos/dri/r128_dri.o
#%endif
#%%{_mandir}/man4/r128*
%endif

%ifnarch alpha
#%files driver-radeon.2
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/modules.gatos/drivers/radeon*_drv.o
#%attr(755,root,root) %{_libdir}/modules.gatos/drivers/saa7114_drv.o
#%ifnarch sparc sparc64
#%attr(755,root,root) %{_libdir}/modules.gatos/dri/radeon_dri.o
#%endif
%endif

# Devel: sparc sparc64
%ifarch %{ix86} alpha
%files driver-rendition
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/rendition_drv.o
%{_mandir}/man4/rendition*
%endif

# Devel: sparc sparc64
%ifarch %{ix86} mips alpha ppc arm
%files driver-s3virge
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/s3virge_drv.o
%{_mandir}/man4/s3virge*
%endif

%ifarch %{ix86} mips alpha ppc arm
%files driver-s3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/s3_drv.o
#%%{_mandir}/man4/s3.4*
%endif

# Devel: sparc sparc64
%ifarch %{ix86} mips alpha ppc arm
%files driver-savage
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/savage_drv.o
%{_mandir}/man4/savage*
%endif

# Devel: sparc sparc64
%ifarch %{ix86} alpha
%files driver-siliconmotion
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/siliconmotion_drv.o
%{_mandir}/man4/siliconmotion*
%endif

%ifarch %{ix86} mips ppc arm
%files driver-sis
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/sis_drv.o
%ifarch %{ix86}
#%attr(755,root,root) %{_libdir}/modules/dri/sis_dri.so
%endif
%{_mandir}/man4/sis*
%endif

%ifarch sparc sparc64
%files driver-sunbw2
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/sunbw2_drv.o
%{_mandir}/man4/sunbw2*
%endif

%ifarch sparc sparc64
%files driver-suncg14
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/suncg14_drv.o
%{_mandir}/man4/suncg14*
%endif

%ifarch sparc sparc64
%files driver-suncg3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/suncg3_drv.o
%{_mandir}/man4/suncg3*
%endif

%ifarch sparc sparc64
%files driver-suncg6
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/suncg6_drv.o
%{_mandir}/man4/suncg6*
%endif

%ifarch sparc sparc64
%files driver-sunffb
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/sunffb_drv.o
%attr(755,root,root) %{_libdir}/modules/dri/ffb_dri.so
%{_mandir}/man4/sunffb*
%endif

%ifarch sparc sparc64
%files driver-sunleo
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/sunleo_drv.o
%{_mandir}/man4/sunleo*
%endif

%ifarch sparc sparc64
%files driver-suntcx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/suntcx_drv.o
%{_mandir}/man4/suntcx*
%endif

%ifarch %{ix86} sparc sparc64 mips alpha arm
%{!?_without_tdfx:%files driver-tdfx}
%{!?_without_tdfx:%defattr(644,root,root,755)}
%{!?_without_tdfx:%attr(755,root,root) %{_libdir}/modules/drivers/tdfx_drv.o}
%ifarch %{ix86} alpha arm
%{!?_without_tdfx:%attr(755,root,root) %{_libdir}/modules/dri/tdfx_dri.so}
%endif
%{!?_without_tdfx:%{_mandir}/man4/tdfx*}
%endif

# Devel: sparc sparc64
%ifarch %{ix86} alpha
%files driver-tga
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/tga_drv.o
%endif

# Devel: sparc sparc64
%ifarch %{ix86} mips ppc arm
%files driver-trident
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/trident_drv.o
%{_mandir}/man4/trident*
%endif

%ifarch %{ix86}
%files driver-tseng
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/tseng_drv.o
%{_mandir}/man4/tseng*
%endif

%ifarch %{ix86}
%files driver-via
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/via_drv.o
%{_mandir}/man4/via.4*
%endif

# Devel: sparc sparc64
%ifarch %{ix86}
%files driver-vmware
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/modules/drivers/vmware_drv.o
%{_mandir}/man4/vmware*
%endif

%files libs -f XFree86-libs.lang
%defattr(644,root,root,755)
%dir %{_themesdir}
%dir %{_themesdir}/Default
%dir %{_themesdir}/ThinIce
%{_libdir}/X11/XErrorDB
%{_libdir}/X11/XKeysymDB
%dir %{_libdir}/X11/app-defaults
%lang(cs) %dir %{_libdir}/X11/app-defaults/cs
%lang(da) %dir %{_libdir}/X11/app-defaults/da
%lang(de) %dir %{_libdir}/X11/app-defaults/de
%lang(es) %dir %{_libdir}/X11/app-defaults/es
%lang(fr) %dir %{_libdir}/X11/app-defaults/fr
%lang(hu) %dir %{_libdir}/X11/app-defaults/hu
%lang(ko) %dir %{_libdir}/X11/app-defaults/ko
%lang(nl) %dir %{_libdir}/X11/app-defaults/nl
%lang(pl) %dir %{_libdir}/X11/app-defaults/pl
%lang(pt) %dir %{_libdir}/X11/app-defaults/pt
%lang(ru) %dir %{_libdir}/X11/app-defaults/ru
%lang(sk) %dir %{_libdir}/X11/app-defaults/sk
%lang(zh_CN) %dir %{_libdir}/X11/app-defaults/zh_CN.gb2312
%lang(zh_TW) %dir %{_libdir}/X11/app-defaults/zh_TW.big5
%{_libdir}/X11/locale
%dir %{_includedir}
%dir %{_includedir}/X11
/usr/include/X11
%dir %{_sbindir}
%dir %{_datadir}/locale
%dir %{_datadir}/misc
%dir %{_pixmapsdir}
%dir %{_pixmapsdir}/mini
%dir %{_soundsdir}
%dir %{_wmpropsdir}
%attr(755,root,root) %{_libdir}/libX[1Ta-eg-t]*.so.*.*
%attr(755,root,root) %{_libdir}/libXfont*.so.*.*
%attr(755,root,root) %{_libdir}/libI*.so.*.*
%attr(755,root,root) %{_libdir}/libS*.so.*.*
%attr(755,root,root) %{_libdir}/libx*.so.*.*
%attr(755,root,root) %{_libdir}/libXv.so.*.*

%exclude %{_libdir}/libXrender.so.*.*
%exclude %{_libdir}/libXcursor.so.*.*

%files modules
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xkbcomp
%{_libdir}/X11/xkb
%{_sysconfdir}/X11/xkb
/var/lib/xkb
%dir %{_libdir}/modules
%dir %{_libdir}/modules/dri
%dir %{_libdir}/modules/drivers
%ifnarch sparc sparc64 ppc
%{_libdir}/modules/*.uc
%endif
%attr(755,root,root) %{_libdir}/modules/*.a
%attr(755,root,root) %{_libdir}/modules/codeconv
%attr(755,root,root) %{_libdir}/modules/drivers/linux
%ifarch %{ix86} sparc sparc64 alpha ppc arm
%attr(755,root,root) %{_libdir}/modules/drivers/vga_drv.o
%endif
%ifarch %{ix86} sparc sparc64
%attr(755,root,root) %{_libdir}/modules/drivers/vesa_drv.o
%endif
%dir %{_libdir}/modules/extensions
%attr(755,root,root) %{_libdir}/modules/extensions/libdbe.a
%attr(755,root,root) %{_libdir}/modules/extensions/libdri.a
%attr(755,root,root) %{_libdir}/modules/extensions/libextmod.a
%attr(755,root,root) %{_libdir}/modules/extensions/librecord.a
%attr(755,root,root) %{_libdir}/modules/extensions/libxtrap.a
%attr(755,root,root) %{_libdir}/modules/fonts
%attr(755,root,root) %{_libdir}/modules/input
%attr(755,root,root) %{_libdir}/modules/linux
%attr(755,root,root) %{_libdir}/X11/xserver
%dir /etc/X11/xserver
/etc/X11/xserver/SecurityPolicy
#%%{_mandir}/man1/xtr*
%{_mandir}/man1/xkbcomp.1*
%{_mandir}/man4/citron*
%{_mandir}/man4/dmc.4*
%{_mandir}/man4/dynapro*
%{_mandir}/man4/fpit.4*
%{_mandir}/man4/js_x.4*
%{_mandir}/man4/kbd.4*
%{_mandir}/man4/keyboard*
%{_mandir}/man4/microtouch*
%{_mandir}/man4/mouse-x.4*
%{_mandir}/man4/palmax.4*
%{_mandir}/man4/penmount.4*
%{_mandir}/man4/tek4957.4*
%{_mandir}/man4/v4l*
%ifarch %{ix86} sparc sparc64 alpha ppc arm
%{_mandir}/man4/vga*
%endif
%ifarch %{ix86} sparc sparc64
%{_mandir}/man4/vesa*
%endif
%{_mandir}/man4/void*
%{_mandir}/man4/wacom*
%{_mandir}/man4/elographics*
%{_mandir}/man4/mutouch*

%files setup
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pcitweak
%ifnarch ppc
%attr(755,root,root) %{_bindir}/scanpci
%endif
%attr(755,root,root) %{_bindir}/xf86cfg
%attr(755,root,root) %{_bindir}/xf86config
%{_libdir}/X11/app-defaults/XF86Cfg
%ifnarch ppc
%{_mandir}/man1/scanpci.1*
%endif
%{_mandir}/man1/pcitweak.1*
%{_mandir}/man1/xf86cfg.1*
%{_mandir}/man1/xf86config.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/libICE.a
%{_libdir}/libSM.a
%{_libdir}/libX11.a
%{_libdir}/libXRes.a
%{_libdir}/libXaw.a
%{_libdir}/libXext.a
%{_libdir}/libXfont.a
%{_libdir}/libXi.a
%{_libdir}/libXmu.a
%{_libdir}/libXmuu.a
%{_libdir}/libXp.a
%{_libdir}/libXpm.a
%{_libdir}/libXt.a
%{_libdir}/libXtst.a

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/beforelight
%attr(755,root,root) %{_bindir}/ico
%attr(755,root,root) %{_bindir}/listres
%attr(755,root,root) %{_bindir}/showfont
%attr(755,root,root) %{_bindir}/viewres
%attr(755,root,root) %{_bindir}/x11perf
%attr(755,root,root) %{_bindir}/x11perfcomp
%attr(755,root,root) %{_bindir}/xbiff
%attr(755,root,root) %{_bindir}/xcalc
%attr(755,root,root) %{_bindir}/xclipboard
%attr(755,root,root) %{_bindir}/xclock
%attr(755,root,root) %{_bindir}/xditview
%attr(755,root,root) %{_bindir}/xedit
%attr(755,root,root) %{_bindir}/xev
%attr(755,root,root) %{_bindir}/xeyes
%attr(755,root,root) %{_bindir}/xfd
%attr(755,root,root) %{_bindir}/xfontsel
%attr(755,root,root) %{_bindir}/xgc
%attr(755,root,root) %{_bindir}/xload
%attr(755,root,root) %{_bindir}/xmag
%attr(755,root,root) %{_bindir}/xman
%attr(755,root,root) %{_bindir}/xmessage
%attr(755,root,root) %{_bindir}/xmh
%attr(755,root,root) %{_bindir}/xwininfo
%attr(755,root,root) %{_bindir}/oclock
%attr(755,root,root) %{_bindir}/xlogo
%attr(755,root,root) %{_bindir}/xkill
%attr(755,root,root) %{_bindir}/rman
%attr(755,root,root) %{_bindir}/xtrap*
%attr(755,root,root) %{_bindir}/texteroids
%{_libdir}/X11/xedit
%{_libdir}/X11/xman.help
%{_mandir}/man1/beforelight.1*
%{_mandir}/man1/ico.1*
%{_mandir}/man1/listres.1*
%{_mandir}/man1/showfont.1*
%{_mandir}/man1/viewres.1*
%{_mandir}/man1/x11perf.1*
%{_mandir}/man1/x11perfcomp.1*
%{_mandir}/man1/xbiff.1*
%{_mandir}/man1/xcalc.1*
%{_mandir}/man1/xclipboard.1*
%{_mandir}/man1/xclock.1*
%{_mandir}/man1/xditview.1*
%{_mandir}/man1/xedit.1*
%{_mandir}/man1/xev.1*
%{_mandir}/man1/xeyes.1*
%{_mandir}/man1/xfd.1*
%{_mandir}/man1/xfontsel.1*
%{_mandir}/man1/xgc.1*
%{_mandir}/man1/xload.1*
%{_mandir}/man1/xmag.1*
%{_mandir}/man1/xman.1*
%{_mandir}/man1/xmessage.1*
%{_mandir}/man1/xmh.1*
%{_mandir}/man1/xwininfo.1*
%{_mandir}/man1/xkill.1*
%{_mandir}/man1/xlogo.1*
%{_mandir}/man1/oclock.1*
%{_mandir}/man1/rman.1*
%{_mandir}/man1/xtr*
%{_mandir}/man1/texteroids.1*

%lang(it) %{_mandir}/it/man1/xload.1*

%lang(pl) %{_mandir}/pl/man1/rman.1*

%{_libdir}/X11/app-defaults/Beforelight
%{_libdir}/X11/app-defaults/Bitmap
%{_libdir}/X11/app-defaults/Bitmap-color
%{_libdir}/X11/app-defaults/Clock-color
%{_libdir}/X11/app-defaults/Editres
%{_libdir}/X11/app-defaults/Editres-color
%{_libdir}/X11/app-defaults/Viewres
%{_libdir}/X11/app-defaults/XConsole
%{_libdir}/X11/app-defaults/Xedit
%{_libdir}/X11/app-defaults/Xedit-color
%{_libdir}/X11/app-defaults/Xfd
%{_libdir}/X11/app-defaults/Xgc
%{_libdir}/X11/app-defaults/Xmag
%{_libdir}/X11/app-defaults/Xman
%{_libdir}/X11/app-defaults/Xmessage
%{_libdir}/X11/app-defaults/Xmessage-color
%{_libdir}/X11/app-defaults/Xmh
%{_libdir}/X11/app-defaults/XFontSel
%{_libdir}/X11/app-defaults/Xditview
%{_libdir}/X11/app-defaults/Xditview-chrtr

%{_applnkdir}/Utilities/xclipboard.desktop
%{_applnkdir}/Utilities/oclock.desktop
%{_applnkdir}/Utilities/xclock.desktop
%{_applnkdir}/Editors/xedit.desktop
%{_applnkdir}/Amusements/xeyes.desktop
%{_pixmapsdir}/oclock*

%files -n imake
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ccmakedep
%attr(755,root,root) %{_bindir}/cleanlinks
%attr(755,root,root) %{_bindir}/gccmakedep
%attr(755,root,root) %{_bindir}/imake
%attr(755,root,root) %{_bindir}/makedepend
%attr(755,root,root) %{_bindir}/xmkmf

%{_mandir}/man1/imake.1*
%{_mandir}/man1/ccmakedep.1*
%{_mandir}/man1/cleanlinks.1*
%{_mandir}/man1/gccmakedep.1*
%{_mandir}/man1/makedepend.1*
%{_mandir}/man1/xmkmf.1*

%files -n sessreg
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sessreg
%{_mandir}/man1/sessreg.1*

%files -n twm
%defattr(644,root,root,755)
%{_wmpropsdir}/twm.desktop
%attr(755,root,root) %{_bindir}/twm
%dir %{_sysconfdir}/X11/twm
%config %{_sysconfdir}/X11/twm/system.twmrc
%attr(755,root,root) %{_libdir}/X11/twm
%{_mandir}/man1/twm.1*

%files -n xauth
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xauth
%{_mandir}/man1/xauth.1*

%files -n xdm
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/pam.d/xdm
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/security/blacklist.xdm
%attr(754,root,root) /etc/rc.d/init.d/xdm
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/sysconfig/xdm
/var/lib/xdm

%{_libdir}/X11/app-defaults/Chooser

%attr(755,root,root) %{_libdir}/X11/xdm
%attr(755,root,root) %{_bindir}/xdm
%attr(755,root,root) %{_bindir}/chooser
%ifarch alpha
%attr(755,root,root) %{_libdir}/libXdmGreet.so*
%endif
%{_mandir}/man1/xdm.1*

%dir /etc/X11/xdm
%attr(755,root,root) %config(noreplace) %verify(not size mtime md5) /etc/X11/xdm/GiveConsole
%attr(755,root,root) %config(noreplace) %verify(not size mtime md5) /etc/X11/xdm/TakeConsole
%attr(755,root,root) %config(noreplace) %verify(not size mtime md5) /etc/X11/xdm/Xsession
%attr(755,root,root) %config(noreplace) %verify(not size mtime md5) /etc/X11/xdm/Xsetup_0
%attr(755,root,root) %config(noreplace) %verify(not size mtime md5) /etc/X11/xdm/Xwilling
%config(noreplace) %verify(not size mtime md5) /etc/X11/xdm/Xaccess
%config(noreplace) %verify(not size mtime md5) /etc/X11/xdm/Xresources
%config(noreplace) %verify(not size mtime md5) /etc/X11/xdm/Xservers
%config(noreplace) %verify(not size mtime md5) /etc/X11/xdm/xdm-config
/etc/X11/xdm/pixmaps
/etc/X11/xdm/authdir

%files -n xfs
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/xfs
%attr(640,root,root) %config(noreplace) %verify(not md5 size mtime) /etc/sysconfig/xfs
%dir %{_sysconfdir}/X11/fs
%attr(755,root,root) %{_libdir}/X11/fs
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/X11/fs/config

%attr(755,root,root) %{_bindir}/xfs
%attr(755,root,root) %{_bindir}/fslsfonts
%attr(755,root,root) %{_bindir}/fstobdf
%attr(755,root,root) %{_bindir}/mkcfm
%attr(755,root,root) %{_bindir}/xfsinfo
#%attr(755,root,root) %{_bindir}/xftcache

%{_mandir}/man1/xfs.1*
%{_mandir}/man1/fslsfonts.1*
%{_mandir}/man1/fstobdf.1*
%{_mandir}/man1/mkcfm.1*
%{_mandir}/man1/xfsinfo.1*
#%%{_mandir}/man1/xftcache.1*

%files render
%defattr(644,root,root,755)
%{_includedir}/X11/extensions/render.h
%{_includedir}/X11/extensions/renderproto.h

%files xrender
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXrender.so.*.*

%files xrender-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXrender.so
%{_includedir}/X11/extensions/Xrender.h

%files xrender-static
%defattr(644,root,root,755)
%{_libdir}/libXrender.a

%files xcursor
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXcursor.so.*.*

%files xcursor-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xcursor-config
%attr(755,root,root) %{_libdir}/libXcursor.so
%{_includedir}/X11/Xcursor
%{_pkgconfigdir}/xcursor.pc

%files xcursor-static
%defattr(644,root,root,755)
%{_libdir}/libXcursor.a
