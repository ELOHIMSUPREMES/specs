%define _unpackaged_files_terminate_build 1
%define dist HTTP-Tiny
Name: perl-%dist
Version: 0.047
Release: alt1

Summary: A small, simple, correct HTTP/1.1 client
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/D/DA/DAGOLDEN/HTTP-Tiny-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Apr 28 2011
BuildRequires: perl-devel

%description
This is a very simple HTTP/1.1 client, designed primarily for doing
simple GET requests without the overhead of a large framework like
LWP::UserAgent.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/HTTP

%changelog
* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.047-alt1
- automated CPAN update

* Mon Feb 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.043-alt1
- automated CPAN update

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.042-alt1
- automated CPAN update

* Thu Nov 28 2013 Igor Vlasenko <viy@altlinux.ru> 0.039-alt1
- automated CPAN update

* Thu Nov 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.038-alt1
- automated CPAN update

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.037-alt1
- automated CPAN update

* Fri Sep 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.036-alt1
- automated CPAN update

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.035-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.034-alt1
- automated CPAN update

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.024-alt1
- automated CPAN update

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.022-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1
- automated CPAN update

* Thu Apr 28 2011 Alexey Tourbin <at@altlinux.ru> 0.012-alt1
- initial revision
