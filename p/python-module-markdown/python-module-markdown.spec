%def_disable check

%define version 2.6.2
%define release alt2.git20150620
%define modulename markdown

%def_with python3

%setup_python_module %modulename

Name: python-module-%modulename
Version: %version
Release: %release

Summary: Python implementation of Markdown text-to-HTML convertor.
Group: Development/Python
License: %gpl2plus | %bsd
Url: http://pypi.python.org/pypi/Markdown/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# git://github.com/waylan/Python-Markdown.git
Source: %name-%version.tar

BuildArch: noarch
BuildPreReq: rpm-build-licenses

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-yaml python-modules-logging
BuildPreReq: python-module-nose python-module-coverage
BuildPreReq: python-modules-xml
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-yaml
BuildPreReq: python3-module-nose python3-module-coverage
%endif

Conflicts: discount
%py_provides %modulename
%py_requires yaml logging xml

%description
Markdown is a plain text formatting syntax designed to be as readable as
possible while being structured enough to allow conversion to other formats.

This package contains Python implementation of markdown-to-HTML convertor.

%if_with python3
%package -n python3-module-%modulename
Summary: Python 3 implementation of Markdown text-to-HTML convertor
Group: Development/Python

%description -n python3-module-%modulename
Markdown is a plain text formatting syntax designed to be as readable as
possible while being structured enough to allow conversion to other formats.
%endif

%package docs
Summary: Documentation for Markdown
Group: Development/Documentation
BuildArch: noarch

%description docs
Markdown is a plain text formatting syntax designed to be as readable as
possible while being structured enough to allow conversion to other formats.

This package contains documentation for Markdown.

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
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/%{modulename}_py \
	%buildroot%_bindir/%{modulename}_py3
%endif

%python_install

ln -s %{modulename}_py %buildroot%_bindir/%modulename

%check
nosetests -v
%if_with python3
pushd ../python3
nosetests3 -v
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%buildroot%_bindir/%modulename README.md >README.html

%files
%_bindir/*
%if_with python3
%exclude %_bindir/%{modulename}_py3
%endif
%python_sitelibdir/*


%if_with python3
%files -n python3-module-%modulename
%_bindir/%{modulename}_py3
%python3_sitelibdir/*
%endif

%changelog
* Mon Feb 08 2016 Sergey Alembekov <rt@altlinux.ru> 2.6.2-alt2.git20150620
- Disabled Doc, tests and unnecessary dependents

* Mon Aug 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.2-alt1.git20150620
- Version 2.6.2

* Wed Mar 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0-alt1.git20150219
- Version 2.6.0

* Thu Nov 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.2-alt1.git20141119
- Version 2.5.2

* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1.git20141028
- Version 2.5.1

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.1-alt1
- Version 2.4.1

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt1.alpha
- Version 2.4.0.alpha

* Sat Mar 02 2013 Aleksey Avdeev <solo@altlinux.ru> 2.2.1-alt1
- Version 2.2.1

* Tue Apr 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1
- Version 2.1.1
- Added module for Python 3

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1
- Version 2.1.0

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.3-alt2.1
- Rebuild with Python-2.7

* Fri Jul 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.3-alt2
- Added explicit conflict with discount

* Thu Jul 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.3-alt1
- Version 2.0.3 (ALT #23510)

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6b-alt1.1
- Rebuilt with python 2.6

* Sun Feb 17 2008 Mikhail Gusarov <dottedmag@altlinux.org> 1.6b-alt1
- Initial build
