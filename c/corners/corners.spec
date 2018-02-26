Name: corners
Version: 1.4
Release: alt1
License: GPLv.2
Summary: A logical board game as known as Halma
Summary (ru_RU.KOI8-R):	���� � ������ (������ �������� -- ������)
Group: Games/Boards
Source: %name-%version.tar.bz2
Source1: %name.desktop

# Automatically added by buildreq on Fri Apr 17 2009
BuildRequires: ImageMagick-tools ctags gcc-c++ libgtk+2-devel

%description
Corners is a logical board game as known as Halma. This game has two AI's; one
of them isn't too hard to play with, whereas the second one is relatively
strong and you need to have good mathematical abilities to defeat it

%description -l ru_RU.KOI8-R
� ���� ��������� ��� ������, ����� ������� ����������� � ���������������
����� �����. ���� ���� - ����������� ��� ���� ����� �� ������ ���� ����� �
���������������. ������ ��� ����� ���� ����������� ���� �� ����� ����� �
�������� ������, ���� ������������� �� ����� ���� ��� ��������� ����� ���
����� �����, ��� ���� ������������ �������������� �� ����������� �
���������. ���������� ��� �����, ������� ���������� ��� ���� ����� �
��������������� ���� �� ������� ����� �����.

%prep
%setup

%build
make
convert %name.png -size 48x48 48x48.png

%install
mkdir -p %buildroot%_bindir
%makeinstall INSTALL_DIR=%buildroot%prefix
mv %buildroot%_datadir/%name/%name %buildroot%_bindir/%name.bin
cat > %buildroot%_bindir/%name <<EOF
#!/bin/sh
cd %_datadir/%name
%_bindir/%name.bin
EOF
install -D %name.png %buildroot%_niconsdir/%name.png
install -D 48x48.png %buildroot%_miconsdir/%name.png
install -D %SOURCE1 %buildroot%_desktopdir/%name.desktop

%files
%doc README
%_datadir/%name
%attr(755,games,games) %_bindir/%{name}*
%_niconsdir/%name.png
%_miconsdir/%name.png
%_desktopdir/%name.desktop

%changelog
* Wed Jul 27 2011 Fr. Br. George <george@altlinux.ru> 1.4-alt1
- Autobuild version bump to 1.4

* Fri Apr 17 2009 Fr. Br. George <george@altlinux.ru> 1.2-alt2
- Desktop file added

* Fri Apr 17 2009 Fr. Br. George <george@altlinux.ru> 1.2-alt1
- Initial build from scratch

