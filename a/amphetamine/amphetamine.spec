Name: amphetamine
Version: 0.8.10
Release: alt5

%define dataver 0.8.6

Summary: Amphetamine is a cool Jump'n Run game
License: GPL
Group: Games/Arcade

Url: http://n.ethz.ch/student/loehrerl/amph/amph.html
Source0: %name-%version.tar.bz2
Source1: %name-data-%dataver.tar.bz2
Source2: %name-icons.tar.bz2
Source3: amphetamine.desktop
Patch:   amphetamine-%version-eols_at_eofs.patch.bz2
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Sun Oct 05 2008
BuildRequires: gcc-c++ libSDL-devel libXpm-devel libXt-devel

Summary(ru_RU.KOI8-R): Amphetamine -- �������� ��������
Summary(uk_UA.KOI8-U): Amphetamine -- ������� ��������

%description
Amphetamine is a 2D jump'n'run shooter in the tradition of Super Mario Bros
and other classics. But it has unique features:
   - Fast 256 colour graphics
   - Seven weapons: fight with arrow and bow, a scie, fire hands, etc.
   - Never seen graphics (in this genre) such as coronas (remember Unreal),
     dynamic coloured lightning, fogging, semitransparence and much more...
   - Raging fights against 11 bloodsucking monsters which themselves have
     several killing powers.
   - Cryptic labyrinths - definitely not boring shoot'em'up!

%description -l ru_RU.KOI8-R
Amphetamine -- ��������� �������� � ����� Super Mario Bros � �������� ��������.
���������� �����������:
   - ������� 256-������� �������
   - ���� ����� ������
   - ���������� (��� ����� �����) ������� ����� ������ (������� Unreal?),
     ������������� ���������, �����, ���������������� � ������� �������...
   - ������� � 11-� ������ �����������, ������� � ���� �������� ������� ���
     ����� ��� ����� ��������
   - ���������� ��������� -- ����������� �� ����� ���������!

%description -l uk_UA.KOI8-U
Amphetamine -- �����ͦ��� �������� � ���̦ Super Mario Bros �� ����ϧ �������.
�Φ����Φ ���������Ԧ:
   - ������ 256-��������� ���Ʀ��
   - �� ��Ħ� ���ϧ
   - ������Φ (��� ����� �����) ������ �� ������ ����� (���'������ Unreal?),
     ����ͦ����� ��צ������, ������, ��Ц���������Ԧ � ������ ���� ������...
   - ���� �� 11-�� ������ ����������˦�, ����Ҧ � ��ͦ ����Φ �������� ���
     ¦��� Φ� ����� ��������
   - �������צ ��¦����� -- ��� ������� �� ���� ��Ҧ�����!

%prep
%setup -q -a 2
%patch -p1

sed -i 's,/usr/local,%_datadir,g' Makefile
sed -i 's,/usr/local,%_datadir,g' src/System.hpp

%build
%make_build

%install
mkdir -p %buildroot{%_gamesdatadir,%_menudir}
tar -C %buildroot%_gamesdatadir -jxf %SOURCE1

install -pD -c -s amph %buildroot%_gamesbindir/amph
install -pD amph.xpm %buildroot%_niconsdir/%name.xpm
install -pD amphetamine-icons/amph-16.png %buildroot%_liconsdir/%name.png
install -pD amphetamine-icons/amph-32.png %buildroot%_niconsdir/%name.png
install -pD amphetamine-icons/amph-48.png %buildroot%_miconsdir/%name.png
install -pD %SOURCE3 %buildroot%_desktopdir/%name.desktop

%files
%doc BUGS ChangeLog NEWS README
%_gamesdatadir/amph/
%_niconsdir/%name.*
%_miconsdir/%name.*
%_liconsdir/%name.*
%_gamesbindir/*
%_desktopdir/*

%changelog
* Sun Jul 26 2009 Michael Shigorin <mike@altlinux.org> 0.8.10-alt5
- applied repocop patch

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 0.8.10-alt4
- applied repocop patch

* Sun Oct 05 2008 Michael Shigorin <mike@altlinux.org> 0.8.10-alt3
- fixed build requires
- fixed broken description translations' charset
- replaced debian menufile with debian freedesktop file
- spec cleanup

* Fri Mar 28 2008 Sergey Balbeko <balbeko@altlinux.org> 0.8.10-alt2
- Rebuild with xorg & etc.

* Wed Oct 19 2005 Michael Shigorin <mike@altlinux.org> 0.8.10-alt1
- updated Url
- removed COPYING, INSTALL (package has all the needed info)
- added menu icons (#4709); thanks Anton Farygin (rider@)
- spec cleanup

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.8.10-alt0.2.1
- Rebuilt with libstdc++.so.6.

* Sat Nov 09 2002 Michael Shigorin <mike@altlinux.ru> 0.8.10-alt0.2
- initial build for ALT Linux

