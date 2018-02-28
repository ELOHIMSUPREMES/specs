Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Summary:        Maven Shared Components
URL:            http://maven.apache.org/shared/
Name:           maven-shared
Version:        21
Release:        alt1_2jpp8
License:        ASL 2.0
Group:          Development/Java

Source0:        https://github.com/apache/%{name}/archive/%{name}-components-%{version}.tar.gz

BuildRequires:  maven-local

BuildArch:      noarch

# Obsoleting retired subpackages. The packages with hardcoded versions and
# releases had their versions manually set in maven-shared-15 to something else
# than {version}. To make the change effective, the release below is one
# greater than the last release of maven-shared-15 in rawhide.
Obsoletes:      maven-shared-ant < 1.0-32
Obsoletes:      maven-shared-model-converter < 2.3-32
Obsoletes:      maven-shared-runtime < 1.0-32
Obsoletes:      maven-shared-monitor < 1.0-32
Obsoletes:      maven-shared-javadoc < %{version}-%{release}
Source44: import.info

%description
Maven Shared Components

%prep
%setup -q -n %{name}-%{name}-components-%{version}
chmod -R go=u-w *

# Maven-scm-publish-plugin is not in Fedora
%pom_remove_plugin org.apache.maven.plugins:maven-scm-publish-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%changelog
* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:21-alt1_2jpp8
- new version

* Wed Jan 20 2016 Igor Vlasenko <viy@altlinux.ru> 0:21-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:19-alt1_4jpp7
- new release

* Sat Aug 23 2014 Igor Vlasenko <viy@altlinux.ru> 0:19-alt1_3jpp7
- new version

* Thu Aug 07 2014 Igor Vlasenko <viy@altlinux.ru> 0:15-alt10_28jpp7
- rebuild with maven-local

* Mon Jul 21 2014 Igor Vlasenko <viy@altlinux.ru> 0:15-alt9_28jpp7
- update

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 0:15-alt9_24jpp7
- new fc release

* Tue Apr 17 2012 Igor Vlasenko <viy@altlinux.ru> 0:15-alt9_23jpp7
- dropped versioned requires

* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 0:15-alt8_23jpp7
- complete build

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:15-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

