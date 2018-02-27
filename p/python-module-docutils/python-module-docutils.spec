%define oname docutils
%def_with python3

Summary: Docutils -- Python Documentation Utilities
Version: 0.12
Release: alt1.svn20130917
%setup_python_module %oname
Name: %packagename
# http://svn.code.sf.net/p/docutils/code/trunk/docutils/
Source0: %modulename-%version.tar.gz
License: public domain, Python, BSD, GPL (see COPYING.txt)
Group: Development/Python
BuildArch: noarch
URL: http://docutils.sourceforge.net/
Packager: Python Development Team <python@packages.altlinux.org>
Conflicts: Zope-docutils
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python-tools-2to3
%endif

%description
Docutils is a modular system for processing documentation
into useful formats, such as HTML, XML, and LaTeX.  For
input Docutils supports reStructuredText, an easy-to-read,
what-you-see-is-what-you-get plaintext markup syntax.

%if_with python3
%package -n python3-module-%oname
Summary: Docutils -- Python 3 Documentation Utilitie
Group: Development/Python3

%description -n python3-module-%oname
Docutils is a modular system for processing documentation
into useful formats, such as HTML, XML, and LaTeX.  For
input Docutils supports reStructuredText, an easy-to-read,
what-you-see-is-what-you-get plaintext markup syntax.

%package -n python3-module-%oname-tests
Summary: Tests for Docutils -- Python 3 Documentation Utilitie
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Docutils is a modular system for processing documentation
into useful formats, such as HTML, XML, and LaTeX.  For
input Docutils supports reStructuredText, an easy-to-read,
what-you-see-is-what-you-get plaintext markup syntax.

This package contains tests for Docutils.
%endif

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w '{}' +
find -type f -name '*.py' -exec sed -i 's|%_bindir/python|%_bindir/python3|' -- '{}' +
find -type f -name '*.py' -exec sed -i 's|%_bindir/env python|%_bindir/python3|' -- '{}' +
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i py3_$i
done
popd
%endif
%python_install --optimize=2 --record=INSTALLED_FILES
install -d %buildroot%_datadir/%modulename
cp -rp tools %buildroot%_datadir/%modulename

install -p -m644 docutils/utils/roman.py \
	%buildroot%python_sitelibdir

export LC_ALL=en_US.UTF-8

#check
#export LC_ALL=en_US.UTF-8
#python test/alltests.py
#if_with python3
%if 0
pushd ../python3
python3 %buildroot%python3_sitelibdir/test/alltests.py
popd
%endif

%files -f INSTALLED_FILES
%doc docs *.txt
%_datadir/%modulename
%python_sitelibdir/roman.py*
%if_with python3
%exclude %_bindir/py3_*

%files -n python3-module-%oname
%_bindir/py3_*
%python3_sitelibdir/*
#exclude %python3_sitelibdir/test
%exclude %python3_sitelibdir/%modulename/examples.py*
#exclude %python3_sitelibdir/tools/editors/emacs/tests
#exclude %python3_sitelibdir/tools/test

%files -n python3-module-%oname-tests
%python3_sitelibdir/%modulename/examples.py*
#python3_sitelibdir/tools/editors/emacs/tests
#python3_sitelibdir/tools/test
%endif

%changelog
* Mon Sep 23 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12-alt1.svn20130917
- Version 0.12

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt2.svn20130117
- Use 'find... -exec...' instead of 'for ... $(find...'

* Wed Mar 20 2013 Aleksey Avdeev <solo@altlinux.ru> 0.11-alt1.svn20130117.1
- Rebuild with Python-3.3

* Fri Jan 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11-alt1.svn20130117
- Version 0.11

* Wed Apr 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt3
- Extracted tests into separate package

* Tue Apr 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt2
- Added module for Python 3

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1
- Version 0.9, snapshot 20111212

* Fri Oct 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7-alt1.1
- Rebuild with Python-2.7

* Thu Jul 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1
- Version 0.7

* Thu Jan 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.20100119-alt1
- Version 0.6, upstream snapshot 20100119

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.1
- Rebuilt with python 2.6

* Thu Apr 16 2009 Fr. Br. George <george@altlinux.ru> 0.5-alt1
- Version up
- tools and docs packaged

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.4-alt1.1
- Rebuilt with python-2.5.

* Tue Feb 07 2006 Ivan Fedorov <ns@altlinux.ru> 0.4-alt1
- Initial build for ALT Linux
