Name: itstool
Version: 2.0.3
Release: alt1

Summary: ITS-based XML translation tool
Group: Development/GNOME and GTK+
License: GPLv3+
Url: http://itstool.org/

Source: http://files.itstool.org/itstool/%name-%version.tar.bz2

BuildArch: noarch

BuildRequires: python-module-libxml2

%description
ITS Tool allows to translate XML documents with PO files, using rules
from the W3C Internationalization Tag Set (ITS) to determine what to
translate and how to separate it into PO file messages.

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%check
%make check

%files
%_bindir/%name
%_datadir/%name/
%_man1dir/%name.1.*
%doc NEWS

%changelog
* Fri Oct 06 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.3-alt1
- 2.0.3

* Fri Jan 03 2014 Yuri N. Sedunov <aris@altlinux.org> 2.0.2-alt1
- 2.0.2

* Sat Sep 08 2012 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 1.1.2-alt1
- 1.1.2

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.1-alt1.1
- Rebuild with Python-2.7

* Thu Sep 29 2011 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- 1.1.1

* Thu Sep 08 2011 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- first build for Sisyphus

