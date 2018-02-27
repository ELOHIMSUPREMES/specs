%define oname boto3

%def_with python3

Name: python-module-%oname
Version: 0.0.5
Release: alt1.git20141209
Summary: The AWS SDK for Python
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/boto3/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/boto/boto3.git
# branch: develop
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-botocore python-module-bcdoc
BuildPreReq: python-module-jmespath python-module-six
BuildPreReq: python-module-nose python-module-mock
BuildPreReq: python-module-sphinx-devel python-module-sphinx_rtd_theme
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-botocore python3-module-bcdoc
BuildPreReq: python3-module-jmespath python3-module-six
BuildPreReq: python3-module-nose python3-module-mock
%endif

%py_provides %oname

%description
Boto is the Amazon Web Services (AWS) Software Development Kit (SDK) for
Python, which allows Python developers to write software that makes use
of services like Amazon S3 and Amazon EC2.

WARNING: Boto 3 is in developer preview and should not be used in
production yet! Please try it out and give feedback by opening issues or
pull requests on this repository. Thanks!

%package -n python3-module-%oname
Summary: The AWS SDK for Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Boto is the Amazon Web Services (AWS) Software Development Kit (SDK) for
Python, which allows Python developers to write software that makes use
of services like Amazon S3 and Amazon EC2.

WARNING: Boto 3 is in developer preview and should not be used in
production yet! Please try it out and give feedback by opening issues or
pull requests on this repository. Thanks!

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Boto is the Amazon Web Services (AWS) Software Development Kit (SDK) for
Python, which allows Python developers to write software that makes use
of services like Amazon S3 and Amazon EC2.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Boto is the Amazon Web Services (AWS) Software Development Kit (SDK) for
Python, which allows Python developers to write software that makes use
of services like Amazon S3 and Amazon EC2.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

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

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
export PYTHONPATH=$PWD
python setup.py test
#py.test
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
python3 setup.py test
#py.test-%_python3_version
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Dec 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.5-alt1.git20141209
- Version 0.0.5

* Tue Dec 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.4-alt1.git20141208
- Version 0.0.4

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20141126
- Version 0.0.3

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1.git20141120
- Version 0.0.2

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20141111
- Initial build for Sisyphus

