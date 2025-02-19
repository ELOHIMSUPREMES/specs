%define _unpackaged_files_terminate_build 1
%define dist URI
Name: perl-%dist
Version: 1.76
Release: alt1

Summary: A Perl interface for URI objects
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/O/OA/OALDERS/%{dist}-%{version}.tar.gz

BuildArch: noarch

%add_findreq_skiplist */isbn.pm

# Automatically added by buildreq on Wed Sep 26 2012
BuildRequires: perl-Encode perl-devel perl-libnet perl(Test/Needs.pm)

%description
This package contains the URI.pm module with friends.  The module
implements the URI class.  Objects of this class represent Uniform
Resource Identifier (URI) references as specified in RFC 2396.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes CONTRIBUTING.md
%perl_vendor_privlib/URI*

%changelog
* Wed Jan 30 2019 Igor Vlasenko <viy@altlinux.ru> 1.76-alt1
- automated CPAN update

* Wed Apr 25 2018 Igor Vlasenko <viy@altlinux.ru> 1.74-alt1
- automated CPAN update

* Tue Jan 16 2018 Igor Vlasenko <viy@altlinux.ru> 1.73-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.72-alt1
- automated CPAN update

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1.71-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.69-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 1.67-alt1
- automated CPAN update

* Thu Nov 13 2014 Igor Vlasenko <viy@altlinux.ru> 1.65-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.64-alt1
- automated CPAN update

* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.61-alt1
- automated CPAN update

* Wed Sep 26 2012 Alexey Tourbin <at@altlinux.ru> 1.60-alt1
- 1.59 -> 1.60

* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 1.59-alt1
- 1.58 -> 1.59
- rebuilt as plain src.rpm

* Mon Jan 24 2011 Alexey Tourbin <at@altlinux.ru> 1.58-alt1
- 1.56 -> 1.58

* Fri Dec 24 2010 Alexey Tourbin <at@altlinux.ru> 1.56-alt1
- 1.53 -> 1.56

* Wed Mar 17 2010 Alexey Tourbin <at@altlinux.ru> 1.53-alt1
- 1.52 -> 1.53

* Tue Feb 16 2010 Alexey Tourbin <at@altlinux.ru> 1.52-alt1
- 1.51 -> 1.52

* Thu Nov 26 2009 Alexey Tourbin <at@altlinux.ru> 1.51-alt1
- 1.40 -> 1.51

* Sun Oct 18 2009 Alexey Tourbin <at@altlinux.ru> 1.40-alt1
- 1.38 -> 1.40

* Sat May 30 2009 Alexey Tourbin <at@altlinux.ru> 1.38-alt1
- 1.37 -> 1.38

* Tue Jun 17 2008 Alexey Tourbin <at@altlinux.ru> 1.37-alt1
- 1.36 -> 1.37

* Sat Apr 12 2008 Alexey Tourbin <at@altlinux.ru> 1.36-alt1
- 1.35 -> 1.36

* Sun Mar 02 2008 Alexey Tourbin <at@altlinux.ru> 1.35-alt3
- decoupled %dist-ImpliedBase

* Sun Dec 19 2004 Alexey Tourbin <at@altlinux.ru> 1.35-alt2
- rebuild in new environment
- manual pages not packaged (use perldoc)

* Mon Nov 08 2004 Alexey Tourbin <at@altlinux.ru> 1.35-alt1
- 1.34 -> 1.35
- alt-utf8.patch merged upstream (cpan #7586)

* Wed Oct 06 2004 Alexey Tourbin <at@altlinux.ru> 1.34-alt1
- 1.33 -> 1.34

* Sun Sep 26 2004 Alexey Tourbin <at@altlinux.ru> 1.33-alt1
- 1.30 -> 1.33
- patched not to use Encode for utf8 (cpan #7586)

* Sat Apr 24 2004 Alexey Tourbin <at@altlinux.ru> 1.30-alt2
- packaged %dist-ImpliedBase-0.05 here (laziness is virtue)

* Wed Jan 14 2004 Alexey Tourbin <at@altlinux.ru> 1.30-alt1
- 1.30

* Mon Dec 01 2003 Alexey Tourbin <at@altlinux.ru> 1.28-alt1
- 1.28

* Fri Oct 31 2003 Alexey Tourbin <at@altlinux.ru> 1.27-alt1
- 1.27

* Fri Oct 03 2003 Alexey Tourbin <at@altlinux.ru> 1.26-alt1
- 1.26

* Thu Aug 21 2003 Alexey Tourbin <at@altlinux.ru> 1.25-alt1
- 1.25

* Fri Jul 25 2003 Alexey Tourbin <at@altlinux.ru> 1.24-alt1
- 1.24

* Sun Jan 26 2003 Alexey Tourbin <at@altlinux.ru> 1.23-alt1
- 1.23
- don't exclude isbn.pm, rather use _findreq_skiplist

* Fri Dec 20 2002 Alexey Tourbin <at@altlinux.ru> 1.22-alt2
- isbn support disabled
- buildreq applied
- more %%docs

* Thu Dec 19 2002 Stanislav Ievlev <inger@altlinux.ru> 1.22-alt1
- 1.22

* Wed Oct 23 2002 Alexey Tourbin <at@altlinux.ru> 1.18-alt2
- rebuilt for perl-5.8 with new rpm macros

* Wed Mar 27 2002 Stanislav Ievlev <inger@altlinux.ru> 1.18-alt1
- 1.18

* Mon Jun 25 2001 Stanislav Ievlev <inger@altlinux.ru> 1.12-alt1
- 1.12 . Rebuilt with perl-5.6.1

* Sun Jan 28 2001 Mikhail Zabaluev <zabaluev@parascript.com> 1.10-ipl1mdk
- Updated:
  + version 1.10
- Changed:
  + adapted spec for Sisyphus

* Wed Jun 28 2000 Mikhail Zabaluev <mookid@sigent.ru> 1.07-1mdk_mhz
- new version
- redid filelist

* Fri Mar 31 2000 Pixel <pixel@mandrakesoft.com> 1.05-2mdk
- new group, rebuild, cleanup

* Tue Feb 29 2000 Jean-Michel Dault <jmdault@netrevolution.com>
- upgraded to 1.05

* Mon Jan  3 2000 Jean-Michel Dault <jmdault@netrevolution.com>
- final cleanup for Mandrake 7

* Thu Dec 30 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- rebuilt for Mandrake 7

* Sun Aug 29 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- bzip2'd sources
- updated to 1.04

* Tue May 11 1999 root <root@alien.devel.redhat.com>
- Spec file was autogenerated.
