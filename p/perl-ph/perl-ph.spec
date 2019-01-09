%define dist ph
Name: perl-%dist
Version: 0.11.1
Release: alt1

Summary: Perl *.ph files
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar

# Automatically added by buildreq on Sun Sep 19 2010
BuildRequires: perl-devel

%description
This package provides the following Perl header files.

	ioctl.ph	sys/ioctl.ph
	syscall.ph	sys/syscall.ph
	syslog.ph	sys/syslog.ph
	socket.ph	sys/socket.ph
	sys/resource.ph

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_archlib/*.ph
%dir %perl_vendor_archlib/sys
%perl_vendor_archlib/sys/*.ph

%changelog
* Wed Dec 26 2018 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.11.1-alt1
- Fixed build of ioctl.ph:
  + on ppc* architectures;
  + with linux v4.20 headers.

* Mon Sep 16 2013 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt1
- added sys/resource.ph perl header

* Sun Sep 19 2010 Alexey Tourbin <at@altlinux.ru> 0.10-alt1
- separate package
