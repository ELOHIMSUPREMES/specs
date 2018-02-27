%define branch 1.5
%define version %branch.0
%define release alt4.1
%define origname Django
%define oname django
%define py3_name python3-module-%oname

%def_with python3

%setup_python_module django
%add_python_req_skip cx_Oracle
%add_findreq_skiplist %python_sitelibdir/%modulename/contrib/gis/db/backends/*/*
%if_with python3
%add_python3_req_skip cx_Oracle
%add_findreq_skiplist %python3_sitelibdir/%oname/contrib/gis/db/backends/*/*
%endif

Summary: A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
Name: python-module-%oname
Version: %version
Release: %release
Source0: %origname-%version.tar
License: BSD
Group: Development/Python
BuildArch: noarch
URL: http://www.djangoproject.com/
Provides: Django = %EVR
Provides: %name%branch = %EVR
Obsoletes: python-module-django1.5 <= 1.5.0-alt3
Conflicts: python-module-django1.0 python-module-django1.1
Conflicts: python-module-django1.2

BuildPreReq: %py_dependencies setuptools

# Automatically added by buildreq on Tue Jul 29 2008 (-ba)
BuildRequires: python-module-setuptools python-modules-email
BuildRequires: python-modules-encodings python-modules-sqlite3
BuildRequires: python-modules-xml
BuildRequires: python-modules-ctypes

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-distribute
BuildPreReq: python-tools-2to3

%add_python3_req_skip hotshot
%endif

%description
%summary

%package tests
Summary: Tests for Django
Group: Development/Python
BuildArch: noarch
Requires: %name = %EVR
Provides: %name%branch = %EVR
Obsoletes: python-module-django1.5-tests <= 1.5.0-alt3
Conflicts: python-module-django1.0-tests
Conflicts: python-module-django1.1-tests
Conflicts: python-module-django1.2-tests

%description tests
%summary

This package contains tests for Django.

%package mod_python
Summary: mod_python support for Django.
Group: Development/Python
Requires: %name = %EVR
Requires: apache2-mod_python
Provides: %name%branch = %EVR
Obsoletes: python-module-django1.5-mod_python <= 1.5.0-alt3
Conflicts: python-module-django1.0-mod_python
Conflicts: python-module-django1.1-mod_python
Conflicts: python-module-django1.2-mod_python

%description mod_python
%summary

%package dbbackend-mysql
Summary: MySQLSQL support for Django.
Group: Development/Python
Requires: %name = %EVR
%py_requires MySQLdb
Provides: %name%branch = %EVR
Obsoletes: python-module-django1.5-dbbackend-mysql <= 1.5.0-alt3
Conflicts: python-module-django1.0-dbbackend-mysql
Conflicts: python-module-django1.1-dbbackend-mysql
Conflicts: python-module-django1.2-dbbackend-mysql

%description dbbackend-mysql
%summary

%package dbbackend-psycopg
Summary: PostgreSQL support for Django. (via psycopg)
Group: Development/Python
Requires: %name = %EVR
%py_requires psycopg
Provides: %name%branch = %EVR
Obsoletes: python-module-django1.5-dbbackend-psycopg <= 1.5.0-alt3
Conflicts: python-module-django1.0-dbbackend-psycopg
Conflicts: python-module-django1.1-dbbackend-psycopg
Conflicts: python-module-django1.2-dbbackend-psycopg

%description dbbackend-psycopg
%summary

%package dbbackend-psycopg2
Summary: PostgreSQL support for Django. (via psycopg2)
Group: Development/Python
Requires: %name = %EVR
%py_requires psycopg2
Provides: %name%branch = %EVR
Obsoletes: python-module-django1.5-dbbackend-psycopg2 <= 1.5.0-alt3
Conflicts: python-module-django1.0-dbbackend-psycopg2
Conflicts: python-module-django1.1-dbbackend-psycopg2
Conflicts: python-module-django1.2-dbbackend-psycopg2

%description dbbackend-psycopg2
%summary

%package dbbackend-sqlite3
Summary: SQLite3 support for Django.
Group: Development/Python
Requires: %name = %EVR
%py_requires sqlite3
Provides: %name%branch = %EVR
Obsoletes: python-module-django1.5-dbbackend-sqlite3 <= 1.5.0-alt3
Conflicts: python-module-django1.0-dbbackend-sqlite3
Conflicts: python-module-django1.1-dbbackend-sqlite3
Conflicts: python-module-django1.2-dbbackend-sqlite3

%description dbbackend-sqlite3
%summary

