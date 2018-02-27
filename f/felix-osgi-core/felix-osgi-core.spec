Epoch: 0
BuildRequires: /proc
BuildRequires: jpackage-compat
%global bundle org.osgi.core

Name:    felix-osgi-core
Version: 1.4.0
Release: alt3_14jpp7
Summary: Felix OSGi R4 Core Bundle
Group:   Development/Java
License: ASL 2.0
URL:     http://felix.apache.org/site/apache-felix-osgi-core.html
Source0: http://www.apache.org/dist/felix/%{bundle}-%{version}-project.tar.gz

BuildArch: noarch

BuildRequires: jpackage-utils
BuildRequires: maven-local
BuildRequires: felix-parent
BuildRequires: maven-surefire-provider-junit4
BuildRequires: mockito
Source44: import.info


%description
OSGi Service Platform Release 4 Core Interfaces and Classes.

%package javadoc
Group:          Development/Java
Summary:        API documentation for %{name}
BuildArch: noarch

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

%mvn_file :%{bundle} "felix/%{bundle}"
%mvn_alias "org.apache.felix:%{bundle}" "org.osgi:%{bundle}"

%build
export LC_ALL=en_US.UTF-8
%mvn_build -- -Drat.numUnapprovedLicenses=50

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt3_14jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt3_12jpp7
- new release

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt3_10jpp7
- NMU rebuild to move poms and fragments

* Thu Aug 23 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt2_10jpp7
- new release

* Fri Mar 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt2_6jpp6
- fixed build with java 7

* Mon Feb 14 2011 Igor Vlasenko <viy@altlinux.ru> 0:1.4.0-alt1_6jpp6
- new version

