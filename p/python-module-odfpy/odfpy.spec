%define oname odfpy
Name: python-module-%oname
Version: 1.3.4
Release: alt1
Summary: Python library for manipulating OpenDocument files

Group: Development/Python
License: GPLv2+
Url: https://joinup.ec.europa.eu/software/odfpy/home

# Source-url: https://pypi.io/packages/source/o/%oname/%oname-%version.tar.gz
Source: odfpy-%version.tar

%setup_python_module %oname

BuildArch: noarch

# Automatically added by buildreq on Tue Feb 02 2010
BuildRequires: python-devel python-module-setuptools

%description
Odfpy aims to be a complete API for OpenDocument in Python. Unlike
other more convenient APIs, this one is essentially an abstraction
layer just above the XML format. The main focus has been to prevent
the programmer from creating invalid documents. It has checks that
raise an exception if the programmer adds an invalid element, adds an
attribute unknown to the grammar, forgets to add a required attribute
or adds text to an element that doesn't allow it.

These checks and the API itself were generated from the RelaxNG
schema, and then hand-edited. Therefore the API is complete and can
handle all ODF constructions, but could be improved in its
understanding of data types.

%prep
%setup -n %oname-%version

%build
%python_build

%install
%python_install

%files
%docdir examples
%docdir contrib
%_bindir/*
%_man1dir/*
%python_sitelibdir/*egg-info
%python_sitelibdir/odf/

%changelog
* Sat Jul 22 2017 Vitaly Lipatov <lav@altlinux.ru> 1.3.4-alt1
- new version 1.3.4 (with rpmrb script)

* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 1.3.3-alt1
- Autobuild version bump to 1.3.3

* Mon Aug 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1
- Version 1.3.1

* Tue May 21 2013 Fr. Br. George <george@altlinux.ru> 0.9.6-alt1
- Autobuild version bump to 0.9.6

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.2-alt1.1
- Rebuild with Python-2.7

* Tue Feb 02 2010 Vitaly Lipatov <lav@altlinux.ru> 0.9.2-alt1
- initial build for ALT Linux Sisyphus

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 20 2009 Ian Weller <ianweller@gmail.com> - 0.9-1
- Update upstream

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.8-2
- Rebuild for Python 2.6

* Fri Aug 22 2008 Ian Weller <ianweller@gmail.com> 0.8-1
- Update upstream

* Tue Jul 15 2008 Ian Weller <ianweller@gmail.com> 0.7-2
- Change macros
- Remove license file

* Sun Jul 13 2008 Ian Weller <ianweller@gmail.com> 0.7-1
- Add COPYING file
- Use setuptools instead
- sed out shebangs from module files
- Other minor fixes

* Sun Jul 13 2008 Paul W. Frields <stickster@gmail.com> - 0.7-0.1
- Initial RPM package
