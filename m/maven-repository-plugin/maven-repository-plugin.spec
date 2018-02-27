# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-repository-plugin
Version:        2.3.1
Release:        alt2_10jpp7
Summary:        Plugin to create bundles of artifacts for manual uploaded to repository

Group:          Development/Java
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-repository-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
Patch0:         add_compat.patch
BuildArch: noarch

BuildRequires: plexus-utils
BuildRequires: ant
BuildRequires: maven-local
BuildRequires: maven-install-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-plugin-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-plugin-testing-harness
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: jpackage-utils
BuildRequires: junit
BuildRequires: maven-shared-verifier
Requires: ant
Requires: maven
Requires: jpackage-utils

Obsoletes: maven2-plugin-repository <= 0:2.0.8
Provides: maven2-plugin-repository = 1:%{version}-%{release}
Source44: import.info

%description
This plugin is used to create bundles of artifacts that 
can be uploaded to the central repository.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}
Requires: jpackage-utils
BuildArch: noarch

%description javadoc
API documentation for %{name}.


%prep
%setup -q 
%patch0

%build
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt2_10jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt2_8jpp7
- new release

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt2_6jpp7
- fixed build

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_6jpp7
- new fc release

* Sat Mar 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1_5jpp7
- new version

