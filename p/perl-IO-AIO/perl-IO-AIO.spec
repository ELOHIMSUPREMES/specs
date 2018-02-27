Epoch: 1
%define dist IO-AIO
Name: perl-%dist
Version: 4.31
Release: alt1

Summary: Asynchronous Input/Output
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/M/ML/MLEHMANN/IO-AIO-%{version}.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-common-sense perl-devel

%description
This module implements asynchronous I/O using whatever means your
operating system supports.

Asynchronous means that operations that can normally block your program
(e.g. reading from disk) will be done asynchronously: the operation
will still block, but you can do something else in the meantime. This
is extremely useful for programs that need to stay interactive even
when doing heavy I/O (GUI programs, high performance network servers
etc.), but can also be used to easily do operations in parallel that are
normally done sequentially, e.g. stat'ing many files, which is much faster
on a RAID volume or over NFS when you do a number of stat operations
concurrently.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_autolib/IO
%perl_vendor_archlib/IO

%changelog
* Tue Jun 10 2014 Igor Vlasenko <viy@altlinux.ru> 1:4.31-alt1
- automated CPAN update

* Mon Apr 14 2014 Igor Vlasenko <viy@altlinux.ru> 1:4.3-alt1
- automated CPAN update

* Sat Jan 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:4.2-alt2
- bumped serial

* Sat Jan 25 2014 Igor Vlasenko <viy@altlinux.ru> 4.2-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 4.18-alt2
- built for perl 5.18

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 4.18-alt1
- automated CPAN update

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 4.15-alt1
- 4.0 -> 4.15
- built for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 4.0-alt2
- rebuilt for perl-5.14

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1
- automated CPAN update

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 3.65-alt1.1
- rebuilt with perl 5.12

* Thu Jul 15 2010 Igor Vlasenko <viy@altlinux.ru> 3.65-alt1
- automated CPAN update

* Sat Jun 27 2009 Michael Bochkaryov <misha@altlinux.ru> 3.25-alt1
- 3.25 version build

* Wed Sep 17 2008 Michael Bochkaryov <misha@altlinux.ru> 3.07-alt1
- 3.07 version build
- fix directory ownership violation

* Mon Apr 28 2008 Michael Bochkaryov <misha@altlinux.ru> 2.62-alt1
- first build for ALT Linux Sisyphus
