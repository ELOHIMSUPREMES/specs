%define dist Event-Lib
Name: perl-%dist
Version: 1.03
Release: alt3

Summary: Perl extentions for event-based programming
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz
Patch1: Event-Lib-tests-fork.patch

# in 5.16 get_sv("$", FALSE) returns NULL sometimes
# use getpid() call instead
Patch2: Event-Lib-getpid.patch

# Automatically added by buildreq on Tue Oct 11 2011
BuildRequires: libevent-devel perl-Test-Fork perl-Test-Pod perl-Test-Pod-Coverage

%description
This module is a Perl wrapper around libevent(3) as available from
<http://www.monkey.org/~provos/libevent/>.  It allows to execute a function
whenever a given event on a filehandle happens, a timeout occurs or a signal
is received.

%prep
%setup -q -n %dist-%version
%patch1 -p1
%patch2 -p2

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Event
%perl_vendor_autolib/Event

%changelog
* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 1.03-alt3
- rebuilt for perl-5.16
- fixed build

* Tue Oct 11 2011 Alexey Tourbin <at@altlinux.ru> 1.03-alt2.2
- rebuilt for perl-5.14

* Sat Jun 25 2011 Igor Vlasenko <viy@altlinux.ru> 1.03-alt2.1.1
- rebuilt with libevent2

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.03-alt2.1
- rebuilt with perl 5.12

* Mon Jul 13 2009 Vladimir Lettiev <crux@altlinux.ru> 1.03-alt2
- fix tests with fork

* Sat Aug 23 2008 Vladimir Lettiev <crux@altlinux.ru> 1.03-alt1
- Initial build for Sisyphus
