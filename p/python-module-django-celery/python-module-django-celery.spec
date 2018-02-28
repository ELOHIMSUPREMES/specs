%define module_name django-celery

%add_python3_req_skip celery.registry
%add_python3_req_skip celery.task.control

%def_with python3
%def_disable check

Name: python-module-%module_name
Version: 3.2.1
Release: alt1
Group: Development/Python
License: BSD License
Summary: django-celery provides Celery integration for Django
URL: https://github.com/celery/django-celery
Source: %name-%version.tar

#BuildPreReq: python-module-setuptools-tests
#BuildPreReq: python-module-pytest python-module-django-tests
#BuildPreReq: python-module-celery python-module-django-nose
#BuildPreReq: python-module-django-dbbackend-sqlite3
#BuildPreReq: python-module-nose-cover3 python-module-py
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-pytest python3-module-django-tests
#BuildPreReq: python3-module-celery python3-module-django-nose
#BuildPreReq: python3-module-django-dbbackend-sqlite3
#BuildPreReq: python3-module-nose-cover3 python3-module-py
%endif

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-chardet python-module-cryptography python-module-django python-module-ecdsa python-module-enum34 python-module-ndg-httpsclient python-module-nose python-module-ntlm python-module-psycopg2 python-module-pyasn1 python-module-pycrypto python-module-pytz python-module-setuptools python-module-yaml python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python-modules-wsgiref python3 python3-base python3-module-chardet python3-module-django python3-module-ecdsa python3-module-nose python3-module-psycopg2 python3-module-pycrypto python3-module-pytz python3-module-setuptools python3-module-yaml python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3
BuildRequires: python-module-celery python-module-nose-cover3 python-module-pytest python3-module-celery python3-module-nose-cover3 python3-module-pytest rpm-build-python3

%description
Using the Django ORM and cache backend for storing results,
autodiscovery of task modules for applications listed in INSTALLED_APPS,
and more.

%package -n python3-module-%module_name
Summary: django-celery provides Celery integration for Django
Group: Development/Python3

%description -n python3-module-%module_name
Using the Django ORM and cache backend for storing results,
autodiscovery of task modules for applications listed in INSTALLED_APPS,
and more.

%prep
%setup

%if_with python3
cp -fR . ../python3
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
%endif

%python_install

%if "%_target_libdir_noarch" != "%_libdir"
mv %buildroot%_target_libdir_noarch %buildroot%_libdir
%endif

%check
python setup.py test

%files
%doc AUTHORS Changelog FAQ LICENSE README.rst THANKS
%python_sitelibdir/djcelery*
%python_sitelibdir/django_celery*

%if_with python3
%files -n python3-module-%module_name
%doc AUTHORS Changelog FAQ LICENSE README.rst THANKS
%python3_sitelibdir/djcelery*
%python3_sitelibdir/django_celery*
%endif

%changelog
* Sat Jun 03 2017 Lenar Shakirov <snejok@altlinux.ru> 3.2.1-alt1
- Version 3.2.1

* Tue Jun 07 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.2.0-alt1.a1.git20150124.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.2.0-alt1.a1.git20150124.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.2.0-alt1.a1.git20150124.1
- NMU: Use buildreq for BR.

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.0-alt1.a1.git20150124
- New snapshot

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.0-alt1.a1.git20140924
- Version 3.2.0a1
- Enabled testing

* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.10-alt1.git20140331
- Version 3.1.10
- Added module for Python 3

* Mon May 07 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.5.3-alt1
- build for ALT
