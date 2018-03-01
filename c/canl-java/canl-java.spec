Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		canl-java
Version:	2.4.1
Release:	alt1_3jpp8
Summary:	EMI Common Authentication library - bindings for Java

#		The main parts of the code are BSD
#		Parts derived from glite security utils java are Apache 2.0
#		Parts derived from bouncycastle are MIT
#		Parts derived from Apache Commons IO are Apache 2.0
#		See LICENSE.txt for details
License:	BSD and ASL 2.0 and MIT
URL:		https://github.com/eu-emi/%{name}/
Source0:	https://github.com/eu-emi/%{name}/archive/canl-%{version}.tar.gz
#		Disable tests that require network connections
Patch0:		%{name}-test.patch
BuildArch:	noarch

BuildRequires:	maven-local
BuildRequires:	mvn(commons-io:commons-io)
BuildRequires:	mvn(junit:junit)
BuildRequires:	mvn(org.bouncycastle:bcpkix-jdk15on) >= 1.54
BuildRequires:	mvn(org.bouncycastle:bcprov-jdk15on) >= 1.54
Source44: import.info

%description
This is the Java part of the EMI caNl -- the Common Authentication Library.

%package javadoc
Group: Development/Java
Summary:	Javadoc documentation for %{name}
BuildArch: noarch

%description javadoc
Javadoc documentation for EMI caNl.

%prep
%setup -q -n %{name}-canl-%{version}
%patch0 -p1

# Remove maven-wagon-webdav-jackrabbit dependency
%pom_xpath_remove pom:build/pom:extensions

# GPG signing requires a GPG key
%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin

# Do not create source jars
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin

# Do not stage
%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc API-Changes.txt README.md
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Thu Nov 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt1_3jpp8
- fc27 update

* Sun Oct 22 2017 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt1_2jpp8
- new jpp release

* Fri Dec 16 2016 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt1_1jpp8
- new version

* Fri Nov 25 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_1jpp8
- new version

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_1jpp8
- new version

