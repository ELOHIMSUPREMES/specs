%define oldname python-cliapp
%global pkgname cliapp

Name: python-module-cliapp
Version: 1.20140719
Release: alt2

Summary: Python framework for Unix command line programs

Group: Other
License: GPLv2+
Url: http://liw.fi/%pkgname

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: http://code.liw.fi/debian/pool/main/p/%oldname/%{oldname}_%version.orig.tar.gz
Source: %name-%version.tar
Source44: import.info

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel

BuildArch: noarch
# due missed coverage.erase()
#BuildRequires: python-module-coverage-test-runner
BuildRequires: python-module-sphinx

%description
cliapp is a Python framework for Unix-like command line programs. It
contains the typical stuff such programs need to do, such as parsing
the command line for options, and iterating over input files.

%package doc
Group: Other
Summary: Documentation for %pkgname

%description doc
This package contains the documentation for %pkgname, a Python
framework for Unix command line programs.

%prep
%setup

%build
%python_build
# Build documentation
%make_build

%install
%python_install

%check
exit 0
# CoverageTestRunner trips up on build directory;
# since we've already done the install phase, remove it first
rm -rf build
# ./cliapp/runcmd.py also missing tests
# (fixed in current Git but introduces other changes)
echo ./cliapp/runcmd.py >> without-tests
make check

%files
%doc COPYING NEWS README
%_man5dir/cliapp.5*
%python_sitelibdir_noarch/%pkgname
%python_sitelibdir_noarch/%pkgname-%version-py?.?.egg-info

%files -n python-module-cliapp-doc
%doc doc/_build/html/*

%changelog
* Wed Aug 12 2015 Vitaly Lipatov <lav@altlinux.ru> 1.20140719-alt2
- human build for ALT Linux Sisyphus

* Tue Dec 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.20140719-alt1_1
- update to new release by fcimport

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.20130808-alt1_2
- update to new release by fcimport

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.20130808-alt1_1
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.20130613-alt1_2
- update to new release by fcimport

* Fri Jun 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.20130613-alt1_1
- update to new release by fcimport

* Sat May 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.20130424-alt1_1
- update to new release by fcimport

* Thu Mar 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.20130313-alt1_1
- update to new release by fcimport

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.20121216-alt1_1
- update to new release by fcimport

* Thu Feb 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.20120630-alt1_3
- update to new release by fcimport

* Mon Dec 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.20120630-alt1_2
- initial fc import

