%define oname plone.app.users

%def_disable check

Name: python-module-%oname
Version: 2.1
Release: alt1.dev0.git20141009
Summary: A package for all things users and groups related (specific to plone)
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.users/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.users.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFDefault
BuildPreReq: python-module-Products.PlonePAS
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-plone.app.controlpanel
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.autoform
BuildPreReq: python-module-plone.formwidget.namedfile
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-plone.protect
BuildPreReq: python-module-plone.uuid
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-Products.MailHost
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-plone.keyring
#BuildPreReq: python-module-Products.CMFPlone

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone.app ZODB3 Products.CMFCore Products.CMFDefault
%py_requires Products.PlonePAS Products.statusmessages plone.app.layout
%py_requires plone.app.controlpanel plone.autoform plone.namedfile
%py_requires plone.formwidget.namedfile plone.protect plone.uuid
%py_requires z3c.form zope.component zope.event zope.interface
%py_requires zope.schema zope.site
#py_requires Products.CMFPlone

%description
This package provide the registration form for new users using z3c.form
forms. It allows the site administrator to select fields from a schema
to appear on the registration form.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.MailHost Products.PloneTestCase plone.keyring

%description tests
This package provide the registration form for new users using z3c.form
forms. It allows the site administrator to select fields from a schema
to appear on the registration form.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/tests

%files tests
%python_sitelibdir/plone/app/*/tests

%changelog
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt1.dev0.git20141009
- Initial build for Sisyphus

