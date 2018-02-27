%define Name KeyLaunch
Name: keylaunch
Version: 1.3.3
Release: alt1.qa1
Summary: Small utility for binding commands to a hot key.
Summary(uk_UA.CP1251): �������� ������ ��� ����������� �������� "������� �����"
Summary(ru_RU.CP1251): ��������� ������� ��� ���������� �������� "������� ������"
License: GPL
Group: Graphical desktop/Other
URL: http://www.oroborus.org/
Source: %{name}_%version.tar.bz2

# Automatically added by buildreq on Fri Jun 16 2006
BuildRequires: libSM-devel libX11-devel xorg-cf-files

%description
%Name is a small utility for binding commands to a hot key.

%description -l uk_UA.CP1251
%Name - �������� ������ ��� ����������� �������� "������� �����".

%description -l ru_RU.CP1251
%Name - ��������� ������� ��� ���������� �������� "������� ������".



%prep
%setup -q -n %name-%version
subst 's/\r//g' README


%build
%configure
%make_build


%install
%make_install DESTDIR=%buildroot install
rm -rf %buildroot%_docdir/%name
gzip --best --stdout -- debian/changelog > changelog.gz


%files
%doc README docs/example_rc changelog.*
%_bindir/*
%_man1dir/*


%changelog
* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.3.3-alt1.qa1
- NMU: rebuilt for updated dependencies.

* Fri Jun 16 2006 Led <led@altlinux.ru> 1.3.3-alt1
- initial build
