Group: Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: gcc-c++ perl(Class/Accessor/Fast.pm) perl(ExtUtils/MY_Metafile.pm) perl(ExtUtils/MakeMaker.pm) perl(Math/Trig.pm) perl(OpenGL.pm) perl(Wx/Event.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
#
%add_findreq_skiplist %{perl_vendor_archlib}/Wx/DemoModules/*
%add_findprov_skiplist %{perl_vendor_archlib}/Wx/DemoModules/*
%add_findreq_skiplist %{perl_vendor_archlib}/Wx/*
%add_findprov_skiplist %{perl_vendor_archlib}/Wx/*
BuildRequires: libGL-devel libGLU-devel
Name:           perl-Wx-GLCanvas
Version:        0.09
Release:        alt1_6
Summary:        Interface to wxWidgets' OpenGL canvas
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Wx-GLCanvas/
Source0:        http://www.cpan.org/authors/id/M/MB/MBARBON/Wx-GLCanvas-%{version}.tar.gz

BuildRequires:  perl
BuildRequires:  perl(Alien/wxWidgets.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Wx/build/MakeMaker.pm)
BuildRequires:  wxGTK-devel

%if 0%{?with_tests}
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Wx.pm)
BuildRequires:  perl(Wx/ScrolledWindow.pm)
%endif



Source44: import.info

%description
A wrapper for wxWidgets' wxGLCanvas, used to display OpenGL graphics.

%prep
%setup -q -n Wx-GLCanvas-%{version}
rm -rf wx

chmod -x Changes README.txt

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor OPTIMIZE="%{optflags} -I/usr/include/wx-2.8"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;

# %{_fixperms} %{buildroot}/*

%if 0%{?with_tests}
%check
DISPLAY=:0.0 make test
%endif

%files
%doc Changes README.txt
%{perl_vendor_archlib}/auto/*
%{perl_vendor_archlib}/Wx*

%changelog
* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_6
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_5
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_4
- update to new release by fcimport

* Tue Feb 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_3
- moved to Sisyphus for Slic3r (by dd@ request)

