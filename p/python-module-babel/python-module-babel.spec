%define oname babel

%def_with python3
%def_without docs
%def_disable check

Name: python-module-%oname
Version: 3.0
Release: alt2.dev.git20150805

Summary: a collection of tools for internationalizing Python applications
License: BSD
Group: Development/Python

Url: http://babel.edgewall.org

# https://github.com/mitsuhiko/babel.git
Source: %name-%version.tar
Source1: CLDR.tar

BuildArch: noarch
BuildPreReq: python-module-setuptools-tests python-module-sphinx-devel
BuildPreReq: python-module-pytest-cov
%{?!_without_check:%{?!_disable_check:BuildRequires: %py_dependencies setuptools.command.test pytz}}

%setup_python_module babel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pytest-cov
BuildPreReq: python3-module-pytz python-tools-2to3
%endif
%py_requires pytz

%description
Babel is an integrated collection of utilities that assist in
internationalizing and localizing Python applications, with an emphasis
on web-based applications.
The functionality Babel provides for internationalization (I18n) and
localization (L10N) can be separated into two different aspects:
  * tools to build and work with gettext message catalogs, and
  * a Python interface to the CLDR (Common Locale Data Repository),
    providing access to various locale display names, localized number
    and date formatting, etc.

%if_with python3
%package -n python3-module-%oname
Summary: a collection of tools for internationalizing Python 3 applications
Group: Development/Python3
%py3_requires pytz

%description -n python3-module-%oname
Babel is an integrated collection of utilities that assist in
internationalizing and localizing Python applications, with an emphasis
on web-based applications.
The functionality Babel provides for internationalization (I18n) and
localization (L10N) can be separated into two different aspects:
  * tools to build and work with gettext message catalogs, and
  * a Python interface to the CLDR (Common Locale Data Repository),
    providing access to various locale display names, localized number
    and date formatting, etc.
%endif

%prep
%setup -a1
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
python scripts/import_cldr.py CLDR/
%python_build
%if_with python3
pushd ../python3
python scripts/import_cldr.py CLDR/
find -type f -name '*.py' -exec sed -i 's|%_bindir/env python|%_bindir/python3|' -- '{}' +
find -type f -name '*.py' -exec 2to3 -w '{}' +
%python3_build build_ext
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
install -p -m644 %oname/localedata/__init__.py \
	%buildroot%python3_sitelibdir/%oname/localedata/
popd
mv %buildroot%python3_sitelibdir/Babel-*-py%_python3_version.egg-info \
	%buildroot%python3_sitelibdir/Babel-%version-py%_python3_version.egg-info
mv %buildroot%_bindir/pybabel %buildroot%_bindir/pybabel3
%endif

%python_install
install -p -m644 %oname/localedata/__init__.py \
	%buildroot%python_sitelibdir/%oname/localedata/
mv %buildroot%python_sitelibdir/Babel-*-py%_python_version.egg-info \
	%buildroot%python_sitelibdir/Babel-%version-py%_python_version.egg-info

%if_with docs
%make -C docs html
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%_bindir/pybabel
%python_sitelibdir/babel/
%python_sitelibdir/*.egg-info
%doc AUTHORS CHANGES README
%if_with docs
%doc docs/_build/html
%endif

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGES README
%if_with docs
%doc docs/_build/html
%endif
%_bindir/pybabel3
%python3_sitelibdir/babel/
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Mon Aug 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt2.dev.git20150805
- Added missing files

* Mon Aug 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt1.dev.git20150805
- Version 3.0-dev

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.dev.git20140407
- Version 2.0-dev

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.svn20121012
- Version 1.0

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.6-alt1.1
- Use 'find... -exec...' instead of 'for ... $(find...'

* Thu Feb 21 2013 Aleksey Avdeev <solo@altlinux.ru> 0.9.6-alt1
- 0.9.6

* Thu May 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt1.2
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.5-alt1.1
- Rebuild with Python-2.7

* Sat Aug 28 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.9.5-alt1
- 0.9.5
- build from SVN
- run tests
- add pytz to Requires according to the upstream recommendation

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt1.1
- Rebuilt with python 2.6

* Sun Oct 18 2009 Vladimir Lettiev <crux@altlinux.ru> 0.9.4-alt1
- initial build