%if_with python3
%package -n %py3_name
Summary: A high-level Python 3 Web framework that encourages rapid development and clean, pragmatic design.
Group: Development/Python3
BuildArch: noarch
Provides: %py3_name%branch = %EVR
Obsoletes: python3-module-django1.5 <= 1.5.0-alt3

%description -n %py3_name
%summary

%package -n %py3_name-tests
Summary: Tests for Django (Python 3)
Group: Development/Python3
BuildArch: noarch
Requires: %py3_name = %EVR
Provides: %py3_name%branch-tests = %EVR
Obsoletes: python3-module-django1.5-tests <= 1.5.0-alt3
%add_python3_req_skip new

%description -n %py3_name-tests
%summary

This package contains tests for Django.

%package -n %py3_name-mod_python
Summary: mod_python support for Django (Python 3)
Group: Development/Python3
Requires: %py3_name = %EVR
Requires: apache2-mod_python
Provides: %py3_name%branch-mod_python = %EVR
Obsoletes: python3-module-django1.5-mod_python <= 1.5.0-alt3

%description -n %py3_name-mod_python
%summary

%package -n %py3_name-dbbackend-mysql
Summary: MySQLSQL support for Django (Python 3)
Group: Development/Python3
Requires: %py3_name = %EVR
Provides: %py3_name%branch-dbbackend-mysql = %EVR
Obsoletes: python3-module-django1.5-dbbackend-mysql <= 1.5.0-alt3
%py3_requires MySQLdb

%description -n %py3_name-dbbackend-mysql
%summary

%package -n %py3_name-dbbackend-psycopg
Summary: PostgreSQL support for Django. (via psycopg) (Python 3)
Group: Development/Python3
Requires: %py3_name = %EVR
Provides: %py3_name%branch-dbbackend-psycopg = %EVR
Obsoletes: python3-module-django1.5-dbbackend-psycopg <= 1.5.0-alt3
%py3_requires psycopg

%description -n %py3_name-dbbackend-psycopg
%summary

%package -n %py3_name-dbbackend-psycopg2
Summary: PostgreSQL support for Django. (via psycopg2) (Python 3)
Group: Development/Python3
Requires: %py3_name = %EVR
Provides: %py3_name%branch-dbbackend-psycopg2 = %EVR
Obsoletes: python3-module-django1.5-dbbackend-psycopg2 <= 1.5.0-alt3
%py3_requires psycopg2

%description -n %py3_name-dbbackend-psycopg2
%summary

%package -n %py3_name-dbbackend-sqlite3
Summary: SQLite3 support for Django (Python 3)
Group: Development/Python3
Requires: %py3_name = %EVR
Provides: %py3_name%branch-dbbackend-sqlite3 = %EVR
Obsoletes: python3-module-django1.5-dbbackend-sqlite3 <= 1.5.0-alt3
%py3_requires sqlite3

%description -n %py3_name-dbbackend-sqlite3
%summary

%endif

%package doc
Summary: Django documentation
Group: Development/Python
Provides: %name%branch-doc = %EVR
Provides: %py3_name%branch-doc = %EVR
Provides: %py3_name%branch-doc = %EVR
Obsoletes: python-module-django1.5-doc <= 1.5.0-alt3
Obsoletes: python3-module-django-doc <= 1.5.0-alt1.alpha
Conflicts: python-module-django1.0-doc
Conflicts: python-module-django1.1-doc
Conflicts: python-module-django1.2-doc

%description doc
%summary

%prep
%setup -n %origname-%version
%if_with python3
rm -rf ../python3
cp -a . ../python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	sed -i 's|%_bindir/env python|%_bindir/env python3|' $i
	sed -i 's|.*from future_builtins import zip.*||' $i
	2to3 -w -n $i
done
popd
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
export LC_ALL=en_US.UTF-8

%if_with python3
pushd ../python3
%python3_install
mv %buildroot%_bindir/django-admin.py %buildroot%_bindir/django-admin.py3
popd
%endif

mkdir -p %buildroot/%_sysconfdir/bash_completion.d

%python_install --record=INSTALLED_FILES
#sed -i -e '/\/test/d' INSTALLED_FILES

install -m 0755 extras/django_bash_completion %buildroot/%_sysconfdir/bash_completion.d/django.sh

%check
# Run tests
#export PYTHONPATH="$PYTHONPATH:%buildroot/%python_sitelibdir/"
#cat >tests/settings.py << EOF
#DATABASE_ENGINE = 'sqlite3'
#DATABASE_NAME = 'demodb'
#ROOT_URLCONF=None 
#EOF
#tests/runtests.py --settings=settings --noinput -v 1
# End tests

