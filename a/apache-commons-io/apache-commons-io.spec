Group: Development/Java
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-compat
%global base_name       io
%global short_name      commons-%{base_name}

Name:           apache-%{short_name}
Version:        2.4
Release:        alt3_10jpp7
Epoch:          1
Summary:        Utilities to assist with developing IO functionality
License:        ASL 2.0
URL:            http://commons.apache.org/%{base_name}
Source0:        http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  apache-commons-parent

Provides:       jakarta-%{short_name} = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name} < %{epoch}:%{version}-%{release}
Source44: import.info
# jpackage compat
Provides:       jakarta-%{short_name} = %version
Obsoletes:      jakarta-%{short_name} < %version
Provides:       %{short_name} = %version

%description
Commons-IO contains utility classes, stream implementations,
file filters, and endian classes. It is a library of utilities
to assist with developing IO functionality.

%package javadoc
Group: Development/Java
Summary:        API documentation for %{name}
Provides:       jakarta-%{short_name}-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-javadoc < %{epoch}:%{version}-%{release}
BuildArch: noarch

%description javadoc
This package provides %{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src
sed -i 's/\r//' *.txt

%build
%mvn_file  : %{short_name} %{name}
%mvn_alias : org.apache.commons:
%mvn_build

%install
%mvn_install
# jpp compat
ln -sf %{name}.jar %{buildroot}%{_javadir}/jakarta-%{short_name}.jar

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.4-alt3_10jpp7
- new release

* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.4-alt3_9jpp7
- new release

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.4-alt3_2jpp7
- rebuild with maven-local

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.4-alt2_2jpp7
- NMU rebuild to move poms and fragments

* Thu Sep 06 2012 Igor Vlasenko <viy@altlinux.ru> 1:2.4-alt1_2jpp7
- new release

* Wed Sep 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_13jpp6
- added osgi manifest

* Sun Feb 13 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt3_12jpp6
- added compat mapping

* Wed Jan 05 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4-alt2_12jpp6
- renamed

