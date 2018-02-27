%define mname xstatic
%define oname %mname-html5shiv

%def_with python3

Name: python-module-%oname
Version: 3.6.1
Release: alt2
Summary: html5shiv 3.6 (XStatic packaging standard)
License: MIT & GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/XStatic-html5shiv/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-%mname
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-%mname
%endif

%py_provides %mname.pkg.html5shiv
%py_requires %mname.pkg

%description
html5shiv packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these
files.

%package -n python3-module-%oname
Summary: html5shiv 3.6 (XStatic packaging standard)
Group: Development/Python3
%py3_provides %mname.pkg.html5shiv
%py3_requires %mname.pkg

%description -n python3-module-%oname
html5shiv packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these
files.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

# There is a file in the package named .DS_Store or .DS_Store.gz, 
# the file name used by Mac OS X to store folder attributes.  
# Such files are generally useless in packages and were usually accidentally 
# included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name '*.DS_Store' -o -name '*.DS_Store.gz' \) -print -delete

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt
%python_sitelibdir/%mname/pkg/html5shiv
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/%mname/pkg/html5shiv
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Tue Nov 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt2
- Applied python-module-xstatic-html5shiv-3.6.1-alt1.diff

* Mon Nov 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.1-alt1
- Initial build for Sisyphus

