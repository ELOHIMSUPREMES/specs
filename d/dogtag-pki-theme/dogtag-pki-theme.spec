# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-java
BuildRequires: gcc-c++ java-devel-default python-devel rpm-build-java rpm-build-python
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:             dogtag-pki-theme
Version:          10.3.1
Release:          alt1_1jpp8
Summary:          Certificate System - Dogtag PKI Theme Components
URL:              http://pki.fedoraproject.org/
License:          GPLv2
Group:            System/Base

BuildArch:        noarch


BuildRequires: ctest cmake
BuildRequires:    java-devel >= 1.7.0
BuildRequires:    jpackage-utils >= 1.7.5

%if 0%{?rhel}
# NOTE:  In the future, as a part of its path, this URL will contain a release
#        directory which consists of the fixed number of the upstream release
#        upon which this tarball was originally based.
Source0:          http://pki.fedoraproject.org/pki/sources/%{name}/%{version}/%{release}/rhel/%{name}-%{version}%{?prerel}.tar.gz
%else
Source0:          http://pki.fedoraproject.org/pki/sources/%{name}/%{version}/%{release}/%{name}-%{version}%{?prerel}.tar.gz
%endif

%global overview                                                       \
Several PKI packages utilize a "virtual" theme component.  These       \
"virtual" theme components are "Provided" by various theme "flavors"   \
including "dogtag" or a user customized theme package.  Consequently,  \
all "dogtag" and any customized theme components MUST be mutually      \
exclusive!                                                             \
%{nil}
Source44: import.info

%description %{overview}


%package -n       dogtag-pki-server-theme
Summary:          Certificate System - PKI Server Framework User Interface
Group:            System/Base

Obsoletes:        dogtag-pki-common-theme <= %{version}-%{release}
Obsoletes:        dogtag-pki-common-ui
Obsoletes:        dogtag-pki-ca-theme <= %{version}-%{release}
Obsoletes:        dogtag-pki-ca-ui
Obsoletes:        dogtag-pki-kra-theme <= %{version}-%{release}
Obsoletes:        dogtag-pki-kra-ui
Obsoletes:        dogtag-pki-ocsp-theme <= %{version}-%{release}
Obsoletes:        dogtag-pki-ocsp-ui
Obsoletes:        dogtag-pki-tks-theme <= %{version}-%{release}
Obsoletes:        dogtag-pki-tks-ui
Obsoletes:        dogtag-pki-ra-theme <= %{version}-%{release}
Obsoletes:        dogtag-pki-ra-ui
Obsoletes:        dogtag-pki-tps-theme <= %{version}-%{release}
Obsoletes:        dogtag-pki-tps-ui

Provides:         dogtag-pki-common-theme = %{version}-%{release}
Provides:         pki-server-theme = %{version}-%{release}
Provides:         pki-common-theme = %{version}-%{release}
Provides:         pki-common-ui = %{version}-%{release}

Provides:         dogtag-pki-ca-theme = %{version}-%{release}
Provides:         pki-ca-theme = %{version}-%{release}
Provides:         pki-ca-ui = %{version}-%{release}

Provides:         dogtag-pki-kra-theme = %{version}-%{release}
Provides:         pki-kra-theme = %{version}-%{release}
Provides:         pki-kra-ui = %{version}-%{release}

Provides:         dogtag-pki-ocsp-theme = %{version}-%{release}
Provides:         pki-ocsp-theme = %{version}-%{release}
Provides:         pki-ocsp-ui = %{version}-%{release}

Provides:         dogtag-pki-tks-theme = %{version}-%{release}
Provides:         pki-tks-theme = %{version}-%{release}
Provides:         pki-tks-ui = %{version}-%{release}

Provides:         dogtag-pki-tps-theme = %{version}-%{release}
Provides:         pki-tps-theme = %{version}-%{release}
Provides:         pki-tps-ui = %{version}-%{release}

%description -n   dogtag-pki-server-theme
This PKI Server Framework User Interface contains
the Dogtag textual and graphical user interface for the PKI Server Framework.

This package is used by the Dogtag Certificate System.

%{overview}


%package -n       dogtag-pki-console-theme
Summary:          Certificate System - PKI Console User Interface
Group:            System/Base

Requires:         java >= 1.7.0

%if 0%{?rhel}
# EPEL version of Dogtag "theme" conflicts with all versions of Red Hat "theme"
Conflicts:        redhat-pki-console-theme
Conflicts:        redhat-pki-console-ui
%endif

Obsoletes:        dogtag-pki-console-ui <= 9

Provides:         pki-console-theme = %{version}-%{release}
Provides:         pki-console-ui = %{version}-%{release}

%description -n   dogtag-pki-console-theme
This PKI Console User Interface contains
the Dogtag textual and graphical user interface for the PKI Console.

This package is used by the Dogtag Certificate System.

%{overview}


%prep


%setup -q -n %{name}-%{version}%{?prerel}


%build
%{__mkdir_p} build
cd build
%{fedora_cmake} -DVERSION=%{version}-%{release} \
	-DVAR_INSTALL_DIR:PATH=/var \
	-DBUILD_DOGTAG_PKI_THEME:BOOL=ON \
	-DJAVA_LIB_INSTALL_DIR=%{_jnidir} \
	..
%{__make} VERBOSE=1 %{?_smp_mflags}


%install
cd build
%{__make} install DESTDIR=%{buildroot} INSTALL="install -p"


# NOTE:  Several "theme" packages require ownership of the "/usr/share/pki"
#        directory because the PKI subsystems (CA, KRA, OCSP, TKS, TPS)
#        which require them may be installed either independently or in
#        multiple combinations.

%files -n dogtag-pki-server-theme
%doc dogtag/common-ui/LICENSE
%dir %{_datadir}/pki
%{_datadir}/pki/common-ui/


%files -n dogtag-pki-console-theme
%doc dogtag/console-ui/LICENSE
%{_javadir}/pki/


%changelog
* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 10.3.1-alt1_1jpp8
- new version

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 10.2.6-alt1_1jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 10.1.0-alt1_1jpp7
- new release

* Sat Jul 19 2014 Igor Vlasenko <viy@altlinux.ru> 10.0.6-alt1_1jpp7
- new version

* Thu Feb 07 2013 Igor Vlasenko <viy@altlinux.ru> 10.0.0-alt1_1jpp7
- fc update

* Tue Dec 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 10.0.0-alt1_0.1.a1jpp7.1
- new version

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 10.0.0-alt1_0.1.a1jpp7
- new version

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 9.0.11-alt1_2jpp7
- new version