%files -f INSTALLED_FILES
#%%exclude %python_sitelibdir/%modulename/core/handlers/modpython.py*
#%%exclude %python_sitelibdir/%modulename/contrib/auth/handlers/modpython.py*

%exclude %python_sitelibdir/%modulename/db/backends/mysql/
#exclude %python_sitelibdir/%modulename/db/backends/postgresql/
%exclude %python_sitelibdir/%modulename/db/backends/postgresql_psycopg2/
%exclude %python_sitelibdir/%modulename/db/backends/sqlite3/

%exclude %python_sitelibdir/%modulename/test
%exclude %python_sitelibdir/%modulename/*/*/test*.py*
%exclude %python_sitelibdir/%modulename/*/*/tests
%exclude %python_sitelibdir/%modulename/*/*/*/tests

%config %_sysconfdir/bash_completion.d/django.sh

%files tests
%python_sitelibdir/%modulename/test
%python_sitelibdir/%modulename/*/*/test*.py*
%python_sitelibdir/%modulename/*/*/tests
%python_sitelibdir/%modulename/*/*/*/tests

%if_with python3
%files -n %py3_name
%_bindir/django-admin.py3
%python3_sitelibdir/*
#exclude %python3_sitelibdir/%oname/core/handlers/modpython.py*
#exclude %python3_sitelibdir/%oname/contrib/auth/handlers/modpython.py*

%exclude %python3_sitelibdir/%oname/db/backends/mysql/
#exclude %python3_sitelibdir/%oname/db/backends/postgresql/
%exclude %python3_sitelibdir/%oname/db/backends/postgresql_psycopg2/
%exclude %python3_sitelibdir/%oname/db/backends/sqlite3/

%exclude %python3_sitelibdir/%oname/test
%exclude %python3_sitelibdir/%oname/*/*/test*.py*
%exclude %python3_sitelibdir/%oname/*/*/tests
%exclude %python3_sitelibdir/%oname/*/*/*/tests

%files -n %py3_name-tests
%python3_sitelibdir/%oname/test
%python3_sitelibdir/%oname/*/*/test*.py*
%python3_sitelibdir/%oname/*/*/tests
%python3_sitelibdir/%oname/*/*/*/tests
%endif

%files doc
%doc docs

#%%files mod_python
#%%python_sitelibdir/%modulename/core/handlers/modpython.py*
#%%python_sitelibdir/%modulename/contrib/auth/handlers/modpython.py*

%files dbbackend-mysql
%python_sitelibdir/%modulename/db/backends/mysql/

#files dbbackend-psycopg
#python_sitelibdir/%modulename/db/backends/postgresql/

%files dbbackend-psycopg2
%python_sitelibdir/%modulename/db/backends/postgresql_psycopg2/

%files dbbackend-sqlite3
%python_sitelibdir/%modulename/db/backends/sqlite3/

%if_with python3
#files -n %py3_name-mod_python
#python3_sitelibdir/%oname/core/handlers/modpython.py*
#python3_sitelibdir/%oname/contrib/auth/handlers/modpython.py*

%files -n %py3_name-dbbackend-mysql
%python3_sitelibdir/%oname/db/backends/mysql/

#files -n %py3_name-dbbackend-psycopg
#python3_sitelibdir/%oname/db/backends/postgresql/

%files -n %py3_name-dbbackend-psycopg2
%python3_sitelibdir/%oname/db/backends/postgresql_psycopg2/

%files -n %py3_name-dbbackend-sqlite3
%python3_sitelibdir/%oname/db/backends/sqlite3/
%endif

%changelog
* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.5.0-alt4.1
- Rebuild with Python-3.3

* Wed Feb 27 2013 Aleksey Avdeev <solo@altlinux.ru> 1.5.0-alt4
- Rename package to python-module-django

* Wed Feb 27 2013 Aleksey Avdeev <solo@altlinux.ru> 1.5.0-alt3
- Version 1.5.0

* Tue Feb 26 2013 Aleksey Avdeev <solo@altlinux.ru> 1.5.0-alt2.rc2
- Version 1.5.0-rc2
- Rename package to python-module-django1.5
- Remove %%name-mod_python subpackage

* Tue Jun 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1.alpha
- Version 1.5.0-alpha

