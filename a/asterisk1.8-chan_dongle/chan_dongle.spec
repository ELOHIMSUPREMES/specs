%define ast_version 1.8.23.0
%define modules_dir %_libdir/asterisk/%ast_version/modules

Name: asterisk1.8-chan_dongle
Summary: Channel driver for Asterisk to use Huawei 3G modem series.
Version: 1.1
Release: alt12
License: GPL
Group: System/Libraries
Url: http://code.google.com/p/asterisk-chan-dongle/

Source: %name-%version.tar

# Automatically added by buildreq on Sat Oct 03 2009
BuildRequires(pre): asterisk1.8-devel

Requires: usb_modeswitch
Requires: asterisk1.8 = %ast_version

%description
%summary

%prep
%setup

%build
export CFLAGS="-I /usr/include/asterisk-%ast_version" 

%configure \
    --with-asterisk=/usr/include/asterisk-%ast_version
%make_build OPTFLAGS="-I /usr/include/asterisk-%ast_version" LIBS="-l pthread"

%install
mkdir -p %buildroot%modules_dir/
cp *.so %buildroot%modules_dir/
mkdir -p %buildroot%_docdir/%name

%files
%modules_dir/*.so
%doc LICENSE.txt README.txt TODO.txt INSTALL BUGS etc

%changelog
* Thu Aug 01 2013 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt12
- Asterisk update

* Sun May 19 2013 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt11
- Asterisk update

* Wed Apr 10 2013 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt10
- Asterisk update

* Thu Feb 14 2013 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt9
- update to r14

* Wed Jan 30 2013 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt8
- add Url tag

* Sat Jan 26 2013 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt7
- Asterisk update

* Mon Jan 21 2013 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt6
- Asterisk update

* Sat Jan 05 2013 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt5
- Asterisk update

* Sat Jan 05 2013 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt4
- Asterisk update

* Tue Dec 11 2012 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt3
- Asterisk update

* Sun Nov 11 2012 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt2
- Asterisk update

* Fri Nov 09 2012 Denis Smirnov <mithraen@altlinux.ru> 1.1-alt1.r14
- first build for Sisyphus
