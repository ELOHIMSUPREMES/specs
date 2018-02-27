%define _unpackaged_files_terminate_build 1
Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Config.pm) perl(IPC/Open3.pm) perl(open.pm) perl(subs.pm) perl-Module-Build perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-File-Map
Version:        0.62
Release:        alt1
Summary:        Memory mapping made simple and safe
License:        GPL+ or Artistic

URL:            http://search.cpan.org/dist/File-Map/
Source:        http://www.cpan.org/authors/id/L/LE/LEONT/File-Map-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl(Module/Build.pm)
# Run-time
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(PerlIO/Layers.pm)
BuildRequires:  perl(Sub/Exporter.pm)
BuildRequires:  perl(Sub/Exporter/Progressive.pm)
BuildRequires:  perl(XSLoader.pm)
# Tests
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(if.pm)
BuildRequires:  perl(IO/Handle.pm)
BuildRequires:  perl(IO/Socket/INET.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Test/Exception.pm)
BuildRequires:  perl(Test/Fatal.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/NoWarnings.pm)
BuildRequires:  perl(Test/Warn.pm)
BuildRequires:  perl(Test/Warnings.pm)
BuildRequires:  perl(threads.pm)
BuildRequires:  perl(Time/HiRes.pm)


Source44: import.info

%description
File::Map maps files or anonymous memory into perl variables.


%prep
%setup -q -n File-Map-%{version}
chmod -x examples/fastsearch.pl


%build
%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build


%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*


%check
./Build test


%files
%doc Changes examples LICENSE README
%{perl_vendor_archlib}/auto/*
%{perl_vendor_archlib}/File*


%changelog
* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.62-alt1
- automated CPAN update

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.61-alt2_2
- update to new release by fcimport

* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.61-alt2_1
- moved to Sisyphus for Slic3r (by dd@ request)

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.61-alt1_1
- update to new release by fcimport

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 0.60-alt2_1
- rebuild to get rid of unmets

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.60-alt1_1
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.57-alt1_2
- update to new release by fcimport

* Fri May 31 2013 Igor Vlasenko <viy@altlinux.ru> 0.57-alt1_1
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.56-alt1_2
- update to new release by fcimport

* Wed Jan 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.56-alt1_1
- update to new release by fcimport

* Fri Dec 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.55-alt1_1
- update to new release by fcimport

* Wed Dec 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1_1
- update to new release by fcimport

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 0.31-alt3_7
- rebuild with new perl

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.31-alt2_7
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1_7
- fc import