* Thu May 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1
- Version 1.4 (ALT #27288)

* Thu Dec 15 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 1.3.1-alt1
- Version 1.3.1. Security fixes:
  https://www.djangoproject.com/weblog/2011/sep/09/security-releases-issued/

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3-alt1.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1
- Version 1.3

* Fri Feb 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.5-alt1
- Version 1.2.5

* Sat Nov 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt1
- Version 1.2.3

* Thu Aug 26 2010 Andrey Rahmatullin <wrar@altlinux.org> 1.2.1-alt2
- do not search for dependencies in django/contrib/gis/db/backends (closes: #23924)

* Mon Aug 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1
- Version 1.2.1
- Added tests (ALT #22479)

* Sun Mar 21 2010 Denis Klimov <zver@altlinux.org> 1.2-alt3.svn12825
- fix inherit with alt gear

* Sun Mar 21 2010 Denis Klimov <zver@altlinux.org> 1.2-alt2.svn12825
- new version
- remove examples subpackage. It was removed from Django.

* Tue Feb 09 2010 Denis Klimov <zver@altlinux.org> 1.2-alt2.svn12398
- new version

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2.svn11756.1
- Rebuilt with python 2.6

* Sat Nov 21 2009 Denis Klimov <zver@altlinux.org> 1.2-alt2.svn11756
- add conflicts

* Sat Nov 21 2009 Denis Klimov <zver@altlinux.org> 1.2-alt1.svn11756
- new version
- use python macros
- add doc and examples subpackages
- remove test files

* Sat Sep 19 2009 Denis Klimov <zver@altlinux.org> 1.1-alt2.svn11581
- change depend for sqlite python module (Closes: #18957)

* Fri Sep 18 2009 Denis Klimov <zver@altlinux.org> 1.1-alt1.svn11581
- new version (Closes: #21617)

* Thu Jun 04 2009 Denis Klimov <zver@altlinux.org> 1.1-alt1.svn10914
- new version (Closes: #20300)

* Thu May 07 2009 Denis Klimov <zver@altlinux.org> 1.1-alt1.svn10702
- new version from trunk
- remove needless -q option from setup macros
- remove commented lines
- turn off test section

* Fri Mar 20 2009 Denis Klimov <zver@altlinux.org> 1.0-alt5.svn10105
- new version from trunk

* Sun Feb 15 2009 Denis Klimov <zver@altlinux.org> 1.0-alt5.svn9832
- new version from trunk

* Thu Sep 04 2008 Andrew Kornilov <hiddenman@altlinux.ru> 1.0-alt5
- 1.0 release

* Mon Sep 01 2008 Andrew Kornilov <hiddenman@altlinux.ru> 1.0-alt4.beta_2
- 1.0 beta 2

* Sun Aug 17 2008 Andrew Kornilov <hiddenman@altlinux.ru> 1.0-alt3.beta_1
- 1.0 beta 1

* Thu Aug 14 2008 Andrew Kornilov <hiddenman@altlinux.ru> 1.0-alt2.alpha_2
- 1.0 alpha 2
- BuildReq updates

* Fri Jul 25 2008 Andrew Kornilov <hiddenman@altlinux.ru> 1.0-alt1.alpha
- First 1.0 alpha
- Spec updates
- Removed ChangeLog.bz2
- Use Django unit tests

* Tue May 20 2008 Andrew Kornilov <hiddenman@altlinux.ru> 0.97-alt1.svn7540
- Latest SVN trunk sources (Closes: #15646)
- Security fixes (http://groups.google.com/group/django-developers/browse_thread/thread/903d7c2af239ec42)
- Spec updates (pack subdirs)

* Fri Apr 11 2008 Andrew Kornilov <hiddenman@altlinux.ru> 0.97-alt1.svn7412
- Latest SVN trunk sources
- Fixed packages description

* Thu Mar 20 2008 Andrew Kornilov <hiddenman@altlinux.ru> 0.97-alt1.svn7152
- SVN trunk

* Sat Feb 09 2008 Andrew Kornilov <hiddenman@altlinux.ru> 0.97-alt1.svn7103
- Latest svn trunk sources

* Mon Dec 10 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.97-alt0.2.svn6903
- Latest svn trunk sources

* Sat Dec 08 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.97-alt0.2.svn6898
- Latest svn trunk sources

* Sun Sep 24 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.97-alt0.1.svn6410
- Latest svn trunk sources
- Temporarily removed cx_Oracle requirement
- ChangeLog added to the docs
- Removed core/handler.py because it's deprecated

* Mon Jul 02 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.97-alt0.1.svn5583
- Near the 0.97 release

* Sat May 26 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.96-alt1
- New version
- Spec cleanups (package names)

* Thu Mar 08 2007 Ivan Fedorov <ns@altlinux.ru> 0.95.1-alt1
- Initial build for ALT Linux Sisyphus.
