# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Data/Dump.pm) perl(ExtUtils/MakeMaker.pm) perl(Lingua/EN/Numbers/Easy.pm) perl(Storable.pm) perl-Module-Build perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Data-Rmap
Version:        0.62
Release:        alt2_7
Summary:        Recursive map, apply a block to a data structure
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Data-Rmap/
Source0:        http://www.cpan.org/authors/id/B/BO/BOWMANBS/Data-Rmap-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Test/Exception.pm)
BuildRequires:  perl(Test/More.pm)
Source44: import.info

%description
This perl module evaluates a BLOCK over a list of data structures
recursively (locally setting $_ to each element) and return the list
composed of the results of such evaluations.  $_ can be used to modify
the elements.

%prep
%setup -q -n Data-Rmap-%{version}

%build
perl Build.PL --install_path bindoc=%_man1dir installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0

# %{_fixperms} %{buildroot}/*

%check
./Build test


%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.62-alt2_7
- moved to Sisyphus for Slic3r (by dd@ request)

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.62-alt1_7
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.62-alt1_6
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.62-alt1_5
- initial fc import

