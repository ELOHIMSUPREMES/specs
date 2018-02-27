%define dist Net-Pcap
Name: perl-%dist
Version: 0.17
Release: alt1

Summary: Interface to pcap(3) LBL packet capture library
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz
Patch1: %name-0.17-cflags.patch

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: libpcap-devel perl-Test-Exception perl-Test-Pod perl-podlators

%description
Net::Pcap is a Perl binding to the LBL pcap(3) library.
The README for libpcap describes itself as:

"a system-independent interface for user-level packet capture.
libpcap provides a portable framework for low-level network
monitoring.  Applications include network statistics collection,
security monitoring, network debugging, etc."

%prep
%setup -q -n %dist-%version
%patch1 -p2

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc Changes README
%_bindir/pcapinfo
%_man1dir/pcapinfo.1*
%perl_vendor_archlib/Net
%perl_vendor_autolib/Net

%changelog
* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.17-alt1
- 0.16 -> 0.17

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 0.16-alt3
- rebuilt for perl-5.16

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 0.16-alt2.2
- rebuilt for perl-5.14

* Mon Nov 08 2010 Vladimir Lettiev <crux@altlinux.ru> 0.16-alt2.1
- rebuilt with perl 5.12

* Tue Sep 02 2008 Sergey Y. Afonin <asy@altlinux.ru> 0.16-alt2
- fixed directory ownership viloation

* Wed Mar 05 2008 Sergey Y. Afonin <asy@altlinux.ru> 0.16-alt1
- new version

* Mon May 07 2007 Sergey Y. Afonin <asy@altlinux.ru> 0.14-alt1
- new version

* Tue Jul 27 2004 Alexander V. Denisov <rupor at altlinux dot ru> 0.05-alt1
- Initial build for ALTLinux
