# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           spice-parent
Version:        15
Release:        alt1_10jpp7
Summary:        Sonatype Spice Components

Group:          Development/Java
License:        ASL 2.0
URL:            http://svn.sonatype.org/spice/tags/spice-parent-15
#svn export http://svn.sonatype.org/spice/tags/spice-parent-15 spice-parent-15
#tar zcf spice-parent-15.tar.gz spice-parent-15/
Source0:        %{name}-%{version}.tar.gz
Source1:        http://apache.org/licenses/LICENSE-2.0.txt
Patch0:         pom.patch

BuildArch: noarch

BuildRequires:  jpackage-utils
BuildRequires:  maven-local
BuildRequires:  forge-parent

Requires:          jpackage-utils
Requires:          forge-parent
Source44: import.info

%description
Spice components and libraries are common components
used throughout the Sonatype Forge.

%prep
%setup -q -n %{name}-%{version}
#Remove plexus-javadoc
%patch0
cp %{SOURCE1} .

%build
#nothing to do for the pom

%install
# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap JPP-%{name}.pom

%check
mvn-rpmbuild verify

%files -f .mfiles
%doc LICENSE-2.0.txt


%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 15-alt1_10jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 15-alt1_9jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 15-alt1_6jpp7
- new fc release

* Fri Mar 30 2012 Igor Vlasenko <viy@altlinux.ru> 15-alt1_5jpp7
- complete build

* Wed Mar 07 2012 Igor Vlasenko <viy@altlinux.ru> 15-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

